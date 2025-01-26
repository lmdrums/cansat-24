from colorama import Style
import time
import apollosat.constants as c
import serial
from utils.path import get_resource_path

try:
    serial_connection = serial.Serial(c.PORT, c.BAUDRATE, c.BYTESIZE, parity="N")
except serial.serialutil.SerialException:
    print("Groundstation not connected. Proceeding with empty GUI.")
    serial_connection = None

cansat_connected = False

def permanent_file(filename: str) -> None:
    """Writes all data from temporary data.txt file and writes it to a permanent file"""

    with open(get_resource_path(c.MAIN_DATA), "r") as file:
        contents = file.read()

    with open(get_resource_path(filename), "a") as file:
        file.write(contents)

def wipe_file(filename: str):
    """Deletes contents of data file at beginning of program"""

    with open(get_resource_path(filename), "w") as file:
        file.truncate()

def record_data(parent):
    """Records all mission data in one file"""

    global cansat_connected
    serial_connection.reset_input_buffer()
    raw_data = serial_connection.readline()
    data = raw_data.decode("utf-8").strip()

    if not cansat_connected:
        if raw_data:
            parent.flash_window_function("CanSat Connected")
            cansat_connected = True

    with open(get_resource_path(c.MAIN_DATA), "a", encoding="utf-8") as file:
        file.write(f"{data}\n")

def animate(data_dict: dict, key: str) -> tuple:
    """Pulls and returns data from the txt files so that the graph can be updated.
    Deletes malformed packets from the data file."""
    
    column_index = data_dict[key]
    packet_index = data_dict["packet_count"]
    
    x_list = []
    y_list = []
    valid_lines = []  # Store valid lines to rewrite the file later
    
    with open(get_resource_path(c.MAIN_DATA), "r") as file:
        for line in file:
            if len(line.strip()) > 0:
                try:
                    columns = line.split()  # Split line into columns by spaces
                    x_value = int(columns[packet_index])
                    y_value = float(columns[column_index])
                    
                    x_list.append(x_value)
                    y_list.append(y_value)
                    
                    valid_lines.append(line)
                except (IndexError, ValueError):
                    continue # Skip malformed lines
    
    # Rewrite the file with only valid lines
    with open(get_resource_path(c.MAIN_DATA), "w") as file:
        file.writelines(valid_lines)
    
    return x_list, y_list


def animate_text() -> tuple:
    """Updates the text fields every second"""
    radio_strength = None
    estimated_altitude = None
    
    with open(get_resource_path(c.MAIN_DATA), "r") as file:
        for line in file:
            if len(line.strip()) > 0:
                try:
                    data_fields = line.strip().split(" ")

                    radio_strength = data_fields[c.DATA_DICT["radio_strength"]]
                    estimated_altitude = data_fields[c.DATA_DICT["cansat_estimated_altitude"]]
                   
                except (IndexError, ValueError):
                    continue
    
    return radio_strength, estimated_altitude


def gradient_text(text):
    colors = [
        '\033[38;5;214m',
        '\033[38;5;208m',
        '\033[38;5;202m',
        '\033[38;5;196m',
    ]
    
    color_index = 0
    for line in text.splitlines():
        for char in line:
            print(colors[color_index % len(colors)] + char, end="")
            color_index += 1
        print(Style.RESET_ALL)
        time.sleep(0.05)

def get_gps_data() -> tuple:
    gps_gngga = None
    gps_gnrmc = None
    with open(get_resource_path(c.MAIN_DATA), "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1]  # Get the last line
            if len(last_line.strip()) > 0:
                try:
                    def split_latitude(lat):
                        lat_str = str(lat)
                        degrees = int(lat_str[:2])
                        minutes = float(lat_str[2:])
                        return degrees, minutes
                    
                    def split_longitude(lon):
                        lon_str = str(lon)
                        degrees = int(lon_str[:3])
                        minutes = float(lon_str[3:])
                        return degrees, minutes

                    def convert_to_decimal(degrees, minutes) -> float:
                        decimal = degrees + minutes / 60
                        return decimal
                    
                    data_fields = last_line.strip().split(" ")

                    gps_gngga = data_fields[c.DATA_DICT["cansat_gps_gngga"]]
                    gps_gnrmc = data_fields[c.DATA_DICT["cansat_gps_gnrmc"]]

                    individual_readings_gngga = gps_gngga.split(",")
                    gngga_data = {
                        "time": individual_readings_gngga[1],
                        "latitude": individual_readings_gngga[2],
                        "lat_direction": individual_readings_gngga[3],
                        "longitude": individual_readings_gngga[4],
                        "long_direction": individual_readings_gngga[5],
                        "estimated_altitude": individual_readings_gngga[9],
                    }

                    individual_readings_gnrmc = gps_gnrmc.split(",")
                    gnrmc_data = {
                        "speed": individual_readings_gnrmc[7],
                        "heading": individual_readings_gnrmc[8]
                    }

                    degrees, minutes = split_latitude(gngga_data["latitude"])
                    actual_latitude = convert_to_decimal(degrees, minutes)
                    if gngga_data["lat_direction"] == "S":
                        actual_latitude *= -1
                    degrees1, minutes1 = split_longitude(gngga_data["longitude"])
                    actual_longitude = convert_to_decimal(degrees1, minutes1)
                    if gngga_data["long_direction"] == "W":
                        actual_longitude *= -1
                    return (actual_latitude, actual_longitude, gngga_data["estimated_altitude"],
                            gngga_data["time"], gnrmc_data["speed"], gngga_data["time"])

                except Exception as e:
                    return None, None, None, None, None, None

    return None, None, None, None, None, None

def delete_line():
    with open(get_resource_path(c.MAIN_DATA), "r") as file:
        lines = file.readlines()
    lines.pop()

    with open(get_resource_path(c.MAIN_DATA), "w") as file:
        file.writelines(lines)
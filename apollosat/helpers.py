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
                   
                except (IndexError, ValueError) as e:
                    pass
    
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
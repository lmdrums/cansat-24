import os

ASCII_LOGO = """
 █████  ██████   ██████  ██      ██       ██████  ███████  █████  ████████ 
██   ██ ██   ██ ██    ██ ██      ██      ██    ██ ██      ██   ██    ██    
███████ ██████  ██    ██ ██      ██      ██    ██ ███████ ███████    ██    
██   ██ ██      ██    ██ ██      ██      ██    ██      ██ ██   ██    ██    
██   ██ ██       ██████  ███████ ███████  ██████  ███████ ██   ██    ██    
                                                                          
"""

# Folders

IMAGES_FOLDER = os.path.join("apollosat", "images")
FILES_FOLDER = os.path.join("apollosat", "files")

#  App

APP_TITLE = "ApolloSat"
FONT = ("Segoe UI", 12)
HEADER_FONT = ("Segoe UI", 15, "bold")
HEADER_FONT_NORMAL = ("Segoe UI", 15)
APP_ICON = os.path.join(IMAGES_FOLDER, "logo.ico")
BANNER_IMAGE = os.path.join(IMAGES_FOLDER, "banner.png")

# Data

MAIN_DATA = os.path.join(FILES_FOLDER, "data.txt")
PERMANENT_DATA = os.path.join(FILES_FOLDER, "permanent.txt")
DATA_DICT = {
    "packet_count":0,
    "radio_strength":1,
    "ground_temperature":2,
    "ground_pressure":3,
    "ground_humidity":4,
    "ground_gas":5,
    "cansat_temperature":6,
    "cansat_pressure":7,
    "cansat_estimated_altitude":8,
    "cansat_humidity":9,
    "cansat_gas":10,
    "cansat_gps_gngga":11,
    "cansat_gps_gnrmc":12
}
DATABASE_PATH = os.path.join(FILES_FOLDER, "offline_tiles.db")

# Serial
PORT = "COM3"
BAUDRATE = 9600
BYTESIZE = 8
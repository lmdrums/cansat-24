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
    "cansat_temperature":4,
    "cansat_pressure":5,
    "cansat_estimated_altitude":6,
    "cansat_humidity":7,
    "cansat_gas":8
}

# Serial
PORT = "COM3"
BAUDRATE = 9600
BYTESIZE = 8
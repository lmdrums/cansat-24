import os

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
GROUNDSTATION_DATA = os.path.join(FILES_FOLDER, "groundstation.txt")
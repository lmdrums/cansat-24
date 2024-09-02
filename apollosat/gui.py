from customtkinter import (CTk, CTkLabel, CTkFrame, CTkEntry, CTkButton, CTkOptionMenu,
                           CTkCheckBox, StringVar, CTkImage, CTkScrollableFrame, CTkToplevel,
                           set_appearance_mode, set_default_color_theme, CTkBaseClass, TOP, BOTH)
import tkintermapview as tkmap
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from PIL import Image, ImageTk

import apollosat.helpers as h
import apollosat.graphs as g
import apollosat.constants as c
from utils.path import get_resource_path

get_pillow_image = lambda relative_path: Image.open(get_resource_path(relative_path))

class App(CTk):
    def __init__(self) -> None:
        """Main application"""
    
        super().__init__()

        # Sets up the app
        self.title(c.APP_TITLE)
        self.iconbitmap(c.APP_ICON)
        self.frame = CTkFrame(self)
        self.frame.pack(expand=True, fill=BOTH, pady=10, padx=10, anchor="center")
        
        
        pil_image_banner = Image.open(get_resource_path(c.BANNER_IMAGE))
        pil_image_banner = pil_image_banner.resize((406,115))
        self.banner_image = ImageTk.PhotoImage(pil_image_banner)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        
        g.Temp(self) # Creates the temperature graph
        g.Humidity(self)
        g.Pressure(self)
        g.Gas(self)

        self.map = tkmap.TkinterMapView(self.frame, height=400)
        self.map.grid(column=0, row=1, padx=(20,0),sticky="ew")
        self.map.set_position(48.860381, 2.338594)
        self.map_option_menu = CTkOptionMenu(self.frame, values=["OpenStreetMap", "Google Normal", "Google Satellite"],
                                             command=self.change_map, font=c.FONT, width=160)
        self.map_option_menu.grid(column=2, row=5, pady=(10,0), sticky="e")

        self.radio_strength = CTkLabel(self.frame, text=f"Radio Strength:", font=c.HEADER_FONT)
        self.radio_strength.grid(column=0, row=2, padx=(20,0), pady=(10,0), sticky="e")
        self.est_altitude = CTkLabel(self.frame, text=f"Estimated Altitude:", font=c.HEADER_FONT)
        self.est_altitude.grid(column=0, row=3, padx=(20,0), pady=(10,0), sticky="e")
        self.gps_altitude = CTkLabel(self.frame, text=f"GPS Altitude:", font=c.HEADER_FONT)
        self.gps_altitude.grid(column=0, row=4, padx=(20,0), pady=(10,0), sticky="e")
        self.est_speed = CTkLabel(self.frame, text=f"Estimated Speed:", font=c.HEADER_FONT)
        self.est_speed.grid(column=0, row=5, padx=(20,0), pady=(10,0), sticky="e")

        self.banner = CTkLabel(self.frame, text="", image=self.banner_image)
        self.banner.grid(column=0, row=2, rowspan=4, pady=(20,0), padx=(20,0), sticky="w")

        self.radio_strength_label = CTkLabel(self.frame, text="80dB", font=c.HEADER_FONT_NORMAL)
        self.radio_strength_label.grid(column=1, row=2, padx=(5,0), pady=(10,0), sticky="w")
        self.est_altitude_label = CTkLabel(self.frame, text="80dB", font=c.HEADER_FONT_NORMAL)
        self.est_altitude_label.grid(column=1, row=3, padx=(5,0), pady=(10,0), sticky="w")
        self.gps_altitude_label = CTkLabel(self.frame, text="80dB", font=c.HEADER_FONT_NORMAL)
        self.gps_altitude_label.grid(column=1, row=4, padx=(5,0), pady=(10,0), sticky="w")
        self.est_speed_label = CTkLabel(self.frame, text="80dB", font=c.HEADER_FONT_NORMAL)
        self.est_speed_label.grid(column=1, row=5, padx=(5,0), pady=(10,0), sticky="w")
        
    def change_map(self, new_map: str):
        """Changes the view (tiles) of the map"""
        if new_map == "OpenStreetMap":
            self.map.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google Normal":
            self.map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "Google Satellite":
            self.map.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
     
def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
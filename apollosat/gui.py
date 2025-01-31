from customtkinter import (CTk, CTkLabel, CTkFrame, CTkEntry, CTkButton, CTkOptionMenu,
                           CTkCheckBox, StringVar, CTkImage, CTkScrollableFrame, CTkToplevel,
                           set_appearance_mode, set_default_color_theme, CTkBaseClass, TOP, BOTH)
import tkintermapview as tkmap
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from PIL import Image, ImageTk

import threading

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
        self.iconbitmap(get_resource_path(c.APP_ICON))
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
        
        self.map = tkmap.map_widget.TkinterMapView(self.frame, height=400, corner_radius=0,
                            use_database_only=True,
                            database_path=c.DATABASE_PATH)
        self.map.grid(column=0, row=1, padx=(20,0), sticky="ew")
        self.map.set_zoom(9)
        self.map.set_position(52.5, -1)
        self.map.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png") # OSM
        #self.map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22) # Google Maps (normal)

        self.radio_strength = CTkLabel(self.frame, text=f"Radio Strength:", font=c.HEADER_FONT)
        self.radio_strength.grid(column=0, row=2, padx=(20,0), pady=(10,0), sticky="e")
        
        ### CHANGE THIS TO ACCEL WHEN ACCELEROMETER ARRIVES!!
        self.est_altitude = CTkLabel(self.frame, text=f"Acceleration:", font=c.HEADER_FONT) 
        self.est_altitude.grid(column=0, row=3, padx=(20,0), pady=(10,0), sticky="e")
        ###

        self.gps_altitude = CTkLabel(self.frame, text=f"GPS Altitude:", font=c.HEADER_FONT)
        self.gps_altitude.grid(column=0, row=4, padx=(20,0), pady=(10,0), sticky="e")
        self.est_speed = CTkLabel(self.frame, text=f"Estimated Speed:", font=c.HEADER_FONT)
        self.est_speed.grid(column=0, row=5, padx=(20,0), pady=(10,0), sticky="e")

        self.banner = CTkLabel(self.frame, text="", image=self.banner_image)
        self.banner.grid(column=0, row=2, rowspan=4, pady=(20,0), padx=(20,0), sticky="w")

        self.radio_strength_label = CTkLabel(self.frame, text="-", font=c.HEADER_FONT_NORMAL)
        self.radio_strength_label.grid(column=1, row=2, padx=(5,0), pady=(10,0), sticky="w")
        self.est_altitude_label = CTkLabel(self.frame, text="-", font=c.HEADER_FONT_NORMAL)
        self.est_altitude_label.grid(column=1, row=3, padx=(5,0), pady=(10,0), sticky="w")
        self.gps_altitude_label = CTkLabel(self.frame, text="-", font=c.HEADER_FONT_NORMAL)
        self.gps_altitude_label.grid(column=1, row=4, padx=(5,0), pady=(10,0), sticky="w")
        self.est_speed_label = CTkLabel(self.frame, text="-", font=c.HEADER_FONT_NORMAL)
        self.est_speed_label.grid(column=1, row=5, padx=(5,0), pady=(10,0), sticky="w")
        self.clock_label = CTkLabel(self.frame, text="-", font=("Consolas", 15))
        self.clock_label.grid(column=2, row=5, padx=(5,0), pady=(5,0), sticky="e")
        self.record_data()
        self.animate_text()

    def flash_window_function(self, text: str):
        """Creates a flash window (transparent)"""

        self.flash_window = CTkToplevel(self)
        self.flash_window.geometry(f"{self.winfo_width()}x{self.winfo_height()}+{self.winfo_x()}+{self.winfo_y()}")
        self.flash_window.overrideredirect(True)
        self.flash_window.attributes("-topmost", True)
        self.flash_window.attributes("-alpha", 0.7)

        label = CTkLabel(
            self.flash_window, 
            text=text,
            font=("Segoe UI", 34, "bold"), 
            text_color="black",
            corner_radius=10
        )
        label.place(relx=0.5, rely=0.5, anchor="center")

        self.after(2000, self.flash_window.destroy)

    def record_data(self):
        """Records data to file"""
        def task():
            try:
                h.record_data(self)
            except Exception as e:
                print(f"Error during data recording: {e}")

        threading.Thread(target=task).start()
        self.after(1000, self.record_data)

    def animate_text(self):
        """Changes text fields in UI"""
        try:
            self.radio_strength_reading, self.estimated_altitude = h.animate_text()
            self.radio_strength_label.configure(text=f"{self.radio_strength_reading}dB")

            if self.estimated_altitude is not None:
                self.estimated_altitude = float(self.estimated_altitude)
                #self.est_altitude_label.configure(text=f"{round(self.estimated_altitude, 1)}m")
            else:
                self.est_altitude_label.configure(text="-")

            self.latitude, self.longitude, self.altitude, self.time, self.speed, self.gps_time = h.get_gps_data()

            if self.latitude is not None:
                self.map.set_position(self.latitude, self.longitude)
                self.map.delete_all_marker()
                self.map.set_marker(self.latitude, self.longitude)
                self.gps_altitude_label.configure(text=f"{self.altitude}m")
                self.est_speed_label.configure(text=f"{self.speed} knots")
                self.clock_label.configure(text=self.gps_time)

            self.after(1000, self.animate_text)

        except Exception as e:
            h.delete_line()
            self.animate_text()
     
def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
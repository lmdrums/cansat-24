from customtkinter import (CTk, CTkLabel, CTkFrame, CTkEntry, CTkButton, CTkOptionMenu,
                           CTkCheckBox, StringVar, CTkImage, CTkScrollableFrame, CTkToplevel,
                           set_appearance_mode, set_default_color_theme, CTkBaseClass, TOP, BOTH)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np

import cansat.helpers as h
import cansat.graphs as g

class App(CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Cansat 2024")
        self.frame = CTkFrame(self)
        self.frame.pack()
        g.Temp(self)
        
def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
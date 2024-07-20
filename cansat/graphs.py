import cansat.helpers as h
from customtkinter import (CTk, TOP, BOTH)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

font = {"fontname":"Segoe UI"}

class Temp:
    def __init__(self, parent: CTk) -> None:
        self.parent = parent
        self.fig, self.ax = plt.subplots()
        self.fig.set_figheight(4)
        self.fig.set_figwidth(6)
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent.frame)  
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.animate()

    def animate(self):
        x_list, y_list = h.animate("cansat/files/data.txt")
        self.ax.clear()
        self.ax.set_title("Temperature ('C)", **font)
        self.ax.set_ylabel("Temperature ('C)", **font)
        self.ax.set_xlabel("Time (s)", **font)
        
        self.ax.plot(x_list, y_list)
        self.canvas.draw()
        self.parent.after(1000, self.animate)
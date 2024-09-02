from customtkinter import (CTk, TOP, BOTH)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

import apollosat.helpers as h

font = {"fontname":"Segoe UI"}

class Temp:
    """Graph for temperature"""

    def __init__(self, parent: CTk) -> None:
        self.parent = parent
        self.fig, self.ax = plt.subplots()
        self.fig.set_figheight(4)
        self.fig.set_figwidth(6)
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent.frame)  
        self.canvas.get_tk_widget().grid(column=0, row=0, padx=(20,0), pady=(20,0), sticky="ew")
        self.animate()

    def animate(self) -> None:
        """Animates the graph every second"""

        x_list, y_list = h.animate("apollosat/files/data.txt")
        x2_list, y2_list = h.animate("apollosat/files/groundstation.txt")
        self.ax.clear()
        self.ax.set_title("Temperature ('C)", **font)
        self.ax.set_ylabel("Temperature ('C)", **font)
        self.ax.set_xlabel("Time (s)", **font)
        self.ax.plot(x_list, y_list, label="Cansat")
        self.ax.plot(x2_list, y2_list, label="Groundstation")
        self.ax.spines["right"].set_visible(False)
        self.ax.spines["top"].set_visible(False)
        self.ax.legend(fontsize="9")
        self.canvas.draw()
        self.parent.after(1000, self.animate) # Change this value if refresh rate IS NOT 1 second

# ---

class Humidity:
    def __init__(self, parent: CTk) -> None:
        self.parent = parent
        self.fig, self.ax = plt.subplots()
        self.fig.set_figheight(4)
        self.fig.set_figwidth(6)
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent.frame)  
        self.canvas.get_tk_widget().grid(column=1, row=0, pady=(20,0), sticky="ew")
        self.animate()

    def animate(self) -> None:
        """Animates the graph every second"""

        x_list, y_list = h.animate("apollosat/files/data.txt")
        x2_list, y2_list = h.animate("apollosat/files/groundstation.txt")
        self.ax.clear()
        self.ax.set_title("Humidity (%)", **font)
        self.ax.set_ylabel("Humidity (%)", **font)
        self.ax.set_xlabel("Time (s)", **font)
        self.ax.set_ylim(0,100)
        self.ax.plot(x_list, y_list, label="Cansat")
        self.ax.plot(x2_list, y2_list, label="Groundstation")
        self.ax.spines["right"].set_visible(False)
        self.ax.spines["top"].set_visible(False)
        self.ax.legend(fontsize="9")
        self.canvas.draw()
        self.parent.after(1000, self.animate) # Change this value if refresh rate IS NOT 1 second

# ---

class Pressure:
    def __init__(self, parent: CTk) -> None:
        self.parent = parent
        self.fig, self.ax = plt.subplots()
        self.fig.set_figheight(4)
        self.fig.set_figwidth(6)
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent.frame)  
        self.canvas.get_tk_widget().grid(column=2, row=0, pady=(20,0), sticky="ew")
        self.animate()

    def animate(self) -> None:
        """Animates the graph every second"""

        x_list, y_list = h.animate("apollosat/files/data.txt")
        x2_list, y2_list = h.animate("apollosat/files/groundstation.txt")
        self.ax.clear()
        self.ax.set_title("Pressure (hPa)", **font)
        self.ax.set_ylabel("Pressure (hPa)", **font)
        self.ax.set_xlabel("Time (s)", **font)
        self.ax.plot(x_list, y_list, label="Cansat")
        self.ax.plot(x2_list, y2_list, label="Groundstation")
        self.ax.spines["right"].set_visible(False)
        self.ax.spines["top"].set_visible(False)
        self.ax.legend(fontsize="9")
        self.canvas.draw()
        self.parent.after(1000, self.animate) # Change this value if refresh rate IS NOT 1 second

# ---

class Gas:
    def __init__(self, parent: CTk) -> None:
        self.parent = parent
        self.fig, self.ax = plt.subplots()
        self.fig.set_figheight(4)
        self.fig.set_figwidth(6)
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent.frame)  
        self.canvas.get_tk_widget().grid(column=1, row=1, sticky="w")
        self.animate()

    def animate(self) -> None:
        """Animates the graph every second"""

        x_list, y_list = h.animate("apollosat/files/data.txt")
        x2_list, y2_list = h.animate("apollosat/files/groundstation.txt")
        self.ax.clear()
        self.ax.set_title("Gas Quality (Ω)", **font)
        self.ax.set_ylabel("Humidity (Ω)", **font)
        self.ax.set_xlabel("Time (s)", **font)
        self.ax.plot(x_list, y_list, label="Cansat")
        self.ax.plot(x2_list, y2_list, label="Groundstation")
        self.ax.spines["right"].set_visible(False)
        self.ax.spines["top"].set_visible(False)
        self.ax.legend(fontsize="9")
        self.canvas.draw()
        self.parent.after(1000, self.animate) # Change this value if refresh rate IS NOT 1 second
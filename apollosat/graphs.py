from customtkinter import (CTk, TOP, BOTH)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.ticker import MaxNLocator

import apollosat.helpers as h
import apollosat.constants as c

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
        self.first_packet_count = None
        self.animate()

    def animate(self) -> None:
        """Animates the graph every second"""

        x_list, y_list = h.animate(c.DATA_DICT, "cansat_temperature")
        x2_list, y2_list = h.animate(c.DATA_DICT, "ground_temperature")

        # Determine the initial packet count
        if self.first_packet_count is None and x_list:
            self.first_packet_count = x_list[0]

        # Adjust x values to start from zero
        if self.first_packet_count is not None:
            x_list = [x - self.first_packet_count for x in x_list]
            x2_list = [x - self.first_packet_count for x in x2_list]

        self.ax.clear()
        self.ax.set_title("Temperature (°C)", **font)
        self.ax.set_ylabel("Temperature (°C)", **font)
        self.ax.set_xlabel("Time (~s)", **font)
        try:
            self.ax.plot(x_list, y_list, label="Cansat")
            self.ax.plot(x2_list, y2_list, label="Groundstation")
            self.ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            self.ax.spines["right"].set_visible(False)
            self.ax.spines["top"].set_visible(False)
            self.ax.legend(fontsize="9")
            self.ax.patch.set_edgecolor("black")
            self.ax.patch.set_linewidth(1)
            if y_list:
                min_pressure = min(min(y_list), min(y2_list))
                max_pressure = max(max(y_list), max(y2_list))
                self.ax.set_ylim(min_pressure - 1, max_pressure + 1)
            self.canvas.draw()
            self.parent.after(1000, self.animate) # Change this value if refresh rate IS NOT 1 second
        except ValueError:
            h.delete_line()
            return

class Humidity:
    def __init__(self, parent: CTk) -> None:
        self.parent = parent
        self.fig, self.ax = plt.subplots()
        self.fig.set_figheight(4)
        self.fig.set_figwidth(6)
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent.frame)  
        self.canvas.get_tk_widget().grid(column=1, row=0, pady=(20,0), sticky="ew")
        self.first_packet_count = None
        self.animate()

    def animate(self) -> None:
        """Animates the graph every second"""

        x_list, y_list = h.animate(c.DATA_DICT, "cansat_humidity")
        x2_list, y2_list = h.animate(c.DATA_DICT, "ground_humidity")

        # Determine the initial packet count
        if self.first_packet_count is None and x_list:
            self.first_packet_count = x_list[0]

        # Adjust x values to start from zero
        if self.first_packet_count is not None:
            x_list = [x - self.first_packet_count for x in x_list]
            x2_list = [x - self.first_packet_count for x in x2_list]
        self.ax.clear()
        self.ax.set_title("Humidity (%)", **font)
        self.ax.set_ylabel("Humidity (%)", **font)
        self.ax.set_xlabel("Time (~s)", **font)
        self.ax.set_ylim(0,100)
        try:
            self.ax.plot(x_list, y_list, label="Cansat")
            self.ax.plot(x2_list, y2_list, label="Groundstation")
            self.ax.xaxis.set_major_locator(MaxNLocator(integer=True))        
            self.ax.spines["right"].set_visible(False)
            self.ax.spines["top"].set_visible(False)
            self.ax.legend(fontsize="9")
            self.ax.patch.set_edgecolor("black")
            self.ax.patch.set_linewidth(1)
            self.canvas.draw()
            self.parent.after(1000, self.animate) # Change this value if refresh rate IS NOT 1 second
        except ValueError:
            h.delete_line()
            return

class Pressure:
    def __init__(self, parent: CTk) -> None:
        self.parent = parent
        self.fig, self.ax = plt.subplots()
        self.fig.set_figheight(4)
        self.fig.set_figwidth(6)
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent.frame)  
        self.canvas.get_tk_widget().grid(column=2, row=0, pady=(20,0), sticky="ew")
        self.first_packet_count = None
        self.animate()

    def animate(self) -> None:
        """Animates the graph every second"""

        x_list, y_list = h.animate(c.DATA_DICT, "cansat_pressure")
        x2_list, y2_list = h.animate(c.DATA_DICT, "ground_pressure")

        # Determine the initial packet count
        if self.first_packet_count is None and x_list:
            self.first_packet_count = x_list[0]

        # Adjust x values to start from zero
        if self.first_packet_count is not None:
            x_list = [x - self.first_packet_count for x in x_list]
            x2_list = [x - self.first_packet_count for x in x2_list]

        self.ax.clear()
        self.ax.set_title("Pressure (hPa)", **font)
        self.ax.set_ylabel("Pressure (hPa)", **font)
        self.ax.set_xlabel("Time (~s)", **font)
        self.ax.ticklabel_format(useOffset=False, style='plain', axis='y')

        try:
            self.ax.plot(x_list, y_list, label="Cansat")
            self.ax.plot(x2_list, y2_list, label="Groundstation")
            self.ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            self.ax.spines["right"].set_visible(False)
            self.ax.spines["top"].set_visible(False)
            self.ax.legend(fontsize="9")
            self.ax.patch.set_edgecolor("black")
            self.ax.patch.set_linewidth(1)
            if y_list:
                min_pressure = min(min(y_list), min(y2_list))
                max_pressure = max(max(y_list), max(y2_list))
                self.ax.set_ylim(min_pressure - 10, max_pressure + 10)
            self.canvas.draw()
            self.parent.after(1000, self.animate) # Change this value if refresh rate IS NOT 1 second
        except ValueError:
            h.delete_line()
            return

class Gas:
    def __init__(self, parent: CTk) -> None:
        self.parent = parent
        self.fig, self.ax = plt.subplots()
        self.fig.set_figheight(4)
        self.fig.set_figwidth(6)
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent.frame)  
        self.canvas.get_tk_widget().grid(column=1, row=1, sticky="w")
        self.first_packet_count = None
        self.animate()

    def animate(self) -> None:
        """Animates the graph every second"""

        x_list, y_list = h.animate(c.DATA_DICT, "cansat_gas")
        #x2_list, y2_list = h.animate(c.DATA_DICT, "ground_gas")

        # Determine the initial packet count
        if self.first_packet_count is None and x_list:
            self.first_packet_count = x_list[0]

        # Adjust x values to start from zero
        if self.first_packet_count is not None:
            x_list = [x - self.first_packet_count for x in x_list]
            #x2_list = [x - self.first_packet_count for x in x2_list]

        self.ax.clear()
        self.ax.set_title("Gas Quality (Ω)", **font)
        self.ax.set_ylabel("Gas Quality (Ω)", **font)
        self.ax.set_xlabel("Time (~s)", **font)
        try:
            self.ax.plot(x_list, y_list, label="Cansat")
            #self.ax.plot(x2_list, y2_list, label="Groundstation")
            self.ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            self.ax.spines["right"].set_visible(False)
            self.ax.spines["top"].set_visible(False)
            self.ax.legend(fontsize="9")
            self.ax.patch.set_edgecolor("black")
            self.ax.patch.set_linewidth(1)
            self.canvas.draw()
            self.parent.after(1000, self.animate) # Change this value if refresh rate IS NOT 1 second
        except ValueError:
            h.delete_line()
            return
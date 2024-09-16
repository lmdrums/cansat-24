from colorama import Style
import time

def animate(filename: str) -> tuple:
    """Pulls and returns data from the txt files so that the graph can be updated"""

    with open(filename) as data:
        pull_data = data.read()
        data_list = pull_data.split("\n")
        x_list = []
        y_list = []
        for line in data_list:
            if len(line) > 1:
                x, y = line.split(",")
                x_list.append(int(x))
                y_list.append(int(y))

    return x_list, y_list

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
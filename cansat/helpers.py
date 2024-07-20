def animate(filename: str) -> tuple:
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
def average(lst):
    return sum(lst) / len(lst)


def data_to_plot(data):
    avg_times = []
    maze_sizes = []
    times_array = []
    min_times = []
    max_times = []
    count_array = []
    avg_counts = []
    min_counts = []
    max_counts = []

    for maze in data:
        times_string = ""
        times_string = maze.get("timers")
        times_string = times_string.replace(" ", "")
        times_string = times_string.replace("[", "")
        times_string = times_string.replace("]", "")
        times = times_string.split(",")
        int_times = []
        for time in times:
            int_times.append(int(time))
        times_array.append(int_times)

    for maze in data:
        maze_sizes.append(int(maze.get("size")))

    for array in times_array:
        min_times.append(min(array))

    for array in times_array:
        max_times.append(max(array))

    for maze in data:
        count_string = ""
        count_string = maze.get("counts")
        count_string = count_string.replace(" ", "")
        count_string = count_string.replace("[", "")
        count_string = count_string.replace("]", "")
        counts = count_string.split(",")
        int_counts = []
        for count in counts:
            int_counts.append(int(count))
        count_array.append(int_counts)

    for array in count_array:
        avg_counts.append(round(average(array), 2))

    for array in times_array:
        avg_times.append(round(average(array), 2))

    for array in count_array:
        min_counts.append(min(array))

    for array in count_array:
        max_counts.append(max(array))

    plot_data_dict = {"avg_times": avg_times,
                      "maze_sizes": maze_sizes,
                      "times_array": times_array,
                      "min_times": min_times,
                      "max_times": max_times,
                      "count_array": count_array,
                      "avg_counts": avg_counts,
                      "min_counts": min_counts,
                      "max_counts": max_counts}

    return plot_data_dict

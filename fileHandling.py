import csv
import platform

def newline_system():
    if platform.system() == 'Windows':
        newline = ''
    else:
        newline = None
    return newline


def write_mazes_to_file(mazeList):
    try:
        with open('files//maze.csv', 'w', newline=newline_system()) as csvFile:
            writer = csv.writer(csvFile)
            for maze in mazeList:
                for row in maze:
                    writer.writerow(row)
    except FileNotFoundError:
        pass


def read_mazes_from_file():
    try:
        with open('files//maze.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)

            sizes = []
            row_grid = []
            full_grid = []
            all_mazes = []
            
            number_of_sizes = next(csv_reader)[0]

            for __ in range(int(number_of_sizes)):
                rows_in_maze = 0
                number_of_mazes = 0
                maze_info = next(csv_reader)
                maze_size = int(maze_info[0])
                sizes.append(maze_size)
                maze_numbers = int(maze_info[1])

                while(number_of_mazes < maze_numbers):
                    while(rows_in_maze < maze_size):
                        rows_in_maze += 1
                        for i in next(csv_reader):
                            row_grid.append(int(i))
                        full_grid.append(row_grid)
                        row_grid = []

                    rows_in_maze = 0
                    all_mazes.append(full_grid)
                    full_grid = []
                    number_of_mazes += 1
        return all_mazes, number_of_mazes, sizes
    except FileNotFoundError as e:
        raise e
    except StopIteration as e:
        raise e


def write_maze_dict(dict_data):
    try:
        with open('files//mazeinformation.csv', 'w', newline=newline_system()) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[
                                    "size", "timers", "counts"])
            writer.writeheader()
            # Når writer skriver timers array bliver det lavet til en string. hvoirfor?
            for data in dict_data:
                writer.writerow(data)
    except TypeError:
        pass


def read_maze_dict():
    try:
        with open('files//mazeinformation.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            maze_data_list = []
            maze_dict = {}
            keys = next(csv_reader)
            for row in csv_reader:
                maze_dict = {keys[0]: row[0], keys[1]: row[1],
                             keys[2]: row[2]}
                maze_data_list.append(maze_dict)
                maze_dict = {}
            return maze_data_list
    except FileNotFoundError:
        pass
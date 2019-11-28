import time
import csv
import platform

count = 0


def search(x, y, grid):
    global count
    if grid[x][y] == 2:
#        print("found at %d,%d" % (x, y))
        return True
    elif grid[x][y] == 1:
#        print('wall at %d,%d' % (x, y))
        return (False)
    elif grid[x][y] == 3:
        count += 1
#        print('visited at %d,%d' % (x, y))
        return (False)
#    print('visiting %d,%d' % (x, y))

# mark as visited
    grid[x][y] = 3

# explore neighbors clockwise starting by the one on the right
    if ((x < (len(grid)-1) and search(x+1, y, grid))
        or (y > 0 and search(x, y+1, grid))
        or (x > 0 and search(x-1, y, grid))
            or (y < len(grid)-1 and search(x, y-1, grid))):
        return True
#    print("Im out of the search")
    return False


def average_calculator(list_time):
    average = 0
    sum = 0
    for x in list_time:
        sum = sum+x
        average = sum/len(list_time)
    return average


def solve(all_mazes, number_of_mazes, sizes):
    global count
    k = 0
    maze_count = 0
    maze_dict_list = []
    maze_count = 0
    for k in range(len(sizes)):
        timers = []
        counts = []

        for __ in range(number_of_mazes):
            start = time.time_ns()
            search(1, 1, all_mazes[maze_count])
            end = time.time_ns()
            timers.append(end-start)
            counts.append(count)
            maze_count += 1
            count = 0
        mazeDict = {"size": int((sizes[k]-1)/2), "timers": timers,
                    "counts": counts, "avg_time": round(average_calculator(timers), 2)}
        maze_dict_list.append(mazeDict)
        k += 1
    # write_maze_info(maze_dict_list)
    return maze_dict_list


def solve_single_maze(maze):
    search(1, 1, maze)
    return maze







def write_maze_info(dict_data):
    if platform.system() == 'Windows':
        newline = ''
    else:
        newline = None

    try:
        with open('files//mazeinformation.csv', 'w', newline=newline) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[
                                    "size", "timers", "counts", "avg_time"])
            writer.writeheader()
            # Når writer skriver timers array bliver det lavet til en string. hvoirfor?
            for data in dict_data:
                writer.writerow(data)
    except FileNotFoundError:
        print("No file found, creating one")


def import_mazes():
    try:
        with open('files//maze.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)

            sizes = []
            row_grid = []
            full_grid = []
            all_mazes = []

            number_of_sizes = next(csv_reader)
            #j = 0
            for __ in range(int(number_of_sizes[0])):
                # while(int(number_of_sizes[0])>j):

                rows_in_maze = 0
                number_of_mazes = 0
                maze_info = next(csv_reader)
                maze_size = int(maze_info[0])
                sizes.append(maze_size)
                maze_numbers = int(maze_info[1])

                #print(maze_info[0] + " " + maze_info[1])
                #j += 1
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
    except (FileNotFoundError):
        print("Error. Try making new mazes")


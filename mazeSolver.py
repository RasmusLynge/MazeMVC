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
                    "counts": counts}
        maze_dict_list.append(mazeDict)
        k += 1
    return maze_dict_list


def solve_single_maze(maze):
    search(1, 1, maze)
    return maze
import time
import csv
import os
import platform

import threading
import concurrent.futures


count = 0

# Checking each neighbor field around the field the program is standing on
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
        or (y > 0 and search(x, y-1, grid))
        or (x > 0 and search(x-1, y, grid))
        or (y < len(grid)-1 and search(x, y+1, grid))):
        return True
#    print("Im out of the search")
    return False


def threadTask(all_mazes, maze_counter,thread_id,counts_map,timer_map):
    global count

    start = time.time_ns()
    search(1, 1, all_mazes[maze_counter])
    end = time.time_ns()

    timer_map[thread_id] = end-start
    counts_map[thread_id] = count

    count = 0
    #Lig hver sin thread ned i et hashmap, med tilhørende id. Gem informationen count

def solve(all_mazes,  number_of_mazes, sizes):
   
    maze_dict_list = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_mazes) as executor:
   
        iterator = 0
        for size in range(len(sizes)):

            timer_map=dict()
            counts_map=dict()
            for maze_count in range(number_of_mazes):
                thread_id = "ID"+str(size)+str(maze_count)
                executor.submit( threadTask(all_mazes, iterator,thread_id,counts_map,timer_map))
                iterator+=1
                
                

            mazeDict = {"size": int((sizes[size]-1)/2),"timers": list(timer_map.values()), "counts": list(counts_map.values())}
            maze_dict_list.append(mazeDict)

    return maze_dict_list

def solve_single_maze(maze):
    search(1, 1, maze)
    return maze

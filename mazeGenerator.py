from random import randint, shuffle, choice
import sys
import csv
import platform
import os

import threading
import time
import concurrent.futures


#needed for DFS...
sys.setrecursionlimit(10000)

#Each maze cell contains a tuple of directions of cells to which it is connected
#Takes a maze and converts it to an array of 1's and blanks to represent walls, etc
def convert(maze, mazeList):
    pretty_maze = [["1"]*(2*len(maze[0])+1) for a in range(2*len(maze)+1)]
    for y,row in enumerate(maze):
        for x,col in enumerate(row):
            pretty_maze[2*y+1][2*x+1] = "0"
            for direction in col:
                pretty_maze[2*y+1+direction[0]][2*x+1+direction[1]] = "0"
    pretty_maze[len(maze*2)-1][len(maze*2)-1] = "2"
    #global mazeList
    mazeList.append(pretty_maze)
    return pretty_maze

#Returns an empty maze of given size
def make_empty_maze(width, height):
    maze = [[[] for b in range(width)] for a in range(height)]
    return maze

#Recursive backtracker.
#Looks at its neighbors randomly, if unvisitied, visit and recurse
def DFS(maze, coords=(0,0)):
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    shuffle(directions)
    for direction in directions:
        new_coords = (coords[0] + direction[0], coords[1] + direction[1])
        if (0 <= new_coords[0] < len(maze)) and \
        (0 <= new_coords[1] < len(maze[0])) and \
        not maze[new_coords[0]][new_coords[1]]:
            maze[coords[0]][coords[1]].append(direction)
            maze[new_coords[0]][new_coords[1]].append((-direction[0], -direction[1]))
            DFS(maze, new_coords)
    return maze

def generate(number_of_mazes, sizes):
    mazeList = []
    mazeList.append(([[len(sizes)]]))
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_mazes) as executor:
        for x in sizes:
            mazeList.append([[x*2+1, number_of_mazes]])
            for _ in range(number_of_mazes):
                executor.submit(convert(DFS(make_empty_maze(x,x)), mazeList))
    write_to_file(mazeList)
    return mazeList
 

def write_to_file(mazeList):
    with open('files//maze.csv', 'w',newline='') as csvFile:
            writer = csv.writer(csvFile)
            for maze in mazeList:
                for row in maze:
                    writer.writerow(row)


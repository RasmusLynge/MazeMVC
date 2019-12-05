import fileHandling as db


def write_mazes_to_file(maze_list):
    db.write_mazes_to_file(maze_list)

def read_mazes_from_file():
    # db.read_mazes_from_file() returns list with mazes, a number of mazes and a size of mazes.
    maze_list, __, __ = db.read_mazes_from_file()
    return maze_list

def write_maze_dict(maze_dict_list):
    db.write_maze_dict(maze_dict_list)

def read_maze_dict():
    # returns list of dicts
    data = db.read_maze_dict()
    return data

def read_maze_and_data_from_file():
    all_mazes, number_of_mazes, sizes = db.read_mazes_from_file()
    return all_mazes, number_of_mazes, sizes
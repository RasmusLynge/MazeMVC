import mazeGenerator as maze_generator
import mazeSolver as maze_solver
import dataToPlot as data_to_plot

import TKView
import model

def mazes_from_file():
   return model.read_mazes_from_file()

def solve_one_maze(maze):
   # retuner muligvis også maze data? count time ect...
   return maze_solver.solve_single_maze(maze)

def generate_mazes(number_of_mazes, sizes):
   maze_list = maze_generator.generate(number_of_mazes, sizes)
   model.write_mazes_to_file(maze_list)

def show_plot():
   # Få alle mazes ud af 
   all_mazes, number_of_mazes, sizes = model.read_maze_and_data_from_file()
   # løs alle mazes (mazes solve)
   maze_dict_list = maze_solver.solve(all_mazes, number_of_mazes, sizes)
   # lig dataen fra løsning i fil
   model.write_maze_dict(maze_dict_list)
   # hent fil ud (model.read_maze_dict)
   maze_dict = model.read_maze_dict()
   # lav brugbar data (maze_dict to data)
   plot_data = data_to_plot.data_to_plot(maze_dict)
   # send dataen og lad View kalde plotning
   return plot_data




if __name__ == "__main__":
   # running controller function
   # Skal køre TKview
   TKView.start_plot()
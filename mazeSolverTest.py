import unittest
import mazeSolver as ms
import mazeGenerator as mg
import controller as ct
import fileHandling as fh

class TestSolver(unittest.TestCase):
    def setUp(self):
        self.size = 10
        self.maze_list = mg.generate(1,[self.size])
        self.maze =[]
        for row in self.maze_list[2]:
            row =[int(x) for x in row]
            self.maze.append(row)
        self.solved_maze = ms.solve_single_maze(self.maze)

    def test_path_around_endpoint_visisted(self):  
       left_index_from_end = self.solved_maze[len(self.solved_maze)-2][len(self.solved_maze[len(self.solved_maze)-2])-3]
       top_index_from_end = self.solved_maze[len(self.solved_maze)-3][len(self.solved_maze[len(self.solved_maze)-3])-2]
       self.assertEqual(left_index_from_end or top_index_from_end, 3,"No path visited around the finish")
    
    def test_each_row_contains_a_visited_path(self):
        for index in range(1,len(self.solved_maze)-2):
            if 3 in self.solved_maze[index]:
                self.assertTrue(True)
            else:
                self.assertTrue(False,"No visited path in row: "+ str(index) )

if __name__ == '__main__':
    print("Starting unit-test")
    unittest.main()
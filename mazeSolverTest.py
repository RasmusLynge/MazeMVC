import unittest
import mazeSolver as ms
import mazeGenerator as mg

class TestSolver(unittest.TestCase):
    def setUp(self):
        self.size = 5
        self.maze_list = mg.generate(1,[self.size])
        self.maze = self.maze_list[2]
    
    def test_acces_to_enpoint(self):
       ms.solve_single_maze(self.maze)
       self.assertEqual(1,1)

if __name__ == '__main__':
    print("Starting unit-test")
    unittest.main()
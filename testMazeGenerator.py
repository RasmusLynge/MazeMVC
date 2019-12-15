import unittest
import mazeGenerator as mg

class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.size = 5
        self.maze_list = mg.generate(1,[self.size])
        self.maze = self.maze_list[2]

    def test_generator_wall(self):
        self.assertListEqual(self.maze[0],['1']*(self.size*2+1),"Maze top wall dosn't fit the requirement")
        self.assertListEqual(self.maze[2*self.size],['1']*(self.size*2+1),"Maze bottom wall dosn't fit the requirement")
        for row in self.maze_list[2]:
            self.assertEqual(row[0],'1',"The rows dosnt first and last index dosn't match a wall")
            self.assertEqual(row[len(row)-1],'1',"The rows dosnt first and last index dosn't match a wall")
    
    def test_endpoint(self):
        self.assertEqual(self.maze[len(self.maze)-2][9],'2',"There's no endpoint at the correct location")
    
    def test_correct_size_Input(self):
        self.assertEqual(self.maze_list[1][0][0],self.size*2+1,"The input size dosnt match the size in maze_list")
        self.assertEqual(len(self.maze) and len(self.maze[0]),self.size*2+1,"The generated maze dosnt match the size input")

    def test_is_maze_empty(self):
        self.assertTrue(self.maze is not [],"The maze array is empty")
  
if __name__ == '__main__':
    print("Starting unit-test")
    unittest.main()
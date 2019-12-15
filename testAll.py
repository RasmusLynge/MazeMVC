import unittest
import testException
import testMazeGenerator
import testMazeSolver

if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromModule(testMazeSolver)
    suite2 = unittest.TestLoader().loadTestsFromModule(testException)
    suite3 = unittest.TestLoader().loadTestsFromModule(testMazeGenerator)
    unittest.TextTestRunner(verbosity=2).run(suite1)
    unittest.TextTestRunner(verbosity=2).run(suite2)
    unittest.TextTestRunner(verbosity=2).run(suite3)

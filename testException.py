import unittest
import fileHandling as fh
import controller as ct
import mazeGenerator

class TestException(unittest.TestCase):
    def setUp(self):
        fh.write_mazes_to_file([])

    def test_fileNotFound(self):
        self.assertRaises(StopIteration,fh.read_mazes_from_file)

    def test_ValueError_not_an_Integer(self):
        self.assertRaises(ValueError,mazeGenerator.generate,5,["s"])

if __name__ == '__main__':
    print("Starting unit-test")
    unittest.main()
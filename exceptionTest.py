import unittest
import fileHandling as fh

class TestException(unittest.TestCase):
    def setUp(self):
        fh.write_mazes_to_file([])
    def testFileNotFound(self):
        #self.assertRaises(StopIteration,fh.read_mazes_from_file)
        with self.assertRaises(StopIteration) as cm:
            fh.read_mazes_from_file()
        print("------------------")
        print(cm.exception)
        self.assertTrue("Error. Try making new mazes" in cm.exception) 
 
if __name__ == '__main__':
    print("Starting unit-test")
    unittest.main()
import unittest   # The test framework
from Subseq1 import compute

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compute([2, 7, 5], [2,5]), 2)

    def test_2(self):
        self.assertEqual(compute([7], [1,2,3,4]), 0)
    
    def test_3(self):
        self.assertEqual(compute([2, 7, 8, 3], [5,2,8,7]), 2)

    def test_4(self):
        self.assertEqual(compute([2, 3, 9], [2, 9, 7, 8]), 2)
    
if __name__ == '__main__':
    unittest.main()

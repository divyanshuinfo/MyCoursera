import unittest   # The test framework
from Subseq2 import compute

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compute([1, 2, 3], [2, 1, 3], [1,3,5]), 2)

    def test_2(self):
        self.assertEqual(
            compute([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6,8,3,1,4,7]), 3)
    
if __name__ == '__main__':
    unittest.main()

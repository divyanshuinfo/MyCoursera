import unittest   # The test framework
from Primitive_Calculator import compute

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compute(1), [0, [1]])
    def test_2(self):
        self.assertEqual(compute(5), [3, [1, 2, 4, 5]], compute(5))

    def test_3(self):
        self.assertEqual(compute(96234), [14, [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234]])
    
if __name__ == '__main__':
    unittest.main()

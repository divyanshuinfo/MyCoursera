import unittest   # The test framework
from Edit_Distance import compute

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compute("ab", "ab"), 0)

    def test_2(self):
        self.assertEqual(compute("short", "ports"), 3)
    
    def test_3(self):
        self.assertEqual(compute("editing", "distance"), 5)
    
if __name__ == '__main__':
    unittest.main()

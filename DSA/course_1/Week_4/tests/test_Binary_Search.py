import unittest   # The test framework
from Binary_Search import compute

def convert(line):
    return list(map(int, line.split()))

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compute(convert("1 5 8 12 13"), convert("8 1 23 1 11")), "2 0 -1 0 -1")
    
    def test_2(self):
        self.assertEqual(compute(convert("1 2 3 4 5"),
                         convert("1 2 3 4 5")), "0 1 2 3 4")


if __name__ == '__main__':
    unittest.main()

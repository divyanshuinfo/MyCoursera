import unittest   # The test framework
from Money_Change_Again import compute

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compute(2), 2)
    def test_2(self):
        self.assertEqual(compute(34), 9)
    
if __name__ == '__main__':
    unittest.main()

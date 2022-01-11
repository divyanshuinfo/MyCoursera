import unittest   # The test framework
from Majority_Element import compute


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compute([2,3,9,2,2], 5), True)

    def test_2(self):
        self.assertEqual(compute([1,2,3,4], 4), False)

    def test_3(self):
        self.assertEqual(compute([1,2,3,1], 4), False)

    def test_4(self):
        self.assertEqual(compute([512766168, 717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772], 10), False)

if __name__ == '__main__':
    unittest.main()

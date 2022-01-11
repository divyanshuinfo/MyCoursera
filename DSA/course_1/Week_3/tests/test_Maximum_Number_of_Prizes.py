import unittest   # The test framework
from Maximum_Number_of_Prizes import Compute_Maximum_Number_of_Prizes


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Compute_Maximum_Number_of_Prizes(6), "3\n1 2 3")

    def test_2(self):
        self.assertEqual(Compute_Maximum_Number_of_Prizes(8), "3\n1 2 5")

    def test_3(self):
        self.assertEqual(Compute_Maximum_Number_of_Prizes(2), "1\n2")

    def test_4(self):
        self.assertEqual(Compute_Maximum_Number_of_Prizes(1), "1\n1")

if __name__ == '__main__':
    unittest.main()

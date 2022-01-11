import unittest   # The test framework
from Maximum_Salary import Maximum_Salary


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Maximum_Salary(list(map(str, [21, 2]))), 221)

    def test_2(self):
        self.assertEqual(Maximum_Salary(list(map(str, [9, 4, 6, 1, 9]))), 99641)

    def test_3(self):
        self.assertEqual(Maximum_Salary(list(map(str, [23, 39, 92]))), 923923)

    # def test_4(self):
    #     self.assertEqual(Maximum_Salary(1), "1\n1")

if __name__ == '__main__':
    unittest.main()

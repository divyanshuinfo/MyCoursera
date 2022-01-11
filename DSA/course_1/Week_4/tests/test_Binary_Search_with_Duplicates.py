import unittest   # The test framework
from Binary_Search_with_Duplicates import compute
from Binary_Search_with_Duplicates import first
import random
from algorithms.sort import quick_sort

def convert(line):
    return list(map(int, line.split()))

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compute(convert("1 5 8 12 13"), convert("8 1 23 1 11")), "2 0 -1 0 -1")

    def test_2(self):
        self.assertEqual(compute(convert("2 4 4 4 7 7 9"), convert(
            "9 4 5 2")), ("6 1 -1 0"))

    def test_3(self):
        for i in range(1000):
            lst = []
            for i in range(random.randint(0, 5000)):
                lst.append(random.randint(0, 5000))
            check = random.randint(0, 5000)
            lst.sort()
            value = first(lst, check)
            try:
                value2 = lst.index(check)
            except:
                value2 = -1
            self.assertEqual(value, value2, (lst, check))
            
    

if __name__ == '__main__':
    unittest.main()

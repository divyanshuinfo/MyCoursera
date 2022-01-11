import unittest   # The test framework
from Organizing_a_Lottery import compute
from random import randint
from Organizing_a_Lottery import naive_compute

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compute(2, 3, [[0, 5], [7, 10]], [1, 6, 11]), "1 0 0")
    def test_2(self):
        self.assertEqual(compute(1, 3, [[-10, 10]], [-100, 100, 0]), "0 0 1")
    def test_3(self):
        self.assertEqual(
            compute(3, 2, [[0, 5], [-3, 2], [7, 10]], [1, 6]), "2 0")

    def test_4(self):
        for i in range(100):
            s = randint(0, 500)
            p = randint(0, 500)
            lst = []
            lst2 = []
            for j in range(s):
                x = randint(-500, 500)
                y = 0
                while y < x:
                    y = randint(-500, 500)
                lst.append([x, y])
            for k in range(p):
                lst2.append(randint(-500, 500))
            
            self.assertEqual(
                compute(s, p, lst, lst2), naive_compute(s, p, lst, lst2), (s, p, lst, lst2))
    # def test_4(self):
    #     self.assertEqual(compute(2, 3, [[0, 5], [7, 10]], [1, 6, 11]), True)
if __name__ == '__main__':
    unittest.main()

import unittest   # The test framework
from Car_Fueling import compute_min_refills


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compute_min_refills( 950, 400, 4, [200, 375, 550, 750]), 2)

    def test_2(self):
        self.assertEqual(compute_min_refills(10,3,4,[1, 2, 5, 9]), -1)

    def test_3(self):
        self.assertEqual(compute_min_refills(200,
                                             250,
                                             2,
                                             [100, 150]), 0)
    def test_4(self):
        self.assertEqual(compute_min_refills(700,
                                             200,
                                             4,
                                             [100, 200, 300, 400]), -1)

if __name__ == '__main__':
    unittest.main()

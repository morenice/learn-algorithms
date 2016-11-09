import unittest
import solve


class SolveTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve.find_fraction(14), '2/4')
        self.assertEqual(solve.find_fraction(1), '1/1')
        self.assertEqual(solve.find_fraction(5), '2/2')
        self.assertEqual(solve.find_fraction(8), '2/3')

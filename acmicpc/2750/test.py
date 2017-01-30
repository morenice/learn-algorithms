import unittest
import solve


class TestSelectSort(unittest.TestCase):
    def test_sort1(self):
        input_list = list()
        input_list.append(5)
        input_list.append(4)
        input_list.append(3)
        input_list.append(2)
        input_list.append(1)

        solve.sort_select(input_list)

        self.assertEqual(input_list[0], 1)
        self.assertEqual(input_list[1], 2)
        self.assertEqual(input_list[2], 3)
        self.assertEqual(input_list[3], 4)
        self.assertEqual(input_list[4], 5)
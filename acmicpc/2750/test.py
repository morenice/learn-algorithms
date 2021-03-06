import unittest
import solve


class TestSelectSort(unittest.TestCase):
    def test_sort_select1(self):
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

    def test_sort_select2(self):
        input_list = list()
        input_list.append(100)
        input_list.append(55)
        input_list.append(23)
        input_list.append(77)
        input_list.append(99)

        solve.sort_select(input_list)

        self.assertEqual(input_list[0], 23)
        self.assertEqual(input_list[1], 55)
        self.assertEqual(input_list[2], 77)
        self.assertEqual(input_list[3], 99)
        self.assertEqual(input_list[4], 100)

    def test_sort_insertion1(self):
        input_list = list()
        input_list.append(5)
        input_list.append(4)
        input_list.append(3)
        input_list.append(2)
        input_list.append(1)

        solve.sort_insertion(input_list)

        self.assertEqual(input_list[0], 1)
        self.assertEqual(input_list[1], 2)
        self.assertEqual(input_list[2], 3)
        self.assertEqual(input_list[3], 4)
        self.assertEqual(input_list[4], 5)

    def test_sort_insertion2(self):
        input_list = list()
        input_list.append(100)
        input_list.append(55)
        input_list.append(23)
        input_list.append(77)
        input_list.append(99)

        solve.sort_insertion(input_list)

        self.assertEqual(input_list[0], 23)
        self.assertEqual(input_list[1], 55)
        self.assertEqual(input_list[2], 77)
        self.assertEqual(input_list[3], 99)
        self.assertEqual(input_list[4], 100)



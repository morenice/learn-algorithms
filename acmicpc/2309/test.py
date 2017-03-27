import unittest
import solve


class TestSelectSort(unittest.TestCase):
    def test_find_dwarf(self):
        input_list = list()

        input_list.append(20)
        input_list.append(7)
        input_list.append(23)
        input_list.append(19)
        input_list.append(10)
        input_list.append(15)
        input_list.append(25)
        input_list.append(8)
        input_list.append(13)

        new_list = solve.find_dwarf_for_princess(input_list)

        self.assertEqual(new_list[0], 7)
        self.assertEqual(new_list[1], 8)
        self.assertEqual(new_list[2], 10)
        self.assertEqual(new_list[3], 13)
        self.assertEqual(new_list[4], 19)
        self.assertEqual(new_list[5], 20)
        self.assertEqual(new_list[6], 23)

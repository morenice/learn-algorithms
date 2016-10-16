import unittest
import solve


class TestHoneycomb(unittest.TestCase):
    def test_pass_room1(self):
        self.assertEqual(solve.get_pass_room_count_honeycomb(13), 3)
        self.assertEqual(solve.get_pass_room_count_honeycomb(58), 5)
        self.assertEqual(solve.get_pass_room_count_honeycomb(25), 4)

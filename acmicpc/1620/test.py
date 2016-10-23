import unittest
import solve


class PocketBookTest(unittest.TestCase):
    def setUp(self):
        input_data = """
        Bulbasaur
        Ivysaur
        Venusaur
        Charmander
        Charmeleon
        Charizard
        Squirtle
        Wartortle
        Blastoise
        Caterpie
        Metapod
        Butterfree
        Weedle Kakuna
        Beedrill
        Pidgey
        Pidgeotto
        Pidgeot
        Rattata
        Raticate
        Spearow
        Fearow
        Ekans
        Arbok
        Pikachu
        Raichu
        """
        self.pocket_book = solve.create_pocketbook()
        for data in input_data.split():
            self.pocket_book.append(data)

    def tearDown(self):
        del(self.pocket_book)

    def test_find_pocket_by_name(self):
        self.assertEqual(solve.find_pocketbook_by_name(self.pocket_book, 'Bulbasaur'), 1)
        self.assertEqual(solve.find_pocketbook_by_name(self.pocket_book, 'Ekans'), 23)
        self.assertEqual(solve.find_pocketbook_by_name(self.pocket_book, 'Pikachu'), 25)

    def test_find_pocket_by_index(self):
        self.assertEqual(solve.find_pocketbook_by_index(self.pocket_book, 23), 'Ekans')
        self.assertEqual(solve.find_pocketbook_by_index(self.pocket_book, 22), 'Fearow')


if __name__ == '__main__':
    unittest.main()

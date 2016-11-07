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
        self.pocketbook = solve.create_pocketbook()
        self.bs_pocketbook = solve.create_bs_pocketbook()
        for data in input_data.split():
            solve.add_pocketbook(self.pocketbook, data)
            solve.add_bs_pocketbook(self.bs_pocketbook, data)

        self.bs_pocketbook.sort(key=lambda r: r[0])
        self.bs_keys = [p[0] for p in self.bs_pocketbook]

    def tearDown(self):
        del(self.pocketbook)

    def test_find_pocket_by_name(self):
        self.assertEqual(solve.find_bs_pocketbook(self.bs_pocketbook, self.bs_keys, 'Bulbasaur'), 1)
        self.assertEqual(solve.find_bs_pocketbook(self.bs_pocketbook, self.bs_keys, 'Ekans'), 23)
        self.assertEqual(solve.find_bs_pocketbook(self.bs_pocketbook, self.bs_keys, 'Pikachu'), 25)

    def test_find_pocket_by_index(self):
        self.assertEqual(solve.find_pocketbook(self.pocketbook, 1), 'Bulbasaur')
        self.assertEqual(solve.find_pocketbook(self.pocketbook, 22), 'Fearow')
        self.assertEqual(solve.find_pocketbook(self.pocketbook, 22), 'Fearow')


if __name__ == '__main__':
    unittest.main()

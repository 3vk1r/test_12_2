from runner_and_tournament import Runner, Tournament
from unittest import TestCase as TC
import unittest

class TournamentTest(TC):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usain = Runner('Усейн', 10)
        self.Andrei = Runner('Андрей', 9)
        self.Nick = Runner('Ник', 3)

    def test1(self):
        tournament = Tournament(90, self.Usain, self.Nick)
        result = tournament.start()
        last_runner = result[max(result.keys())]
        self.assertTrue(last_runner == 'Ник')
        self.all_results['tour1'] = result
    def test2(self):
        tournament = Tournament(90, self.Andrei, self.Nick)
        result = tournament.start()
        last_runner = result[max(result.keys())]
        self.assertTrue(last_runner == 'Ник')
        self.all_results['tour2'] = result
    def test3(self):
        tournament = Tournament(90, self.Usain, self.Andrei, self.Nick)
        result = tournament.start()
        last_runner = result[max(result.keys())]
        self.assertTrue(last_runner == 'Ник')
        self.all_results['tour3'] = result
    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            print(key, end= ': ')
            for items, value in cls.all_results[key].items():
                print(items, '-', value, end=' ')
            print()


if __name__ == '__main__':
    unittest.main()
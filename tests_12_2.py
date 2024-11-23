import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = Runner("Усэйн", 10)
        self.r2 = Runner("Андрей", 9)
        self.r3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for name, result in cls.all_results.items():
            print(f'{name}')
            for key, value in result.items():
                print(f'\t{key}: {value}')


    def test_race1(self):
        tournament_1 = Tournament(90, self.r1, self.r3)
        results = tournament_1.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
        self.all_results['1'] = results

    def test_race2(self):
        tournament_2 = Tournament(90, self.r2, self.r3)
        results = tournament_2.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
        self.all_results['2'] = results

    def test_race3(self):
        tournament_3 = Tournament(90, self.r1, self.r2, self.r3)
        results = tournament_3.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
        self.all_results['3'] = results


    if __name__ == "__main__":
        unittest.main()
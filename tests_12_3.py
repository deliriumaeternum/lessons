import unittest
from runner_and_tournament import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        r1 = Runner('Usain Bolt')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance,50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        r2 = Runner('Andre De Grasse')
        for i in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        r3 = Runner('Letsile Tebogo')
        r4 = Runner('Shawn Crawford')
        for i in range(10):
            r3.run()
            r4.walk()
        self.assertNotEqual(r3.distance, r4.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
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

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_race1(self):
        tournament_1 = Tournament(90, self.r1, self.r3)
        results = tournament_1.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
        self.all_results['1'] = results

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_race2(self):
        tournament_2 = Tournament(90, self.r2, self.r3)
        results = tournament_2.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
        self.all_results['2'] = results

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_race3(self):
        tournament_3 = Tournament(90, self.r1, self.r2, self.r3)
        results = tournament_3.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
        self.all_results['3'] = results


    if __name__ == "__main__":
        unittest.main()
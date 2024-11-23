import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        r1 = Runner('Usain Bolt')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance,50)

    def test_run(self):
        r2 = Runner('Andre De Grasse')
        for i in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    def test_challenge(self):
        r3 = Runner('Letsile Tebogo')
        r4 = Runner('Shawn Crawford')
        for i in range(10):
            r3.run()
            r4.walk()
        self.assertNotEqual(r3.distance, r4.distance)

if __name__ == "__main__":
    unittest.main()
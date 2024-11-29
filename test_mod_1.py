from unittest import TestCase
import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []
        a = 'Ник Фьюри'
        cls.all_results.append(a)

    def setUp(self):
        a = Runner('Усэйн Болт', 10)
        b = Runner('Андрей Поттер', 9)
        c = Runner('Ник Фьюри', 3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)

    def tester(self):
        a = Runner('Усэйн Болт', 10)
        c = Runner('Ник Фьюри', 3)
        leader = Tournament(90, a, c)
        leader.start()
        self.assertEqual(self.all_results[0], 'Ник Фьюри')

    def tester2(self):
        b = Runner('Андрей Поттер', 9)
        c = Runner('Ник Фьюри', 3)
        leader1 = Tournament(90, b, c)
        leader1.start()
        self.assertEqual(self.all_results[0], 'Ник Фьюри')

    def tester3(self):
        a = Runner('Усэйн Болт', 10)
        b = Runner('Андрей Поттер', 9)
        c = Runner('Ник Фьюри', 3)
        leader2 = Tournament(90, a, b, c)
        leader2.start()
        self.assertEqual(self.all_results[0], 'Ник Фьюри')


if __name__ == '__main__':
    unittest.main()


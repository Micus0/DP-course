import unittest


class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        mediator.people.append(self)

    def say(self, value):
        self.mediator.broadcast(self, value)


# without events
class Mediator:
    def __init__(self):
        self.people = []

    def broadcast(self, sender, value):
        for person in self.people:
            if person != sender:
                person.value += value


class FirstTestSuite(unittest.TestCase):
    def test(self):
        m = Mediator()
        p1 = Participant(m)
        p2 = Participant(m)

        self.assertEqual(0, p1.value)
        self.assertEqual(0, p2.value)

        p1.say(2)

        self.assertEqual(0, p1.value)
        self.assertEqual(2, p2.value)

        p2.say(4)

        self.assertEqual(4, p1.value)
        self.assertEqual(2, p2.value)

from unittest import TestCase
from app.Amity import Amity


class TestFunctionality(TestCase):

    def setUp(self):
        self.amity = Amity()

    def test_room_is_created(self):
        original_room_count = len(self.amity.rooms)
        self.amity.create_room('Camelot', 'Office')
        new_room_count = len(self.amity.rooms)
        self.assertEqual(
            new_room_count,
            original_room_count + 1,
            msg='''Room count should increment on office creation'''
        )

        self.amity.create_room('Ruby', 'Living Space')
        new_room_count = len(self.amity.rooms)
        self.assertEqual(
            new_room_count,
            original_room_count + 2,
            msg='''Room count should increment on living space creation'''
        )

    def test_add_person(self):
        joshua = self.amity.add_person('Joshua Mwaniki', 'Staff')
        self.assertIn(
            joshua,
            self.amity.people,
            msg='''Should be able to add staff'''
        )

        john = self.amity.add_person('John Doe', 'Fellow', 'Y')
        self.assertIn(
            john,
            self.amity.people,
            msg='''Should be able to add fellows with accomodation'''
        )

        jane = self.amity.add_person('Jane Doe', 'Fellow', 'N')
        self.assertIn(
            jane,
            self.amity.people,
            msg='''Should be able to add fellows without accomodation'''
        )

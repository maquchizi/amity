from unittest import TestCase
from app.Amity import Amity


class TestFunctionality(TestCase):

    def setUp(self):
        self.amity = Amity()
        self.amity.create_room('Test Office', 'Office')
        self.amity.create_room('Test Living Space', 'Living Space')

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
        original_people_count = len(self.amity.people)

        self.amity.add_person('Joshua Mwaniki', 'Staff')
        new_people_count = len(self.amity.people)
        self.assertEqual(
            original_people_count,
            new_people_count - 1,
            msg='''Should be able to add staff'''
        )

        self.amity.add_person('John Doe', 'Fellow', 'Y')
        new_people_count = len(self.amity.people)
        self.assertEqual(
            original_people_count,
            new_people_count - 2,
            msg='''Should be able to add fellows with accomodation'''
        )

        self.amity.add_person('Jane Doe', 'Fellow', 'N')
        new_people_count = len(self.amity.people)
        self.assertEqual(
            original_people_count,
            new_people_count - 3,
            msg='''Should be able to add fellows without accomodation'''
        )

    def test_reallocate_person(self):
        pass

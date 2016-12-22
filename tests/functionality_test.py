from unittest import TestCase
from app.Amity import Amity


class TestFunctionality(TestCase):

    def setUp(self):
        self.amity = Amity()
        self.amity.create_room('Test Office', 'Office')
        self.amity.create_room('Second Test Office', 'Office')
        self.amity.create_room('Test Living Space', 'Living Space')
        self.amity.create_room('Second Test Living Space', 'Living Space')

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
        # Cannot reallocate person who doesn't exists
        response = self.amity.reallocate_person('Random Name', 'Test Office')
        self.assertEqual(response, 'Sorry, we could not find that person')

        # Cannot reallocate to room that doesn't exist
        response = self.amity.reallocate_person('Jane Doe', 'Random Office')
        self.assertEqual(response, 'Sorry, we could not find that room')

        # Cannot reallocate staff to living space
        response = self.amity.reallocate_person('Joshua Mwaniki', 'Test Living Space')
        self.assertEqual(response, 'Sorry, you can\'t add a staff member to a living space')

        # Cannot reallocate to current room
        self.amity.rooms = {}
        self.amity.people = []
        self.amity.create_room('Test Office', 'Office')
        self.amity.add_person('Joshua Mwaniki', 'Staff')
        response = self.amity.reallocate_person('Joshua Mwaniki', 'Test Office')
        self.assertEqual(response, 'This person is already in that room')

        # Cannot rellocate to full room
        self.amity.add_person('Joshua Mwanik', 'Staff')
        self.amity.add_person('Joshua Mwani', 'Staff')
        self.amity.add_person('Joshua Mwan', 'Staff')
        self.amity.add_person('Joshua Mwa', 'Staff')
        self.amity.add_person('Joshua Mw', 'Staff')
        self.amity.create_room('Second Test Office', 'Office')
        self.amity.add_person('Joshua M', 'Staff')
        response = self.amity.reallocate_person('Joshua M', 'Test Office')
        self.assertEqual(response, 'Sorry, that room is already full')

        # Actually reallocates

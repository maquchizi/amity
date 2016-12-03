from unittest import TestCase
from app.Room import LivingSpace, Office


class TestRoom(TestCase):

    def setUp(self):
        self.ruby = LivingSpace('Ruby')
        self.camelot = Office('Camelot')

    def test_living_space_room_type(self):
        self.assertEqual(
            self.ruby.room_type, 'Living Space',
            msg='Living space should have a room type of \'Living Space\''
        )

    def test_office_room_type(self):
        self.assertEqual(
            self.camelot.room_type,
            'Office',
            msg='Office should have a room type of office'
        )

    def test_living_space_has_max_capacity(self):
        self.assertEqual(
            self.ruby.capacity,
            4,
            msg='A living space should have a capacity of four'
        )

    def test_office_has_max_capacity(self):
        self.assertEqual(
            self.camelot.capacity,
            6,
            msg='An office should have a capacity of six'
        )

    def test_living_space_is_a_room(self):
        self.assertIsInstance(
            self.ruby,
            LivingSpace,
            msg='A living space should be a room'
        )

    def test_office_is_a_room(self):
        self.assertIsInstance(
            self.camelot,
            Office,
            msg='An office should be a room'
        )

    def test_cannot_add_person_to_full_living_space(self):
        pass

    def test_cannot_add_person_to_full_office(self):
        pass

    def test_cannot_assign_living_space_to_staff_member(self):
        pass

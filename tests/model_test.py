from unittest import TestCase
from app import Room


class TestRoom(TestCase):

    def setUp(self):
        self.ruby = Room.LivingSpace('Ruby')
        self.camelot = Room.Office('Camelot')

    def test_living_space(self):
        self.assertEqual(
            self.ruby.room_type, 'Living Space',
            msg='Living space should have a room type of \'Living Space\''
        )

    def test_office(self):
        self.assertEqual(
            self.camelot.room_type,
            'Office',
            msg='Office should have a room type of office'
        )

    def test_living_space_capacity(self):
        self.assertEqual(
            self.ruby.capacity,
            4,
            msg='A living space should have a capacity of four'
        )

    def test_office_capacity(self):
        self.assertEqual(
            self.camelot.capacity,
            6,
            msg='An office should have a capacity of six'
        )

    def test_living_space_is_a_room(self):
        self.assertIsInstance(
            self.ruby,
            Room.LivingSpace,
            msg='A living space should be a room'
        )

    def test_office_is_a_room(self):
        self.assertIsInstance(
            self.camelot,
            Room.Office,
            msg='An office should be a room'
        )

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

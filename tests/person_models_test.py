from unittest import TestCase, skip
from app.Person import Person, Fellow, Staff


class TestPerson(TestCase):

    def setUp(self):
        self.ganga = Fellow('Ganga', 'Y')
        self.joshua = Staff('Joshua')

    def test_fellow_is_a_person(self):
        self.assertIsInstance(
            self.ganga,
            Person,
            msg='''A fellow should be a person'''
        )

    def test_staff_is_a_person(self):
        self.assertIsInstance(
            self.joshua,
            Person,
            msg='''A staff member should be a person'''
        )

    def test_fellow_has_fellow_role(self):
        self.assertEqual(
            self.ganga.role,
            'FELLOW',
            msg='''Fellow should have fellow roles'''
        )

    def test_staff_has_staff_role(self):
        self.assertEqual(
            self.joshua.role,
            'STAFF',
            msg='''Staff Member should have staff role'''
        )

    @skip("WIP")
    def test_staff_member_cannot_have_accommodation(self):
        self.assertRaises(
            AttributeError(),
            self.joshua.wants_accommodation,
            msg='''A staff member cannot have accommodation'''
        )

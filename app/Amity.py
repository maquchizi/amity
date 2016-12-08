from Room import LivingSpace, Office
from Person import Fellow, Staff


class Amity:
    """docstring for Amity"""

    def create_room(self, room_name):
        pass

    def add_person(self, name, designation, wants_accomadation):
        pass

    def reallocate_person(self, person_id, new_room):
        pass

    def load_people(self, txt_file):
        pass

    def print_allocations(self, filename):
        pass

    def print_unallocated(self, filename):
        pass

    def print_room(self, room_name):
        pass

    def save_state(self, db=None):
        pass

    def load_state(self, db):
        pass

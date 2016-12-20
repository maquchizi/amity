from app.Room import LivingSpace, Office
from app.Person import Fellow, Staff


class Amity:
    """docstring for Amity"""
    rooms = {}
    people = {}

    def create_room(self, room_name, room_type):
        """
        Create a single or multiple rooms of a specific type
        """
        room_name = room_name.strip()
        if room_type == 'Living Space':
            room = LivingSpace(room_name)
        else:
            room = Office(room_name)

        self.rooms[room_name] = room

    def add_person(self, name, designation, wants_accomodation):
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

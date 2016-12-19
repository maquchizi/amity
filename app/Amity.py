from app.Room import LivingSpace, Office
from app.Person import Fellow, Staff


class Amity:
    """docstring for Amity"""
    rooms = {}
    all_people = {}

    def create_room(self, *args):
        """
            Create a single or multiple rooms of a specific type

            Uses the following switches:
                -l to create a room of type living space
                -o to create a room of type office

            Multiple rooms of a single type can be created by providing
            the switch and a comma-separated list of room name like so:
                create_room -l Ruby, Python, PHP
                    or
                create_room -o Mordor, Round Table, Camelot

            Room types can also be mixed like this:
                create_room -l Ruby, Python, PHP -o Mordor, Round Table
        """
        print(args)

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

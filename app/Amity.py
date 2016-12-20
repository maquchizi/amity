from app.Room import LivingSpace, Office
from app.Person import Fellow, Staff
import random


class Amity:
    """docstring for Amity"""
    rooms = {}
    offices = {}
    livingspaces = {}
    vacant_offices = {}
    vacant_livingspaces = {}
    people = []
    staff = []
    fellows = []

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
        self.update_offices()
        self.update_livingspaces()

    def add_person(self, name, designation, wants_accomodation='N'):
        """
        Add a person
        Specify their designation and whether they need accommodation
        Default is to mot require accommodation
        """
        if designation == 'Staff':
            person = Staff(name)
            self.people.append(person)
        else:
            if wants_accomodation == 'Y':
                # Attempt to assign living space. Fail if no vacant living
                # spaces available
                try:
                    livingspace = random.sample(self.vacant_livingspaces, 1)[0]
                    person = Fellow(name, True)
                    self.people.append(person)
                    self.rooms[livingspace].occupants.append(person)
                    self.update_livingspaces()
                except ValueError:
                    print('No Living Spaces Available')
                    return
            else:
                person = Fellow(name, False)
                self.people.append(person)

        # Attempt to assign office. Fail if no vacant offices available
        try:
            office = random.sample(self.vacant_offices, 1)[0]
            self.rooms[office].occupants.append(person)
            self.update_offices()
        except ValueError:
            print('No Offices Available')
            return

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

    def update_offices(self):
        self.offices = {key: value for key, value in
                        self.rooms.iteritems() if value.room_type == 'Office'}

        self.vacant_offices = {key: value for key, value in
                               self.offices.iteritems()
                               if (len(value.occupants) < value.capacity)}

    def update_livingspaces(self):
        self.livingspaces = {key: value for key, value in
                             self.rooms.iteritems() if
                             value.room_type == 'Living Space'}

        self.vacant_livingspaces = {key: value for key, value in
                                    self.livingspaces.iteritems()
                                    if (len(value.occupants) < value.capacity)}

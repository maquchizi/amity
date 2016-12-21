from app.Room import LivingSpace, Office
from app.Person import Fellow, Staff
# from app.DB import PersonModel, RoomModel
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
        self.update_livingspaces()
        self.update_offices()

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
                    print('%s was assigned the living space %s' % (person.name, self.rooms[livingspace].room_name))
                except ValueError:
                    print(self.livingspaces)
                    for key, value in self.livingspaces.iteritems():
                        print(key, value.occupants)
                    print(self.vacant_livingspaces)
                    print('No Living Spaces Available')
                    return
            else:
                person = Fellow(name, False)
                self.people.append(person)

        # Attempt to assign office. Fail if no vacant offices available
        try:
            office = random.sample(self.vacant_offices, 1)[0]
            print(self.rooms[office])
            self.rooms[office].occupants.append(person)
            print('%s was assigned the office %s' % (person.name, self.rooms[office].room_name))
        except ValueError:
            for key, value in self.offices.iteritems():
                print(key, value.occupants)
            print(self.vacant_offices)
            print('No Offices Available')
            return

        self.update_livingspaces()
        self.update_offices()

    def reallocate_person(self, name, new_room):
        # Check that person exists
        person_to_reallocate = False
        room_exists = None
        room_vacant = False
        current_room = None

        for person in self.people:
            if name == person.name:
                person_to_reallocate = person
                break

        if not person_to_reallocate:
            print('Sorry, we could not find that person')
            return

        # Check that room exists
        for key, value in self.rooms.iteritems():
            if new_room == value.room_name:
                room_exists = True
                break

        if not room_exists:
            print('Sorry, we could not find that room')
            return

        # Check that person can be added to that room
        # The whole idea of this is not to assign a staff member living space
        if person_to_reallocate.designation == 'STAFF' and self.rooms[new_room].room_type == 'Living Space':
            print('Sorry, you can\'t add a staff member to a living space')
            return

        # Check that room is not person's current room
        for key, value in self.rooms.iteritems():
            if person_to_reallocate in value.occupants:
                current_room = value
                if new_room == current_room.room_name:
                    print('This person is already in that room')
                    return

        # Check that room isn't full
        for key, value in self.vacant_livingspaces.iteritems():
            if new_room == value.room_name:
                room_vacant = True
                break

        for key, value in self.vacant_offices.iteritems():
            if new_room == value.room_name:
                room_vacant = True
                break

        if not room_vacant:
            print('Sorry, that room is already full')
            return

        for key, value in self.rooms.iteritems():
            # Remove person from old room
            if person_to_reallocate in value.occupants:
                value.occupants.remove(person_to_reallocate)
            # Add person to new room
            if new_room == value.room_name:
                value.occupants.append(person_to_reallocate)
                print('%s was reassigned to the %s %s' % (person_to_reallocate.name, current_room.room_type, value.room_name))

    def load_people(self, txt_file):
        pass

    def print_allocations(self, filename):
        pass

    def print_unallocated(self, filename):
        pass

    def print_room(self, room_name):
        pass

    def save_state(self, db=None):
        # Loop through all rooms, create room in DB
        # For each occupant, create person in DB with reference to room
        pass

    def load_state(self, db):
        pass

    def update_offices(self):
        self.offices = {key: value for key, value in
                        self.rooms.iteritems() if value.room_type == 'Office'}

        self.vacant_offices = {key: value for key, value in
                               self.offices.iteritems()
                               if len(value.occupants) < value.capacity}

    def update_livingspaces(self):
        self.livingspaces = {key: value for key, value in
                             self.rooms.iteritems() if
                             value.room_type == 'Living Space'}

        self.vacant_livingspaces = {key: value for key, value in
                                    self.livingspaces.iteritems()
                                    if len(value.occupants) < value.capacity}

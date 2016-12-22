from app.Room import LivingSpace, Office
from app.Person import Fellow, Staff
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.DB import PersonModel, RoomModel, Base
import random


class Amity:
    """docstring for Amity"""
    rooms = {}
    offices = {}
    livingspaces = {}
    vacant_offices = {}
    vacant_livingspaces = {}
    people = []

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

        return '%s %s created succesfully' % (room_type, room_name)

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
                    return '%s was assigned the living space %s' % (person.name, self.rooms[livingspace].room_name)
                except ValueError:
                    return 'No Living Spaces Available'

            else:
                person = Fellow(name, False)
                self.people.append(person)

        # Attempt to assign office. Fail if no vacant offices available
        try:
            office = random.sample(self.vacant_offices, 1)[0]
            self.rooms[office].occupants.append(person)
            print('%s was assigned the office %s' % (person.name, self.rooms[office].room_name))
        except ValueError:
            return 'No Offices Available'

        self.update_livingspaces()
        self.update_offices()

    def reallocate_person(self, name, new_room):
        # Check that person exists
        person_to_reallocate = None
        room_exists = None
        room_vacant = False
        current_room = None

        for person in self.people:
            if name == person.name:
                person_to_reallocate = person
                break

        if person_to_reallocate is None:
            return 'Sorry, we could not find that person'

        # Check that room exists
        for key, value in self.rooms.iteritems():
            if new_room == value.room_name:
                room_exists = True
                break

        if not room_exists:
            return 'Sorry, we could not find that room'

        # Check that person can be added to that room
        # The whole idea of this is not to assign a staff member living space
        if person_to_reallocate.designation ==\
                'STAFF' and self.rooms[new_room].room_type == 'Living Space':

            return 'Sorry, you can\'t add a staff member to a living space'

        # Check that room is not person's current room
        for key, value in self.rooms.iteritems():
            if person_to_reallocate in value.occupants:
                current_room = value
                if new_room == current_room.room_name:
                    return 'This person is already in that room'

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
            return 'Sorry, that room is already full'

        for key, value in self.rooms.iteritems():
            # Remove person from old room
            if person_to_reallocate in value.occupants:
                value.occupants.remove(person_to_reallocate)

            # Add person to new room
            if new_room == value.room_name:
                value.occupants.append(person_to_reallocate)

                return '%s was reassigned to the %s %s'\
                    % (person_to_reallocate.name, current_room.room_type,
                       value.room_name)

    def load_people(self, txt_file):
        with open('txt_files/' + txt_file, 'r') as file:
            # Read file line by line
            file_content = file.readlines()
            # Extract info from each line
            for line in file_content:
                # Split line on space
                info = line.split()
                name = info[0] + ' ' + info[1]
                designation = info[2].lower()
                try:
                    wants_accomodation = info[3]
                except IndexError:
                    pass

                self.add_person(name, designation, wants_accomodation)

    def print_allocations(self, filename):
        lines = ''

        if len(self.rooms) == 0:
            print('No Rooms Available')
            return

        # Go through all rooms
        # Add header line for each new room
        # Add content line for occupants
        for key, value in self.rooms.iteritems():
            lines += ('\n\n\t' + value.room_name + ' - ' + value.room_type + '\n' + '-' * 50 + '\n\t')
            for occupant in value.occupants:
                lines += (occupant.name + ', ')

        if not filename:
            print(lines)
        else:
            txt_file = open('txt_files/' + filename, "w")
            txt_file.write(lines)
            txt_file.close()

    def print_unallocated(self, filename):
        pass

    def print_room(self, room_name):
        lines = ''

        for key, value in self.rooms.iteritems():
            if value.room_name == room_name:
                lines += ('\n\n\t' + value.room_name + ' - ' + value.room_type + '\n' + '-' * 50 + '\n\t')
                if len(value.occupants) > 0:
                    for occupant in value.occupants:
                        lines += (occupant.name + ', ')
                else:
                    lines += 'Room is empty'
                return lines

    def save_state(self, db='amity.db'):

        engine = create_engine('sqlite:///database_files/%s' % db)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Loop through all rooms, create room in DB
        for key, value in self.rooms.iteritems():
            room = RoomModel()

            room.room_name = value.room_name
            room.room_type = value.room_type
            room.room_capacity = value.capacity

            retrieved_room = session.query(RoomModel).\
                filter(RoomModel.room_name == room.room_name).\
                first()

            # Prevent app from creating duplicate rooms
            if not retrieved_room:
                session.add(room)
                session.commit()
                current_room_id = room.room_id
            else:
                current_room_id = retrieved_room.room_id

            # For each occupant, create person in DB with reference to room
            for occupant in value.occupants:
                person = PersonModel()

                person.name = occupant.name
                person.designation = occupant.designation
                if room.room_type == 'Office':
                    person.office = current_room_id
                else:
                    person.living_space = current_room_id

                # Make sure to check if person already exists
                # and update instead of creating
                retrieved_person = session.query(PersonModel).\
                    filter(PersonModel.name == person.name,
                           PersonModel.designation == person.designation).\
                    first()

                if retrieved_person:
                    if person.office:
                        retrieved_person.office = person.office
                    elif person.living_space:
                        retrieved_person.living_space = person.living_space
                    session.commit()
                else:
                    session.add(person)
                    session.commit()

        return 'State successfully saved to DB'

    def load_state(self, db):
        if not db:
            engine = create_engine('sqlite:///database_files/amity.db')
        else:
            engine = create_engine('sqlite:///database_files/%s' % db)

        Session = sessionmaker(bind=engine)
        session = Session()

        rooms = session.query(RoomModel).all()
        people = session.query(PersonModel).all()
        self.rooms = {}
        self.people = []
        for room in rooms:
            print room.room_name
            self.create_room(room.room_name, room.room_type)
            for person in people:
                if person.office == room.room_id or person.living_space == room.room_id:
                    if person.designation == 'FELLOW':
                        person_to_add = Fellow(person.name, 'Y')
                    else:
                        person_to_add = Staff(person.name)
                    self.rooms[room.room_name].occupants.append(person_to_add)

        self.update_offices()
        self.update_livingspaces()

        return 'State successfully loaded from DB'

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

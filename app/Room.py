class Room(object):
    """
    docstring for Room
    """
    def __init__(self, room_name, room_type):
        super(Room, self).__init__()
        self.room_name = room_name
        self.room_type = room_type
        self.occupants = []


class LivingSpace(Room):
    """
    docstring for LivingSpace
    """
    capacity = 4
    room_type = 'Living Space'
    occupants = []

    def __init__(self, room_name):
        super(Room, self).__init__()
        self.room_name = room_name


class Office(Room):
    """
    docstring for Office
    """
    capacity = 6
    room_type = 'Office'
    occupants = []

    def __init__(self, room_name):
        super(Room, self).__init__()
        self.room_name = room_name

class Person(object):
    """
    docstring for Person
    """
    def __init__(self, name, designation, wants_accommodation):
        super(Person, self).__init__()
        self.name = name
        self.designation = designation
        self.wants_accommodation = wants_accommodation


class Staff(Person):
    """
    docstring for Staff
    """
    designation = 'STAFF'
    office = None

    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name


class Fellow(Person):
    """
    docstring for Fellow
    """
    designation = 'FELLOW'
    office = None
    living_space = None

    def __init__(self, name, wants_accommodation):
        super(Person, self).__init__()
        self.name = name
        self.wants_accommodation = wants_accommodation

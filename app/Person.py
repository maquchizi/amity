class Person(object):
    """
    docstring for Person
    """
    def __init__(self, name, role, wants_accommodation):
        super(Person, self).__init__()
        self.name = name
        self.role = role
        self.wants_accommodation = wants_accommodation

    def assign_office(self):
        pass


class Staff(Person):
    """
    docstring for Staff
    """
    role = 'STAFF'
    office = None

    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name


class Fellow(Person):
    """
    docstring for Fellow
    """
    role = 'FELLOW'
    office = None
    living_space = None

    def __init__(self, name, wants_accommodation):
        super(Person, self).__init__()
        self.name = name
        self.wants_accommodation = wants_accommodation

    def assign_living_space(self):
        pass

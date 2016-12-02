class Person(object):
    """
    docstring for Person
    """
    def __init__(self, name, role, wants_accommodation):
        super(Person, self).__init__()
        self.name = name
        self.role = role
        self.wants_accommodation = wants_accommodation


class Staff(Person):
    """
    docstring for Staff
    """
    role = 'STAFF'

    def __init__(self):
        super(Person, self).__init__()


class Fellow(object):
    """
    docstring for Fellow
    """
    role = 'FELLOW'

    def __init__(self):
        super(Person, self).__init__()

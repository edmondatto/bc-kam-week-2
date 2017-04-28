class Room(object):
    """A Class that defines a room and its properties"""
    def __init__(self, name):
        self.name = name
        self.occupants = []
        self.number_of_occupants = 0
        self.has_free_space = True

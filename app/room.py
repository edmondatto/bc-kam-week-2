class Room(object):
    def __init__(self, name):
        self.name = name
        self.occupants = []
        self.number_of_occupants = 0
        self.has_free_space = True

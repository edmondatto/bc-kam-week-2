from app.room import Room


class Office(Room):
    """A Class that defines an office and its properties"""

    capacity = 6
    room_type = 'Office'

    def __init__(self, office_name):
        super(Office, self).__init__(office_name)
        self.name = office_name

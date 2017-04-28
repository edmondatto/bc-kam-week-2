from app.person import Person


class Staff(Person):
    """A Class that defines a staff and their properties"""
    def __init__(self, staff_name):
        super(Staff, self).__init__(staff_name)
        self.position = 'Staff'

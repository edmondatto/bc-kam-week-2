from app.person import Person


class Staff(Person):
    def __init__(self, staff_name):
        super(Staff, self).__init__(staff_name)
        self.position = 'Staff'

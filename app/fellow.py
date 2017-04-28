from app.person import Person


class Fellow(Person):
    """A Class that defines a fellow and their properties"""
    def __init__(self, fellow_name, wants_accommodation='N'):
        super(Fellow, self).__init__(fellow_name)
        self.position = 'Fellow'
        self.living_space_assigned = ''
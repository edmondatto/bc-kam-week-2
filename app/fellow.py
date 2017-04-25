from app.person import Person


class Fellow(Person):
    POSITION = 'Fellow'

    def __init__(self, fellow_name, wants_accommodation='N'):
        super(Fellow, self).__init__(fellow_name)
        self.position = self.POSITION
        self.wants_accommodation = wants_accommodation

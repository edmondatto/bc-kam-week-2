from app.room import Room


class LivingSpace(Room):
    capacity = 4
    room_type = 'living space'

    def __init__(self, living_space_name):
        super(LivingSpace, self).__init__(living_space_name)
        self.name = living_space_name

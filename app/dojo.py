from app.fellow import Fellow
from app.staff import Staff
from app.living_space import LivingSpace
from app.office import Office


class Dojo(object):
    def __init__(self):
        self.total_number_of_rooms = 0
        self.number_of_living_spaces = 0
        self.number_of_offices = 0
        self.all_rooms = []
        self.list_of_people = []
        self.list_of_fellows = []
        self.list_of_staff = []
        self.number_of_fellows = 0
        self.total_number_of_staff = 0
        self.total_number_of_people = 0

    def create_room(self, room_name, room_type):
        if room_type.lower().strip() == 'office':
            new_office = Office(room_name)
            self.total_number_of_rooms += 1
            self.number_of_offices += 1
            return new_office
        elif room_type.lower().strip() == 'living space':
            room_name = LivingSpace(room_name)
            self.total_number_of_rooms += 1
            self.number_of_living_spaces += 1
            return room_name
        else:
            return 'Enter a valid room type!'

    def add_person(self, person_name, person_position):
        if person_position.lower().strip() == 'fellow':
            new_fellow = Fellow(person_name)
            self.list_of_people.append(person_name)
            self.list_of_fellows.append(person_name)
            self.number_of_fellows += 1
            self.total_number_of_people += 1
            return new_fellow
        elif person_position.lower().strip() == 'staff':
            new_staff = Staff(person_name)
            self.list_of_people.append(person_name)
            self.list_of_staff.append(person_name)
            self.total_number_of_staff += 1
            self.total_number_of_people += 1
            return new_staff
        else:
            return 'Enter a valid position e.g. Fellow, Staff'

    def remove_person(self, person_name, room_name):
        pass

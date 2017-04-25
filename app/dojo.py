from app.fellow import Fellow
from app.staff import Staff
from app.living_space import LivingSpace
from app.office import Office
import random


class Dojo(object):
    def __init__(self):
        self.total_number_of_rooms = 0
        self.number_of_living_spaces = 0
        self.number_of_offices = 0
        self.all_rooms = {}
        self.living_spaces = {}
        self.list_of_people = []
        self.list_of_fellows = []
        self.list_of_staff = []
        self.number_of_fellows = 0
        self.total_number_of_staff = 0
        self.total_number_of_people = 0

    def create_room(self, room_name, room_type):
        if isinstance(room_name, str) and isinstance(room_type, str):
            if room_type.lower().strip() == 'office':
                new_office = Office(room_name)
                self.total_number_of_rooms += 1
                self.number_of_offices += 1
                return new_office
            elif room_type.lower().strip() == 'living space':
                new_living_space = LivingSpace(room_name)
                self.total_number_of_rooms += 1
                self.number_of_living_spaces += 1
                self.living_spaces[room_name] = new_living_space
                return new_living_space
            else:
                return 'Enter a valid room type!'
        else:
            raise TypeError('Arguments must both be strings')

    def add_person(self, person_name, person_position, wants_accommodation=False):
        if person_position.lower().strip() == 'fellow':
            new_fellow = Fellow(person_name)
            self.list_of_people.append(person_name)
            self.list_of_fellows.append(person_name)
            self.number_of_fellows += 1
            self.total_number_of_people += 1
            if wants_accommodation:
                return self.allocate_living_space(person_name)
                # return random_living_space
                # return new_fellow
        elif person_position.lower().strip() == 'staff':
            new_staff = Staff(person_name)
            self.list_of_people.append(person_name)
            self.list_of_staff.append(person_name)
            self.total_number_of_staff += 1
            self.total_number_of_people += 1
            return new_staff
        else:
            return 'Enter a valid position e.g. Fellow, Staff'

    def allocate_living_space(self, person_name):
        room_assigned = False
        while not room_assigned:
            random_living_space = random.choice(list(self.living_spaces.keys()))
            if self.living_spaces[random_living_space].capacity == len(
                    self.living_spaces[random_living_space].occupants):
                room_assigned = False
            elif self.living_spaces[random_living_space].capacity > len(
                    self.living_spaces[random_living_space].occupants):
                self.living_spaces[random_living_space].occupants.append(person_name)
                room_assigned = True
                return '{} has been allocated the livingspace {}'.format(person_name, random_living_space)

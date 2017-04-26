import random

from app.fellow import Fellow
from app.living_space import LivingSpace
from app.office import Office
from app.staff import Staff


# Optimise the list_of_people
# Optimise the total_number_of_people

class Dojo(object):
    def __init__(self):
        self.total_number_of_rooms = 0
        self.number_of_living_spaces = 0
        self.number_of_offices = 0
        self.all_rooms = {}
        self.living_spaces = {}
        self.office_spaces = {}
        self.list_of_people = []
        self.list_of_fellows = []
        self.list_of_staff = []
        self.total_number_of_fellows = 0
        self.total_number_of_staff = 0
        self.total_number_of_people = 0

    def create_room(self, room_name, room_type):
        if isinstance(room_name, str) and isinstance(room_type, str):
            if room_type.lower().strip() == 'office':
                new_office = Office(room_name)
                self.total_number_of_rooms += 1
                self.number_of_offices += 1
                self.office_spaces[room_name] = new_office
                self.all_rooms[room_name] = new_office
                return new_office
            elif room_type.lower().strip() == 'living space':
                new_living_space = LivingSpace(room_name)
                self.total_number_of_rooms += 1
                self.number_of_living_spaces += 1
                self.living_spaces[room_name] = new_living_space
                self.all_rooms[room_name] = new_living_space
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
            self.total_number_of_fellows += 1
            self.total_number_of_people += 1
            self.allocate_office_space(person_name)
            if wants_accommodation:
                self.allocate_living_space(person_name)
                # new_fellow.office_assigned =
                # new_fellow.living_space_assigned =
                # return new_fellow
        elif person_position.lower().strip() == 'staff':
            new_staff = Staff(person_name)
            self.list_of_people.append(person_name)
            self.list_of_staff.append(person_name)
            self.total_number_of_staff += 1
            self.total_number_of_people += 1
            self.allocate_office_space(person_name)
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

    def allocate_office_space(self, person_name):
        office_assigned = False
        while not office_assigned:
            print(self.office_spaces)
            random_office_space = random.choice(list(self.office_spaces.keys()))
            if self.office_spaces[random_office_space].capacity == len(
                    self.office_spaces[random_office_space].occupants):
                office_assigned = False
            elif self.office_spaces[random_office_space].capacity > len(
                    self.office_spaces[random_office_space].occupants):
                self.office_spaces[random_office_space].occupants.append(person_name)
                office_assigned = True
                return '{} has been allocated the Office {}'.format(person_name, random_office_space)

    def create_multiple_rooms(self, room_type, *room_names):
        if room_type.lower().strip() == 'office' or room_type.lower().strip() == 'living space':
            for room_name in room_names:
                print(self.create_room(room_name, room_type))
        else:
            return 'Enter a valid room type e.g. Office, Living space'

    def add_multiple_people(self, position, *people_names):
        if position.lower().strip() == 'fellow' or position.lower().strip() == 'staff':
            for person_name in people_names:
                print(self.add_person(person_name, position))
        else:
            return 'Enter a valid position e.g. Staff, Fellow'

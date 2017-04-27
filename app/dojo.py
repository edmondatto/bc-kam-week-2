import random

from app.fellow import Fellow
from app.living_space import LivingSpace
from app.office import Office
from app.staff import Staff


class Dojo(object):
    def __init__(self):
        self.total_number_of_rooms = 0
        self.number_of_living_spaces = 0
        self.number_of_offices = 0
        self.all_rooms = {}
        self.living_spaces = {}
        self.office_spaces = {}
        self.list_of_people = {}
        self.list_of_fellows = {}
        self.list_of_staff = {}
        self.total_number_of_fellows = 0
        self.total_number_of_staff = 0
        self.total_number_of_people = 0
        self.unallocated_people = []

    def create_room(self, room_name, room_type):
        if type(room_name) == str and type(room_type) == str:
            if room_name in list(self.all_rooms.keys()):
                return 'A room called {} already exists'.format(room_name)
            else:
                if room_type.lower().strip() == 'office':
                    new_office = Office(room_name)
                    self.total_number_of_rooms += 1
                    self.number_of_offices += 1
                    self.office_spaces[room_name] = new_office
                    self.all_rooms[room_name] = new_office
                    return 'An office called ' + room_name + ' has been successfully created!'
                elif room_type.lower().strip() == 'living space':
                    new_living_space = LivingSpace(room_name)
                    self.total_number_of_rooms += 1
                    self.number_of_living_spaces += 1
                    self.living_spaces[room_name] = new_living_space
                    self.all_rooms[room_name] = new_living_space
                    return 'A living space called ' + room_name + ' has been successfully created!'
                else:
                    return 'Enter a valid room type!'
        else:
            raise TypeError('Arguments must both be strings')

    def add_person(self, person_name, person_position, wants_accommodation=False):
        if person_name not in list(self.list_of_people.keys()):
            if person_position.lower().strip() == 'fellow':
                new_fellow = Fellow(person_name)
                self.list_of_people[person_name] = new_fellow
                self.list_of_fellows[person_name] = new_fellow
                self.total_number_of_fellows += 1
                self.total_number_of_people += 1
                office_allocation_msg = self.allocate_office_space(person_name)
                living_space_allocation_message = ''
                if not len(self.list_of_people[person_name].office_assigned):
                    self.unallocated_people.append(person_name)
                if wants_accommodation:
                    living_space_allocation_message = self.allocate_living_space(person_name)
                return 'Fellow ' + person_name + ' has been successfully added.\n' + office_allocation_msg + '\n' + living_space_allocation_message
            elif person_position.lower().strip() == 'staff':
                new_staff = Staff(person_name)
                self.list_of_people[person_name] = new_staff
                self.list_of_staff[person_name] = new_staff
                self.total_number_of_staff += 1
                self.total_number_of_people += 1
                office_allocation_msg = self.allocate_office_space(person_name)
                if not len(self.list_of_people[person_name].office_assigned):
                    self.unallocated_people.append(person_name)
                return 'Staff ' + person_name + ' has been successfully added.' + '\n' + office_allocation_msg
            else:
                return 'Enter a valid position e.g. Fellow, Staff'
        else:
            return 'A person with this name already exists'

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
            print('It runs')
            return 'Enter a valid position e.g. Staff, Fellow'

    def allocate_office_space(self, person_name):
        rooms_with_space = []
        if self.office_spaces:
            for key, value in self.office_spaces.items():
                if self.office_spaces[key].has_free_space:
                    rooms_with_space.append(key)
            try:
                random_office_space = random.choice(rooms_with_space)
            except IndexError:
                return 'No offices with free space!'
            self.office_spaces[random_office_space].occupants.append(person_name)
            self.office_spaces[random_office_space].number_of_occupants += 1
            self.list_of_people[person_name].office_space_assigned = random_office_space
            if self.office_spaces[random_office_space].capacity == self.office_spaces[
                random_office_space].number_of_occupants:
                self.office_spaces[random_office_space].has_free_space = False
            return '{} has been allocated the Office {}'.format(person_name, random_office_space)
        else:
            return 'There are no rooms of type office spaces!'

    def allocate_living_space(self, person_name):
        rooms_with_space = []
        if self.living_spaces:
            for key, value in self.living_spaces.items():
                if self.living_spaces[key].has_free_space:
                    rooms_with_space.append(key)
            try:
                random_living_space = random.choice(rooms_with_space)
            except IndexError:
                return 'No offices with free space!'
            self.living_spaces[random_living_space].occupants.append(person_name)
            self.living_spaces[random_living_space].number_of_occupants += 1
            self.list_of_people[person_name].living_space_assigned = random_living_space
            if self.living_spaces[random_living_space].capacity == self.living_spaces[
                random_living_space].number_of_occupants:
                self.living_spaces[random_living_space].has_free_space = False
            return '{} has been allocated the Living Space {}'.format(person_name, random_living_space)
        else:

            warning = 'There are no rooms of type living spaces!'
            return warning

    def print_room(self, room_name):
        list_of_occupants = self.all_rooms[room_name].occupants
        for occupant in list_of_occupants:
            print(occupant)
            return

import random

from app.fellow import Fellow
from app.living_space import LivingSpace
from app.office import Office
from app.staff import Staff
from db_models.models import *


class Dojo(object):
    """A Class that defines a dojo, its properties and characteristics"""

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
        """A method for creating new rooms of one of 2 types (Office or Living Space) in the Dojo"""
        if type(room_name) == str and type(room_type) == str:
            if room_name in list(self.all_rooms.keys()):
                return ' A room called {} already exists!\n'.format(room_name)
            else:
                if room_type.lower().strip() == 'office':
                    new_office = Office(room_name)
                    self.total_number_of_rooms += 1
                    self.number_of_offices += 1
                    self.office_spaces[room_name] = new_office
                    self.all_rooms[room_name] = new_office
                    return ' An office called ' + room_name + ' has been successfully created!'
                elif room_type.lower().strip() == 'living space':
                    new_living_space = LivingSpace(room_name)
                    self.total_number_of_rooms += 1
                    self.number_of_living_spaces += 1
                    self.living_spaces[room_name] = new_living_space
                    self.all_rooms[room_name] = new_living_space
                    return ' A living space called ' + room_name + ' has been successfully created!'
                else:
                    return ' Enter a valid room type!'
        else:
            raise TypeError(' Arguments must both be strings')

    def add_person(self, person_name, person_position, wants_accommodation=False):
        """A method that defines how a new occupant of the dojo is created and assigned space"""
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
                return ' Fellow ' + person_name + ' has been successfully added.\n' + office_allocation_msg + '\n' + living_space_allocation_message + '\n'
            elif person_position.lower().strip() == 'staff':
                new_staff = Staff(person_name)
                self.list_of_people[person_name] = new_staff
                self.list_of_staff[person_name] = new_staff
                self.total_number_of_staff += 1
                self.total_number_of_people += 1
                office_allocation_msg = self.allocate_office_space(person_name)
                if not len(self.list_of_people[person_name].office_assigned):
                    self.unallocated_people.append(person_name)
                return ' Staff ' + person_name + ' has been successfully added.' + '\n' + office_allocation_msg + '\n'
            else:
                return ' Enter a valid position e.g. Fellow, Staff'
        else:
            return ' A person with this name already exists'

    def create_multiple_rooms(self, room_type, *room_names):
        """A method that allows for creation of multiple rooms simultaneously"""
        if room_type.lower().strip() == 'office' or room_type.lower().strip() == 'living space':
            for room_name in room_names:
                print(self.create_room(room_name, room_type))
        else:
            return ' Enter a valid room type e.g. Office, Living space'

    def add_multiple_people(self, position, *people_names):
        """A method that allows for addition of multiple people to the dojo simultaneously"""
        if position.lower().strip() == 'fellow' or position.lower().strip() == 'staff':
            for person_name in people_names:
                print(self.add_person(person_name, position))
        else:
            return ' Enter a valid position e.g. Staff, Fellow'

    def allocate_office_space(self, person_name):
        """A method that is called from within the add_person method to assign them office space"""
        rooms_with_space = []
        if self.office_spaces:
            for key, value in self.office_spaces.items():
                if self.office_spaces[key].has_free_space:
                    rooms_with_space.append(key)
            try:
                random_office_space = random.choice(rooms_with_space)
                self.office_spaces[random_office_space].occupants.append(person_name)
                self.office_spaces[random_office_space].number_of_occupants += 1
                self.list_of_people[person_name].office_assigned += random_office_space
                if self.office_spaces[random_office_space].capacity == self.office_spaces[
                    random_office_space].number_of_occupants:
                    self.office_spaces[random_office_space].has_free_space = False
                return ' {} has been allocated the Office {}'.format(person_name, random_office_space) + '\n'
            except IndexError:
                return ' No offices with free space!'

        else:
            return ' There are no rooms of type office spaces!'

    def allocate_living_space(self, person_name):
        """A method that is called from within the add_person_method to assign them a living space"""
        rooms_with_space = []
        if self.living_spaces:
            for key, value in self.living_spaces.items():
                if self.living_spaces[key].has_free_space:
                    rooms_with_space.append(key)
            try:
                random_living_space = random.choice(rooms_with_space)
                self.living_spaces[random_living_space].occupants.append(person_name)
                self.living_spaces[random_living_space].number_of_occupants += 1
                self.list_of_people[person_name].living_space_assigned += random_living_space
                if self.living_spaces[random_living_space].capacity == self.living_spaces[
                    random_living_space].number_of_occupants:
                    self.living_spaces[random_living_space].has_free_space = False
                return ' {} has been allocated the Living Space {}'.format(person_name, random_living_space)
            except IndexError:
                return ' No living spaces with free space!'

        else:
            self.unallocated_people.append(person_name)
            warning = ' There are no rooms of type living spaces!'
            return warning

    def print_room(self, room_name):
        """A method that returns a list of all the occupants in a particular room"""
        return self.all_rooms[room_name].occupants

    def print_allocations(self, *file_names):
        """A method that prints to the screen and optionally to a file, all the people assigned to the different 
        rooms in the dojo."""
        room_names = list(self.all_rooms.keys())
        if len(room_names) > 0:
            file_content = ''
            for room_name in room_names:
                title = '\n ' + room_name.upper() + ' (' + self.all_rooms[room_name].room_type + ')'
                divider = ' ' + '-' * 40 + '\n'
                content = ' ' + ', '.join(self.all_rooms[room_name].occupants) + '\n\n'
                file_content += title + '\n' + divider + content
                print(title)
                print(divider)
                print(content)
            try:
                if file_names[0] is not None:
                    for file_name in file_names:
                        new_path = 'Exports/' + file_name
                        room_allocations = open(new_path, 'w')
                        room_allocations.write(file_content)
                        room_allocations.close()
                        print('\n Room allocations have been printed to the file {}\n'.format(file_name))
                return ''
            except IndexError:
                pass
        else:
            return ' No rooms have been created yet!\n'

    def print_unallocated(self, *file_name):
        """A method that prints to the screen and optionally to a file, all the people who haven't been assigned 
        space in the dojo. """
        if len(self.unallocated_people) > 0:
            title = '\n UNALLOCATED PEOPLE'
            divider = ' ' + ('-' * 40) + '\n'
            content = ' ' + ', '.join(self.unallocated_people) + '\n\n'
            print(title)
            print(divider)
            print(content)
            try:
                if file_name[0] is not None:
                    for name in file_name:
                        new_path = 'Exports/' + name
                        unallocated_people = open(new_path, 'w')
                        unallocated_people.write(title + '\n')
                        unallocated_people.write(divider)
                        unallocated_people.write(content)
                        unallocated_people.close()
                        print('\n Unallocated people have been printed to the file {}\n'.format(name))
                return ''
            except IndexError:
                pass
        else:
            return ' Nobody is unallocated'

    def remove_person(self, person_name, room_name):
        if person_name in self.all_rooms[room_name].occupants and room_name in self.all_rooms.keys():
            self.all_rooms[room_name].occupants.remove(person_name)
            self.all_rooms[room_name].number_of_occupants -= 1
        else:
            return person_name + ' has not been assigned to the room ' + room_name + ', or, the room ' + room_name + ' is invalid '

    def reallocate_person(self, person_name, new_room_name):
        if person_name in list(self.list_of_people.keys()):
            if new_room_name in list(self.all_rooms.keys()):
                new_room = self.all_rooms[new_room_name]
                old_room = self.list_of_people[person_name].office_assigned
                if new_room.room_type.lower() == 'office':
                    if new_room.room_type == self.all_rooms[old_room].room_type:
                        self.remove_person(person_name, old_room)
                        if new_room.has_free_space:
                            new_room.occupants.append(person_name)
                            new_room.number_of_occupants += 1
                            self.list_of_people[person_name].office_assigned = new_room_name
                            return ' {} has successfully been reallocated to the rooom {}.\n'.format(person_name,
                                                                                                     new_room_name)
                        else:
                            return ' {} does not have any free space!\n'.format(new_room_name)
                    else:
                        return ' You cannot reallocate a person to a room of a different type!\n'
                if new_room.room_type.lower() == 'living space':
                    if self.list_of_people[person_name].position == 'fellow':
                        if new_room.room_type == self.all_rooms[old_room].room_type:
                            self.remove_person(person_name, old_room)
                            if new_room.has_free_space:
                                new_room.occupants.append(person_name)
                                new_room.number_of_occupants += 1
                                self.list_of_people[person_name].living_space_assigned = new_room_name
                            else:
                                return ' {} does not have any free space!\n'.format(new_room_name)
                        else:
                            return ' You cannot reallocate a person to a room of a different type\n'
                    else:
                        return ' Staff members cannot be allocated living spaces!\n'
            else:
                return ' A room called {} does not exist in the dojo\n'.format(new_room_name)
        else:
            return ' A person called {} does not exist in the dojo!\n'.format(person_name)

    def load_people(self):
        """A function that adds people to rooms from a txt file"""
        load_file = open('Imports/load_file', 'r')
        people_list = [x.strip('\n') for x in load_file.readlines()]
        for person in people_list:
            if person.split(' ')[2].lower() == 'staff':
                self.add_person(person.split(' ')[0] + ' ' + person.split(' ')[1], 'staff')
            if person.split(' ')[2].lower() == 'fellow':
                if person.split(' ')[3].lower() == 'y':
                    self.add_person(person.split(' ')[0] + ' ' + person.split(' ')[1], 'fellow', True)
                if person.split(' ')[3].lower() == 'n':
                    self.add_person(person.split(' ')[0] + ' ' + person.split(' ')[1], 'fellow')
        return " People have been loaded successfully from the file"

    def save_state(self):
        """A function that saves the applications data to a database"""
        db.connect()
        db.create_tables([FellowModel, StaffModel, RoomModel], safe=True)
        for key, value in self.list_of_fellows.items():
            try:
                FellowModel.create(person_name=key,
                                   person_position=self.list_of_fellows[key].position,
                                   office_assigned=self.list_of_fellows[key].office_assigned,
                                   living_space_assigned=self.list_of_fellows[key].living_space_assigned
                                   )
            except IntegrityError:
                pass
        for key, value in self.list_of_staff.items():
            try:
                StaffModel.create(person_name=key,
                                  person_position=self.list_of_staff[key].position,
                                  office_assigned=self.list_of_staff[key].office_assigned
                                  )
            except IntegrityError:
                pass
        for key, value in self.all_rooms.items():
            try:
                RoomModel.create(room_name=key,
                                 room_type=self.all_rooms[key].room_type,
                                 capacity=self.all_rooms[key].capacity,
                                 has_free_space=self.all_rooms[key].has_free_space,
                                 occupants=self.all_rooms[key].occupants,
                                 number_of_occupants=self.all_rooms[key].number_of_occupants)
            except IntegrityError:
                pass
        db.close()
        return "Saved state successfully"

    def load_state(self):
        db.connect()
        queried_fellows = FellowModel.select()
        for queried_fellow in queried_fellows:
            new_fellow_object = Fellow(queried_fellow.person_name)
            new_fellow_object.living_space_assigned = queried_fellow.living_space_assigned
            new_fellow_object.office_assigned = queried_fellow.office_assigned
            new_fellow_object.position = 'Fellow'
            self.list_of_fellows[queried_fellow.person_name] = new_fellow_object
            self.list_of_people[queried_fellow.person_name] = new_fellow_object
            self.total_number_of_fellows += 1
            self.total_number_of_people += 1
        queried_staffers = StaffModel.select()
        for queried_staffer in queried_staffers:
            new_staffer_object = Staff(queried_staffer.person_name)
            new_staffer_object.position = queried_staffer.person_position
            new_staffer_object.office_assigned = queried_staffer.office_assigned
            self.list_of_staff[queried_staffer.person_name] = new_staffer_object
            self.list_of_people[queried_staffer.person_name] = new_staffer_object
            self.total_number_of_staff += 1
            self.total_number_of_people += 1
        queried_rooms = RoomModel.select()
        for queried_room in queried_rooms:
            if queried_room.room_type.lower() == 'office':
                new_office_object = Office(queried_room.room_name)
                new_office_object.room_type = queried_room.room_type
                new_office_object.number_of_occupants = queried_room.number_of_occupants
                new_office_object.capacity = queried_room.capacity
                new_office_object.occupants = queried_room.occupants
                if queried_room.has_free_space == 0:
                    new_office_object.has_free_space = False
                if queried_room.has_free_space == 1:
                    new_office_object.has_free_space = True
                self.office_spaces[queried_room.room_name] = new_office_object
                self.all_rooms[queried_room.room_name] = new_office_object
                self.number_of_offices += 1
            if queried_room.room_type.lower() == 'living space':
                new_living_space_object = LivingSpace(queried_room.room_name)
                new_living_space_object.room_type = queried_room.room_type
                new_living_space_object.number_of_occupants = queried_room.number_of_occupants
                new_living_space_object.occupants = queried_room.occupants
                new_living_space_object.capacity = queried_room.capacity
                if queried_room.has_free_space == 0:
                    new_living_space_object.has_free_space = False
                if queried_room.has_free_space == 1:
                    new_living_space_object.has_free_space = True
                self.living_spaces[queried_room.room_name] = new_living_space_object
                self.all_rooms[queried_room.room_name] = new_living_space_object
                self.number_of_living_spaces += 1
            self.total_number_of_rooms += 1
        db.close()
        return 'Loaded state successfully'

from unittest import TestCase
from app.dojo import Dojo
from app.person import Person
from app.fellow import Fellow
from app.staff import Staff
from app.room import Room
from app.living_space import LivingSpace
from app.office import Office


class TestClassRelationships(TestCase):
    def test_fellow_subclass_of_person(self):
        self.assertTrue(issubclass(Fellow, Person), msg='Fellow is not a subclass of Person')

    def test_staff_subclass_of_person(self):
        self.assertTrue(issubclass(Staff, Person), msg='Staff is not a subclass of Person')

    def test_office_subclass_of_room(self):
        self.assertTrue(issubclass(Office, Room), msg='Office is not a subclass of Room.')

    def test_livingspace_subclass_of_room(self):
        self.assertTrue(issubclass(LivingSpace, Room), msg='LivingSpace is not a subclass of Room')


class TestDojoClass(TestCase):
    def setUp(self):
        self.my_dojo = Dojo()

    def test_successfully_create_room(self):
        initial_room_count = self.my_dojo.total_number_of_rooms
        sanctuary = self.my_dojo.create_room('Sanctuary', 'office')
        self.assertTrue(sanctuary, msg='Sanctuary room was not created successfully')
        new_room_count = self.my_dojo.total_number_of_rooms
        self.assertEqual(new_room_count - initial_room_count, 1, msg='Inaccurate Number of rooms')

    def test_successfully_add_person(self):
        initial_people_count = len(self.my_dojo.list_of_people)
        self.my_dojo.add_person('John', 'Staff')
        new_people_count = len(self.my_dojo.list_of_people)
        self.assertEqual(new_people_count - initial_people_count, 1, msg='Inaccurate number of people')

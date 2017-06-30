import os
from unittest import TestCase

from app.dojo import Dojo
from app.fellow import Fellow
from app.living_space import LivingSpace
from app.office import Office
from app.person import Person
from app.room import Room
from app.staff import Staff


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

    def test_valid_room_type(self):
        invalid_room_type = self.my_dojo.create_room('war room', 'bathroom')
        self.assertEqual(invalid_room_type, ' Enter a valid room type!', msg='Permits invalid room types to be created')
        self.assertIn('Enter a valid room type e.g. Office, Living space',
                      self.my_dojo.create_multiple_rooms('pantry', 'one', 'two'))

    def test_valid_input_for_create_room(self):
        with self.assertRaises(TypeError):
            self.my_dojo.create_room('Sanctuary', 5)

    def test_successfully_add_person(self):
        self.my_dojo.create_room('command center', 'office')
        initial_people_count = len(self.my_dojo.list_of_people)
        self.my_dojo.add_person('John', 'Staff')
        new_people_count = len(self.my_dojo.list_of_people)
        self.assertEqual(new_people_count - initial_people_count, 1, msg='Inaccurate number of people')

    def test_successfully_allocate_living_space(self):
        self.my_dojo.create_room('penthouse', 'living space')
        self.my_dojo.create_room('command center', 'office')
        self.assertIn('penthouse', self.my_dojo.living_spaces.keys())
        self.assertIn('command center', self.my_dojo.office_spaces.keys())
        initial_num_of_occupants = len(self.my_dojo.living_spaces['penthouse'].occupants)
        self.my_dojo.add_person('kimberly', 'fellow', True)
        new_num_of_occupants = len(self.my_dojo.living_spaces['penthouse'].occupants)
        self.assertEqual(new_num_of_occupants - initial_num_of_occupants, 1, msg='Inaccurate number of occupants in '
                                                                                 'room')

    def test_successfully_allocate_office_space(self):
        self.my_dojo.create_room('command center', 'office')
        self.my_dojo.create_room('cozy space', 'living space')
        initial_num_of_occupants = len(self.my_dojo.office_spaces['command center'].occupants)
        self.my_dojo.add_person('tinky winky', 'fellow')
        self.my_dojo.add_person('dipsy', ' staff')
        final_num_of_occupants = len(self.my_dojo.office_spaces['command center'].occupants)
        new_assignees = final_num_of_occupants - initial_num_of_occupants
        self.assertEqual(new_assignees, 2, msg='Inaccurate number of occupants. Expected 2!')
        self.assertEqual(self.my_dojo.office_spaces['command center'].occupants, ['tinky winky', 'dipsy'], msg='{} != '
                                                                                                               '[\'tinky winky\', \'dipsy\']'.format(
            self.my_dojo.office_spaces['command center'].occupants))

    def test_successfully_create_multiple_rooms(self):
        initial_room_count = self.my_dojo.number_of_offices
        self.my_dojo.create_multiple_rooms('office', 'War room', 'kitchen')
        final_room_count = self.my_dojo.number_of_offices
        num_of_new_offices = final_room_count - initial_room_count
        self.assertEqual(num_of_new_offices, 2, msg='Inaccurate number of offices')

    def test_successfully_add_multiple_people(self):
        self.my_dojo.create_multiple_rooms('office', 'War room', 'kitchen')
        initial_staff_count = self.my_dojo.total_number_of_staff
        self.my_dojo.add_multiple_people('staff', 'Harry', 'Hermione', 'Voldermort')
        final_staff_count = self.my_dojo.total_number_of_staff
        num_of_new_staff = final_staff_count - initial_staff_count
        self.assertEqual(num_of_new_staff, 3, msg='Inaccurate number of new staff')

    def test_rejects_duplicate_rooms(self):
        self.my_dojo.create_room('ops center', 'office')
        self.assertEqual(self.my_dojo.create_room('ops center', 'office'),
                         ' A room called ops center already exists!\n',
                         msg='Does not detect duplicate room entry')

    def test_print_room(self):
        self.my_dojo.create_room('ops center', 'office')
        self.my_dojo.add_person('Wolverine', 'staff')
        occupant_list = self.my_dojo.print_room('ops center')
        self.assertEqual(1, len(occupant_list), msg='Incorrect number of occupants')
        self.assertEqual(['Wolverine'], occupant_list, msg='Wolverine not in list of occupants')

    def test_fellow_unallocated_living_space(self):
        self.my_dojo.create_room('main office', 'office')
        self.my_dojo.add_person('Professor X', 'fellow')
        self.assertEqual('', self.my_dojo.list_of_fellows['Professor X'].living_space_assigned)
        self.assertIn('There are no rooms of type living spaces!', self.my_dojo.add_person('Storm', 'fellow', True))
        self.assertIn('Storm', self.my_dojo.unallocated_people)

    def test_duplicate_name(self):
        self.my_dojo.add_person('Cyclops', 'staff')
        self.assertIn('A person with this name already exists', self.my_dojo.add_person('Cyclops', 'fellow'),
                      msg='Duplicate name permitted!')

    def test_valid_person_position_check(self):
        self.assertIn('Enter a valid position e.g. Fellow, Staff', self.my_dojo.add_person('Magneto', 'villain'),
                      msg='Invalid position permitted')
        self.assertIn('Enter a valid position e.g. Staff, Fellow',
                      self.my_dojo.add_multiple_people('good guys', 'logan', 'mystique'),
                      msg='Invalid position permitted')

    def test_no_office_spaces_with_free_space(self):
        self.my_dojo.create_room('home', 'office')
        self.my_dojo.add_multiple_people('staff', 'hulk', 'black panther', 'black widow', 'iron man', 'loki', 'thor')
        self.assertFalse(self.my_dojo.all_rooms['home'].has_free_space)
        self.assertIn('No offices with free space!', self.my_dojo.add_person('captain america', 'staff'),
                      msg='No alert of no free office space')

    def test_no_living_spaces_with_free_space(self):
        self.my_dojo.create_room('home', 'office')
        self.my_dojo.create_room('penthouse', 'living space')
        self.my_dojo.add_person('the flash', 'fellow', True)
        self.my_dojo.add_person('arrow', 'fellow', True)
        self.my_dojo.add_person('aquaman', 'fellow', True)
        self.my_dojo.add_person('joker', 'fellow', True)
        self.assertFalse(self.my_dojo.all_rooms['penthouse'].has_free_space)
        self.assertIn('No living spaces with free space!', self.my_dojo.add_person('supergirl', 'fellow', True))

    def test_print_unallocated(self):
        self.assertIn('Nobody is unallocated', self.my_dojo.print_unallocated())
        self.my_dojo.add_person('Unallocated guy', 'staff')
        self.assertIsNone(self.my_dojo.print_unallocated())

    def test_print_allocations(self):
        self.assertIn('No rooms have been created yet!', self.my_dojo.print_allocations())
        self.my_dojo.create_room('main', 'office')
        self.my_dojo.add_person('Allocated guy', 'staff')
        self.assertIsNone(self.my_dojo.print_allocations())

    def test_successfully_removes_person_from_room(self):
        self.my_dojo.create_room('Krypton', 'office')
        self.my_dojo.add_person('John Wick', 'Staff')
        self.assertTrue('John Wick' in self.my_dojo.all_rooms['Krypton'].occupants, msg='Failed room allocation')
        self.my_dojo.remove_person('John Wick', 'Krypton')
        self.assertFalse('John Wick' in self.my_dojo.all_rooms['Krypton'].occupants, msg='Failed room allocation')
        wrong_attempt = self.my_dojo.remove_person('King Kong', 'Krypton')
        self.assertEqual(wrong_attempt,
                         'King Kong has not been assigned to the room Krypton, or, the room Krypton is invalid ')

    def test_successfully_load_people_from_file(self):
        THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        my_data_path = os.path.join(THIS_DIR, os.pardir, 'Imports/load_file')
        self.my_dojo.create_room('main', 'office')
        self.my_dojo.create_room('penthouse', 'living space')
        self.my_dojo.load_people(my_data_path)
        self.assertIn('OLUWAFEMI SULE', self.my_dojo.list_of_people, msg='File did not load successfully')
        self.assertIn('DOMINIC WALTERS', self.my_dojo.list_of_staff, msg='File did not load successfully')
        self.assertEqual(8, self.my_dojo.total_number_of_people, msg='Wrong number of people loaded')

    def test_save_state(self):
        self.my_dojo.create_room('mordor', 'office')
        self.my_dojo.create_room('penthouse', 'living space')
        self.my_dojo.create_room('main', 'office')
        self.my_dojo.create_room('cozy space', 'living space')
        self.my_dojo.add_person('the flash', 'fellow', True)
        self.my_dojo.add_person('arrow', 'fellow', True)
        self.my_dojo.add_person('aquaman', 'fellow', True)
        self.my_dojo.add_person('joker', 'fellow', True)
        self.assertEqual(self.my_dojo.save_state(), ' Saved state successfully', msg='State not saved successfully')

    def test_load_state(self):
        self.my_dojo.add_person('inferno', 'staff')
        self.my_dojo.add_person('supergirl', 'fellow', True)
        self.my_dojo.create_room('mordor', 'office')
        self.my_dojo.create_room('penthouse', 'living space')
        self.my_dojo.create_room('main', 'office')
        self.my_dojo.create_room('cozy space', 'living space')
        self.my_dojo.add_person('the flash', 'fellow', True)
        self.my_dojo.add_person('arrow', 'fellow', True)
        self.my_dojo.add_person('aquaman', 'staff')
        self.my_dojo.add_person('joker', 'staff')
        self.assertEqual(self.my_dojo.save_state(), ' Saved state successfully', msg='State not saved successfully')
        self.assertEqual(self.my_dojo.load_state('dojo.db'), ' Loaded state successfully')
        self.assertEqual(self.my_dojo.load_state('strange_one.db'), ' A database called strange_one.db does not exist!')

    def test_successfully_reallocate_office(self):
        self.my_dojo.create_room('mordor', 'office')
        self.my_dojo.add_person('john mayer', 'staff')
        initial_number_of_mordor_occupants = len(self.my_dojo.all_rooms['mordor'].occupants)
        self.my_dojo.create_room('oculus', 'office')
        initial_number_of_oculus_occupants = len(self.my_dojo.all_rooms['oculus'].occupants)
        self.my_dojo.reallocate_person('john mayer', 'oculus')
        final_number_of_mordor_occupants = len(self.my_dojo.all_rooms['mordor'].occupants)
        final_number_of_oculus_occupants = len(self.my_dojo.all_rooms['oculus'].occupants)
        self.assertEqual(1, initial_number_of_mordor_occupants - final_number_of_mordor_occupants)
        self.assertEqual(1, final_number_of_oculus_occupants - initial_number_of_oculus_occupants)
        self.assertIn(' john mayer has successfully been reallocated to the room oculus.',
                      self.my_dojo.reallocate_person('john mayer', 'oculus'),
                      msg='john mayer not reallocated successfully')

    def test_successfully_reallocate_living_space(self):
        self.my_dojo.create_room('mordor', 'living space')
        self.my_dojo.add_person('john mayer', 'fellow', True)
        initial_number_of_mordor_occupants = len(self.my_dojo.all_rooms['mordor'].occupants)
        self.my_dojo.create_room('oculus', 'living space')
        initial_number_of_oculus_occupants = len(self.my_dojo.all_rooms['oculus'].occupants)
        self.my_dojo.reallocate_person('john mayer', 'oculus')
        final_number_of_mordor_occupants = len(self.my_dojo.all_rooms['mordor'].occupants)
        final_number_of_oculus_occupants = len(self.my_dojo.all_rooms['oculus'].occupants)
        self.assertEqual(1, initial_number_of_mordor_occupants - final_number_of_mordor_occupants)
        self.assertEqual(1, final_number_of_oculus_occupants - initial_number_of_oculus_occupants)
        self.assertIn(' john mayer has successfully been reallocated to the room oculus.',
                      self.my_dojo.reallocate_person('john mayer', 'oculus'),
                      msg='john mayer not reallocated successfully')

    def test_reallocate_room_rejects_non_existent_room(self):
        self.my_dojo.create_room('mordor', 'office')
        self.my_dojo.add_person('john mayer', 'staff')
        self.assertIn(' A room called oculus does not exist in the dojo',
                      self.my_dojo.reallocate_person('john mayer', 'oculus'))

    def test_rejects_reallocate_staff_to_living_space(self):
        self.my_dojo.create_room('mordor', 'office')
        self.my_dojo.create_room('penthouse', 'living space')
        self.my_dojo.add_person('john mayer', 'staff')
        self.assertIn('Staff members cannot be allocated living spaces!',
                      self.my_dojo.reallocate_person('john mayer', 'penthouse'))

    def test_cannot_reallocate_to_full_living_space(self):
        self.my_dojo.create_room('penthouse', 'living space')
        self.my_dojo.add_person('the flash', 'fellow', True)
        self.my_dojo.add_person('arrow', 'fellow', True)
        self.my_dojo.add_person('aquaman', 'fellow', True)
        self.my_dojo.add_person('joker', 'fellow', True)
        self.my_dojo.create_room('mordor', 'living space')
        self.my_dojo.add_person('john mayer', 'fellow', True)
        self.assertIn('penthouse does not have any free space!',
                      self.my_dojo.reallocate_person('john mayer', 'penthouse'))

    def test_cannot_reallocate_to_full_office(self):
        self.my_dojo.create_room('penthouse', 'office')
        self.my_dojo.add_person('the flash', 'staff')
        self.my_dojo.add_person('arrow', 'staff')
        self.my_dojo.add_person('aquaman', 'staff')
        self.my_dojo.add_person('joker', 'staff')
        self.my_dojo.add_person('deadshot', 'staff')
        self.my_dojo.add_person('harley quinn', 'staff')
        self.my_dojo.create_room('mordor', 'office')
        self.my_dojo.add_person('john mayer', 'staff')
        self.assertIn('penthouse does not have any free space!',
                      self.my_dojo.reallocate_person('john mayer', 'penthouse'))

    def test_reallocate_room_rejects_non_existent_person(self):
        self.assertIn('A person called john mayer does not exist in the dojo!',
                      self.my_dojo.reallocate_person('john mayer', 'penthouse'))

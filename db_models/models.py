from peewee import *

db = SqliteDatabase(None)


class FellowModel(Model):
    person_name = CharField(max_length=255, unique=True)
    person_position = CharField(max_length=255)
    office_assigned = CharField(max_length=255)
    living_space_assigned = CharField(max_length=255)

    class Meta:
        database = db


class StaffModel(Model):
    person_name = CharField(max_length=255, unique=True)
    person_position = CharField(max_length=255)
    office_assigned = CharField(max_length=255)

    class Meta:
        database = db


class RoomModel(Model):
    room_name = CharField(max_length=255, unique=True)
    room_type = CharField(max_length=255)
    capacity = IntegerField()
    has_free_space = BooleanField()
    occupants = TextField()
    number_of_occupants = IntegerField()

    class Meta:
        database = db

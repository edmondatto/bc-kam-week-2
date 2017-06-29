[![Build Status](https://travis-ci.org/edmondatto/bc-kam-week-2.svg?branch=master)](https://travis-ci.org/edmondatto/bc-kam-week-2)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ce741707f6fe46bf9f73065779778368)](https://www.codacy.com/app/edmondatto/bc-kam-week-2?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=edmondatto/bc-kam-week-2&amp;utm_campaign=Badge_Grade)

## Overview
This command line application is used to create office and living spaces and manage their random assignment to staff and/or fellows at Andela. 

### Dependencies
* **[coverage==4.3.4](https://coverage.readthedocs.io/)** - A tool for measuring code coverage in Python tests. This measurement is typically used to gauge the effectiveness of tests

* **[docopt==0.6.2](http://docopt.org/)** - A tool that helps you define the interface for your command-line app, and automatically generate a parser for it.

* **[peewee==2.10.1](docs.peewee-orm.com/)** - A simple ORM that manages all the aspects of saving and loading the application's data

## Use cases

### Create room
```
USAGE: create_room <room_type> <room_name>...
```
This command allows the user to enter a room type as the first argument and it's name as the second. 
A room is then created and a message is printed to the screen.
```
INPUT: create_room office BizLounge
```
```
OUTPUT: An office called BizLounge has been successfully created!
```

This method also allows for creation of multiple rooms of the same type at a time by providing for passing of multiple room names at a go.

```
INPUT: create_room livingspace Lounge Hall
```

```
OUTPUT:
An office called Lounge has been successfully created!
An office called Hall has been successfully created!
```
### Add person
This command allows a user to add a person and assign them either an office, living space or both; depending on whether they are a fellow or not and whether they want accommodation or not.
```
USAGE: add_person <first_name> <last_name> <Fellow_or_Staff> [<wants_accommodation>]
```

```
INPUT: add_person John Doe Fellow Y
```
 
```
OUTPUT:
Fellow edmond atto has been successfully added.
John Doe has been allocated the Office BizLounge
John Doe has been allocated the Living Space Hall
```

### Print Room
This command prints the names of all the people in a room name to the screen.
```
USAGE: print_room <room_name>
```

```
INPUT: print_room OpsCenter
```

```
OUTPUT:
John Doe
Jane Doe
Uncle Jane
```

### Print Allocations
This command takes no required arguments and prints to the screen a list of all rooms and their occupants. 
```
USAGE: print_allocations [<-o=filename>]
```
```
INPUT: print_allocations
```
```
OUTPUT:

OPS CENTER
--------------------------------------------------
Wolverine, Storm, Professor X


WAR ROOM
--------------------------------------------------
Chuck Norris, Bruce Lee
```

To print the allocations to a text file, use the optional argument [<-o=filename>] to set the name of the text file
```
INPUT: print_allocations allocations.txt 
```

```
OUTPUT:

OPS CENTER
--------------------------------------------------
Wolverine, Storm, Professor X


WAR ROOM
--------------------------------------------------
Chuck Norris, Bruce Lee


The list of allocations has been written to the file allocations.txt
```

### Print Unallocated
This command takes no required arguments and prints to the screen a list of all rooms and their occupants. 
```
USAGE: print_allocations [<-o=filename>]
```
```
INPUT: print_unallocated
```
```
OUTPUT:

UNALLOCATED
--------------------------------------------------
Wolverine, Storm, Professor X

```

To print the allocations to a text file, use the optional argument [<-o=filename>] to set the name of the text file
```
INPUT: print_allocations allocations.txt 
```

```
OUTPUT

UNALLOCATED
--------------------------------------------------
Wolverine, Storm, Professor X

The list of Unallocated people has been written to the file unallocated.txt
```

### Load people
This command takes no arguments and creates people loaded from a text file and automatically assigns them rooms and/or office spaces respectively.
```
USAGE: load_people
```
```
INPUT: load_people
```
```
OUTPUT: People have been loaded successfully from the file
```

### Save state
This function persists all the data stored in the app to a SQLite database. Specifying the ​--db​ parameter explicitly stores the data in the sqlite_database​ specified.
```
USAGE: save_state [--db=sqlite_database]
```
```
INPUT: save_state
```
```
OUTPUT: Saved state successfully
```

### Load state
Loads data from a specified database into the application.
```
USAGE: load_state <sqlite_database>
```
```
INPUT: load_state dojo.db
```
```
OUTPUT: Loaded state successfully
```
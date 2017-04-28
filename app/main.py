# ************************************************************************************************
#    BASED ON DOCOPT EXAMPLE FROM GITHUB
#    Title: interactive_example.py
#    Author: JonLundy & TheWaWar
#    Date: Jun 1, 2015
#    Availability: https://github.com/docopt/docopt/blob/master/examples/interactive_example.py
# ***********************************************************************************************

""" rand string

Usage:
        
    dojo create_room <room_type> <room_name>...
    dojo add_person <first_name> <last_name> <Fellow_or_Staff> [wants_accommodation]
    dojo print_room <room_name>
    dojo print_allocations [<-o=filename>]
    dojo print_unallocated [<print_unallocated>]
    dojo (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.

"""
import cmd
import sys

from docopt import docopt, DocoptExit

from app.dojo import Dojo

the_dojo = Dojo()


def docopt_cmd(func):
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.
            print('Invalid Command!')
            print(e)
            return
        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return
        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():
    print(__doc__)


class AndelaDojo(cmd.Cmd):
    intro = '\nThis is the Andela Dojo Ops Center!' \
            + ' (type help for a list of commands)\n'
    prompt = '[dojo] > '
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        room_names = arg['<room_name>']
        room_type = arg['<room_type>']
        if room_type == 'livingspace':
            room_type = 'living space'
        for room_name in room_names:
            output = the_dojo.create_room(room_name, room_type)
            print(output)

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <last_name> <Fellow_or_Staff> [<wants_accomodation>]"""
        person_name = arg['<first_name>'] + ' ' + arg['<last_name>']
        person_position = arg['<Fellow_or_Staff>']
        if arg['<wants_accomodation>'] == 'Y':
            wants_accomodation = True
        else:
            wants_accomodation = False
        output = the_dojo.add_person(person_name, person_position, wants_accomodation)
        print(output)

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        room_name = arg['<room_name>']
        output = the_dojo.print_room(room_name)
        for person_name in output:
            print(person_name)

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [<-o=filename>]"""
        file_to_print = arg['<-o=filename>']
        output = the_dojo.print_allocations(file_to_print)
        print(output)

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [<-o=filename>]"""
        file_to_print = arg['<-o=filename>']
        output = the_dojo.print_unallocated(file_to_print)
        print(output)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print('You have left the Dojo!')
        exit()


opt = docopt(__doc__, sys.argv[1:])
AndelaDojo().cmdloop()
print(opt)

#!/usr/bin/env python

"""
Amity has rooms which can be offices or living spaces.
An office can occupy a maximum of 6 people.
A living space can inhabit a maximum of 4 people.

A person to be allocated could be a fellow or staff.
Staff cannot be allocated living spaces.
Fellows have a choice to choose a living space or not.

This system will be used to automatically allocate spaces to people at random.


Usage:
    amity create_room <room_name> <room_type>
    amity add_person <first_name> <last_name> <designation> [<wants_accomodation>]
    amity reallocate_person <first_name> <last_name> <new_room>
    amity load_people <txt_file_name>
    amity print_allocations [<txt_file_name>]
    amity print_room [<room_name>]
    amity save_state [--db=database_name_goes_here]
    amity load_state <database_name>
    amity (-i | --interactive)
    amity (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from app.Amity import Amity


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
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


class AmityInteractive (cmd.Cmd):

    prompt = '(amity) '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """
        Create a new room with specified name and type

        Usage:
            create_room <room_name> <room_type>
        """
        pass

    @docopt_cmd
    def do_add_person(self, arg):
        """
        Create a person and assign them random office and a living space
        (if they want one)

        Usage:
            add_person <first_name> <last_name> <designation>
            [<wants_accomodation>]
        """
        pass

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """
        Reallocate a person to a new room

        Usage:
            reallocate_person <first_name> <last_name> <new_room>
        """
        pass

    @docopt_cmd
    def do_load_people(self, arg):
        """
        Add people to rooms from a txt file

        Usage:
            load_people <txt_file_name>
        """
        pass

    @docopt_cmd
    def do_print_allocations(self, arg):
        """
        Print a list of allocations onto the screen

        Specifying a txt_file_name outputs the information to that txt file

        Usage:
            print_allocations [<txt_file_name>]
        """
        pass

    @docopt_cmd
    def do_print_room(self, arg):
        """
        Print the names of all the people in specified room on the screen

        Usage:
            print_room [<room_name>]
        """
        pass

    @docopt_cmd
    def do_save_state(self, arg):
        """
        Persist all the data stored in the app to an SQLite database

        Specifying the --db parameter explicitly stores the data in the
        sqlite_database specified

        Usage:
            save_state [--db=database_name_goes_here]
        """
        pass

    @docopt_cmd
    def do_load_state(self, arg):
        """
        Load data from a database into the application

        Usage:
            load_state <database_name>
        """
        pass

    def do_quit(self, arg):
        """
        Quit app
        """

        print('Don\'t forget to be awesome. Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:], help=True)

if opt['--interactive']:
    try:
        AmityInteractive().cmdloop()
    except SystemExit:
        pass
    except KeyboardInterrupt:
        pass

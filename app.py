#!/usr/bin/env python
"""
Usage:
    create_room -l room_name
    add_person name, designation, (wants_accomodation([Y|N]))
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


class MyInteractive(cmd.Cmd):

    intro = 'Welcome to my interactive program!' \
        + ' (type help for a list of commands.)' \
        + "\n click on the screen to be able to type"
    prompt = '(my_program) '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        Amity.create_room(args)


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        MyInteractive().cmdloop()
    except SystemExit:
        pass
    except KeyboardInterrupt:
        pass

print(opt)

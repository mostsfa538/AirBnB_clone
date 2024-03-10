#!/usr/bin/python3
"""airbnb entry point"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """manual cmd
    """
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def help_emptyline(self):
        sys.stdout.write("doing nothing if you press enter when emptyline\n")

    def do_EOF(self, line):
        """ending the console session
        """
        return True

    def help_EOF(self):
        sys.stdout.write("[EOF] ending the program ctrl + D in linux\n")

    def do_quit(self, line):
        """quitting the console session
        """
        return True

    def help_quit(self):
        sys.stdout.write("quiting the program by typing <quit>")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

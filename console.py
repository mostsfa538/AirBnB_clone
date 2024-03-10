#!/usr/bin/python3
"""airbnb entry point"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """manual cmd
    """
    prompt = "(hbnb) "
    def do_EOF(self, line):
        """ending the console session
        """
        return True

    def do_quit(self, line):
        """quitting the console session
        """
        return True

    def do_emptyline(self, line):
        pass
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()

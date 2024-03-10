#!/usr/bin/python3
"""airbnb entry point"""

import cmd


class HBNBCommand(cmd.Cmd):
    """manual cmd
    """
    prompt = "(hbnb) "
    def do_EOF(self, line):
        """ending the console session
        """
        return True

    def do_quit(self, line):
        """ending the console session
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

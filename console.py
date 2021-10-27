#!/usr/bin/python3
"""AirBnB console"""


import cmd


class HBNBCommand(cmd.Cmd):
    """AirBnB console"""
    prompt = "(hbnb)"

    def quit(self):
        """quit function"""

    def EOF(self):
        """EOF function"""

    def help(self):
        """does some bullshit whatever"""


if __name__ == '__main__':
        HBNBCommand().cmdloop()

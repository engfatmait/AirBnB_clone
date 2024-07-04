#!/usr/bin/python3
"""
 contains the entry point of the command interpreter

"""
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
        quit the program
        """
        return True

    def help_quit(self, arg):
        """
        help to quit
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        print white line and exit
        """
        print("")
        return True
    def emptyline(self):
        """
        handle empty line to make nothing
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

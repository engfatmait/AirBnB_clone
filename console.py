#!/usr/bin/python3
"""
 contains the entry point of the command interpreter

"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    valid_classes =["BaseModel"]

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
    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it
        """
        if len(args) == 0:
            print("** class name missing **")
        token = args.split()
        if token[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)





if __name__ == '__main__':
    HBNBCommand().cmdloop()

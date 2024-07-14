#!/usr/bin/python3
"""
 contains the entry point of the command interpreter

"""
import cmd
from models.base_model import BaseModel
from models import storage


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
        token = args.split()
        if len(token) == 0:
            print("** class name missing **")
        elif token[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class name and id
        """
        command = args.split()
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(command[0], command[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        obj = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif obj[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(obj) < 2:
            print("** instance id missing **")
        else:
            objects = FileStorage.all()
            key = "{}.{}".format(obj[0], obj[1])
            if key in objects:
                del objects[key]
                FileStorage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):

        """
         Prints all string representation of all instances based or not on the class name
        """
        objects = storage.all()
        command = args.split()
        if len(command) == 0:
            for key, value in objects.items():
                print(str(value))
        elif command[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == command[0]:
                    print(str(value))
    def do_update(self, arg):
        """
         Updates an instance based on the class name and id by adding 
         or updating attribute (save the change into the JSON file).
        """
        commands = arg.split()
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
             objects = storage.all()

        key = "{}.{}".format(commands[0], commands[1])
        if key not in objects:
            print("** no instance found **")
        elif len(commands) < 3:
            print ("** attribute name missing **")
        elif len(commands) < 4:
            print ("** value missing **")
        else:
             obj = objects[key]
             attr_name = commands[2]
             attr_value = commands[3]

        try:
            attr_value = eval(attr_value)
        except exception:
            pass
        setattr(obj, attr_name, attr_value)
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

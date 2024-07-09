#!/usr/bin/python3
""" contains the entry point of the comman interpreter """
import cmd
import json
from models import storage


class HBNBCommand(cmd.Cmd):
    """ command interpreter """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit program\n"""
        return True

    def do_EOF(self, arg):
        """Ctrl-D to exit program\n"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        cls = (line.split()[0]).strip()
        if line is None or len(cls) == 0:
            print("** class name missing **")
        elif cls != "BaseModel":
            print("** class doesn't exist **")
        else:
            from models.base_model import BaseModel
            new = eval(cls)()
            new.save()
            print(new.id)

    def do_show(self, line):
        """Prints string repr of an instance"""
        class_name, ids  = line.split()
        if (class_name is None or len(class_name.strip()) == 0):
            print("** class name missing **")
        elif (ids is None or len(ids.strip()) == 0):
            print("** instance id missing **")


    def destroy(self):
        """Deletes an instance based on the class name"""

    def all(self):
        """Prints str repr of all instances"""

    def update(self):
        """Updates an instance basn class name and id"""


if __name__ == "__main__":
    HBNBCommand().cmdloop()

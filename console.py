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
        if line is None or len(line.strip()) == 0:
            print("** class name missing **")
        elif line.split()[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            from models.base_model import BaseModel
            new = BaseModel()
            new.save()
            print(new.id)

    def show(self):
        """Prints string repr of an instance"""

    def destroy(self):
        """Deletes an instance based on the class name"""

    def all(self):
        """Prints str repr of all instances"""

    def update(self):
        """Updates an instance basn class name and id"""


if __name__ == "__main__":
    HBNBCommand().cmdloop()

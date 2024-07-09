#!/usr/bin/python3
""" contains the entry point of the comman interpreter """
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = ["BaseModel",
           "User",
           "State",
           "City",
           "Amenity",
           "Place",
           "Review"]


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
        elif line.split()[0].strip() not in classes:
            print("** class doesn't exist **")
        else:
            cls = (line.split()[0]).strip()
            new = eval(cls)()
            new.save()
            print(new.id)

    def do_show(self, line):
        """Prints string repr of an instance"""
        if (line is None or len(line.strip()) == 0):
            print("** class name missing **")
        elif (line.split()[0] not in classes):
            print("** class doesn't exist **")
        else:
            try:
                class_name, ids = line.split()
                inst = storage.all()[class_name + '.' + ids]
                print(inst)
            except ValueError:
                print("** instance id missing **")
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name"""
        if (line is None or len(line.strip()) == 0):
            print("** class name missing **")
        elif (line.split()[0] not in classes):
            print("** class doesn't exist **")
        else:
            try:
                class_name, ids = line.split()
                del storage.all()[class_name + '.' + ids]
                storage.save()
            except ValueError:
                print("** instance id missing **")
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """Prints str repr of all instances"""
        if (line is None or len(line.strip()) == 0):
            for key, value in storage.all().items():
                class_name, ids = key.split('.')
                inst = storage.all()[class_name + '.' + ids]
                print(inst)
        elif line.strip() not in classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                class_name, ids = key.split('.')
                if class_name == line.strip():
                    inst = storage.all()[class_name + '.' + ids]
                    print(inst)

    def update(self):
        """Updates an instance basn class name and id"""


if __name__ == "__main__":
    HBNBCommand().cmdloop()

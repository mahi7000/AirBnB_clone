#!/usr/bin/python3
""" contains the entry point of the comman interpreter """
import cmd
import json
import models


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
        elif line.split()[0].strip() != "BaseModel":
            print("** class doesn't exist **")
        else:
            from models.base_model import BaseModel
            cls = (line.split()[0]).strip()
            new = eval(cls)()
            new.save()
            print(new.id)

    def do_show(self, line):
        """Prints string repr of an instance"""
        classes = ["BaseModel"]
        if (line is None or len(line.strip()) == 0):
            print("** class name missing **")
        elif (line.split()[0] not in classes):
            print("** class doesn't exist **")
        else:
            try:
                class_name, ids = line.split()
                inst = models.storage.all()[class_name + '.' + ids]
                print(inst)
            except ValueError:
                print("** instance id missing **")
            except KeyError:
                print("** no instance found **")

    def destroy(self):
        """Deletes an instance based on the class name"""

    def all(self):
        """Prints str repr of all instances"""

    def update(self):
        """Updates an instance basn class name and id"""


if __name__ == "__main__":
    HBNBCommand().cmdloop()

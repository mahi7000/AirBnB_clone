#!/usr/bin/python3
""" contains the entry point of the comman interpreter """
import cmd


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

    def create(self):
        """Creates a new instance of BaseModel"""

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

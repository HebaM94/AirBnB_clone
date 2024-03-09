#!/usr/bin/python3
"""console"""
import cmd
import sys
from models.base_model import BaseModel
import json


class HBNBCommand(cmd.Cmd):
    """Interactive command line interface."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """Quit the hbnb shell"""
        print("")
        return True

    def emptyline(self):
        """override the cmd emptyline function to do nothing
        if empty line and enter passed to console"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        else:
            class_name = arg.split()[0]
            if class_name != "BaseModel":
                print("** class doesn't exist **")
                return
            else:
                new_obj = BaseModel()
                new_obj.save()
                print("{}".format(new_obj.id))

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)"""

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
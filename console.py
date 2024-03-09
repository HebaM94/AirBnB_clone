#!/usr/bin/python3
"""console"""
import cmd
import sys
from models.base_model import BaseModel
import json


class HBNBCommand(cmd.Cmd):
    """Interactive command line interface."""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """Quit the hbnb shell"""
        print("")
        return True
    
    def do_creat(self, arg):
        """Create a new object Class(arg)"""
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
        """Show all objects of Class(arg)"""

    def do_destroy(self, arg):
        """"""

    def do_all(self, arg):
        """"""

    def do_update(self, arg):
        """"""
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()

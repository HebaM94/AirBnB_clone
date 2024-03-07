#!/usr/bin/python3
"""console"""
import cmd
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

    def do_create(self, arg):
        """Creates new instance of BaseModel, saves it to JSON file & prints id"""
        if arg is None:
            print("** class name missing **")
        return
    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()

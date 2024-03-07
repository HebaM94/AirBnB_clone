#!/usr/bin/python3
"""console"""
import cmd


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

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()

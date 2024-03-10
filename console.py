#!/usr/bin/python3
"""console"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """Interactive command line interface."""
    prompt = '(hbnb)'
    __classes = {"BaseModel", "User", "State", "City",
                 "Amenity", "Place", "Review"}

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
            if class_name not in self.__classes:
                print("** class doesn't exist **")
                return
            else:
                new_obj = eval(class_name)()
                storage.save()
                print("{}".format(new_obj.id))

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in self.__classes:
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print("** instance id missing **")
                return
            else:
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                if key not in storage.all():
                    print("** no instance found **")
                    return
                print(str(storage.all()[key]))

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in self.__classes:
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print("** instance id missing **")
                return
            else:
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                if key not in storage.all():
                    print("** no instance found **")
                    return
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        args = arg.split()
        if len(args) > 0 and args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        obj_list = []
        for obj in storage.all().values():
            if len(args) == 0 or obj.__class__.__name__ == args[0]:
                object_list.append(str(obj))
            print(object_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in self.__classes:
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print("** instance id missing **")
                return
            else:
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                if key not in storage.all():
                    print("** no instance found **")
                    return
                else:
                    obj = storage.all()[key]
                    if len(args) < 3:
                        print("** attribute name missing **")
                        return
                    elif len(args) < 4:
                        print("** value missing **")
                        return
                    else:
                        attr_name = args[2]
                        attr_value = args[3]
                        if attr_name in {'id', 'created_at', 'updated_at'}:
                            return
                        elif attr_name not in obj[key].keys():
                            setattr(obj, attr_name, attr_value)
                        else:
                            obj[key].__dict__[attr_name] = attr_value
                        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

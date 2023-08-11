#!/usr/bin/python3
"""This module defines the HBNBCommand class for the command-line console."""

import cmd
from models.base_model import BaseModel
from models import storage
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Define HBNBCommand class.

    This class implements the command-line console for the AirBnB project.
    """

    intro = 'Welcome to the console, type "help" to know how it works.'
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit the console."""
        return True

    def do_EOF(self, line):
        """Quit the console using EOF (Ctrl+D)."""
        return True

    def do_empty(self, line):
        """Do nothing when the user enters nothing + Enter."""
        pass

    def do_create(self, line):
        """Create a new instance of a specified class."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]

        try:
            # Get the class from storage
            obj_class = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return

        new_instance = obj_class()
        new_instance.save()
        print(new_instance.id)

    def do_all(self, line):
        """Print string representations of all instances.

        based on class name or all classes.
        """
        args = line.split()

        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
        else:
            class_name = args[0]
            try:
                # Get the class from storage
                obj_class = eval(class_name)
            except NameError:
                print("** class doesn't exist **")
                return

            objs = [str(obj) for obj in storage.all(cls=obj_class).values()]
            print(objs)

    def do_show(self, line):
        """Show the string representation of an instance.

        based on class name and ID.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        valid_class_names = [
                'BaseModel',
                'Place',
                'City',
                'Amenity',
                'Review',
                'State'
                ]  # Add more if needed

        if class_name not in valid_class_names:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()

        if key in all_objs:
            obj = all_objs[key]
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Destroy an instance based on class name and ID."""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        valid_class_names = [
                'BaseModel',
                'Place',
                'City',
                'Amenity',
                'Review',
                'State'
                ]  # Add more if needed

        if class_name not in valid_class_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()

        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, line):
        """Update an instance based on class name and ID.

        by adding or updating attributes.
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        valid_class_names = [
                'BaseModel',
                'Place',
                'City',
                'Amenity',
                'Review',
                'State'
                ]  # Add more if needed

        if class_name not in valid_class_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()

        if key in all_objs:
            obj = all_objs[key]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attribute_name = args[2]
            attribute_value = args[3]
            setattr(obj, attribute_name, attribute_value)
            obj.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

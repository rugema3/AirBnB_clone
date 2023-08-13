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
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Define HBNBCommand class.

    This class implements the command-line console for the AirBnB project.
    """
    prompt = "(hbnb) "

    def default(self, line):
        """Called when the command is not recognized."""
        valid_class_names = [
            'BaseModel',
            'Place',
            'City',
            'Amenity',
            'Review',
            'State',
            'User'  # Add more if needed
        ]
        parts = line.split('.')

        if len(parts) == 2:
            class_name = parts[0]

            if class_name in valid_class_names:
                if parts[1] == 'all()':
                    objs = [
                            str(obj)
                            for obj
                            in storage.all(cls=eval(class_name)).values()
                            ]
                    print(objs)
                elif parts[1] == 'count()':
                    count = len(storage.all(cls=eval(class_name)).values())
                    print(count)
                else:
                    args = parts[1].split('(')
                    if len(args) == 2 and args[1].endswith(')'):
                        method_name = args[0]
                        if method_name == 'show':
                            instance_id = args[1][:-1]
                            self.do_show(
                                    "{} {}".format(class_name, instance_id)
                                    )
                        else:
                            print("*** Unknown syntax: {}".format(line))
                    else:
                        print("*** Unknown syntax: {}".format(line))
            else:
                print("** class doesn't exist **")
        else:
            print("*** Unknown syntax: {}".format(line))

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
            all_objs = storage.all()
            for obj in all_objs.values():
                print(obj)
        else:
            class_name = args[0]
            if not hasattr(storage, '_FileStorage__objects'):
                storage.reload()
            valid_class_names = [
                'BaseModel',
                'Place',
                'City',
                'Amenity',
                'Review',
                'State',
                'User'  # Add more if needed
            ]

            if class_name not in valid_class_names:
                print("** class doesn't exist **")
                return

            objs = [
                    str(obj)
                    for obj in storage.all(cls=eval(class_name)).values()
                    ]
            print(objs)

    def do_show(self, line):
        """Show the string representation of an instance.
        This is based on class name and ID.
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
            'State',
            'User'  # Add more if needed
        ]

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

    def do_count(self, line):
        """Count the number of instances of a class."""
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
            'State',
            'User'  # Add more if needed
        ]

        if class_name not in valid_class_names:
            print("** class doesn't exist **")
            return

        count = len(storage.all(cls=eval(class_name)).values())
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

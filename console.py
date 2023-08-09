#!/usr/bin/python3
"""This module defines the HBNBCommand class for the command-line console."""

import cmd
from models.base_model import BaseModel
from models import storage


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

        if class_name not in storage._FileStorage__objects:
            print("** class doesn't exist **")
            return
        new_instance = storage._FileStorage__objects[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Show the string representation of an instance.

        based on class name and ID.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage._FileStorage__objects:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()

        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Destroy an instance based on class name and ID."""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage._FileStorage__objects:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage._FileStorage__objects:
            print("** no instance found **")
            return
        del storage._FileStorage__objects[key]
        storage.save()

    def do_all(self, line):
        """Print string representations of all instances.

        based on class name or all classes.
        """
        args = line.split()
        objects = storage.all()

        if len(args) == 0:
            print([str(obj) for obj in objects.values()])
        else:
            class_name = args[0]

            if class_name not in storage._FileStorage__objects:
                print("** class doesn't exist **")
                return
            filtered_objects = [
                str(obj)
                for obj in objects.values()
                if type(obj).__name__ == class_name
            ]
            print(filtered_objects)

    def do_update(self, line):
        """Update an instance based on class name and ID.

        by adding or updating attributes.
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage._FileStorage__objects:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage._FileStorage__objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]

        obj = storage._FileStorage__objects[key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    def do_quit(self, line):
        """this will help to quit the program."""
        return True

    def do_EOF(self, line):
        """this will help to quit a program"""
        return True
    
    #def do_help(self):
    #   pass
    
    def do_empty(self):
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()


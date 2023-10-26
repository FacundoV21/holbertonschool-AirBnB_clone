#!/usr/bin/python3
"""
    This module has the HBNBCommand class that
    implements the cmd module which provides a simple framework
    for writing line-oriented command interpreters.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity
import sys
    

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    classes = {
        "BaseModel":  BaseModel,
        "User": User,
        "Place": Place,
        "Review": Review,
        "State": State,
        "City": City,
        "Amenity": Amenity
    }

    def do_EOF(self, line):
        return True
    
    def help_EOF(self):
        print("Closes the console and returns True\n")

    def do_quit(self, line):
        return True
    
    def help_quit(self):
        print("Quit command to exit the program\n")
    
    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = self.classes[arg]()
            storage.new(obj)
            storage.save()
            print(obj.id)

    def help_create(self):
        print("Creates a new instace of an object\n")


    def do_show(self, arg):
        arguments = arg.split()
        if not arg:
            print("** class name missing **")
        elif arguments[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            key = f"{arguments[0]}.{arguments[1]}"
            inst = storage.all()
            if key in inst:
                print(inst[key])
            else:
                print("** no instance found **")

    def help_show(self):
        print("Prints the string representation of an instance based on\
 the class name and id\n")

    def help_destroy(self):
        print("Deletes an instance based on the class name and id\n")


    def do_all(self, arg):
        if arg and (arg not in self.classes):
            print("** class doesn't exist **")
        else:
            inst = storage.all()
            prt = []

            if not arg:
                for key, value in inst.items():
                    #prt.append(str(inst[value]))
                    print(str(inst[key]))
            else:
                for key, value in inst.items():
                    if key.startswith(arg):
                        prt.append(str(inst[key]))
            print(prt)


    def help_all(self):
        print("Prints all string representation of all instances based\
 or not on the class name\n")

    def help_update(self):
        print("Updates an instance based on the class name and id by\
 adding or updating attribute\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

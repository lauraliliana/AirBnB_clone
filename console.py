#!/usr/bin/python3
"""
Initializes the console for the project
"""

import models
import cmd
import shlex
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class_dict = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
    }

integers = [
    "number_rooms",
    "number_bathrooms",
    "max_guest",
    "price_by_night"
    ]

floats = ["latitude", "longitude"]


class HBNBCommand(cmd.Cmd):
    """Class containing the console HBNB"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Method to override father method"""
        return False

    def do_EOF(self, arg):
        """Exit the console"""
        return True

    def do_quit(self, arg):
        """Quit the console"""
        return True

    def do_create(self, tmpname):
        """Creates a new instance of a class"""
        instname = shlex.split(tmpname)
        if len(instname) == 0:
            print("** class name missing **")
            return False
        if instname[0] in class_dict:
            new_instance = class_dict[instname[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(new_instance.id)
        new_instance.save

    def do_show(self, clinfo):
        """Prints the string representation of
        an instance based on the class name and id"""
        clinfostr = shlex.split(clinfo)
        if len(clinfostr) == 0:
            print("** class name missing **")
            return False
        if clinfostr[0] in class_dict:
            if len(clinfostr) > 1:
                instanceinfo = clinfostr[0] + "." + clinfostr[1]
                if instanceinfo in models.storage.all():
                    print(models.storage.all()[instanceinfo])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, insinfo):
        "Deletes an instance based on the class name and id"
        instodel = shlex.split(insinfo)
        if len(instodel) == 0:
            print("** class name missing **")
            return False
        if instodel[0] in class_dict:
            if len(instodel) > 1:
                instopop = instodel[0] + "." + instodel[1]
                if instopop in models.storage.all():
                    models.storage.all().pop(instopop)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, clshow):
        """Prints all string representation of all
         instances based or not on the class name"""
        toshow = shlex.split(clshow)
        showls = []
        if len(toshow) == 0:
            for value in models.storage.all().values():
                showls.append(str(value))
            print("[", end="")
            print(", ".join(showls), end="")
            print("]")
        elif toshow[0] in class_dict:
            for clname in models.storage.all():
                if toshow[0] in clname:
                    showls.append(str(models.storage.all()[clname]))
            print("[", end="")
            print(", ".join(showls), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, objtoupdate):
        """Updates an instance based on the class
        name and id by adding or updating attribute"""
        updatelist = shlex.split(objtoupdate)
        if len(updatelist) == 0:
            print("** class name missing **")
        elif updatelist[0] in class_dict:
            if len(updatelist) > 1:
                valuetofind = updatelist[0] + "." + updatelist[1]
                if valuetofind in models.storage.all():
                    if len(updatelist) > 2:
                        if len(updatelist) > 3:
                            if updatelist[0] == "Place":
                                if updatelist[2] in integers:
                                    try:
                                        updatelist[3] = int(updatelist[3])
                                    except:
                                        updatelist[3] = 0
                                elif updatelist[2] in floats:
                                    try:
                                        updatelist[3] = float(updatelist[3])
                                    except:
                                        updatelist[3] = 0.0
                            setattr(models.storage.all()[valuetofind],
                                    updatelist[2], updatelist[3])
                            models.storage.all()[valuetofind].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

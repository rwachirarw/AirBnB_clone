#!/usr/bin/python3
"""
Commandline interpreter module
Defines class HBNBCommand()
"""
import cmd
import readline
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Class to carry out commands for the AirBnb project

    Args:
        cmd: Commands module
    """

    prompt = "(hbnb) "
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

    def emptyline(self):
        """
        Do nothing if no command is passed
        """

        pass

    def do_EOF(self, arg):
        """
        End the program when Ctrl+D is pressed

        Returns:
            True
        """

        print()
        return True

    def do_quit(self, arg):
        """
        End the program when Ctrl+D is pressed

        Returns:
            True
        """

        return True

    def help_quit(self):
        """
        Documentation for the quit command
        """

        print("Usage: quit")
        print("command exits the comand line interpreter program")

    def do_create(self, arg):
        """Creates a new instance of class passed as arg

        Args:
            arg (_type_): _description_
        """
        if not arg or len(arg) == 0:
            print("** class name missing **")
            return

        if arg in HBNBCommand.classes.keys():
            new_instance = HBNBCommand.classes[arg]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """
        Documentation for the create command
        """

        print("create <object_name>")

    def do_show(self, arg):
        """Prints the string representation of
        an instance based on the class name

        Args:
            arg (_type_): _description_
        """
        if not arg or len(arg) == 0:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        instances = storage.all()

        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    def help_show(self):
        """
        Documentation for the show command
        """

        print("show <object_name> <object_id>")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id

        Args:
            arg (_type_): _description_
        """
        if not arg or len(arg) == 0:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        instances = storage.all()

        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def help_destroy(self):
        """
        Documentation for the destroy command
        """

        print("destroy <object_name> <object_id>")

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name

        Args:
            arg (_type_): _description_
        """
        args = arg.split()
        instances = storage.all()

        if not args:
            print([str(instance) for instance in instances.values()])
        elif args[0] in HBNBCommand.classes.keys():
            print([str(instance) for key, instance in instances.items()
                  if key.startswith(args[0] + ".")])
        else:
            print("** class doesn't exist **")

    def help_all(self):
        """
        Documentation for the all command
        """

        print("all [object_name]")
        print("print list of all instances or of the object_name")

    def do_update(self, arg):
        """Updates an instance based on the class
        name and id by adding or updating attribute

        Args:
            arg (_type_): _description_
        """

        if not arg or len(arg) == 0:
            print("** class name missing **")
            return

        args = arg.split()

        if len(args) >= 4:
            if args[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
                return

            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()

            if key in instances:
                instance = instances[key]
                setattr(instance, args[2], args[3])
                instance.save()
            else:
                print("** no instance found **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def help_update(self):
        """
        Documentation for the update command
        """

        print('update <class name> <id> <attribute name> "<attribute value>"')

    def do_count(self, arg):
        """
        Retrieve the number of instances of a class

        Usage:
            count <class name>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return

        instances = storage.all()
        count = sum(1 for key in instances if key.startswith(args[0] + "."))
        print(count)

    def default(self, arg):
        """
        Privides for commands that start with class name followed by argument
        """
        args = arg.split('.')
        if len(args) == 1:
            print("*** Unknown syntax: {}".format(arg))
            return

        class_name = args[0]
        if args[1] == "all()":
            HBNBCommand.do_all(self, class_name)
        elif args[1] == "count()":
            HBNBCommand.do_count(self, class_name)
        elif args[1].startswith("show(") and args[1].endswith(")"):
            instance_id = args[1][6:-2]
            show_command = "{} {}".format(class_name, instance_id)
            HBNBCommand.do_show(self, show_command)
        elif args[1].startswith("destroy(") and args[1].endswith(")"):
            instance_id = args[1][9:-2]
            destroy_command = "{} {}".format(class_name, instance_id)
            HBNBCommand.do_destroy(self, destroy_command)
        elif args[1].startswith("update(") and args[1].endswith(")"):
            instance_id = args[1].split(',')[0][7:].strip()
            update_args = ', '.join(args[1].split(',')[1:]).strip()

            if update_args.startswith("{") and update_args.endswith("}"):
                try:
                    update_dict = {
                        k.strip('\'\"'): v for k, v in update_dict.items()
                        }
                    if isinstance(update_dict, dict):
                        update_command = "{} {} {}".format(class_name,
                                                           instance_id,
                                                           update_dict)
                        HBNBCommand.do_update(self, update_command)
                    else:
                        print("** Invalid dictionary representation **")
                except Exception as e:
                    print("** Error evaluating dictionary \
                          representation: {} **".format(e))
            else:
                attribute_name = update_args.split(',')[0].strip()
                attribute_value = update_args.split(',')[1].strip()
                update_command = "{} {} {} {}".format(class_name,
                                                      instance_id,
                                                      attribute_name,
                                                      attribute_value)
                HBNBCommand.do_update(self, update_command)
        else:
            print("*** Unknown syntax: {}".format(arg))


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""AirBnB console"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """AirBnB console"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        exit()

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        exit()

    #def do_help(self, arg):
     #   """does some bullshit whatever"""

    def emptyline(self):
        """handles empty line + enter"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it to a JSON file, and prints the id
        
        Usage: $ create BaseModel
        """
        if arg == "" or None:
            print("**class name missing **")
        elif arg != "BaseModel":
            print("**class doesn't exist **")
        else:
            new_model = BaseModel()
        print(new_model.id)
        #still need to save as json file, has to do with storage from number 5

    def do_show(self, arg): #maybe need another arg for id? not sure
        """
        Prints the string representation of an instance
        based on the class name and id

        Usage: $ show BaseModel 1234-1234-1234
        """
        class_name = None
        class_id = None

        if arg: #think I need try/except here for if string isn't the correct number of args
            class_name = arg.split(" ")[0]
            class_id = arg.split(" ")[1]

        if class_name == "" or None:
            print("** class name missing **")
        elif class_name != "BaseModel":
            print("** class doesn't exist **")
        elif class_id == "" or None:
            print("** instance id missing **")
        elif class_id != self.BaseModel.id: #dont think this is correct, logic placeholder
            print("** no instance found **")
        else:
            #call __str__ or just remake here?
            pass

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        
        Usage: $ destroy BaseModel 1234-1234-1234
        """
        class_name = None
        class_id = None
        if arg:
            class_name = arg.split(" ")[0]
            class_id = arg.split(" ")[1]
        if class_name == "" or None:
            print("** class name missing **")
        elif class_name != "BaseModel":
            print("** class doesn't exist **")
        elif class_id == "" or None:
            print("** instance id missing **")
        elif class_id != self.BaseModel.id:
            print("** no instance found **")
        else: #shit for deleting instance based on class name and id
            pass

    def do_all(self, arg):
        """
        Prints all string representations of all instances if
        no class name is passed, or prints a string representation
        of a specific class based on class name

        Usage: $ all or $ all BaseModel
        """
        #saving this for when more of the class is implemented
        pass

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating an attribute
        (saves the change into a JSON file)

        Usage: $ update BaseModel 1234-1234-1234 email "asdf@mail.com
        """
        #will fuck with later
        pass

    if __name__ == '__main__':
        HBNBCommand().cmdloop()

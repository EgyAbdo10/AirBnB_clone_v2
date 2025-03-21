#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        """Returns a dictionary of models currently in storage"""
        obj_dict = {}
        classes_names = ['BaseModel', 'User', 'Place',
                   'State', 'City', 'Amenity', 'Review']
        classes = [BaseModel, User, Place,
                   State, City, Amenity, Review]
        
        if cls in classes_names:
            for key in FileStorage.__objects.keys():
                if key[:key.index(".")] == cls:
                    obj_dict[key] = FileStorage.__objects[key]
            return obj_dict
        elif cls and (cls in classes):
            for key in FileStorage.__objects.keys():
                if key[:key.index(".")] == cls.__name__:
                    obj_dict[key] = FileStorage.__objects[key]
            return obj_dict

        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        this method deletes an object from the __objects dict
        and then saves the changes
        """
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            if key in FileStorage.__objects.keys():
                del FileStorage.__objects[key]
                FileStorage().save()

    def close(self):
        """reload data agian"""
        self.reload()

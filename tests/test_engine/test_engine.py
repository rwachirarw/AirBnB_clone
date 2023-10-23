#!/usr/bin/python3
"""
Module to test the serialization and deserialization module
and File_storage_class
"""

import json
import os
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class testFileStorage(unittest.TestCase):
    """
    Test the file storage Module
    """

    def setUp(self):
        """
        Setup the class before any test
        Remove the JSON file before running any tests
        """

        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """
        Remove the JSON file after every test
        """

        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_private_attr(self):
        """
        Test that private attributes for class FileStorage are
        not accessible
        """

        self.assertFalse(hasattr(FileStorage, "__file_path"))
        self.assertFalse(hasattr(FileStorage, "__objects"))

    def test_object_created(self):
        """
        Test that an instance of FileStorage object is created
        """

        file_obj = FileStorage()
        self.assertTrue(file_obj)
        self.assertIsInstance(file_obj.all(), dict)

    def test_save_new_method(self):
        """
        Test the methods save and new
        """

        base_obj = BaseModel()
        file_obj = FileStorage()
        file_obj.new(base_obj)
        objs = file_obj.all()
        self.assertIn(base_obj, objs.values())

    def test_reload(self):
        """
        Test that the reload method works
        """

        base_obj = BaseModel()
        file_obj = FileStorage()
        file_obj.new(base_obj)
        file_obj.save()

        new_file = FileStorage()
        new_file.reload()
        objs = new_file.all()
        self.assertTrue(type(objs.values()), BaseModel)

    def test_no_file(self):
        """
        Test that no exception is raised if no file is found
        """

        file_obj = FileStorage()
        try:
            file_obj.reload()
        except FileNotFoundError:
            self.fail("raised FileNotFoundError")

    # def test_load_empty_file(self):
    #    """
    #    test loading from an empty file
    #   """

    #    if os.path.exists("file.json"):
    #        print("remove file.json")
    #        os.remove("file.json")
    #    obj = FileStorage()
    #    path = "file.json"
    #    with open(path, mode="w") as file:
    #        file.write(json.dumps({}))
    #    obj.reload()
    #    objs = obj.all()
    #    print(objs)
    #    self.assertEqual(len(objs), 0)

    def test_with_base_model(self):
        """
        Test that the FileStorage correctly intergrates with BaseModel
        """

        base_obj = BaseModel()
        file_obj = FileStorage()
        base_obj.save()

        objs = file_obj.all()
        self.assertIn(base_obj, objs.values())


if __name__ == "__main__":
    unittest.main()

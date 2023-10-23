#!/usr/bin/python3
"""
Defines test module for BaseModel class
"""
import json
import unittest
import models
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test class for BaseModel class module
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

    def test_obj_created(self):
        """
        Test if object is created
        """

        self.assertTrue(BaseModel())

    def test_attributes(self):
        """
        Confirm attributes in the object
        """

        base1 = BaseModel()
        self.assertTrue(hasattr(base1, "id"))
        self.assertTrue(hasattr(base1, "created_at"))
        self.assertTrue(hasattr(base1, "updated_at"))

    def test_id_type(self):
        """
        Test that the id of object is a string
        """

        base1 = BaseModel()
        self.assertIsInstance(base1.id, str)

    def test_id_values(self):
        """
        Check the object id values are unique between objects
        """

        base1 = BaseModel()
        base2 = BaseModel()
        self.assertIsNotNone(base1.id)
        self.assertIsNotNone(base2.id)
        self.assertNotEqual(base1.id, base2.id)

    def test_class_doc(self):
        """
        test documentation for the class is done
        """

        doc = BaseModel.__doc__
        self.assertGreater(len(doc), 3)

    def test_function_doc(self):
        """
        test documentation for functions in class
        """
        self.assertGreater(len(BaseModel.__init__.__doc__), 3)
        self.assertGreater(len(BaseModel.save.__doc__), 3)
        self.assertGreater(len(BaseModel.to_dict.__doc__), 3)
        self.assertGreater(len(models.__init__.__doc__), 3)

    def test_base_created_updated_at(self):
        """
        tests that BaseModel updated and created at times are datetime
        """
        base1 = BaseModel()
        self.assertIsInstance(base1.created_at, datetime)
        self.assertIsInstance(base1.updated_at, datetime)

    def test_base_save_updated_at(self):
        """
        Tests that the Base updated_at time updates when saved
        """
        base = BaseModel()
        prev_update = base.updated_at
        base.save()
        self.assertNotEqual(base.updated_at, prev_update)

    def test_base_to_dict(self):
        """
        Tests the BaseModel method save to dict
        """
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertIn("id", base_dict)
        self.assertIn("created_at", base_dict)
        self.assertIn("updated_at", base_dict)

    def test_base_save_to_file(self):
        """
        Tests that BaseMOdel Object successfully saved to file
        """
        base = BaseModel()
        base.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_base_reload_from_file(self):
        """
        Test that the BaseModel instance can be reloaded from the file
        """
        base = BaseModel()
        file = FileStorage()
        base.save()
        base_id = base.id

        file.reload()
        objs = file.all()

        self.assertIn("BaseModel." + base_id, objs.keys())


if __name__ == "__main__":
    unittest.main()

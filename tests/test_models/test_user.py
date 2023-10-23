#!/usr/bin/python3
"""
Module for testing the User class
"""
import json
import os
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.user import User


class testUser(unittest.TestCase):
    """
    Defines the test methods to test the User class
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

    def test_user_created(self):
        """
        Tests if a User class instance is created
        """

        self.assertTrue(User())

    def test_attributes(self):
        """
        Test the attributes in the User class instance
        """

        user_1 = User()

        self.assertTrue(hasattr(user_1, "email"))
        self.assertTrue(hasattr(user_1, "password"))
        self.assertTrue(hasattr(user_1, "first_name"))
        self.assertTrue(hasattr(user_1, "last_name"))
        self.assertTrue(hasattr(user_1, "id"))
        self.assertTrue(hasattr(user_1, "created_at"))
        self.assertTrue(hasattr(user_1, "updated_at"))

    def test_user_id_type(self):
        """
        Test that the id of object is a string
        """

        user_1 = User()
        self.assertIsInstance(user_1.id, str)

    def test_user_id_values(self):
        """
        Check the object id values are unique between objects
        """

        user_1 = User()
        user_2 = User()
        self.assertIsNotNone(user_1.id)
        self.assertIsNotNone(user_2.id)
        self.assertNotEqual(user_1.id, user_2.id)

    def test_class_doc(self):
        """
        test documentation for the class is done
        """

        doc = User.__doc__
        self.assertGreater(len(doc), 3)
        self.assertGreater(len(User.__init__.__doc__), 3)

    def test_user_created_updated_at(self):
        """
        tests that user updated and created at times are datetime
        """
        user1 = User()
        self.assertIsInstance(user1.created_at, datetime)
        self.assertIsInstance(user1.updated_at, datetime)

    def test_user_save_updated_at(self):
        """
        Tests that the user updated_at time updates when saved
        """
        user = User()
        prev_update = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, prev_update)

    def test_user_to_dict(self):
        """
        Tests the user method save to dict
        """
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertNotIn("name", user_dict)
        user.name = "betty"
        user_dict = user.to_dict()
        self.assertIn("name", user_dict)

    def test_user_save_to_file(self):
        """
        Tests that user Object successfully saved to file
        """
        user = User()
        user.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_user_reload_from_file(self):
        """
        Test that the user instance can be reloaded from the file
        """
        user = User()
        file = FileStorage()
        user.save()
        user_id = user.id

        file.reload()
        objs = file.all()

        self.assertIn("User." + user_id, objs.keys())


if __name__ == "__main__":
    unittest.main()

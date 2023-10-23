#!/usr/bin/python3
"""
Module for testing the State class
"""
import json
import os
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.state import State


class testState(unittest.TestCase):
    """
    Defines the test methods to test the State class
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

    def test_state_created(self):
        """
        Tests if a State class instance is created
        """

        self.assertTrue(State())

    def test_state_attributes(self):
        """
        Test the attributes in the State class instance
        """

        state_1 = State()

        self.assertTrue(hasattr(state_1, "name"))
        self.assertTrue(hasattr(state_1, "id"))
        self.assertTrue(hasattr(state_1, "created_at"))
        self.assertTrue(hasattr(state_1, "updated_at"))

    def test_state_id_type(self):
        """
        Test that the id of object is a string
        """

        state_1 = State()
        self.assertIsInstance(state_1.id, str)

    def test_state_id_values(self):
        """
        Check the object id values are unique between objects
        """

        state_1 = State()
        state_2 = State()
        self.assertIsNotNone(state_1.id)
        self.assertIsNotNone(state_2.id)
        self.assertNotEqual(state_1.id, state_2.id)

    def test_state_class_doc(self):
        """
        test documentation for the class is done
        """

        self.assertGreater(len(State.__doc__), 3)
        self.assertGreater(len(State.__init__.__doc__), 3)

    def test_state_created_updated_at(self):
        """
        tests that state updated and created at times are datetime
        """
        state1 = State()
        self.assertIsInstance(state1.created_at, datetime)
        self.assertIsInstance(state1.updated_at, datetime)

    def test_state_save_updated_at(self):
        """
        Tests that the state updated_at time updates when saved
        """
        state = State()
        prev_update = state.updated_at
        state.save()
        self.assertNotEqual(state.updated_at, prev_update)

    def test_state_to_dict(self):
        """
        Tests the state method save to dict
        """
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertNotIn("name", state_dict)
        state.name = "nairobi"
        state_dict = state.to_dict()
        self.assertIn("name", state_dict)

    def test_state_save_to_file(self):
        """
        Tests that state Object successfully saved to file
        """
        state = State()
        state.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_state_reload_from_file(self):
        """
        Test that the state instance can be reloaded from the file
        """
        state = State()
        file = FileStorage()
        state.save()
        state_id = state.id

        file.reload()
        objs = file.all()

        self.assertIn("State." + state_id, objs.keys())


if __name__ == "__main__":
    unittest.main()

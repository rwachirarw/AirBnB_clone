#!/usr/bin/python3
"""
Module for testing the Place class
"""

import json
import os
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.place import Place


class testPlace(unittest.TestCase):
    """
    Defines the test methods to test the Place class
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

    def test_place_created(self):
        """
        Tests if a Place class instance is created
        """

        self.assertTrue(Place())

    def test_place_attributes(self):
        """
        Test the attributes in the Place class instance
        """

        place_1 = Place()

        self.assertTrue(hasattr(place_1, "name"))
        self.assertTrue(hasattr(place_1, "id"))
        self.assertTrue(hasattr(place_1, "created_at"))
        self.assertTrue(hasattr(place_1, "updated_at"))
        self.assertTrue(hasattr(place_1, "user_id"))
        self.assertTrue(hasattr(place_1, "description"))
        self.assertTrue(hasattr(place_1, "number_rooms"))
        self.assertTrue(hasattr(place_1, "number_bathrooms"))
        self.assertTrue(hasattr(place_1, "max_guest"))
        self.assertTrue(hasattr(place_1, "price_by_night"))
        self.assertTrue(hasattr(place_1, "latitude"))
        self.assertTrue(hasattr(place_1, "longitude"))
        self.assertTrue(hasattr(place_1, "amenity_ids"))

    def test_place_id_type(self):
        """
        Test that the id of object is a string
        """

        place_1 = Place()
        self.assertIsInstance(place_1.id, str)

    def test_place_id_values(self):
        """
        Check the object id values are unique between objects
        """

        place_1 = Place()
        place_2 = Place()
        self.assertIsNotNone(place_1.id)
        self.assertIsNotNone(place_2.id)
        self.assertNotEqual(place_1.id, place_2.id)

    def test_place_class_doc(self):
        """
        test documentation for the class is done
        """

        self.assertGreater(len(Place.__doc__), 3)
        self.assertGreater(len(Place.__init__.__doc__), 3)

    def test_place_created_updated_at(self):
        """
        tests that place updated and created at times are datetime
        """
        place1 = Place()
        self.assertIsInstance(place1.created_at, datetime)
        self.assertIsInstance(place1.updated_at, datetime)

    def test_place_save_updated_at(self):
        """
        Tests that the place updated_at time updates when saved
        """
        place = Place()
        prev_update = place.updated_at
        place.save()
        self.assertNotEqual(place.updated_at, prev_update)

    def test_place_to_dict(self):
        """
        Tests the place method save to dict
        """
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertIn("id", place_dict)
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)
        self.assertNotIn("name", place_dict)
        place.name = "nairobi"
        place_dict = place.to_dict()
        self.assertIn("name", place_dict)

    def test_place_save_to_file(self):
        """
        Tests that place Object successfully saved to file
        """
        place = Place()
        place.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_place_reload_from_file(self):
        """
        Test that the place instance can be reloaded from the file
        """
        place = Place()
        file = FileStorage()
        place.save()
        place_id = place.id

        file.reload()
        objs = file.all()

        self.assertIn("Place." + place_id, objs.keys())


if __name__ == "__main__":
    unittest.main()

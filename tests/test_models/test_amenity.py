#!/usr/bin/python3
"""
Module for testing the Amenity class
"""
import json
import os
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.amenity import Amenity


class testAmenity(unittest.TestCase):
    """
    Defines the test methods to test the Amenity class
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

    def test_amenity_created(self):
        """
        Tests if a Amenity class instance is created
        """

        self.assertTrue(Amenity())

    def test_attributes(self):
        """
        Test the attributes in the Amenity class instance
        """

        amenity_1 = Amenity()

        self.assertTrue(hasattr(amenity_1, "name"))
        self.assertTrue(hasattr(amenity_1, "id"))
        self.assertTrue(hasattr(amenity_1, "created_at"))
        self.assertTrue(hasattr(amenity_1, "updated_at"))

    def test_amenity_id_type(self):
        """
        Test that the id of object is a string
        """

        amenity_1 = Amenity()
        self.assertIsInstance(amenity_1.id, str)

    def test_amenity_id_values(self):
        """
        Check the object id values are unique between objects
        """

        amenity_1 = Amenity()
        amenity_2 = Amenity()
        self.assertIsNotNone(amenity_1.id)
        self.assertIsNotNone(amenity_2.id)
        self.assertNotEqual(amenity_1.id, amenity_2.id)

    def test_class_doc(self):
        """
        test documentation for the class is done
        """

        doc = Amenity.__doc__
        self.assertGreater(len(doc), 3)

    def test_amenity_name(self):
        """
        Test that the name of Amenity instance can be updated
        """

        amenity_1 = Amenity()
        self.assertIsInstance(amenity_1.name, str)
        self.assertEqual(amenity_1.name, "")
        amenity_1.name = "bathroom"
        self.assertTrue(amenity_1.name, "bathroom")

    def test_amenity_created_updated_at(self):
        """
        tests that Amenity updated and created at times are datetime
        """
        amenity1 = Amenity()
        self.assertIsInstance(amenity1.created_at, datetime)
        self.assertIsInstance(amenity1.updated_at, datetime)

    def test_amenity_save_updated_at(self):
        """
        Tests that the amenity updated_at time updates when saved
        """
        amenity = Amenity()
        prev_update = amenity.updated_at
        amenity.save()
        self.assertNotEqual(amenity.updated_at, prev_update)

    def test_amenity_to_dict(self):
        """
        Tests the Amenity method save to dict
        """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertNotIn("name", amenity_dict)
        amenity.name = "bathroom"
        amenity_dict = amenity.to_dict()
        self.assertIn("name", amenity_dict)

    def test_amenity_save_to_file(self):
        """
        Tests that Amenity Object successfully saved to file
        """
        amenity = Amenity()
        amenity.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_amenity_reload_from_file(self):
        """
        Test that the City instance can be reloaded from the file
        """
        amenity = Amenity()
        file = FileStorage()
        amenity.save()
        amenity_id = amenity.id

        file.reload()
        objs = file.all()

        self.assertIn("Amenity." + amenity_id, objs.keys())


if __name__ == "__main__":
    unittest.main()

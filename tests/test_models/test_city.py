#!/usr/bin/python3
"""
Module for testing the City class
"""
import json
import os
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.city import City


class testCity(unittest.TestCase):
    """
    Defines the test methods to test the City class
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

    def test_city_created(self):
        """
        Tests if a City class instance is created
        """

        self.assertTrue(City())

    def test_city_attributes(self):
        """
        Test the attributes in the City class instance
        """

        city_1 = City()

        self.assertTrue(hasattr(city_1, "name"))
        self.assertTrue(hasattr(city_1, "id"))
        self.assertTrue(hasattr(city_1, "state_id"))
        self.assertTrue(hasattr(city_1, "created_at"))
        self.assertTrue(hasattr(city_1, "updated_at"))

    def test_city_id_type(self):
        """
        Test that the id of object is a string
        """

        city_1 = City()
        self.assertIsInstance(city_1.id, str)

    def test_city_id_values(self):
        """
        Check the object id values are unique between objects
        """

        city_1 = City()
        city_2 = City()
        self.assertIsNotNone(city_1.id)
        self.assertIsNotNone(city_2.id)
        self.assertNotEqual(city_1.id, city_2.id)

    def test_city_class_doc(self):
        """
        test documentation for the class is done
        """

        doc = City.__doc__
        self.assertGreater(len(doc), 3)

    def test_city_name(self):
        """
        Test that the name of City instance can be updated
        """

        city_1 = City()
        self.assertIsInstance(city_1.name, str)
        self.assertEqual(city_1.name, "")
        city_1.name = "Nairobi"
        self.assertTrue(city_1.name, "Nairobi")

    def test_city_created_updated_at(self):
        """
        tests that city updated and created at times are datetime
        """
        city1 = City()
        self.assertIsInstance(city1.created_at, datetime)
        self.assertIsInstance(city1.updated_at, datetime)

    def test_city_save_updated_at(self):
        """
        Tests that the city updated_at time updates when saved
        """
        city = City()
        prev_update = city.updated_at
        city.save()
        self.assertNotEqual(city.updated_at, prev_update)

    def test_city_to_dict(self):
        """
        Tests the city method save to dict
        """
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertNotIn("name", city_dict)
        city.name = "nairobi"
        city_dict = city.to_dict()
        self.assertIn("name", city_dict)

    def test_city_save_to_file(self):
        """
        Tests that city Object successfully saved to file
        """
        city = City()
        city.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_city_reload_from_file(self):
        """
        Test that the City instance can be reloaded from the file
        """
        city = City()
        file = FileStorage()
        city.save()
        city_id = city.id

        file.reload()
        objs = file.all()

        self.assertIn("City." + city_id, objs.keys())


if __name__ == "__main__":
    unittest.main()

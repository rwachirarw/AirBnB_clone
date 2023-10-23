#!/usr/bin/python3
"""
Module for testing the Review class
"""
import json
import os
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.review import Review


class testReview(unittest.TestCase):
    """
    Defines the test methods to test the Review class
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

    def test_review_created(self):
        """
        Tests if a Review class instance is created
        """

        self.assertTrue(Review())

    def test_review_attributes(self):
        """
        Test the attributes in the Review class instance
        """

        review_1 = Review()

        self.assertTrue(hasattr(review_1, "text"))
        self.assertTrue(hasattr(review_1, "id"))
        self.assertTrue(hasattr(review_1, "created_at"))
        self.assertTrue(hasattr(review_1, "updated_at"))
        self.assertTrue(hasattr(review_1, "place_id"))
        self.assertTrue(hasattr(review_1, "user_id"))

    def test_review_id_type(self):
        """
        Test that the id of object is a string
        """

        review_1 = Review()
        self.assertIsInstance(review_1.id, str)

    def test_review_id_values(self):
        """
        Check the object id values are unique between objects
        """

        review_1 = Review()
        review_2 = Review()
        self.assertIsNotNone(review_1.id)
        self.assertIsNotNone(review_2.id)
        self.assertNotEqual(review_1.id, review_2.id)

    def test_review_class_doc(self):
        """
        test documentation for the class is done
        """

        self.assertGreater(len(Review.__doc__), 3)
        self.assertGreater(len(Review.__init__.__doc__), 3)

    def test_review_created_updated_at(self):
        """
        tests that review updated and created at times are datetime
        """
        review1 = Review()
        self.assertIsInstance(review1.created_at, datetime)
        self.assertIsInstance(review1.updated_at, datetime)

    def test_review_save_updated_at(self):
        """
        Tests that the review updated_at time updates when saved
        """
        review = Review()
        prev_update = review.updated_at
        review.save()
        self.assertNotEqual(review.updated_at, prev_update)

    def test_review_to_dict(self):
        """
        Tests the review method save to dict
        """
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertIn("id", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        self.assertNotIn("name", review_dict)
        review.text = "awesome place"
        review_dict = review.to_dict()
        self.assertIn("text", review_dict)

    def test_review_save_to_file(self):
        """
        Tests that review Object successfully saved to file
        """
        review = Review()
        review.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_review_reload_from_file(self):
        """
        Test that the review instance can be reloaded from the file
        """
        review = Review()
        file = FileStorage()
        review.save()
        review_id = review.id

        file.reload()
        objs = file.all()

        self.assertIn("Review." + review_id, objs.keys())


if __name__ == "__main__":
    unittest.main()

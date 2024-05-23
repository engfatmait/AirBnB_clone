#!/usr/bin/python3

""" module of unittests """
import unittest
import from models.base_model import basemodel


class BaseModelTests(unittest.TestCase):
    """ Suite of Console Tests """

    my_model = basemodel();

    def test_init(self):
        """ Test attributes value of init """
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """ Test attributes value of a BaseModel instance """

        intial_updated_at = my_model.updated_at
        currnt_updated_at = my_model.save()

        self.assertEqual(intial_updated_at, currnt_updated_at)

    def test_to_dict(self):

        """ test attributes value """

        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model_dict["__class__"], "basemodel")
        self.assertEqual(my_model_dict["id"], my_model.id)
        self.assertEqual(my_model_dict["created_at"], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.updated_at.isoformat())

    def test_str(self):
        self.assertTrue(str(my_model).starttwith('[basemodel]'))

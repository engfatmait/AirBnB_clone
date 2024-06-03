#!/usr/bin/python3

""" module of unittests """
import unittest
import models
from models.base_model import BaseModel


class BaseModelTests(unittest.TestCase):
    """ Suite of Console Tests """

    def test_init(self):
        """ Test attributes value of init """
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """ Test attributes value of a BaseModel instance """
        my_model = BaseModel()
        intial_updated_at = my_model.updated_at
        currnt_updated_at = my_model.save()

        self.assertNotEqual(intial_updated_at, currnt_updated_at)

    def test_to_dict(self):

        """ test attributes value """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model_dict["__class__"], "BaseModel")
        self.assertEqual(my_model_dict["id"], my_model.id)
        self.assertEqual(my_model_dict["updated_at"],
                         my_model.updated_at.isoformat())

    def test_str(self):
        """ test name of the model """
        my_model = BaseModel()
        self.assertTrue(str(my_model).startswith('[BaseModel]'))


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel


# Inherit from both TestBaseModel and unittest.TestCase
class TestAmenity(TestBaseModel, unittest.TestCase):
    """Test the City class."""

    def setUp(self):
        self.model_class = Amenity  # Specify the model class for common tests


if __name__ == '__main__':
    unittest.main()

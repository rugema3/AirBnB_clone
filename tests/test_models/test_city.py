#!/usr/bin/python3
import unittest
from models.city import City
from tests.test_models.test_base_model import TestBaseModel


# Inherit from both TestBaseModel and unittest.TestCase
class TestCity(TestBaseModel, unittest.TestCase):
    """Test the City class."""

    def setUp(self):
        """Define setUp method."""
        self.model_class = City  # Specify the model class for common tests


if __name__ == '__main__':
    unittest.main()

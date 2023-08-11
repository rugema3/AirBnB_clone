#!/usr/bin/python3
import unittest
from models.place import Place
from tests.test_models.test_base_model import TestBaseModel


# Inherit from both TestBaseModel and unittest.TestCase
class TestPlace(TestBaseModel, unittest.TestCase):
    """Test the place class."""

    def setUp(self):
        """Define setUp method."""
        self.model_class = Place  # Specify the model class for common tests


if __name__ == '__main__':
    unittest.main()

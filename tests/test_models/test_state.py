#!/usr/bin/python3
import unittest
from models.state import State
from tests.test_models.test_base_model import TestBaseModel


# Inherit from both TestBaseModel and unittest.TestCase
class TestState(TestBaseModel, unittest.TestCase):
    """Test the State class.
    Description:
                This class inherits all the test that have been
                performed on the BaseModel.That's why we are importing
                TestBaseModel class which is a class that tests the
                BaseModel class.
    """
    def setUp(self):
        """Define setUp method."""
        self.model_class = State  # Specify the model class for common tests


if __name__ == '__main__':
    unittest.main()

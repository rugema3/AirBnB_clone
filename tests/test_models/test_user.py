#!/usr/bin/python3
import unittest
from models.user import User
from tests.test_models.test_base_model import TestBaseModel
# Import the TestBaseModel class


# Inherit from both TestBaseModel and unittest.TestCase
class TestCity(TestBaseModel, unittest.TestCase):
    """Test the User class.
    Description:
                This class inherits all the test that have been
                performed on the BaseModel.That's why we are importing
                TestBaseModel class which is a class that tests the
                BaseModel class.
    """

    def setUp(self):
        """Define setUp method."""
        self.model_class = User  # Specify the model class for common tests


if __name__ == '__main__':
    unittest.main()

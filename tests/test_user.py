import unittest
from models.user import User
from tests.test_base_model import TestBaseModel  # Import the TestBaseModel class

# Inherit from both TestBaseModel and unittest.TestCase
class TestUser(TestBaseModel, unittest.TestCase):
    """Test the User class."""

    

    def setUp(self):
        # Initialize any required resources or configurations for your City tests
        self.model_class = User  # Specify the model class for common tests

if __name__ == '__main__':
    unittest.main()


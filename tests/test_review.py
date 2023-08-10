import unittest
from models.review import Review
from tests.test_base_model import TestBaseModel  # Import the TestBaseModel class

# Inherit from both TestBaseModel and unittest.TestCase
class TestCity(TestBaseModel, unittest.TestCase):
    """Test the City class."""

    

    def setUp(self):
        # Initialize any required resources or configurations for your City tests
        self.model_class = Review  # Specify the model class for common tests

if __name__ == '__main__':
    unittest.main()


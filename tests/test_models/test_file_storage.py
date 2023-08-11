#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test FileStorage class."""

    def setUp(self):
        """Set up test environment before each test case."""
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        """Clean up after each test case."""
        try:
            del self.base_model
        except AttributeError:
            pass

    def test_FileStorage_present(self):
        """Test if the class is present."""
        self.assertIsInstance(self.storage, FileStorage)

    def test_new_object_added(self):
        """Test if a new object is added to __objects."""
        before_count = len(self.storage.all())
        self.storage.new(self.base_model)
        after_count = len(self.storage.all())
        self.assertEqual(before_count + 1, after_count)

    def test_save_method(self):
        """Test if the save method correctly saves objects to the file."""
        # Create a new object
        new_model = BaseModel()
        new_model_id = new_model.id  # Get the ID of the new model
        self.storage.new(new_model)

        # Save the objects to the file
        self.storage.save()

        # Manually reload the storage
        reloaded_storage = FileStorage()
        reloaded_storage.reload()

        # Print the IDs and keys for debugging
        print("Expected ID:", new_model_id)
        print("Reloaded keys:", reloaded_storage.all().keys())

        # Check if the new object ID exists in the reloaded storage's keys
        self.assertIn(new_model_id, reloaded_storage.all().keys())


if __name__ == "__main__":
    unittest.main()

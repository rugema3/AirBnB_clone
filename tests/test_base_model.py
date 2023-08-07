import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class."""

    def test_id_not_empty(self):
        """Test if ID is present."""
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)

    def test_distinct_id(self):
        """Test if the id is always unique."""
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)

    def test_id_is_str(self):
        """Test if the id generated is a string."""
        a = BaseModel()
        self.assertEqual(type(a.id), str)

    def test_created_at(self):
        """Test created_at method.
        Check the time it was created is working."""
        a = BaseModel()
        self.assertIsNotNone(a.created_at)

    def test_format_created_at_and_updated_at(self):
        """Test if the format is that of time."""
        a = BaseModel()
        self.assertIsNotNone(a.updated_at)
        self.assertEqual(type(a.id), str)
        self.assertEqual(type(a.created_at), type(a.updated_at))

    def test_str(self):
        """Test the string representation of BaseModel."""
        base_model = BaseModel()
        expected_str = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected_str)

    def test_save(self):
        """Test the save method of BaseModel."""
        base_model = BaseModel()
        original_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(base_model.updated_at, original_updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        base_model = BaseModel()
        base_dict = base_model.to_dict()
        self.assertTrue(isinstance(base_dict, dict))
        self.assertIn('id', base_dict)
        self.assertIn('created_at', base_dict)
        self.assertIn('updated_at', base_dict)
        self.assertIn('__class__', base_dict)
        self.assertEqual(base_dict['__class__'], 'BaseModel')


if __name__ == '__main__':
    unittest.main()

import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import datetime
import os


class TestBase(unittest.TestCase):
    """Unit tests for the BaseModel."""

    def setUp(self):
        """Set up test environment."""
        # Create an instance of FileStorage
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after the test."""
        # Remove the file created during testing
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init(self):
        """Test initialization of BaseModel."""
        # Testing instance without kwargs
        base_model = BaseModel()
        self.assertEqual(BaseModel, type(base_model))
        self.assertIn(base_model, models.storage.all().values())
        self.assertIsInstance(base_model, BaseModel)
        self.assertIsNotNone(base_model.id)
        self.assertIsInstance(base_model.created_at, datetime.datetime)
        self.assertIsInstance(base_model.updated_at, datetime.datetime)

        # Testing instance with kwargs
        data = {
            'id': '1',
            'created_at': '2024-03-07T12:00:00.000',
            'updated_at': '2024-03-07T12:00:00.000',
            'name': 'Test'
        }
        base_model = BaseModel(**data)
        self.assertIsInstance(base_model, BaseModel)
        self.assertEqual(base_model.id, '1')
        self.assertEqual(base_model.created_at, datetime.datetime(
            2024, 3, 7, 12, 0))
        self.assertEqual(base_model.updated_at, datetime.datetime(
            2024, 3, 7, 12, 0))
        self.assertEqual(base_model.name, 'Test')

    def test_to_dict(self):
        """Test to_dict method"""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()

        self.assertIsInstance(base_model_dict, dict)
        self.assertIn('__class__', base_model_dict)
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)
        self.assertEqual(
            base_model_dict['__class__'], base_model.__class__.__name__)
        self.assertEqual(base_model_dict['id'], base_model.id)
        self.assertEqual(
            base_model_dict['created_at'], base_model.created_at.isoformat())
        self.assertEqual(
            base_model_dict['updated_at'], base_model.updated_at.isoformat())

    def test_str(self):
        """Test __str__ method"""
        base_model = BaseModel()
        expected_output = "[{}] ({}) {}".format(
            base_model.__class__.__name__,
            base_model.id,
            base_model.__dict__
        )
        self.assertEqual(str(base_model), expected_output)

    def test_update_attributes(self):
        """Test updating attributes"""
        base_model = BaseModel()
        base_model.name = 'New Name'
        self.assertEqual(base_model.name, 'New Name')

    def test_save_method(self):
        """Test save method"""
        base_model = BaseModel()
        base_model.save()
        self.assertIsInstance(base_model.updated_at, datetime.datetime)
        with self.assertRaises(TypeError):
            base_model.save(None)

    def test_created_at_updated_at(self):
        """Test created_at and updated_at attributes."""
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime.datetime)
        self.assertIsInstance(base_model.updated_at, datetime.datetime)

    def test_save(self):
        """Test the save() method."""
        # Create a BaseModel instance
        base_model = BaseModel()

        # Add the object to the storage
        self.storage.new(base_model)

        # Save the objects to the file
        self.storage.save()

        # Reload the file to check if the object is saved
        new_storage = FileStorage()
        new_storage.reload()

        # Assert that the object exists in the reloaded storage
        self.assertIn("BaseModel." + base_model.id, new_storage.all())


if __name__ == '__main__':
    unittest.main()

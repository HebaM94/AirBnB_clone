import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """Testing FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        # Create an instance of FileStorage
        self.storage = FileStorage()
        for key in list(self.storage.all().keys()):
            del self.storage.all()[key]

    def tearDown(self):
        """Clean up after the test."""
        # Remove the file created during testing
        if os.path.exists("file.json"):
            os.remove("file.json")
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """Test the all() method."""
        # __objects is empty
        self.assertEqual(len(self.storage.all()), 0)

        # Add an object
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(len(self.storage.all()), 1)
        self.assertIn("BaseModel." + obj.id, self.storage.all())

    def test_new(self):
        """Test the new() method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn("BaseModel." + obj.id, self.storage.all())

    def test_save_reload(self):
        """Test the save() and reload() methods."""
        # Add an object and save it
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        

        # Reload the data and check if the object is present
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + obj.id, objs)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == '__main__':
    unittest.main()

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Testing FileStorage class."""

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
        self.storage.new(obj)
        self.storage.save()

        # Reload the data and check if the object is present
        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(len(new_storage.all()), 1)
        self.assertIn("BaseModel." + obj.id, new_storage.all())

if __name__ == '__main__':
    unittest.main()

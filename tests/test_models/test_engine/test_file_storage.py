import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


class TestFileStorage(unittest.TestCase):
    """Testing FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        # Create an instance of FileStorage
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after the test."""
        # Remove the file created during testing
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test the all() method."""
        # __objects is empty
        self.assertEqual(len(self.storage.all()), 0)

        # Add an object
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()

        self.storage.new(base_model)
        self.storage.new(user)
        self.storage.new(state)
        self.storage.new(place)
        self.storage.new(city)
        self.storage.new(amenity)
        self.storage.new(review)

        self.assertEqual(len(self.storage.all()), 1)
        self.assertIn("BaseModel." + base_model.id, self.storage.all())
        self.assertIn("User." + user.id, self.storage.all())
        self.assertIn("State." + state.id, self.storage.all())
        self.assertIn("Place." + place.id, self.storage.all())
        self.assertIn("city." + city.id, self.storage.all())
        self.assertIn("Amenity." + amenity.id, self.storage.all())
        self.assertIn("Review." + review.id, self.storage.all())

    def test_new(self):
        """Test the new() method."""
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()

        self.storage.new(base_model)
        self.storage.new(user)
        self.storage.new(state)
        self.storage.new(place)
        self.storage.new(city)
        self.storage.new(amenity)
        self.storage.new(review)

        self.assertIn("BaseModel." + base_model.id, self.storage.all())
        self.assertIn("User." + user.id, self.storage.all())
        self.assertIn("State." + state.id, self.storage.all())
        self.assertIn("Place." + place.id, self.storage.all())
        self.assertIn("city." + city.id, self.storage.all())
        self.assertIn("Amenity." + amenity.id, self.storage.all())
        self.assertIn("Review." + review.id, self.storage.all())

    def test_save_reload(self):
        """Test the save() and reload() methods."""
        # Add an object and save it
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()

        self.storage.new(base_model)
        self.storage.new(user)
        self.storage.new(state)
        self.storage.new(place)
        self.storage.new(city)
        self.storage.new(amenity)
        self.storage.new(review)

        self.storage.save()

        # Reload the data and check if the object is present
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn("BaseModel." + base_model.id, self.storage.all())
        self.assertIn("User." + user.id, self.storage.all())
        self.assertIn("State." + state.id, self.storage.all())
        self.assertIn("Place." + place.id, self.storage.all())
        self.assertIn("city." + city.id, self.storage.all())
        self.assertIn("Amenity." + amenity.id, self.storage.all())
        self.assertIn("Review." + review.id, self.storage.all())


if __name__ == '__main__':
    unittest.main()

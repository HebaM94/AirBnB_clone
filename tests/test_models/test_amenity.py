import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Teating Amenity class"""

    def test_init(self):
        """Test initialization of Amenity"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.name, str)
        self.assertEqual(amenity.name, "")

    def test_attribute_setting(self):
        """Test setting attributes of Amenity"""
        amenity = Amenity()
        amenity.name = "Pool"
        self.assertEqual(amenity.name, "Pool")

if __name__ == '__main__':
    unittest.main()

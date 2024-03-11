import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Testing Place class"""

    def test_init(self):
        """Test initialization of Place"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_attribute_setting(self):
        """Test setting attributes of Place"""
        place = Place()
        place.name = "Cozy Home"
        place.city_id = "135"
        place.user_id = "468"
        place.description = "Amazing small home"
        place.number_rooms = 2
        place.number_bathrooms = 2
        place.max_guest = 4
        place.price_by_night = 110
        place.latitude = 42.8126
        place.longitude = -69.0040
        place.amenity_ids = ["wifi", "pool"]

        self.assertEqual(place.name, "Cozy Home")
        self.assertEqual(place.city_id, "135")
        self.assertEqual(place.user_id, "468")
        self.assertEqual(place.description, "Amazing small home")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 110)
        self.assertEqual(place.latitude, 42.8126)
        self.assertEqual(place.longitude, -69.0040)
        self.assertEqual(place.amenity_ids, ["wifi", "pool"])


if __name__ == '__main__':
    unittest.main()

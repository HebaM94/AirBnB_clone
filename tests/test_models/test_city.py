import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Testing City class"""

    def test_init(self):
        """Test initialization of City"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.state_id, str)
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_attribute_setting(self):
        """Test setting attributes of City"""
        city = City()
        city.name = "Alexandria"
        city.state_id = "Alex"
        self.assertEqual(city.name, "Alexandria")
        self.assertEqual(city.state_id, "Alex")

if __name__ == '__main__':
    unittest.main()

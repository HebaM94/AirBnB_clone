import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Testing User class"""

    def test_init(self):
        """Test initialization of User"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_attribute_setting(self):
        """Test setting attributes of User"""
        user = User()
        user.email = "alx@gmail.com"
        user.password = "te3ebt*"
        user.first_name = "Hebas"
        user.last_name = "Team"

        self.assertEqual(user.email, "alx@gmail.com")
        self.assertEqual(user.password, "te3ebt*")
        self.assertEqual(user.first_name, "Hebas")
        self.assertEqual(user.last_name, "Team")


if __name__ == '__main__':
    unittest.main()

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Testing State class"""

    def test_init(self):
        """Test initialization of State"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state.name, str)

    def test_attribute_setting(self):
        """Test setting attributes of State"""
        state = State()
        state.name = "California"

        self.assertEqual(state.name, "California")


if __name__ == '__main__':
    unittest.main()

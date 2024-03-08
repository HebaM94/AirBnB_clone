import unittest
from models.base_model import BaseModel
import datetime


class TestBase(unittest.TestCase):
    """Unit tests for the BaseModel."""
    def test_init(self):
        """Test initialization of BaseModel."""
        # Testing instance without kwargs
        base_model = BaseModel()
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

    def test_str(self):
        """Test __str__ method"""
        base_model = BaseModel()
        expected_output = "[{}] ({}) {}".format(
            base_model.__class__.__name__,
            base_model.id,
            base_model.__dict__
        )
        self.assertEqual(str(base_model), expected_output)


if __name__ == '__main__':
    unittest.main()

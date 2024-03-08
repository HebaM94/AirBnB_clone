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
        self.assertEqual(base_model.created_at, datetime.datetime(2024, 3, 7, 12, 0))
        self.assertEqual(base_model.updated_at, datetime.datetime(2024, 3, 7, 12, 0))
        self.assertEqual(base_model.name, 'Test')


if __name__ == '__main__':
    unittest.main()

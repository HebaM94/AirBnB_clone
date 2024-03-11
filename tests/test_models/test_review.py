import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Testing Review class"""

    def test_init(self):
        """Test initialization of Review"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_attribute_setting(self):
        """Test setting attributes of Review"""
        review = Review()
        review.text = "Best Stay Ever!"
        review.place_id = "123"
        review.user_id = "456"
        
        self.assertEqual(review.text, "Best Stay Ever!")
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")

if __name__ == '__main__':
    unittest.main()

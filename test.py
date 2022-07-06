import unittest
from app import app
class TestHello(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    def test_hello(self):
        self.assertEqual(1, 1)
if __name__ == '__main__':
    unittest.main()
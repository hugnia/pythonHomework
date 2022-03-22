import unittest


class MyTestCase(unittest.TestCase):
    def mock_test(self):
        self.assertEqual(2 + 2 == 4)


import unittest

import calendonator


class CalendonatorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = calendonator.app.test_client()

    def test_index(self):
        rv = self.app.get("/")
        self.assertIn("Welcome to calendonator", rv.data.decode())


if __name__ == "__main__":
    unittest.main()

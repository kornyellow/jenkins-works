import unittest
import app

class TestApp(unittest.TestCase):
    def test_getcode(self):
        self.assertEqual(app.getcode(), "getcode")

    def test_plus(self):
        response = self.app.get("/plus/5/6")
        self.assertEqual(response.data.decode(), "5 + 6 = 11")

        response = self.app.get("/plus/1/4")
        self.assertEqual(response.data.decode(), "1 + 4 = 5")

        response = self.app.get("/plus/103/56")
        self.assertEqual(response.data.decode(), "103 + 56 = 159")

        # Test for invalid input
        response = self.app.get("/plus/a/4")
        self.assertEqual(response.json, {"error_msg": "inputs must be numbers"})

if __name__ == "__main__a":
    unittest.main()

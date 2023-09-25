import unittest
from flask import Flask, jsonify
from unittest.mock import patch

# The method to be tested
def post_days():
    try:
        return jsonify({"success": True}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

app = Flask(__name__)

class TestPostDays(unittest.TestCase):

    # Test case for success scenario
    def test_post_days_success(self):
        with app.test_request_context():
            response = post_days()
            self.assertEqual(response[1], 201)
            self.assertEqual(response[0].json, {"success": True})

    # Test case for failure scenario
    @patch('flask.jsonify', side_effect=Exception)
    def test_post_days_failure(self, mock_jsonify):
        with app.test_request_context():
            try:
                response = post_days()
            except Exception as e:
                response = jsonify({"error": str(e)}), 500
            self.assertEqual(response[1], 500)
            self.assertTrue("error" in response[0].json)

if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify, abort

# Assuming this is the application code
app = Flask(__name__)

@app.route("/<int:day_id>", methods=["GET"])
def get_days(day_id):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if day_id < 0 or day_id > 6:
        abort(404)
    return jsonify(days[day_id])


# This is the test code
class TestDays(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_days_5756192474_success(self):
        response = self.app.get('/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), 'Wednesday')

    def test_get_days_5756192474_failure(self):
        response = self.app.get('/7')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()

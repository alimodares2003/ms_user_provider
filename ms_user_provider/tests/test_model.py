import unittest
import jwt
from ms_user_provider.model import get_user_model


class ModelTest(unittest.TestCase):

    def test_get_valid_data(self):
        payload = {
            'sub': '1',
            'preferred_username': 'ali',
            'name': 'Ali Modares',
            'given_name': 'Ali',
            'family_name': 'Modares',
            'mobile': '09123456789',
        }
        input_token = jwt.encode(payload, 'test_secret_key')
        model = get_user_model(input_token)
        self.assertEqual(model.id, payload['sub'])
        self.assertEqual(model.name, payload['name'])
        self.assertEqual(model.username, payload['preferred_username'])
        self.assertEqual(model.mobile, payload['mobile'])

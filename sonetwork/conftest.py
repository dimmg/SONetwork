import json

from django.test import Client, TestCase


class CustomClient(Client):
    def post(self, path, data=None, content_type='application/json',
             follow=False, secure=False, **extra):
        return super().post(path, json.dumps(data), content_type, follow, secure, **extra)

    def patch(self, path, data='', content_type='application/json',
              follow=False, secure=False, **extra):
        return super().patch(path, json.dumps(data), content_type, follow, secure, **extra)


class BaseTestCase(TestCase):
    AUTH_URL = '/api-token-auth/'
    USERS_URL = '/api/users/'
    POSTS_URL = '/api/posts/'

    def setUp(self):
        self.client = CustomClient()
        self.user = {
            'email': 'root@vps.com',
            'password': 'password',
            'first_name': 'root',
            'last_name': 'root',
            'gender': 'female',
            'bio': 'god'
        }

    def _prepare_auth_payload(self, user_payload):
        return {
            'email': user_payload['email'],
            'password': user_payload['password']
        }

    def _add_auth_header(self, token):
        return {
            'HTTP_AUTHORIZATION': 'Bearer %s' % token
        }

    def tearDown(self):
        pass

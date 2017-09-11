import copy

from sonetwork import conftest


class AuthenticationTestCase(conftest.BaseTestCase):
    def test_user_auth_with_valid_credentials(self):
        self.client.post(self.USERS_URL, self.user)

        response = self.client.post(self.AUTH_URL, self._prepare_auth_payload(self.user))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'token')

    def test_user_auth_with_invalid_credentials(self):
        response = self.client.post(self.AUTH_URL, {'email': 'invalid@email.com', 'password': 'password'})

        self.assertEqual(response.status_code, 400)

    def test_endpoint_that_requires_auth_with_no_auth_header(self):
        response = self.client.get(self.USERS_URL)

        self.assertEqual(response.status_code, 401)


class UserTestCase(conftest.BaseTestCase):
    def setUp(self):
        super().setUp()
        self.persisted_user_resp = self.client.post(self.USERS_URL, self.user)

    def test_user_created_with_valid_data(self):
        self.assertEqual(self.persisted_user_resp.status_code, 201)

    def test_user_not_created_with_existing_email(self):
        response = self.client.post(self.USERS_URL, self.user)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'email': ['user with this email already exists.']})

    def test_user_partial_update(self):
        token = self.client.post(self.AUTH_URL, self._prepare_auth_payload(self.user)).json()['token']

        response = self.client.patch(self.USERS_URL + str(self.persisted_user_resp.json()['id']) + '/',
                                     data={'first_name': 'admin'}, **self._add_auth_header(token))

        self.assertEqual(response.json()['first_name'], 'admin')

    def test_user_update_another_user_fails(self):
        user = copy.copy(self.user)
        user['email'] = 'another@email.com'
        user_response = self.client.post(self.USERS_URL, user)

        token = self.client.post(self.AUTH_URL, self._prepare_auth_payload(self.user)).json()['token']

        response = self.client.patch(self.USERS_URL + str(user_response.json()['id']) + '/',
                                     data={'first_name': 'admin'}, **self._add_auth_header(token))

        self.assertEqual(response.status_code, 403)

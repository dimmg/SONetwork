from sonetwork.conftest import BaseTestCase


class PostTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.persisted_user_resp = self.client.post(self.USERS_URL, self.user)
        self.token = self.client.post(self.AUTH_URL, self._prepare_auth_payload(self.user)).json()['token']
        self.post = {
            'title': 'hello world',
            'description': 'hello world description'
        }

    def test_post_created(self):
        response = self.client.post(self.POSTS_URL, self.post, **self._add_auth_header(self.token))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['title'], self.post['title'])

    def test_post_liked(self):
        response = self.client.post(self.POSTS_URL, self.post, **self._add_auth_header(self.token))

        response = self.client.post(self.POSTS_URL + str(response.json()['id']) + '/like/',
                                    **self._add_auth_header(self.token))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['rating'], 1)

    def test_post_disliked(self):
        response = self.client.post(self.POSTS_URL, self.post, **self._add_auth_header(self.token))

        response = self.client.post(self.POSTS_URL + str(response.json()['id']) + '/dislike/',
                                    **self._add_auth_header(self.token))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['rating'], -1)

    def test_post_liked_by_the_same_user(self):
        response = self.client.post(self.POSTS_URL, self.post, **self._add_auth_header(self.token))

        self.client.post(self.POSTS_URL + str(response.json()['id']) + '/like/',
                         **self._add_auth_header(self.token))

        response = self.client.post(self.POSTS_URL + str(response.json()['id']) + '/like/',
                                    **self._add_auth_header(self.token))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['rating'], 1)

    def test_post_disliked_by_the_same_user(self):
        response = self.client.post(self.POSTS_URL, self.post, **self._add_auth_header(self.token))

        self.client.post(self.POSTS_URL + str(response.json()['id']) + '/dislike/',
                         **self._add_auth_header(self.token))

        response = self.client.post(self.POSTS_URL + str(response.json()['id']) + '/dislike/',
                                    **self._add_auth_header(self.token))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['rating'], -1)

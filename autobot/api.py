import requests

import urls


def user_registration(payload):
    """
    User registration
    :param payload: User information
    :return: User profile
    """
    response = requests.post(url=urls.USERS, json=payload)

    return response.json()


def authenticate(email, password):
    """
    User authentication
    :param email: User email
    :param password: User password
    :return: access token
    """
    response = requests.post(url=urls.AUTH, json={'email': email, 'password': password})

    return response.json()['token']


def create_post(payload, token):
    """
    Creates User post
    :param payload: Post information
    :param token: access token
    :return: serialized Post object
    """
    response = requests.post(url=urls.POSTS, json=payload, headers={'Authorization': 'Bearer ' + token})

    return response.json()


def get_post(post_id, token):
    """
    Returns details about a specific Post
    :param post_id: pk of the Post to be retrieved
    :param token: access token
    :return: serialized Post object
    """
    response = requests.get(url=urls.POST % post_id, headers={'Authorization': 'Bearer ' + token})

    return response.json()


def like_post(post_id, token, user_id):
    """
    Likes a specific Post
    :param post_id: pk of the Post to be liked
    :param token: access token
    :param user_id: pk of the User 
    :return: True if Post was liked, False - otherwise
    :rtype: bool
    """
    original_post = get_post(post_id, token)
    if original_post['author'] == user_id:
        return False

    requests.post(url=urls.LIKE_POST % post_id, headers={'Authorization': 'Bearer ' + token})
    liked_post = get_post(post_id, token)

    return liked_post['rating'] > original_post['rating']

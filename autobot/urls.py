import os

DOMAIN = os.environ.get('DOMAIN', 'http://localhost:8000')

AUTH = DOMAIN + '/api-token-auth/'
USERS = DOMAIN + '/api/users/'
POSTS = DOMAIN + '/api/posts/'
POST = POSTS + '%s/'
LIKE_POST = POST + 'like/'

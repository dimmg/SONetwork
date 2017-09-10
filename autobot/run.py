import random
import logging

import api
import conf
import utils

logging.getLogger().setLevel(logging.INFO)

if __name__ == '__main__':
    _cache = {
        'users': [],
        'total_posts': 0
    }

    logging.info('Starting to register Users and create Posts..')

    for _ in range(conf.NUMBER_OF_USERS):
        user_details = utils.generate_user_details()
        user = api.user_registration(user_details)
        logging.info('Created User with email: %s', user['email'])

        token = api.authenticate(user_details['email'], user_details['password'])

        nr_of_posts = random.choice(range(0, conf.MAX_POSTS_PER_USER + 1))
        logging.info('Creating %s Posts for %s', nr_of_posts, user['email'])
        for _ in range(nr_of_posts):
            post = utils.generate_post_details()
            api.create_post(post, token)

        _cache['users'].append({
            'email': user['email'],
            'likes': 0,
            'posts': nr_of_posts,
            'token': token,
            'id': user['id']
        })
        _cache['total_posts'] += nr_of_posts

    logging.info('Registered Users and created Posts..')

    sorted_users = sorted(_cache['users'], key=lambda x: x['posts'], reverse=True)
    for user in sorted_users:
        while user['likes'] < conf.MAX_LIKES_PER_USER:
            post_id = random.choice(range(1, _cache['total_posts'] + 1))
            liked = api.like_post(post_id, user['token'], user['id'])
            if liked:
                user['likes'] += 1
                logging.info('%s liked Post with id: %s. Now he has %s likes..', user['email'], post_id, user['likes'])

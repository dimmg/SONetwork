from faker import Faker

fake = Faker()


def generate_user_details():
    """
    Generates a random User identity.
    :return: User information
    """
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = '%s.%s@%s' % (first_name.lower(), last_name.lower(), fake.free_email_domain())

    return {
        'first_name': first_name,
        'last_name': last_name,
        'gender': fake.random.choice(['male', 'female']),
        'bio': fake.job(),
        'email': email,
        'password': fake.password()
    }


def generate_post_details():
    """
    Generates information about a Post.
    :return: Post information
    """
    return {
        'title': fake.sentence(),
        'description': fake.text()
    }

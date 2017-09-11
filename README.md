# SONetwork

SONetwork is a small RESTful API with the concept of a social network, where users can register and share posts that can be liked / disliked.

Used Technologies:

- [Django Rest Framework 3.6.4](https://github.com/encode/django-rest-framework) web framework
- [Django Rest Framework JWT 1.11.0](https://github.com/GetBlimp/django-rest-framework-jwt) as authentication mechanism
- [Faker 0.8.3](https://github.com/joke2k/faker) for generating fake data
- SQLite 


#### Prerequisites

- Python 3.5 or upper

#### Installation

- Clone the repository and and `cd` into it 

```
$ git clone git@github.com/dimmg/sonetwork.git
$ cd sonetwork
```

- Create a virtual environment and activate it

```
$ virtualenv -p python3 env
$ source env/bin/activate
```

- Install dependencies

```
(env) $ pip install -r requirements.txt
```

- Generate migrations and apply them

```
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
```

- Export the environment variables and run the server that will run by default on port `:8000`

```
# hunter.io api key
(env) $ HUNTER_API_KEY={{API_KEY}}

# clearbit.com api key
(env) $ CLEARBIT_API_KEY={{API_KEY}}

(env) $ python manage.py runserver
```

#### Result

The result is a minimalistic RESTful API with the following features:

```

Authentication 

- User login               POST   /api-token-auth/

Users Management

- User registration        POST   /api/users/
- User retrieval           GET    /api/users/
                           GET    /api/users{id}
- User update              PUT    /api/users/{id}
                           PATCH  /api/users/{id}
                           
Posts Management

- Post creation            POST   /api/posts/
- Post retrieval           GET    /api/posts?author={id}
                           GET    /api/posts/
- Post update              PUT    /api/posts/{id}
                           PATCH  /api/posts/{id}
- Post deletion            DELETE /api/posts/{id}
- Post like                POST   /api/posts/{id}/like
- Post dislike             POST   /api/posts/{id}/dislike

```

#### Tests

In order to run tests, execute the following command:

```
(env) $ python manage.py tests
```


#### Bot Runner

To demonstrate that the API is properly working, there is a bot 
that creates Users, Posts and likes them randomly.

To populate the database entries do:

```
(env) $ cd /autobot
(env) $ python run.py
```

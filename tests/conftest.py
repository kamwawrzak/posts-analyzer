import pytest


post1 = {'userId': 1, 'id': 1, 'title': 'Example title 1',
         'body': 'Example body 1'}

post2 = {'userId': 1, 'id': 2, 'title': 'Example title 2',
         'body': 'Example body 2'}

post3 = {'userId': 2, 'id': 3, 'title': 'Example title 2',
         'body': 'Example body 3'}

user1 = {'id': 1, 'name': 'John Doe', 'username': 'User1',
         'email': 'user1@gmail.com', 'address': {'geo': {'lat': '1.58',
                                                         'lng': '-2.33'}}}

user2 = {'id': 2, 'name': 'John Smith', 'username': 'User2',
         'email': 'user2@gmail.com', 'address': {'geo': {'lat': '10.5',
                                                         'lng': '20'}}}

user3 = {'id': 3, 'name': 'Richard Bourne', 'username': 'User3',
         'email': 'user3@gmail.com', 'address': {'geo': {'lat': '1.69',
                                                         'lng': '-2.3'}}}

user_posts1 = {'id': 1, 'name': 'John Smith', 'username': 'User1',
               'posts_ids': []}

user_posts2 = {'id': 2, 'name': 'Richard Bourne', 'username': 'User2',
               'posts_ids': [1, 2, 3]}


@pytest.fixture()
def t_users():
    return [user1, user2, user3]


@pytest.fixture()
def t_posts():
    return [post1, post2, post3]


@pytest.fixture()
def t_posts2():
    return [post1, post2]


@pytest.fixture()
def t_user1():
    return user1


@pytest.fixture()
def t_user2():
    return user2


@pytest.fixture()
def t_user3():
    return user3


@pytest.fixture()
def t_post1():
    return post1


@pytest.fixture()
def t_post2():
    return post2


@pytest.fixture()
def t_post3():
    return post3


@pytest.fixture()
def users_with_posts():
    return [user_posts1, user_posts2]

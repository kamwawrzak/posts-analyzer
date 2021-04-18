from data_retriever import DataRetriever


f_post = {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident '
                                         'occaecati excepturi optio '
                                         'reprehenderit',
          'body': 'quia et suscipit\nsuscipit recusandae consequuntur '
                  'expedita et cum\nreprehenderit molestiae ut ut quas '
                  'totam\nnostrum rerum est autem sunt rem eveniet architecto'}

f_user = {'id': 1, 'name': 'Leanne Graham', 'username': 'Bret',
          'email': 'Sincere@april.biz',
          'address': {'street': 'Kulas Light', 'suite': 'Apt. 556',
                      'city': 'Gwenborough', 'zipcode': '92998-3874',
                      'geo': {'lat': '-37.3159', 'lng': '81.1496'}},
          'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org',
          'company': {'name': 'Romaguera-Crona',
                      'catchPhrase': 'Multi-layered client-server neural-net',
                      'bs': 'harness real-time e-markets'}}


def test_get_posts():
    """Test getting posts data from server."""
    data = DataRetriever().get_posts()
    assert data[0] == f_post


def test_get_users():
    """Test getting users data from server."""
    data = DataRetriever().get_users()
    assert data[0] == f_user

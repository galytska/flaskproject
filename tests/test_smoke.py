"""
Smoke tests
"""


def test_status_code(client):
    """
    Check status code
    :param client: client fixture
    :return: bool
    """
    return_value = client.get('/')
    assert return_value.status_code == 200


# def test_status_news(client):
#     """
#     Check status code
#     :param client: client fixture
#     :return: bool
#     """
#     return_value = client.get('/news/1')
#     assert return_value.status_code == 200
#
#
# def test_status_register(client):
#     """
#     Check status code
#     :param client: client fixture
#     :return: bool
#     """
#     return_value = client.get('/register')
#     assert return_value.status_code == 200
#
#
# def test_status_login(client):
#     """
#     Check status code
#     :param client: client fixture
#     :return: bool
#     """
#     return_value = client.get('/login')
#     assert return_value.status_code == 200
#
#
# def test_correct_template(client):
#     """
#     Verify expected template is shown
#     :param client:
#     :return:
#     """
#
#     response = client.get('/')
#     assert b'Good news' in response.data
#
#
# def test_correct_template_register(client):
#     """
#     Verify expected template is shown
#     :param client:
#     :return:
#     """
#
#     response = client.get('/register')
#     assert b'Register Here' in response.data
#
#
# def test_correct_template_login(client):
#     """
#     Verify expected template is shown
#     :param client:
#     :return:
#     """
#
#     response = client.get('/login')
#     assert b'Sign In' in response.data
#
#
# def test_messages(client):
#     """Test that messages work."""
#     response = client.post('/', data=dict(
#         news='Hello',
#         news_text='allowed here'
#     ), follow_redirects=True)
#     assert response.status_code == 200
#
#
# def test_invalid_register_post(client):
#     """Test invalid message."""
#     fake_data = 1
#     response = client.post('/register', data=dict(
#         username=fake_data,
#         email=fake_data,
#         surname=fake_data,
#         password=fake_data
#
#     ), follow_redirects=True)
#     assert b'Invalid email address' in response.data

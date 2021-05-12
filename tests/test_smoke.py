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


def test_status_news(client):
    """
    Check status code
    :param client: client fixture
    :return: bool
    """
    return_value = client.get('/news/1')
    assert return_value.status_code == 200


def test_status_register(client):
    """
    Check status code
    :param client: client fixture
    :return: bool
    """
    return_value = client.get('/register')
    assert return_value.status_code == 200


def test_status_login(client):
    """
    Check status code
    :param client: client fixture
    :return: bool
    """
    return_value = client.get('/login')
    assert return_value.status_code == 200


def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'Good news' in rv.data



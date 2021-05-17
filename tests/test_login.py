"""
Login tests
"""
from tests.test_data import journalist1

email = journalist1['email']
password = journalist1['password']


def login(client, username, password):
    return client.post('/login', data=dict(
        email=username,
        password=password
    ), follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)


def test_login_logout(client):
    """Make sure login and logout works."""
    rv = login(client, email, password)
    assert b'Add news here' in rv.data
    b'Login' not in rv.data

    rv = logout(client)
    assert b'Login' in rv.data


def test_login_invalid_email(client):
    """Make sure login check invalid input"""
    rv = login(client, f"{email}INVALID", password)
    assert b'Please logged in to view this page' in rv.data


def test_login_invalid_passowrd(client):
    """Make sure login check invalid input"""
    rv = login(client, email, f'{password}INVALID')
    assert b'Please logged in to view this page' in rv.data

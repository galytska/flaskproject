"""
Login tests
"""
from conftest import email, login, logout, password


def test_login_logout(client):
    """Make sure login and logout works."""
    rv = login(client, email, password)
    assert b'Add news here' in rv.data
    assert b'Login' not in rv.data

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

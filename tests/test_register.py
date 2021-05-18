"""
Verify registration
"""

from faker import Faker


def test_register_post(client):
    """Test invalid message."""
    f = Faker('en_US')
    email = f.email()
    password = f.password()
    response = client.post('/register', data=dict(
        username=f.first_name(),
        email=email,
        user_surname=f.last_name(),
        password=password,
        password2=password

    ), follow_redirects=True)
    assert b'You successfully register!' in response.data


def test_invalid_register_post(client):
    """Test invalid message."""
    fake_data = 1
    response = client.post('/register', data=dict(
        username=fake_data,
        email=fake_data,
        surname=fake_data,
        password=fake_data

    ), follow_redirects=True)
    assert b'Invalid email address' in response.data

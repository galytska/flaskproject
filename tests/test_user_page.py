"""
Verify user profile page
"""
from conftest import email, login, logout, password
from tests.test_data import journalist1


def test_messages(client):
    """Test that messages work."""
    rv = login(client, email, password)
    expected_greeting = f'Hi {journalist1["name"]}!'.title().encode()
    assert expected_greeting in rv.data
    rv = logout(client)
    assert b'Login' in rv.data


def test_add_news(client):
    """Test it is possible to add news"""
    login(client, email, password)
    test_news_title = 'test_title'
    test_news_txt = 'test text'
    response = client.post(f'/user/{journalist1["name"]}', data=dict(
        news=test_news_title,
        news_text=test_news_txt
    ), follow_redirects=True)
    assert test_news_title.encode() in response.data

"""
Smoke tests
"""
import pytest

from tests.test_data import journalist1, news1


@pytest.mark.parametrize("path",
                         ['/',
                          '/news/1',
                          '/register',
                          '/login',
                          f'/user/{journalist1["name"]}',
                          '/logout'])
def test_status_code(client, path):
    """
    Verify status code is 200
    :param client: client object
    :param path: page pas: str
    :return: bool
    """
    return_value = client.get(path)
    assert return_value.status_code == 200


@pytest.mark.parametrize("path, expected_txt",
                         [('/', b'Good news'),
                          ('/register', b'Register Here'),
                          ('/login', b'Sign In'),
                          ('/news/1', f'{news1["title"]}'.title().encode()),
                          ('/logout', b'Please logged in to view this page'),
                          (f'/user/{journalist1["name"]}',
                           b'Please logged in to view this page')])
def test_correct_template(client, path, expected_txt):
    """
    Verify expected template is shown
    :param client:
    :return:
    """
    response = client.get(path)
    assert expected_txt in response.data

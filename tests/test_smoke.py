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

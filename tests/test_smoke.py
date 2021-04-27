def test_empty_db(client):
    rv = client.get('/')
    assert rv.status_code == 200

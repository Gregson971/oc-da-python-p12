def test_create_client(session, dummy_client):
    client = dummy_client
    session.add(client)
    session.commit()

    assert client.id is not None


def test_client_repr(dummy_client):
    client = dummy_client
    assert repr(client) == "Client, name: Jack Smith, email: jack.smith@example.com"

def test_create_collaborator(session, dummy_commercial, dummy_support, dummy_manager):
    collaborator_commercial = dummy_commercial
    session.add(collaborator_commercial)
    session.commit()

    assert collaborator_commercial.id is not None

    collaborator_support = dummy_support
    session.add(collaborator_support)
    session.commit()

    assert collaborator_support.id is not None

    collaborator_manager = dummy_manager
    session.add(collaborator_manager)
    session.commit()

    assert collaborator_manager.id is not None


def test_collaborator_repr(dummy_commercial, dummy_support, dummy_manager):
    collaborator_commercial = dummy_commercial
    assert repr(collaborator_commercial) == "Commercial, name: Bob Brown, email: bob.brown@example.com"

    collaborator_support = dummy_support
    assert repr(collaborator_support) == "Support, name: Alice Smith, email: alice.smith@example.com"

    collaborator_manager = dummy_manager
    assert repr(collaborator_manager) == "Manager, name: John Doe, email: john.doe@example.com"

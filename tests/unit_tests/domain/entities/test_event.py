def test_create_event(session, dummy_event):
    event = dummy_event
    session.add(event)
    session.commit()

    assert event.id is not None


def test_event_repr(dummy_event):
    event = dummy_event
    assert repr(event) == "Event, name: Event name, location: Event location, attendees: 10"

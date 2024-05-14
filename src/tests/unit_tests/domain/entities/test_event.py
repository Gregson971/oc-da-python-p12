import pytest
from datetime import datetime
import uuid

from src.domain.entities.base import Base
from src.domain.entities.event import Event
from src.domain.entities.collaborator import Support
from src.domain.entities.contract import Contract
from src.domain.entities.client import Client

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an in-memory SQLite database for testing
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


@pytest.fixture
def session():
    session = Session()
    yield session
    session.rollback()


def test_create_event(session):
    support = Support(
        first_name="Alice", last_name="Smith", email="alice@example.com", password="password", role="support"
    )
    session.add(support)
    session.commit()

    client = Client(
        information="Client Information",
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        phone_number="123456789",
        company_name="Example Inc.",
        created_date=datetime.now(),
        commercial_id=1,
    )
    session.add(client)
    session.commit()

    contract = Contract(
        uniq_id=uuid.uuid4(),
        client_id=client.id,
        support_id=support.id,
        total_amount=1000.0,
        remaining_amount=500.0,
        created_date=datetime.now(),
        status="signed",
    )
    session.add(contract)
    session.commit()

    event = Event(
        name='Event name',
        started_date=datetime.now(),
        ended_date=datetime.now(),
        location='Event location',
        attendees=10,
        notes='Event notes',
        support_contact_id=support.id,
        contract_id=contract.id,
    )

    session.add(event)
    session.commit()

    assert event.id is not None


def test_event_repr():
    event = Event(
        name='Event name',
        started_date=datetime.now(),
        ended_date=datetime.now(),
        location='Event location',
        attendees=10,
        notes='Event notes',
        support_contact_id=1,
        contract_id=1,
    )

    assert repr(event) == "Event, name: Event name, location: Event location, attendees: 10"

import pytest
import uuid
from datetime import datetime

from src.domain.entities.base import Base
from src.domain.entities.collaborator import Collaborator
from src.domain.entities.client import Client
from src.domain.entities.contract import Contract
from src.domain.entities.event import Event

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


def test_create_collaborator(session):
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
        support_id=1,
        total_amount=1000.0,
        remaining_amount=500.0,
        created_date=datetime.now(),
        status="signed",
    )
    session.add(contract)
    session.commit()

    event = Event(
        id=1,
        name='Event name',
        started_date=datetime.now(),
        ended_date=datetime.now(),
        location='Event location',
        attendees=10,
        notes='Event notes',
        contract_id=contract.id,
        support_contact_id=1,
    )

    session.add(event)
    session.commit()

    collaborator = Collaborator(
        first_name="John", last_name="Doe", email="john@example.com", password="password", role="manager"
    )

    session.add(collaborator)
    session.commit()

    assert collaborator.id is not None


def test_collaborator_repr():
    collaborator = Collaborator(
        first_name="John", last_name="Doe", email="john@example.com", password="password", role="manager"
    )
    assert collaborator.__repr__() == "Collaborator, name: John Doe, email: john@example.com"

import pytest

from datetime import datetime
import uuid


from app.repository.models.base import Base
from app.repository.models.client import Client
from app.repository.models.collaborator import Support, Commercial
from app.repository.models.contract import Contract
from app.repository.models.event import Event

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


def test_create_client(session):
    commercial = Commercial(
        first_name="John", last_name="Doe", email="john@example.com", password="password", role="support"
    )
    session.add(commercial)
    session.commit()

    support = Support(
        first_name="Alice", last_name="Smith", email="alice@example.com", password="password", role="support"
    )
    session.add(support)
    session.commit()

    contract = Contract(
        uniq_id=uuid.uuid4(),
        client_id=1,
        support_id=support.id,
        total_amount=1000.0,
        remaining_amount=500.0,
        created_date=datetime.now(),
        status="signed",
    )
    session.add(contract)
    session.commit()

    event = Event(
        contract_id=contract.id,
        started_date=datetime.now(),
        ended_date=datetime.now(),
        support_contact_id=1,
        location="Event location",
        attendees=10,
        notes="Event notes",
    )
    session.add(event)
    session.commit()

    client = Client(
        information="Client Information",
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        phone_number="123456789",
        company_name="Example Inc.",
        created_date=datetime.now(),
        commercial_id=commercial.id,
    )
    session.add(client)
    session.commit()

    assert client.id is not None


def test_client_repr():
    client = Client(information="Client Information", first_name="John", last_name="Doe", email="john@example.com")
    assert client.__repr__() == "Client, name: John Doe, email: john@example.com"

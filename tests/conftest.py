import pytest

from datetime import datetime

from src.domain.entities.base import Base
from src.domain.entities.contract import Contract
from src.domain.entities.client import Client

from src.domain.entities.collaborator import Commercial, Manager, Support
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


@pytest.fixture
def dummy_manager():
    return Manager(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        password="password",
        role="manager",
    )


@pytest.fixture
def dummy_updated_manager():
    return Manager(
        first_name="John Upated",
        last_name="Doe",
        email="johnupated.doe@example.com",
        password="password",
        role="manager",
    )


@pytest.fixture
def dummy_support():
    return Support(
        first_name="Alice",
        last_name="Smith",
        email="alice.smith@example.com",
        password="password",
        role="support",
    )


@pytest.fixture
def dummy_updated_support():
    return Support(
        first_name="Alice Updated",
        last_name="Smith",
        email="aliceupdated.smith@example.com",
        password="password",
        role="support",
    )


@pytest.fixture
def dummy_commercial():
    return Commercial(
        first_name="Bob",
        last_name="Brown",
        email="bob.brown@example.com",
        password="password",
        role="commercial",
    )


@pytest.fixture
def dummy_updated_commercial():
    return Commercial(
        first_name="Bob Updated",
        last_name="Brown",
        email="bobupdated.brown@example.com",
        password="password",
        role="commercial",
    )


@pytest.fixture
def dummy_client():
    return Client(
        information="Client Information",
        first_name="Jack",
        last_name="Smith",
        email="jack.smith@example.com",
        phone_number="123456789",
        company_name="Example Inc.",
        created_date=datetime.now(),
        commercial_id=1,
    )


@pytest.fixture
def dummy_updated_client():
    return Client(
        information="Client Information Updated",
        first_name="Jack",
        last_name="Smith",
        email="jack.smith@example.com",
        phone_number="123456789",
        company_name="Example Inc.",
        created_date=datetime.now(),
        commercial_id=1,
    )


@pytest.fixture
def dummy_contract():
    return Contract(
        uniq_id="e837aac6-8b91-4dc8-acbe-08887500832b",
        client_id=1,
        support_id=1,
        total_amount=1000.0,
        remaining_amount=500.0,
        created_date=datetime.now(),
        status="signed",
    )


@pytest.fixture
def dummy_updated_contract():
    return Contract(
        uniq_id="e837aac6-8b91-4dc8-acbe-08887500832b",
        client_id=1,
        support_id=1,
        total_amount=1000.0,
        remaining_amount=250.0,
        created_date=datetime.now(),
        status="signed",
    )


@pytest.fixture
def dummy_event():
    return Event(
        name='Event name',
        started_date=datetime.now(),
        ended_date=datetime.now(),
        location="Event location",
        attendees=10,
        notes="Event notes",
        contract_id=1,
        support_contact_id=1,
    )


@pytest.fixture
def dummy_updated_event():
    return Event(
        name='Event name updated',
        started_date=datetime.now(),
        ended_date=datetime.now(),
        location="Event location",
        attendees=20,
        notes="Event notes",
        contract_id=1,
        support_contact_id=1,
    )

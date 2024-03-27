import pytest
from unittest.mock import patch

from models.models import Event


@pytest.fixture
def mock_client():
    with patch('models.models.Client') as mock_client:
        yield mock_client


@pytest.fixture
def mock_support():
    with patch('models.models.Support') as mock_support:
        yield mock_support


@pytest.fixture
def mock_contract():
    with patch('models.models.Contract') as mock_contract:
        yield mock_contract


@pytest.fixture
def sample_event():
    return Event(
        id=1,
        contract_id=1,
        client_id=1,
        started_date={},
        ended_date={},
        support_contact_id=1,
        location='Event location',
        attendees=10,
        notes='Event notes',
    )


def test_event_repr(sample_event):
    expected_repr = (
        "Event(id=1, contract_id=1, client_id=1, started_date={}, ended_date={}, "
        "support_contact_id=1, location=Event location, attendees=10, notes=Event notes)"
    )
    assert repr(sample_event) == expected_repr


def test_event_client_relationship(sample_event, mock_client):
    sample_event.client = mock_client
    assert sample_event.client == mock_client


def test_event_support_relationship(sample_event, mock_support):
    sample_event.support_contact = mock_support
    assert sample_event.support_contact == mock_support


def test_event_contract_relationship(sample_event, mock_contract):
    sample_event.contract = mock_contract
    assert sample_event.contract == mock_contract

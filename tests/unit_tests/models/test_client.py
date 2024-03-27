import pytest
from unittest.mock import patch

from models.models import Client


@pytest.fixture
def mock_commercial():
    with patch('models.models.Commercial') as mock_commercial:
        yield mock_commercial


@pytest.fixture
def sample_client():
    return Client(
        id=1,
        information='Client information',
        first_name='John',
        last_name='Doe',
        full_name='John Doe',
        email='john.doe@example.com',
        phone_number='123456789',
        company_name='ABCD Inc.',
        created_date={},
        updated_date={},
        commercial_id=1,
    )


def test_client_repr(sample_client):
    expected_repr = (
        "Client(id=1, information=Client information, first_name=John, last_name=Doe, full_name=John Doe, "
        "email=john.doe@example.com, phone_number=123456789, company_name=ABCD Inc., created_date={}, "
        "updated_date={}, commercial_id=1)"
    )
    assert repr(sample_client) == expected_repr


def test_client_commercial_relationship(sample_client, mock_commercial):
    sample_client.commercial = mock_commercial
    assert sample_client.commercial == mock_commercial

import pytest
from unittest.mock import patch

from models.models import Contract


@pytest.fixture
def mock_client():
    with patch('models.models.Client') as mock_client:
        yield mock_client


@pytest.fixture
def mock_commercial():
    with patch('models.models.Commercial') as mock_commercial:
        yield mock_commercial


@pytest.fixture
def sample_contract():
    return Contract(
        id=1,
        uniq_id='ABC123',
        client_id=1,
        commercial_id='1',
        total_amount=1000.0,
        remaining_amount=500.0,
        created_date={},
        status='active',
    )


def test_contract_repr(sample_contract):
    expected_repr = (
        "Contract(id=1, uniq_id=ABC123, client_id=1, commercial_id=1, total_amount=1000.0, "
        "remaining_amount=500.0, created_date={}, status=active)"
    )
    assert repr(sample_contract) == expected_repr


def test_contract_client_relationship(sample_contract, mock_client):
    sample_contract.client = mock_client
    assert sample_contract.client == mock_client


def test_contract_commercial_relationship(sample_contract, mock_commercial):
    sample_contract.commercial = mock_commercial
    assert sample_contract.commercial == mock_commercial

from unittest import mock

from src.domain.use_cases.manage_support import ManageSupport


manage_support = ManageSupport()


@mock.patch('src.infrastructure.repository.client_repository.ClientRepository.get_clients')
def test_get_clients(mock_get_clients, dummy_client):
    mock_get_clients.return_value = [dummy_client]
    assert manage_support.get_clients() == [dummy_client]


@mock.patch('src.infrastructure.repository.contract_repository.ContractRepository.get_contracts')
def test_get_contracts(mock_get_contracts, dummy_contract):
    mock_get_contracts.return_value = [dummy_contract]
    assert manage_support.get_contracts() == [dummy_contract]


@mock.patch('src.infrastructure.repository.event_repository.EventRepository.get_events')
def test_get_events(mock_get_events, dummy_event):
    mock_get_events.return_value = [dummy_event]
    assert manage_support.get_events() == [dummy_event]


@mock.patch('src.infrastructure.repository.event_repository.EventRepository.get_assigned_events')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_get_assigned_events(mock_di, mock_get_assigned_events, dummy_event):
    mock_di.__getitem__.return_value = {'role': 'support'}
    mock_get_assigned_events.return_value = [dummy_event]
    assert manage_support.get_assigned_events() == [dummy_event]


@mock.patch('src.infrastructure.repository.event_repository.EventRepository.update_event')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_update_event(mock_di, mock_update_event, dummy_event, dummy_updated_event):
    mock_di.__getitem__.return_value = {'role': 'support'}

    mock_update_event.return_value = dummy_updated_event
    mock_update_event.return_value.information = "Event Information Updated"

    updated_event = manage_support.update_event(dummy_event.id, {})
    mock_update_event.assert_called_once()
    assert updated_event.information == dummy_updated_event.information

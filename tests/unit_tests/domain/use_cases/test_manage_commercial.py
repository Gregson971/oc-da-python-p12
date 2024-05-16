from unittest import mock

from src.domain.use_cases.manage_commercial import ManageCommercial


manage_commercial = ManageCommercial()


@mock.patch('src.infrastructure.repository.client_repository.ClientRepository.get_clients')
def test_get_clients(mock_get_clients, dummy_client):
    mock_get_clients.return_value = [dummy_client]
    assert manage_commercial.get_clients() == [dummy_client]


@mock.patch('src.infrastructure.repository.contract_repository.ContractRepository.get_contracts')
def test_get_contracts(mock_get_contracts, dummy_contract):
    mock_get_contracts.return_value = [dummy_contract]
    assert manage_commercial.get_contracts() == [dummy_contract]


@mock.patch('src.infrastructure.repository.event_repository.EventRepository.get_events')
def test_get_events(mock_get_events, dummy_event):
    mock_get_events.return_value = [dummy_event]
    assert manage_commercial.get_events() == [dummy_event]


@mock.patch('src.infrastructure.repository.client_repository.ClientRepository.get_client')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_get_client(mock_di, mock_get_client, dummy_client):
    mock_di.__getitem__.return_value = {'role': 'commercial'}
    mock_get_client.return_value = dummy_client
    assert manage_commercial.get_client(1) == dummy_client


@mock.patch('src.infrastructure.repository.client_repository.ClientRepository.create_client')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_create_client(mock_di, mock_create_client, dummy_client):
    mock_di.__getitem__.return_value = {'role': 'commercial'}
    mock_create_client.return_value = dummy_client
    assert manage_commercial.create_client({}) == dummy_client


@mock.patch('src.infrastructure.repository.client_repository.ClientRepository.update_client')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_update_client(mock_di, mock_update_client, dummy_client, dummy_updated_client):
    mock_di.__getitem__.return_value = {'role': 'commercial'}

    mock_update_client.return_value = dummy_updated_client
    mock_update_client.return_value.information = "Client Information Updated"

    updated_client = manage_commercial.update_client(dummy_client.id, {})

    mock_update_client.assert_called_once()
    assert updated_client.information == dummy_updated_client.information


@mock.patch('src.infrastructure.repository.contract_repository.ContractRepository.get_contract')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_get_contract(mock_di, mock_get_contract, dummy_contract):
    mock_di.__getitem__.return_value = {'role': 'commercial'}
    mock_get_contract.return_value = dummy_contract
    assert manage_commercial.get_contract(1) == dummy_contract


@mock.patch('src.infrastructure.repository.contract_repository.ContractRepository.update_contract')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_update_contract(mock_di, mock_update_contract, dummy_contract, dummy_updated_contract):
    mock_di.__getitem__.return_value = {'role': 'commercial'}

    mock_update_contract.return_value = dummy_updated_contract
    mock_update_contract.return_value.remaining_amount = 250.0

    updated_contract = manage_commercial.update_contract(dummy_contract.id, {})

    mock_update_contract.assert_called_once()
    assert updated_contract.remaining_amount == 250.0
    assert updated_contract.total_amount == 1000.0
    assert updated_contract.status == 'signed'


@mock.patch('src.infrastructure.repository.contract_repository.ContractRepository.get_unsigned_contracts')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_get_unsigned_contracts(mock_di, mock_get_unsigned_contracts, dummy_contract):
    mock_di.__getitem__.return_value = {'role': 'commercial'}
    mock_get_unsigned_contracts.return_value = [dummy_contract]
    assert manage_commercial.get_unsigned_contracts() == [dummy_contract]


@mock.patch('src.infrastructure.repository.contract_repository.ContractRepository.get_unpaid_contracts')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_get_unpaid_contracts(mock_di, mock_get_unpaid_contracts, dummy_contract):
    mock_di.__getitem__.return_value = {'role': 'commercial'}
    mock_get_unpaid_contracts.return_value = [dummy_contract]
    assert manage_commercial.get_unpaid_contracts() == [dummy_contract]


@mock.patch('src.infrastructure.repository.event_repository.EventRepository.create_event')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_create_event(mock_di, mock_create_event, dummy_event):
    mock_di.__getitem__.return_value = {'role': 'commercial'}
    mock_create_event.return_value = dummy_event
    assert manage_commercial.create_event({}) == dummy_event

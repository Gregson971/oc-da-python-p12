from unittest import mock

from src.domain.use_cases.manage_manager import ManageManager


manage_manager = ManageManager()


@mock.patch('src.infrastructure.repository.client_repository.ClientRepository.get_clients')
def test_get_clients(mock_get_clients, dummy_client):
    mock_get_clients.return_value = [dummy_client]
    assert manage_manager.get_clients() == [dummy_client]


@mock.patch('src.infrastructure.repository.client_repository.ClientRepository.get_client')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_get_client(mock_di, mock_get_client, dummy_client):
    mock_di.__getitem__.return_value = {'role': 'manager'}
    mock_get_client.return_value = dummy_client
    assert manage_manager.get_client(1) == dummy_client


@mock.patch('src.infrastructure.repository.event_repository.EventRepository.get_events')
def test_get_events(mock_get_events, dummy_event):
    mock_get_events.return_value = [dummy_event]
    assert manage_manager.get_events() == [dummy_event]


@mock.patch('src.infrastructure.repository.commercial_repository.CommercialRepository.get_commercials')
@mock.patch('src.infrastructure.repository.manager_repository.ManagerRepository.get_managers')
@mock.patch('src.infrastructure.repository.support_repository.SupportRepository.get_supports')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_get_collaborators(
    mock_di, mock_get_supports, mock_get_managers, mock_get_commercials, dummy_commercial, dummy_manager, dummy_support
):
    mock_di.__getitem__.return_value = {'role': 'manager'}
    mock_get_commercials.return_value = [dummy_commercial]
    mock_get_managers.return_value = [dummy_manager]
    mock_get_supports.return_value = [dummy_support]
    assert manage_manager.get_collaborators() == [dummy_commercial, dummy_manager, dummy_support]


@mock.patch('src.infrastructure.repository.manager_repository.ManagerRepository.create_manager')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_create_manager(mock_di, mock_create_manager, dummy_manager):
    mock_di.__getitem__.return_value = {'role': 'manager'}
    mock_create_manager.return_value = dummy_manager
    assert manage_manager.create_manager({}) == dummy_manager


@mock.patch('src.infrastructure.repository.manager_repository.ManagerRepository.get_managers')
def test_get_managers(mock_get_managers, dummy_manager):
    mock_get_managers.return_value = [dummy_manager]
    assert manage_manager.get_managers() == [dummy_manager]


@mock.patch('src.infrastructure.repository.manager_repository.ManagerRepository.get_manager')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_get_manager(mock_di, mock_get_manager, dummy_manager):
    mock_di.__getitem__.return_value = {'role': 'manager'}
    mock_get_manager.return_value = dummy_manager
    assert manage_manager.get_manager(1) == dummy_manager


@mock.patch('src.infrastructure.repository.manager_repository.ManagerRepository.update_manager')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_update_manager(mock_di, mock_update_manager, dummy_manager, dummy_updated_manager):
    mock_di.__getitem__.return_value = {'role': 'manager'}

    mock_update_manager.return_value = dummy_updated_manager
    mock_update_manager.return_value.first_name = "John Updated"
    mock_update_manager.return_value.email = "johnupdated.doe@example.com"

    updated_manager = manage_manager.update_manager(dummy_manager.id, {})

    mock_update_manager.assert_called_once()
    assert updated_manager.first_name == dummy_updated_manager.first_name
    assert updated_manager.email == dummy_updated_manager.email


@mock.patch('src.infrastructure.repository.manager_repository.ManagerRepository.delete_manager')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_delete_manager(mock_di, mock_delete_manager, dummy_manager):
    mock_di.__getitem__.return_value = {'role': 'manager'}
    mock_delete_manager.return_value = True
    assert manage_manager.delete_manager(dummy_manager.id) is True


@mock.patch('src.infrastructure.repository.commercial_repository.CommercialRepository.create_commercial')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_create_commercial(mock_di, mock_create_commercial, dummy_commercial):
    mock_di.__getitem__.return_value = {'role': 'manager'}
    mock_create_commercial.return_value = dummy_commercial
    assert manage_manager.create_commercial({}) == dummy_commercial


@mock.patch('src.infrastructure.repository.commercial_repository.CommercialRepository.get_commercials')
def test_get_commercials(mock_get_commercials, dummy_commercial):
    mock_get_commercials.return_value = [dummy_commercial]
    assert manage_manager.get_commercials() == [dummy_commercial]


@mock.patch('src.infrastructure.repository.commercial_repository.CommercialRepository.get_commercial')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_get_commercial(mock_di, mock_get_commercial, dummy_commercial):
    mock_di.__getitem__.return_value = {'role': 'manager'}
    mock_get_commercial.return_value = dummy_commercial
    assert manage_manager.get_commercial(1) == dummy_commercial


@mock.patch('src.infrastructure.repository.commercial_repository.CommercialRepository.update_commercial')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_update_commercial(mock_di, mock_update_commercial, dummy_commercial, dummy_updated_commercial):
    mock_di.__getitem__.return_value = {'role': 'manager'}

    mock_update_commercial.return_value = dummy_updated_commercial
    mock_update_commercial.return_value.first_name = "Bob Updated"
    mock_update_commercial.return_value.email = "bobupdated.brown@example.com"

    updated_commercial = manage_manager.update_commercial(dummy_commercial.id, {})
    mock_update_commercial.assert_called_once()
    assert updated_commercial.first_name == dummy_updated_commercial.first_name
    assert updated_commercial.email == dummy_updated_commercial.email


@mock.patch('src.infrastructure.repository.commercial_repository.CommercialRepository.delete_commercial')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_delete_commercial(mock_di, mock_delete_commercial, dummy_commercial):
    mock_di.__getitem__.return_value = {'role': 'manager'}
    mock_delete_commercial.return_value = True
    assert manage_manager.delete_commercial(dummy_commercial.id) is True


@mock.patch('src.infrastructure.repository.support_repository.SupportRepository.create_support')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_create_support(mock_di, mock_create_support, dummy_support):
    mock_di.__getitem__.return_value = {'role': 'manager'}
    mock_create_support.return_value = dummy_support
    assert manage_manager.create_support({}) == dummy_support


@mock.patch('src.infrastructure.repository.support_repository.SupportRepository.get_supports')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_get_supports(mock_di, mock_get_supports, dummy_support):
    mock_di.__getitem__.return_value = {'role': 'manager'}
    mock_get_supports.return_value = [dummy_support]
    assert manage_manager.get_supports() == [dummy_support]


@mock.patch('src.infrastructure.repository.support_repository.SupportRepository.get_support')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_get_support(mock_di, mock_get_support, dummy_support):
    mock_di.__getitem__.return_value = {'role': 'manager'}
    mock_get_support.return_value = dummy_support
    assert manage_manager.get_support(1) == dummy_support


@mock.patch('src.infrastructure.repository.support_repository.SupportRepository.update_support')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_update_support(mock_di, mock_update_support, dummy_support, dummy_updated_support):
    mock_di.__getitem__.return_value = {'role': 'manager'}

    mock_update_support.return_value = dummy_updated_support
    mock_update_support.return_value.first_name = "Alice Updated"
    mock_update_support.return_value.email = "aliceupdated.smith@example.com"

    updated_support = manage_manager.update_support(dummy_support.id, {})
    mock_update_support.assert_called_once()
    assert updated_support.first_name == dummy_updated_support.first_name
    assert updated_support.email == dummy_updated_support.email


@mock.patch('src.infrastructure.repository.support_repository.SupportRepository.delete_support')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_delete_support(mock_di, mock_delete_support, dummy_support):
    mock_di.__getitem__.return_value = {'role': 'manager'}
    mock_delete_support.return_value = True
    assert manage_manager.delete_support(dummy_support.id) is True


@mock.patch('src.infrastructure.repository.contract_repository.ContractRepository.create_contract')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_create_contract(mock_di, mock_create_contract, dummy_contract):
    mock_di.__getitem__.return_value = {'role': 'manager'}
    mock_create_contract.return_value = dummy_contract
    assert manage_manager.create_contract({}) == dummy_contract


@mock.patch('src.infrastructure.repository.contract_repository.ContractRepository.get_contracts')
def test_get_contracts(mock_get_contracts, dummy_contract):
    mock_get_contracts.return_value = [dummy_contract]
    assert manage_manager.get_contracts() == [dummy_contract]


@mock.patch('src.infrastructure.repository.contract_repository.ContractRepository.get_contract')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_get_contract(mock_di, mock_get_contract, dummy_contract):
    mock_di.__getitem__.return_value = {'role': 'manager'}
    mock_get_contract.return_value = dummy_contract
    assert manage_manager.get_contract(1) == dummy_contract


@mock.patch('src.infrastructure.repository.contract_repository.ContractRepository.update_contract')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_update_contract(mock_di, mock_update_contract, dummy_contract, dummy_updated_contract):
    mock_di.__getitem__.return_value = {'role': 'manager'}

    mock_update_contract.return_value = dummy_updated_contract
    mock_update_contract.return_value.information = "Contract Information Updated"

    updated_contract = manage_manager.update_contract(dummy_contract.id, {})
    mock_update_contract.assert_called_once()
    assert updated_contract.information == dummy_updated_contract.information


@mock.patch('src.infrastructure.repository.event_repository.EventRepository.get_events_with_no_assigned_support')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_get_events_with_no_assigned_support(mock_di, mock_get_events_with_no_assigned_support, dummy_event):
    mock_di.__getitem__.return_value = {'role': 'manager'}
    mock_get_events_with_no_assigned_support.return_value = [dummy_event]
    assert manage_manager.get_events_with_no_assigned_support() == [dummy_event]


@mock.patch('src.infrastructure.repository.event_repository.EventRepository.update_event')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_update_event(mock_di, mock_update_event, dummy_event, dummy_updated_event):
    mock_di.__getitem__.return_value = {'role': 'manager'}

    mock_update_event.return_value = dummy_updated_event
    mock_update_event.return_value.name = "Event name updated"
    mock_update_event.return_value.attendees = 20

    updated_event = manage_manager.update_event(dummy_event.id, {})
    mock_update_event.assert_called_once()
    assert updated_event.name == dummy_updated_event.name
    assert updated_event.attendees == dummy_updated_event.attendees

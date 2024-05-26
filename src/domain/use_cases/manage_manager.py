from typing import List

from src.domain.entities.client import Client
from src.domain.entities.collaborator import Commercial, Manager, Support
from src.domain.entities.contract import Contract
from src.domain.entities.event import Event

from src.domain.permissions.collaborator_permission import require_permission

from src.infrastructure.repository.manager_repository import ManagerRepository
from src.infrastructure.repository.commercial_repository import CommercialRepository
from src.infrastructure.repository.support_repository import SupportRepository
from src.infrastructure.repository.event_repository import EventRepository
from src.infrastructure.repository.contract_repository import ContractRepository
from src.infrastructure.repository.client_repository import ClientRepository


class ManageManager:

    def get_clients(self) -> List[Client]:
        """Get all clients from the repository"""
        return ClientRepository().get_clients()

    def get_client(self, client_id: int) -> Client:
        """Get a client from the repository"""
        return ClientRepository().get_client(client_id)

    def get_events(self) -> List[Event]:
        """Get all events from the repository"""
        return EventRepository().get_events()

    @require_permission('create_collaborator')
    def get_collaborators(self) -> List:
        """Get all collaborators from the repository"""
        return (
            CommercialRepository().get_commercials()
            + ManagerRepository().get_managers()
            + SupportRepository().get_supports()
        )

    @require_permission('create_collaborator')
    def create_manager(self, manager: Manager) -> Manager:
        """Create a manager in the repository"""
        return ManagerRepository().create_manager(manager)

    @require_permission('create_collaborator')
    def get_managers(self) -> List[Manager]:
        """Get all managers from the repository"""
        return ManagerRepository().get_managers()

    @require_permission('create_collaborator')
    def get_manager(self, manager_id: int) -> Manager:
        """Get a manager from the repository"""
        return ManagerRepository().get_manager(manager_id)

    @require_permission('update_collaborator')
    def update_manager(self, manager_id: int, manager: Manager) -> Manager:
        """Update a manager in the repository"""
        return ManagerRepository().update_manager(manager_id, manager)

    @require_permission('delete_collaborator')
    def delete_manager(self, manager_id: int) -> bool:
        """Delete a manager from the repository"""
        return ManagerRepository().delete_manager(manager_id)

    @require_permission('create_collaborator')
    def create_commercial(self, commercial: Commercial) -> Commercial:
        """Create a commercial in the repository"""
        return CommercialRepository().create_commercial(commercial)

    @require_permission('create_collaborator')
    def get_commercials(self) -> List[Commercial]:
        """Get all commercials from the repository"""
        return CommercialRepository().get_commercials()

    @require_permission('create_collaborator')
    def get_commercial(self, commercial_id: int) -> Commercial:
        """Get a commercial from the repository"""
        return CommercialRepository().get_commercial(commercial_id)

    @require_permission('update_collaborator')
    def update_commercial(self, commercial_id: int, commercial: Commercial) -> Commercial:
        """Update a commercial in the repository"""
        return CommercialRepository().update_commercial(commercial_id, commercial)

    @require_permission('delete_collaborator')
    def delete_commercial(self, commercial_id: int) -> bool:
        """Delete a commercial from the repository"""
        return CommercialRepository().delete_commercial(commercial_id)

    @require_permission('create_collaborator')
    def create_support(self, support: Support) -> Support:
        """Create a support in the repository"""
        return SupportRepository().create_support(support)

    @require_permission('create_collaborator')
    def get_supports(self) -> List[Support]:
        """Get all supports from the repository"""
        return SupportRepository().get_supports()

    @require_permission('create_collaborator')
    def get_support(self, support_id: int) -> Support:
        """Get a support from the repository"""
        return SupportRepository().get_support(support_id)

    @require_permission('update_collaborator')
    def update_support(self, support_id: int, support: Support) -> Support:
        """Update a support in the repository"""
        return SupportRepository().update_support(support_id, support)

    @require_permission('delete_collaborator')
    def delete_support(self, support_id: int) -> bool:
        """Delete a support from the repository"""
        return SupportRepository().delete_support(support_id)

    @require_permission('create_contract')
    def create_contract(self, contract: Contract) -> Contract:
        """Create a contract in the repository"""
        return ContractRepository().create_contract(contract)

    @require_permission('create_contract')
    def get_contracts(self) -> List[Contract]:
        """Get all contracts from the repository"""
        return ContractRepository().get_contracts()

    @require_permission('create_contract')
    def get_contract(self, contract_id: int) -> Contract:
        """Get a contract from the repository"""
        return ContractRepository().get_contract(contract_id)

    @require_permission('update_contract')
    def update_contract(self, contract_id: int, contract: Contract) -> Contract:
        """Update a contract in the repository"""
        return ContractRepository().update_contract(contract_id, contract)

    @require_permission('filter_events')
    def get_events_with_no_assigned_support(self) -> List[Event]:
        """Get all events with no assigned support from the repository"""
        return EventRepository().get_events_with_no_assigned_support()

    @require_permission('update_event')
    def update_event(self, event_id: int, event: Event) -> Event:
        """Update an event in the repository"""
        return EventRepository().update_event(event_id, event)

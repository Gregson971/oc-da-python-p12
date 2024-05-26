from typing import List

from src.domain.entities.client import Client
from src.domain.entities.contract import Contract
from src.domain.entities.event import Event

from src.domain.permissions.collaborator_permission import require_permission

from src.infrastructure.repository.client_repository import ClientRepository
from src.infrastructure.repository.contract_repository import ContractRepository
from src.infrastructure.repository.event_repository import EventRepository


class ManageCommercial:

    def get_clients(self) -> List[Client]:
        """Get all clients from the repository"""
        return ClientRepository().get_clients()

    def get_contracts(self) -> List[Contract]:
        """Get all contracts from the repository"""
        return ContractRepository().get_contracts()

    def get_events(self) -> List[Event]:
        """Get all events from the repository"""
        return EventRepository().get_events()

    @require_permission('create_client')
    def get_client(self, client_id: int) -> Client:
        """
        Get a client from the repository

        Args:
            client_id (int): The client id

        Returns:
            Client: The client entity
        """
        return ClientRepository().get_client(client_id)

    @require_permission('create_client')
    def create_client(self, client: Client) -> Client:
        """Create a client in the repository"""
        return ClientRepository().create_client(client)

    @require_permission('update_client')
    def update_client(self, client_id: int, client: Client) -> Client:
        """Update a client in the repository"""
        return ClientRepository().update_client(client_id, client)

    @require_permission('create_client_contract')
    def get_contract(self, contract_id: int) -> Contract:
        """Get a contract from the repository"""
        return ContractRepository().get_contract(contract_id)

    @require_permission('update_client_contract')
    def update_contract(self, contract_id: int, contract: Contract) -> Contract:
        """Update a contract in the repository"""
        return ContractRepository().update_contract(contract_id, contract)

    @require_permission('filter_contracts')
    def get_unsigned_contracts(self) -> List[Contract]:
        """Get all unsigned contracts from the repository"""
        return ContractRepository().get_unsigned_contracts()

    @require_permission('filter_contracts')
    def get_unpaid_contracts(self) -> List[Contract]:
        """Get all unpaid contracts from the repository"""
        return ContractRepository().get_unpaid_contracts()

    @require_permission('create_event')
    def create_event(self, event: Event) -> Event:
        """Create an event in the repository"""
        return EventRepository().create_event(event)

from typing import List

from src.domain.entities.client import Client
from src.domain.entities.contract import Contract
from src.domain.entities.event import Event

from src.domain.permissions.collaborator_permission import require_permission

from src.infrastructure.repository.client_repository import ClientRepository
from src.infrastructure.repository.contract_repository import ContractRepository
from src.infrastructure.repository.event_repository import EventRepository


class ManageCommercial:
    def __init__(self, session):
        self.session = session

    def get_clients(self) -> List[Client]:
        return ClientRepository(self.session).get_clients()

    def get_contrats(self) -> List[Contract]:
        return ContractRepository(self.session).get_contracts()

    def get_events(self) -> List[Event]:
        return EventRepository(self.session).get_events()

    @require_permission('create_client')
    def create_client(self, client: Client) -> Client:
        return ClientRepository(self.session).create_client(client)

    @require_permission('update_client')
    def update_client(self, client: Client) -> Client:
        return ClientRepository(self.session).update_client(client)

    @require_permission('update_client_contract')
    def update_contract(self, contract: Contract) -> Contract:
        return ContractRepository(self.session).update_contract(contract)

    @require_permission('filter_contracts')
    def get_unsigned_contracts(self, contract: Contract) -> List[Contract]:
        return ContractRepository(self.session).get_unsigned_contracts(contract)

    @require_permission('filter_contracts')
    def get_unpaid_contracts(self, contract: Contract) -> List[Contract]:
        return ContractRepository(self.session).get_unpaid_contracts(contract)

    @require_permission('create_event')
    def create_event(self, event: Event) -> Event:
        return EventRepository(self.session).create_event(event)

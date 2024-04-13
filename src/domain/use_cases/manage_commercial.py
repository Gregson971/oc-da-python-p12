from typing import List
from src.domain.entities.client import Client
from src.domain.entities.collaborator import Commercial
from src.domain.entities.contract import Contract
from src.domain.entities.event import Event


class ManageCommercial:
    commercial = None

    def __init__(self, commercial: Commercial):
        self.commercial = commercial

    def create_client(self, client: Client) -> Client:
        pass

    def update_client(self, client: Client) -> Client:
        pass

    def update_contract(self, contract: Contract) -> Contract:
        pass

    def get_unsigned_contracts(self, contract: Contract) -> List[Contract]:
        pass

    def get_unpaid_contracts(self, contract: Contract) -> List[Contract]:
        pass

    def create_event(self, event: Event) -> Event:
        pass

    def get_clients(self) -> List[Client]:
        pass

    def get_contrats(self) -> List[Contract]:
        pass

    def get_events(self) -> List[Event]:
        pass

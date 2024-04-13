from typing import List

from src.domain.entities.client import Client
from src.domain.entities.collaborator import Commercial, Manager, Support
from src.domain.entities.contract import Contract
from src.domain.entities.event import Event

from src.infrastructure.repository.manager_repository import ManagerRepository
from src.infrastructure.repository.commercial_repository import CommercialRepository
from src.infrastructure.repository.support_repository import SupportRepository
from src.infrastructure.repository.event_repository import EventRepository
from src.infrastructure.repository.contract_repository import ContractRepository
from src.infrastructure.repository.client_repository import ClientRepository


class ManageManager:
    manager = None

    def __init__(self, session):
        self.session = session

    def get_clients(self) -> List[Client]:
        return ClientRepository(self.session).get_clients()

    def get_contrats(self) -> List[Contract]:
        return ContractRepository(self.session).get_contracts()

    def get_events(self) -> List[Event]:
        return EventRepository(self.session).get_events()

    def create_manager(self, manager: Manager) -> Manager:
        return ManagerRepository(self.session).create_manager(manager)

    def update_manager(self, manager: Manager) -> Manager:
        return ManagerRepository(self.session).update_manager(manager)

    def delete_manager(self, manager_id: int) -> bool:
        return ManagerRepository(self.session).delete_manager(manager_id)

    def create_commercial(self, commercial: Commercial) -> Commercial:
        return CommercialRepository(self.session).create_commercial(commercial)

    def update_commercial(self, commercial: Commercial) -> Commercial:
        return CommercialRepository(self.session).update_commercial(commercial)

    def delete_commercial(self, commercial_id: int) -> bool:
        return CommercialRepository(self.session).delete_commercial(commercial_id)

    def create_support(self, support: Support) -> Support:
        return SupportRepository(self.session).create_support(support)

    def update_support(self, support: Support) -> Support:
        return SupportRepository(self.session).update_support(support)

    def delete_support(self, support_id: int) -> bool:
        return SupportRepository(self.session).delete_support(support_id)

    def create_contract(self, contract: Contract) -> Contract:
        return ContractRepository(self.session).create_contract(contract)

    def update_contract(self, contract: Contract) -> Contract:
        return ContractRepository(self.session).update_contract(contract)

    def get_events_with_no_assigned_support(self, event: Event) -> List[Event]:
        return EventRepository(self.session).get_events_with_no_assigned_support(event)

    def update_event(self, event: Event) -> Event:
        return EventRepository(self.session).update_event(event)

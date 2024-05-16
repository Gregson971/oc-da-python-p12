from typing import List

from src.domain.entities.client import Client
from src.domain.entities.contract import Contract
from src.domain.entities.event import Event

from src.domain.permissions.collaborator_permission import require_permission

from src.infrastructure.repository.client_repository import ClientRepository
from src.infrastructure.repository.contract_repository import ContractRepository
from src.infrastructure.repository.event_repository import EventRepository


class ManageSupport:

    def get_clients(self) -> List[Client]:
        return ClientRepository().get_clients()

    def get_contracts(self) -> List[Contract]:
        return ContractRepository().get_contracts()

    def get_events(self) -> List[Event]:
        return EventRepository().get_events()

    @require_permission('filter_events')
    def get_assigned_events(self) -> List[Event]:
        return EventRepository().get_assigned_events()

    @require_permission('update_event')
    def update_event(self, event_id: int, event: Event) -> Event:
        return EventRepository().update_event(event_id, event)

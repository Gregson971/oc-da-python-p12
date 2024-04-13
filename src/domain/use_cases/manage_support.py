from typing import List

from src.domain.entities.client import Client
from src.domain.entities.contract import Contract
from src.domain.entities.event import Event


class ManageSupport:
    support = None

    def __init__(self, support):
        self.support = support

    def get_clients(self) -> List[Client]:
        pass

    def get_contrats(self) -> List[Contract]:
        pass

    def get_events(self) -> List[Event]:
        pass

    def filter_events(self, filters: dict) -> List[Event]:
        pass

    def update_event(self, event: Event) -> Event:
        pass

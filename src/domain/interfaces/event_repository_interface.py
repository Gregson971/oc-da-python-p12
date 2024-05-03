from abc import ABC, abstractmethod
from typing import List

from src.domain.entities.event import Event


class EventRepositoryInterface(ABC):
    @abstractmethod
    def create_event(self, event: Event) -> Event:
        pass

    @abstractmethod
    def get_event(self, event_id: int) -> Event:
        pass

    @abstractmethod
    def get_events(self) -> List[Event]:
        pass

    @abstractmethod
    def update_event(self, event: Event) -> Event:
        pass

    @abstractmethod
    def delete_event(self, event_id: int) -> bool:
        pass

    @abstractmethod
    def get_events_with_no_assigned_support(self) -> List[Event]:
        pass

    @abstractmethod
    def get_assigned_events(self, support_id: int) -> List[Event]:
        pass

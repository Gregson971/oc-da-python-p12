from abc import ABC, abstractmethod
from typing import List

from src.domain.entities.event import Event


class EventRepositoryInterface(ABC):
    @abstractmethod
    def create_event(self, event: Event) -> Event:
        """
        Creates a new event

        Args:
            event (Event): An event object with the event information

        Returns:
            Event: The created event object

        Raises:
            Exception: If an error occurs while creating the event
        """
        pass

    @abstractmethod
    def get_event(self, event_id: int) -> Event:
        """
        Retrieves an event by its id

        Args:
            event_id (int): The event id

        Returns:
            Event: The event object

        Raises:
            Exception: If an error occurs while getting the event
        """
        pass

    @abstractmethod
    def get_events(self) -> List[Event]:
        """
        Retrieves all events

        Returns:
            List[Event]: A list of event objects

        Raises:
            Exception: If an error occurs while getting the events
        """
        pass

    @abstractmethod
    def update_event(self, event_id: int, event: Event) -> Event:
        """
        Updates an event

        Args:
            event_id (int): The event id
            event (Event): An event object with the updated event information

        Returns:
            Event: The updated event object
        """
        pass

    @abstractmethod
    def delete_event(self, event_id: int) -> bool:
        """
        Deletes an event

        Args:
            event_id (int): The event id

        Returns:
            bool: True if the event was deleted successfully, otherwise False

        Raises:
            Exception: If an error occurs while deleting the event
        """
        pass

    @abstractmethod
    def get_events_with_no_assigned_support(self) -> List[Event]:
        """
        Retrieves all events with no assigned support

        Returns:
            List[Event]: A list of event objects

        Raises:
            Exception: If an error occurs while getting the events
        """
        pass

    @abstractmethod
    def get_assigned_events(self, support_id: int) -> List[Event]:
        """
        Retrieves all events assigned to a support

        Args:
            support_id (int): The support id

        Returns:
            List[Event]: A list of event objects

        Raises:
            Exception: If an error occurs while getting the events
        """
        pass

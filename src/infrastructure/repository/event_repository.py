from kink import di
from sentry_sdk import capture_event, capture_exception

from sqlalchemy.exc import IntegrityError

from src.domain.interfaces.event_repository_interface import EventRepositoryInterface
from src.infrastructure.repository.abstract_repository import AbstractRepository
from src.domain.entities.event import Event


class EventRepository(EventRepositoryInterface, AbstractRepository):

    def create_event(self, event: Event) -> None:
        try:
            event_entity = Event(
                name=event.name,
                started_date=event.started_date,
                ended_date=event.ended_date,
                location=event.location,
                attendees=event.attendees,
                notes=event.notes,
                support_contact_id=event.support_contact_id,
                contract_id=event.contract_id,
            )

            self.add(event_entity)
            capture_event({"message": f"Event {event.name} created", "level": "info"})

        except IntegrityError as e:
            capture_exception(e)
            raise Exception("Event already exists")

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while creating the event: {e}")

    def get_event(self, event_id: int) -> Event:
        try:
            event = self.get(Event, event_id)

            if event is None:
                raise Exception("Event not found")

            capture_event(
                {
                    "message": f"Event {event.name} retrieved successfully",
                    "level": "info",
                }
            )
            return event

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while getting the event: {e}")

    def get_events(self) -> list[Event]:
        try:
            events = self.get_all(Event)

            if events is None:
                raise Exception("Events not found")

            capture_event({"message": "Events retrieved successfully", "level": "info"})
            return events

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while getting the events: {e}")

    def update_event(self, event) -> None:
        try:
            event_entity = self.get_event(event.id)

            event_entity.name = event.name
            event_entity.started_at = event.started_at
            event_entity.ended_at = event.ended_at
            event_entity.location = event.location
            event_entity.attendes = event.attendes
            event_entity.notes = event.notes

            self.update()
            capture_event({"message": f"Event {event.name} updated successfully", "level": "info"})

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while updating the event: {e}")

    def delete_event(self, event_id: int) -> None:
        try:
            event = self.get_event(event_id)

            self.delete(event)
            capture_event({"message": f"Event {event.name} deleted", "level": "info"})

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while deleting the event: {e}")

    def get_assigned_events(self) -> list[Event]:
        try:
            payload = di["token_payload"]
            support_id = payload["id"]
            events = self.session.query(Event).filter(Event.support_contact_id == support_id).all()

            if events is None:
                raise Exception("Events not found")

            capture_event({"message": "Events retrieved successfully", "level": "info"})
            return events

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while getting the events: {e}")

    def get_events_with_no_assigned_support(self) -> list[Event]:
        try:
            events = self.session.query(Event).filter(Event.support_contact_id is None).all()

            if events is None:
                raise Exception("Events not found")

            capture_event({"message": "Events retrieved successfully", "level": "info"})
            return events

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while getting the events: {e}")

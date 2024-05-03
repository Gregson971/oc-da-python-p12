from sentry_sdk import capture_event, capture_exception

from src.domain.interfaces.event_repository_interface import EventRepositoryInterface
from src.domain.entities.event import Event

from src.infrastructure.services.get_token_payload import get_token_payload


class EventRepository(EventRepositoryInterface):
    def __init__(self, session):
        self.session = session

    def create_event(self, event: Event) -> None:
        try:
            event_entity = Event(
                name=event.name,
                started_at=event.started_at,
                ended_at=event.ended_at,
                location=event.location,
                attendes=event.attendes,
                notes=event.notes,
            )

            self.session.add(event_entity)
            self.session.commit()
            capture_event({"message": f"Event {event.name} created", "level": "info"})

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while creating the event: {e}")

    def get_event(self, event_id: int) -> Event:
        try:
            event = self.session.query(Event).get(event_id)

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
            events = self.session.query(Event).all()

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

            self.session.commit()
            capture_event({"message": f"Event {event.name} updated successfully", "level": "info"})

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while updating the event: {e}")

    def delete_event(self, event_id: int) -> None:
        try:
            event = self.get_event(event_id)

            self.session.delete(event)
            self.session.commit()
            capture_event({"message": f"Event {event.name} deleted", "level": "info"})

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while deleting the event: {e}")

    def get_assigned_events(self) -> list[Event]:
        try:
            payload = get_token_payload()
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

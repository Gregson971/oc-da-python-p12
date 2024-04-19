from src.domain.interfaces.event_repository_interface import EventRepositoryInterface
from src.domain.entities.event import Event


class EventRepository(EventRepositoryInterface):
    def __init__(self, session):
        self.session = session

    def create_event(self, event: Event) -> None:
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

    def get_event(self, event_id: int) -> Event:
        event = self.session.query(Event).get(event_id)

        if event is None:
            raise Exception("Event not found")

        return event

    def get_events(self) -> list[Event]:
        events = self.session.query(Event).all()

        if events is None:
            raise Exception("Events not found")

        return events

    def update_event(self, event) -> None:
        event_entity = self.get_event(event.id)

        event_entity.name = event.name
        event_entity.started_at = event.started_at
        event_entity.ended_at = event.ended_at
        event_entity.location = event.location
        event_entity.attendes = event.attendes
        event_entity.notes = event.notes

        self.session.commit()

    def delete_event(self, event_id: int) -> None:
        event = self.get_event(event_id)

        self.session.delete(event)
        self.session.commit()

    def get_assigned_events(self, support_id: int) -> list[Event]:
        events = self.session.query(Event).filter(Event.support_contact_id == support_id).all()

        if events is None:
            raise Exception("Events not found")

        return events

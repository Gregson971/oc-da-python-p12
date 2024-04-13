from src.domain.interfaces.event_repository_interface import EventRepositoryInterface


class EventRepository(EventRepositoryInterface):
    def __init__(self, session):
        self.session = session

    def create_event(self, event):
        pass

    def get_event(self, event_id: int):
        pass

    def get_events(self):
        pass

    def update_event(self, event):
        pass

    def delete_event(self, event_id: int):
        pass

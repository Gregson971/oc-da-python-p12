from sentry_sdk import capture_event, capture_exception

from src.domain.interfaces.collaborator_repository_interface import CollaboratorRepositoryInterface
from src.infrastructure.repository.abstract_repository import AbstractRepository
from src.domain.entities.collaborator import Collaborator


class CollaboratorRepository(CollaboratorRepositoryInterface, AbstractRepository):

    def login(self, email: str, password) -> Collaborator:
        try:
            collaborator = (
                self.session.query(Collaborator)
                .filter(Collaborator.email == email and Collaborator.password == password)
                .first()
            )

            capture_event(
                {
                    "message": f"Collaborator {collaborator.first_name} {collaborator.last_name} logged in",
                    "level": "info",
                }
            )

        except Exception as e:
            capture_exception(e)
            raise Exception(f"Collaborator not found, error: {e}")

        return collaborator

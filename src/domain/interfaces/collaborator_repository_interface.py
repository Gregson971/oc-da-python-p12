from abc import ABC, abstractmethod

from src.domain.entities.collaborator import Collaborator


class CollaboratorRepositoryInterface(ABC):
    @abstractmethod
    def register_collaborator(self, collaborator: Collaborator) -> Collaborator:
        pass

    @abstractmethod
    def login(self, email: str, password) -> Collaborator:
        pass

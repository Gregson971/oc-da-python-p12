from abc import ABC, abstractmethod

from src.domain.entities.collaborator import Collaborator


class CollaboratorRepositoryInterface(ABC):
    @abstractmethod
    def login(self, email: str, password) -> Collaborator:
        """
        Login a collaborator

        Args:
            email (str): The collaborator email
            password (str): The collaborator password

        Returns:
            Collaborator: The collaborator object

        Raises:
            Exception: If an error occurs while logging in the collaborator
        """
        pass

from abc import ABC, abstractmethod
from typing import List

from src.domain.entities.collaborator import Commercial


class CommercialRepositoryInterface(ABC):
    @abstractmethod
    def create_commercial(self, commercial: Commercial) -> Commercial:
        """
        Creates a new commercial

        Args:
            commercial (Commercial): A commercial object with the commercial information

        Returns:
            Commercial: The created commercial object

        Raises:
            IntegrityError: If the email already exists
            Exception: If an error occurs while creating the commercial
        """
        pass

    @abstractmethod
    def get_commercial(self, commercial_id: int) -> Commercial:
        """
        Retrieves a commercial by its id

        Args:
            commercial_id (int): The commercial id

        Returns:
            Commercial: The commercial object

        Raises:
            Exception: If an error occurs while getting the commercial
        """
        pass

    @abstractmethod
    def get_commercials(self) -> List[Commercial]:
        """
        Retrieves all commercials

        Returns:
            List[Commercial]: A list of commercial objects

        Raises:
            Exception: If an error occurs while getting the commercials
        """
        pass

    @abstractmethod
    def update_commercial(self, commercial_id: int, commercial: Commercial) -> Commercial:
        """
        Updates a commercial

        Args:
            commercial_id (int): The commercial id
            commercial (Commercial): A commercial object with the updated commercial information

        Returns:
            Commercial: The updated commercial object

        Raises:
            Exception: If an error occurs while updating the commercial
        """
        pass

    @abstractmethod
    def delete_commercial(self, commercial_id: int) -> bool:
        """
        Deletes a commercial

        Args:
            commercial_id (int): The commercial id

        Returns:
            bool: True if the commercial was deleted, False otherwise

        Raises:
            Exception: If an error occurs while deleting the commercial
        """
        pass

from abc import ABC, abstractmethod
from typing import List

from src.domain.entities.collaborator import Support


class SupportRepositoryInterface(ABC):
    @abstractmethod
    def create_support(self, support: Support) -> Support:
        """
        Creates a new support

        Args:
            support (Support): A support object with the support information

        Returns:
            Support: The created support object

        Raises:
            IntegrityError: If the email already exists
            Exception: If an error occurs while creating the support
        """
        pass

    @abstractmethod
    def get_support(self, support_id: int) -> Support:
        """
        Retrieves a support by its id

        Args:
            support_id (int): The support id

        Returns:
            Support: The support object

        Raises:
            Exception: If an error occurs while getting the support
        """
        pass

    @abstractmethod
    def get_supports(self) -> List[Support]:
        """
        Retrieves all supports

        Returns:
            List[Support]: A list of support objects

        Raises:
            Exception: If an error occurs while getting the supports
        """
        pass

    @abstractmethod
    def update_support(self, support_id: int, support: Support) -> Support:
        """
        Updates a support

        Args:
            support_id (int): The support id
            support (Support): A support object with the updated support information

        Returns:
            Support: The updated support object

        Raises:
            Exception: If an error occurs while updating the support
        """
        pass

    @abstractmethod
    def delete_support(self, support_id: int) -> bool:
        """
        Deletes a support

        Args:
            support_id (int): The support id

        Returns:
            bool: True if the support was deleted, False otherwise
        """
        pass

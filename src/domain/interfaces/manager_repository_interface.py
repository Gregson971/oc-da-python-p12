from abc import ABC, abstractmethod
from typing import List

from src.domain.entities.collaborator import Manager


class ManagerRepositoryInterface(ABC):
    @abstractmethod
    def create_manager(self, manager: Manager) -> Manager:
        """
        Creates a new manager

        Args:
            manager (Manager): A manager object with the manager information

        Returns:
            Manager: The created manager object

        Raises:
            IntegrityError: If the email already exists
            Exception: If an error occurs while creating the manager
        """
        pass

    @abstractmethod
    def get_manager(self, manager_id: int) -> Manager:
        """
        Retrieves a manager by its id

        Args:
            manager_id (int): The manager id

        Returns:
            Manager: The manager object

        Raises:
            Exception: If an error occurs while getting the manager
        """
        pass

    @abstractmethod
    def get_managers(self) -> List[Manager]:
        """
        Retrieves all managers

        Returns:
            List[Manager]: A list of manager objects

        Raises:
            Exception: If an error occurs while getting the managers
        """
        pass

    @abstractmethod
    def update_manager(self, manager: Manager) -> Manager:
        """
        Updates a manager

        Args:
            manager (Manager): A manager object with the updated manager information

        Returns:
            Manager: The updated manager object

        Raises:
            Exception: If an error occurs while updating the manager
        """
        pass

    @abstractmethod
    def delete_manager(self, manager_id: int) -> bool:
        """
        Deletes a manager

        Args:
            manager_id (int): The manager id

        Returns:
            bool: True if the manager was deleted, False otherwise

        Raises:
            Exception: If an error occurs while deleting the manager
        """
        pass

from abc import ABC, abstractmethod
from typing import List

from src.domain.entities.client import Client


class ClientRepositoryInterface(ABC):
    @abstractmethod
    def create_client(self, client: Client) -> Client:
        """
        Creates a new client

        Args:
            client (Client): A client object with the client information

        Returns:
            Client: The created client object

        Raises:
            Exception: If an error occurs while creating the client
        """
        pass

    @abstractmethod
    def get_client(self, client_id: int) -> Client:
        """
        Retrieves a client by its id

        Args:
            client_id (int): The client id

        Returns:
            Client: The client object

        Raises:
            Exception: If an error occurs while getting the client
        """
        pass

    @abstractmethod
    def get_clients(self) -> List[Client]:
        """
        Retrieves all clients

        Returns:
            List[Client]: A list of client objects

        Raises:
            Exception: If an error occurs while getting the clients
        """
        pass

    @abstractmethod
    def update_client(self, client_id: int, client: Client) -> Client:
        """
        Updates a client

        Args:
            client_id (int): The client id
            client (Client): A client object with the updated client information

        Returns:
            Client: The updated client object

        Raises:
            Exception: If an error occurs while updating the client
        """
        pass

    @abstractmethod
    def delete_client(self, client_id: int) -> bool:
        """
        Deletes a client by its id

        Args:
            client_id (int): The client id

        Returns:
            bool: True if the client was deleted, False otherwise

        Raises:
            Exception: If an error occurs while deleting the client
        """
        pass

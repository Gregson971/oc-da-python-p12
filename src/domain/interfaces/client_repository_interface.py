from abc import ABC, abstractmethod
from typing import List

from src.domain.entities.client import Client


class ClientRepositoryInterface(ABC):
    @abstractmethod
    def create_client(self, client: Client) -> Client:
        pass

    @abstractmethod
    def get_client(self, client_id: int) -> Client:
        pass

    @abstractmethod
    def get_clients(self) -> List[Client]:
        pass

    @abstractmethod
    def update_client(self, client: Client) -> Client:
        pass

    @abstractmethod
    def delete_client(self, client_id: int) -> bool:
        pass

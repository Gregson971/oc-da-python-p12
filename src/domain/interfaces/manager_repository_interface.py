from abc import ABC, abstractmethod
from typing import List

from src.domain.entities.collaborator import Manager


class ManagerRepositoryInterface(ABC):
    @abstractmethod
    def create_manager(self, manager: Manager) -> Manager:
        pass

    @abstractmethod
    def get_manager(self, manager_id: int) -> Manager:
        pass

    @abstractmethod
    def get_managers(self) -> List[Manager]:
        pass

    @abstractmethod
    def update_manager(self, manager: Manager) -> Manager:
        pass

    @abstractmethod
    def delete_manager(self, manager_id: int) -> bool:
        pass

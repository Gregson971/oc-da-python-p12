from abc import ABC, abstractmethod
from typing import List

from src.domain.entities.collaborator import Support


class SupportRepositoryInterface(ABC):
    @abstractmethod
    def create_support(self, support: Support) -> Support:
        pass

    @abstractmethod
    def get_support(self, support_id: int) -> Support:
        pass

    @abstractmethod
    def get_supports(self) -> List[Support]:
        pass

    @abstractmethod
    def update_support(self, support: Support) -> Support:
        pass

    @abstractmethod
    def delete_support(self, support_id: int) -> bool:
        pass

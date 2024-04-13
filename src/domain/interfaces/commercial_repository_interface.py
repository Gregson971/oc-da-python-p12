from abc import ABC, abstractmethod
from typing import List

from src.domain.entities.collaborator import Commercial


class CommercialRepositoryInterface(ABC):
    @abstractmethod
    def create_commercial(self, commercial: Commercial) -> Commercial:
        pass

    @abstractmethod
    def get_commercial(self, commercial_id: int) -> Commercial:
        pass

    @abstractmethod
    def get_commercials(self) -> List[Commercial]:
        pass

    @abstractmethod
    def update_commercial(self, commercial: Commercial) -> Commercial:
        pass

    @abstractmethod
    def delete_commercial(self, commercial_id: int) -> bool:
        pass

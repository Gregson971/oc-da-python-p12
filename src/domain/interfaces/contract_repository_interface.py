from abc import ABC, abstractmethod
from typing import List

from src.domain.entities.contract import Contract


class ContractRepositoryInterface(ABC):
    @abstractmethod
    def create_contract(self, contract: Contract) -> Contract:
        pass

    @abstractmethod
    def get_contract(self, contract_id: int) -> Contract:
        pass

    @abstractmethod
    def get_contracts(self) -> List[Contract]:
        pass

    @abstractmethod
    def update_contract(self, contract: Contract) -> Contract:
        pass

    @abstractmethod
    def delete_contract(self, contract_id: int) -> bool:
        pass

    @abstractmethod
    def get_unsigned_contracts(self) -> List[Contract]:
        pass

    @abstractmethod
    def get_unpaid_contracts(self) -> List[Contract]:
        pass

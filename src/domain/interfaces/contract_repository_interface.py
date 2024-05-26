from abc import ABC, abstractmethod
from typing import List

from src.domain.entities.contract import Contract


class ContractRepositoryInterface(ABC):
    @abstractmethod
    def create_contract(self, contract: Contract) -> Contract:
        """
        Creates a new contract

        Args:
            contract (Contract): A contract object with the contract information

        Returns:
            Contract: The created contract object

        Raises:
            Exception: If an error occurs while creating the contract
        """
        pass

    @abstractmethod
    def get_contract(self, contract_id: int) -> Contract:
        """
        Retrieves a contract by its id

        Args:
            contract_id (int): The contract id

        Returns:
            Contract: The contract object

        Raises:
            Exception: If an error occurs while getting the contract
        """
        pass

    @abstractmethod
    def get_contracts(self) -> List[Contract]:
        """
        Retrieves all contracts

        Returns:
            List[Contract]: A list of contract objects

        Raises:
            Exception: If an error occurs while getting the contracts
        """
        pass

    @abstractmethod
    def update_contract(self, contract_id: int, contract: Contract) -> Contract:
        """
        Updates a contract

        Args:
            contract_id (int): The contract id
            contract (Contract): A contract object with the updated contract information

        Returns:
            Contract: The updated contract object

        Raises:
            Exception: If an error occurs while updating the contract
        """
        pass

    @abstractmethod
    def delete_contract(self, contract_id: int) -> bool:
        """
        Deletes a contract

        Args:
            contract_id (int): The contract id

        Returns:
            bool: True if the contract was deleted, False otherwise

        Raises:
            Exception: If an error occurs while deleting the contract
        """
        pass

    @abstractmethod
    def get_unsigned_contracts(self) -> List[Contract]:
        """
        Retrieves all unsigned contracts

        Returns:
            List[Contract]: A list of unsigned contract objects

        Raises:
            Exception: If an error occurs while getting the unsigned contracts
        """
        pass

    @abstractmethod
    def get_unpaid_contracts(self) -> List[Contract]:
        """
        Retrieves all unpaid contracts

        Returns:
            List[Contract]: A list of unpaid contract objects

        Raises:
            Exception: If an error occurs while getting the unpaid contracts
        """
        pass

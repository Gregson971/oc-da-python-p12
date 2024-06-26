from sentry_sdk import capture_event, capture_exception

from sqlalchemy.exc import IntegrityError

from src.domain.interfaces.contract_repository_interface import ContractRepositoryInterface
from src.infrastructure.repository.abstract_repository import AbstractRepository
from src.domain.entities.contract import Contract


class ContractRepository(ContractRepositoryInterface, AbstractRepository):

    def create_contract(self, contract: Contract) -> None:
        try:
            contract_entity = Contract(
                total_amount=contract.total_amount,
                remaining_amount=contract.remaining_amount,
                status=contract.status,
                client_id=contract.client_id,
                support_id=contract.support_id,
            )

            self.add(contract_entity)
            capture_event({"message": "Contract created sucessfully", "level": "info"})

        except IntegrityError as e:
            capture_exception(e)
            raise Exception("Contract already exists for this client")

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while creating the contract: {e}")

    def get_contract(self, contract_id: int) -> Contract:
        try:
            contract = self.get(Contract, contract_id)

            if contract is None:
                raise Exception("Contract not found")

            capture_event(
                {
                    "message": f"Contract {contract.id} retrieved successfully",
                    "level": "info",
                }
            )
            return contract

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while getting the contract: {e}")

    def get_contracts(self) -> list[Contract]:
        try:
            contracts = self.get_all(Contract)

            if contracts is None:
                raise Exception("Contracts not found")

            capture_event({"message": "Contracts retrieved successfully", "level": "info"})
            return contracts

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while getting the contracts: {e}")

    def update_contract(self, contract_id: int, contract: Contract) -> None:
        try:
            contract_entity = self.get_contract(contract_id)

            contract_entity.total_amount = contract.total_amount
            contract_entity.remaining_amount = contract.remaining_amount
            contract_entity.status = contract.status

            self.update()
            capture_event({"message": f"Contract {contract_id} updated successfully", "level": "info"})

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while updating the contract: {e}")

    def delete_contract(self, contract_id: int) -> None:
        try:
            contract = self.get_contract(contract_id)

            self.delete(contract)
            capture_event({"message": f"Contract {contract_id} deleted", "level": "info"})

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while deleting the contract: {e}")

    def get_unsigned_contracts(self) -> list[Contract]:
        try:
            contracts = self.session.query(Contract).filter(Contract.status == "not-signed").all()

            if contracts is None:
                raise Exception("Contracts not found")

            capture_event({"message": "Unsigned contracts retrieved successfully", "level": "info"})
            return contracts

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while getting the unsigned contracts: {e}")

    def get_unpaid_contracts(self) -> list[Contract]:
        try:
            contracts = self.session.query(Contract).filter(Contract.remaining_amount > 0).all()

            if contracts is None:
                raise Exception("Contracts not found")

            capture_event({"message": "Unpaid contracts retrieved successfully", "level": "info"})
            return contracts

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while getting the unpaid contracts: {e}")

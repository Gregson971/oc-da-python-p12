from src.domain.interfaces.contract_repository_interface import ContractRepositoryInterface
from src.domain.entities.contract import Contract


class ContractRepository(ContractRepositoryInterface):
    def __init__(self, session):
        self.session = session

    def create_contract(self, contract: Contract) -> None:
        contract_entity = Contract(
            total_amount=contract.total_amount,
            remaining_amount=contract.remaining_amount,
            status=contract.status,
        )

        self.session.add(contract_entity)
        self.session.commit()

    def get_contract(self, contract_id: int) -> Contract:
        contract = self.session.query(Contract).get(contract_id)

        if contract is None:
            raise Exception("Contract not found")

        return contract

    def get_contracts(self) -> list[Contract]:
        contracts = self.session.query(Contract).all()

        if contracts is None:
            raise Exception("Contracts not found")

        return contracts

    def update_contract(self, contract: Contract) -> None:
        contract_entity = self.get_contract(contract.id)

        contract_entity.total_amount = contract.total_amount
        contract_entity.remaining_amount = contract.remaining_amount
        contract_entity.status = contract.status

        self.session.commit()

    def delete_contract(self, contract_id: int) -> None:
        contract = self.get_contract(contract_id)

        self.session.delete(contract)
        self.session.commit()

    def get_unsigned_contracts(self) -> list[Contract]:
        contracts = self.session.query(Contract).filter(Contract.status == "not-signed").all()

        if contracts is None:
            raise Exception("Contracts not found")

        return contracts

    def get_unpaid_contracts(self) -> list[Contract]:
        contracts = self.session.query(Contract).filter(Contract.remaining_amount > 0).all()

        if contracts is None:
            raise Exception("Contracts not found")

        return contracts

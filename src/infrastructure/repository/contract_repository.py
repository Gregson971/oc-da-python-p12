from src.domain.interfaces.contract_repository_interface import ContractRepositoryInterface


class ContractRepository(ContractRepositoryInterface):
    def __init__(self, session):
        self.session = session

    def create_contract(self, contract):
        pass

    def get_contract(self, contract_id: int):
        pass

    def get_contracts(self):
        pass

    def update_contract(self, contract):
        pass

    def delete_contract(self, contract_id: int):
        pass

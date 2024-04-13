from src.domain.interfaces.client_repository_interface import ClientRepositoryInterface


class ClientRepository(ClientRepositoryInterface):
    def __init__(self, session):
        self.session = session

    def create_client(self, client):
        pass

    def get_client(self, client_id: int):
        pass

    def get_clients(self):
        pass

    def update_client(self, client):
        pass

    def delete_client(self, client_id: int):
        pass

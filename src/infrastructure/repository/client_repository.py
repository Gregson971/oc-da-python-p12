from src.domain.interfaces.client_repository_interface import ClientRepositoryInterface
from src.domain.entities.client import Client


class ClientRepository(ClientRepositoryInterface):
    def __init__(self, session):
        self.session = session

    def create_client(self, client: Client) -> None:
        client_entity = Client(
            information=client.information,
            first_name=client.first_name,
            last_name=client.last_name,
            email=client.email,
            phone_number=client.phone_number,
            company_name=client.company_name,
            commercial_id=client.commercial_id,
        )

        self.session.add(client_entity)
        self.session.commit()

    def get_client(self, client_id: int) -> Client:
        client = self.session.query(Client).get(client_id)

        if client is None:
            raise Exception("Client not found")

        return client

    def get_clients(self) -> list[Client]:
        clients = self.session.query(Client).all()

        if clients is None:
            raise Exception("Clients not found")

        return clients

    def update_client(self, client: Client) -> None:
        client_entity = self.get_client(client.id)

        client_entity.information = client.information
        client_entity.first_name = client.first_name
        client_entity.last_name = client.last_name
        client_entity.email = client.email
        client_entity.phone_number = client.phone_number
        client_entity.company_name = client.company_name

        self.session.commit()

    def delete_client(self, client_id: int) -> None:
        client = self.get_client(client_id)

        self.session.delete(client)
        self.session.commit()

from sentry_sdk import capture_event, capture_exception

from src.domain.interfaces.client_repository_interface import ClientRepositoryInterface
from src.domain.entities.client import Client


class ClientRepository(ClientRepositoryInterface):
    def __init__(self, session):
        self.session = session

    def create_client(self, client: Client) -> None:
        try:
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
            capture_event({"message": f"Client {client.first_name} {client.last_name} created", "level": "info"})

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while creating the client collaborator: {e}")

    def get_client(self, client_id: int) -> Client:
        try:
            client = self.session.query(Client).get(client_id)

            if client is None:
                raise Exception("Client not found")

            capture_event(
                {
                    "message": f"Client {client.first_name} {client.last_name} retrieved successfully",
                    "level": "info",
                }
            )
            return client

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while getting the client collaborator: {e}")

    def get_clients(self) -> list[Client]:
        try:
            clients = self.session.query(Client).all()

            if clients is None:
                raise Exception("Clients not found")

            capture_event({"message": "Clients retrieved successfully", "level": "info"})
            return clients

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while getting the client collaborator: {e}")

    def update_client(self, client: Client) -> None:
        try:
            client_entity = self.get_client(client.id)

            client_entity.information = client.information
            client_entity.first_name = client.first_name
            client_entity.last_name = client.last_name
            client_entity.email = client.email
            client_entity.phone_number = client.phone_number
            client_entity.company_name = client.company_name

            self.session.commit()
            capture_event(
                {"message": f"Client {client.first_name} {client.last_name} updated successfully", "level": "info"}
            )

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while updating the client collaborator: {e}")

    def delete_client(self, client_id: int) -> None:
        try:
            client = self.get_client(client_id)

            self.session.delete(client)
            self.session.commit()
            capture_event({"message": f"Client {client.first_name} {client.last_name} deleted", "level": "info"})

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while deleting the client collaborator: {e}")

from sentry_sdk import capture_event, capture_exception

from src.domain.interfaces.client_repository_interface import ClientRepositoryInterface
from src.infrastructure.repository.abstract_repository import AbstractRepository
from src.domain.entities.client import Client


class ClientRepository(ClientRepositoryInterface, AbstractRepository):

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

            self.add(client_entity)
            capture_event({"message": f"Client {client.first_name} {client.last_name} created", "level": "info"})

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while creating the client collaborator: {e}")

    def get_client(self, client_id: int) -> Client:
        try:
            client = self.get(Client, client_id)

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
            clients = self.get_all(Client)

            if clients is None:
                raise Exception("Clients not found")

            capture_event({"message": "Clients retrieved successfully", "level": "info"})
            return clients

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while getting the client collaborator: {e}")

    def update_client(self, client_id: int, client: Client) -> None:
        try:
            client_entity = self.get_client(client_id)

            client_entity.information = client.information
            client_entity.first_name = client.first_name
            client_entity.last_name = client.last_name
            client_entity.email = client.email
            client_entity.phone_number = client.phone_number
            client_entity.company_name = client.company_name

            self.update()
            capture_event(
                {"message": f"Client {client.first_name} {client.last_name} updated successfully", "level": "info"}
            )

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while updating the client collaborator: {e}")

    def delete_client(self, client_id: int) -> None:
        try:
            client = self.get_client(client_id)

            self.delete(client)
            capture_event({"message": f"Client {client.first_name} {client.last_name} deleted", "level": "info"})

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while deleting the client collaborator: {e}")

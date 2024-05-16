from sentry_sdk import capture_event, capture_exception
from sqlalchemy.exc import IntegrityError

from src.domain.interfaces.manager_repository_interface import ManagerRepositoryInterface
from src.infrastructure.repository.abstract_repository import AbstractRepository
from src.domain.entities.collaborator import Manager as ManagerEntity


class ManagerRepository(ManagerRepositoryInterface, AbstractRepository):

    def create_manager(self, manager: ManagerEntity) -> None:
        try:
            manager_entity = ManagerEntity(
                first_name=manager.first_name,
                last_name=manager.last_name,
                email=manager.email,
                password=manager.password,
                role='manager',
            )

            self.add(manager_entity)
            capture_event({"message": f"Manager {manager.first_name} {manager.last_name} registered", "level": "info"})

        except IntegrityError as e:
            capture_exception(e)
            raise Exception("Email already exists")
        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while creating the manager collaborator: {e}")

    def get_manager(self, manager_id: int) -> ManagerEntity:
        try:
            manager = self.get(ManagerEntity, manager_id)

            if manager is None:
                raise Exception("Manager not found")

            capture_event(
                {
                    "message": f"Manager {manager.first_name} {manager.last_name} retrieved successfully",
                    "level": "info",
                }
            )
            return manager

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while getting the manager collaborator: {e}")

    def get_managers(self) -> list[ManagerEntity]:
        try:
            managers = self.get_all(ManagerEntity)

            if managers is None:
                raise Exception("Managers not found")

            capture_event({"message": "Managers retrieved successfully", "level": "info"})
            return managers

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while getting the managers collaborator: {e}")

    def update_manager(self, manager_id, manager) -> None:
        try:
            manager_entity = self.get_manager(manager_id)

            manager_entity.first_name = manager.first_name
            manager_entity.last_name = manager.last_name
            manager_entity.email = manager.email
            manager_entity.password = manager.password

            self.update()

            capture_event(
                {"message": f"Manager {manager.first_name} {manager.last_name} updated successfully", "level": "info"}
            )

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while updating the manager collaborator: {e}")

    def delete_manager(self, manager_id: int) -> None:
        try:
            manager = self.get_manager(manager_id)

            self.delete(manager)

            capture_event(
                {"message": f"Manager {manager.first_name} {manager.last_name} deleted successfully", "level": "info"}
            )

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while deleting the manager collaborator: {e}")

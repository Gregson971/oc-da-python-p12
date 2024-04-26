from sentry_sdk import capture_exception
from sqlalchemy.exc import IntegrityError

from src.domain.interfaces.manager_repository_interface import ManagerRepositoryInterface
from src.domain.entities.collaborator import Manager as ManagerEntity


class ManagerRepository(ManagerRepositoryInterface):
    def __init__(self, session):
        self.session = session

    def create_manager(self, manager: ManagerEntity) -> None:
        try:
            manager_entity = ManagerEntity(
                first_name=manager.first_name,
                last_name=manager.last_name,
                email=manager.email,
                password=manager.password,
                role='manager',
            )

            self.session.add(manager_entity)
            self.session.commit()

        except IntegrityError as e:
            capture_exception(e)
            raise Exception("Email already exists")
        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while creating the manager collaborator: {e}")

    def get_manager(self, manager_id: int) -> ManagerEntity:
        manager = self.session.query(ManagerEntity).get(manager_id)

        if manager is None:
            raise Exception("Manager not found")

        return manager

    def get_managers(self) -> list[ManagerEntity]:
        managers = self.session.query(ManagerEntity).all()

        if managers is None:
            raise Exception("Managers not found")

        return managers

    def update_manager(self, manager) -> None:
        manager_entity = self.get_manager(manager.id)

        manager_entity.first_name = manager.first_name
        manager_entity.last_name = manager.last_name
        manager_entity.email = manager.email
        manager_entity.password = manager.password

        self.session.commit()

    def delete_manager(self, manager_id: int) -> None:
        manager = self.get_manager(manager_id)

        self.session.delete(manager)
        self.session.commit()

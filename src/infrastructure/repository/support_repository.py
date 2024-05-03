from sentry_sdk import capture_event, capture_exception
from sqlalchemy.exc import IntegrityError

from src.domain.interfaces.support_repository_interface import SupportRepositoryInterface
from src.domain.entities.collaborator import Support as SupportEntity


class SupportRepository(SupportRepositoryInterface):
    def __init__(self, session):
        self.session = session

    def create_support(self, support: SupportEntity) -> None:
        try:
            support_entity = SupportEntity(
                first_name=support.first_name,
                last_name=support.last_name,
                email=support.email,
                password=support.password,
                role='support',
            )

            self.session.add(support_entity)
            self.session.commit()

            capture_event({"message": f"Support {support.first_name} {support.last_name} registered", "level": "info"})

        except IntegrityError as e:
            capture_exception(e)
            raise Exception("Email already exists")
        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while creating the support collaborator: {e}")

    def get_support(self, support_id: int) -> SupportEntity:
        try:
            support = self.session.query(SupportEntity).get(support_id)

            if support is None:
                raise Exception("Support not found")

            capture_event(
                {
                    "message": f"Support {support.first_name} {support.last_name} retrieved successfully",
                    "level": "info",
                }
            )
            return support

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while getting the support collaborator: {e}")

    def get_supports(self) -> list[SupportEntity]:
        try:
            supports = self.session.query(SupportEntity).all()

            if supports is None:
                raise Exception("Supports not found")

            capture_event({"message": "Supports retrieved successfully", "level": "info"})
            return supports

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while getting the support collaborators: {e}")

    def update_support(self, support) -> None:
        try:
            support_entity = self.get_support(support.id)

            support_entity.first_name = support.first_name
            support_entity.last_name = support.last_name
            support_entity.email = support.email
            support_entity.password = support.password

            self.session.commit()
            capture_event(
                {
                    "message": f"Support {support.first_name} {support.last_name} updated successfully",
                    "level": "info",
                }
            )

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while updating the support collaborator: {e}")

    def delete_support(self, support_id: int) -> None:
        try:
            support = self.get_support(support_id)

            self.session.delete(support)
            self.session.commit()
            capture_event(
                {
                    "message": f"Support {support.first_name} {support.last_name} deleted successfully",
                    "level": "info",
                }
            )

        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while deleting the support collaborator: {e}")

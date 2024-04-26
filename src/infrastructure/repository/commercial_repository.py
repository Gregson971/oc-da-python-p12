from sentry_sdk import capture_exception
from sqlalchemy.exc import IntegrityError

from src.domain.interfaces.commercial_repository_interface import CommercialRepositoryInterface
from src.domain.entities.collaborator import Commercial as CommercialEntity


class CommercialRepository(CommercialRepositoryInterface):
    def __init__(self, session):
        self.session = session

    def create_commercial(self, commercial: CommercialEntity) -> None:
        try:
            commercial_entity = CommercialEntity(
                first_name=commercial.first_name,
                last_name=commercial.last_name,
                email=commercial.email,
                password=commercial.password,
                role='commercial',
            )

            self.session.add(commercial_entity)
            self.session.commit()

        except IntegrityError as e:
            capture_exception(e)
            raise Exception("Email already exists")
        except Exception as e:
            capture_exception(e)
            raise Exception(f"An error occurred while creating the commercial collaborator: {e}")

    def get_commercial(self, commercial_id: int) -> CommercialEntity:
        commercial = self.session.query(CommercialEntity).get(commercial_id)

        if commercial is None:
            raise Exception("Commercial not found")

        return commercial

    def get_commercials(self) -> list[CommercialEntity]:
        commercials = self.session.query(CommercialEntity).all()

        if commercials is None:
            raise Exception("Commercials not found")

        return commercials

    def update_commercial(self, commercial: CommercialEntity) -> None:
        commercial_entity = self.get_commercial(commercial.id)

        commercial_entity.first_name = commercial.first_name
        commercial_entity.last_name = commercial.last_name
        commercial_entity.email = commercial.email
        commercial_entity.password = commercial.password

        self.session.commit()

    def delete_commercial(self, commercial_id: int) -> None:
        commercial = self.get_commercial(commercial_id)

        self.session.delete(commercial)
        self.session.commit()

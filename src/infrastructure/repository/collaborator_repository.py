from src.domain.interfaces.collaborator_repository_interface import CollaboratorRepositoryInterface
from src.domain.entities.collaborator import Collaborator


class CollaboratorRepository(CollaboratorRepositoryInterface):
    def __init__(self, session):
        self.session = session

    def register_collaborator(self, collaborator: Collaborator) -> None:
        collaborator_entity = Collaborator(
            first_name=collaborator.first_name,
            last_name=collaborator.last_name,
            email=collaborator.email,
            password=collaborator.password,
            role=collaborator.role,
        )

        self.session.add(collaborator_entity)
        self.session.commit()

    def login(self, email: str, password) -> Collaborator:
        collaborator = (
            self.session.query(Collaborator)
            .filter(Collaborator.email == email and Collaborator.password == password)
            .first()
        )

        if collaborator is None:
            raise Exception("Collaborator not found")

        return collaborator

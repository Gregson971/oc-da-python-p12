import os
import jwt

from datetime import datetime, timedelta, timezone
from rich.console import Console
from dotenv import load_dotenv

from src.domain.entities.collaborator import Collaborator
from src.infrastructure.repository.collaborator_repository import CollaboratorRepository

console = Console()


class ManageCollaborator:
    def __init__(self, session):
        self.session = session

    def register_collaborator(self, collaborator: Collaborator) -> Collaborator:
        return CollaboratorRepository(self.session).register_collaborator(collaborator)

    def login(self, email: str, password) -> Collaborator:
        load_dotenv()

        secret_key = os.getenv("SECRET_KEY")
        token_delta = os.getenv("TOKEN_DELTA")
        token_delta = int(token_delta)

        collaborator = CollaboratorRepository(self.session).login(email, password)

        if collaborator:
            token = jwt.encode(
                {
                    "id": collaborator.id,
                    "email": collaborator.email,
                    "role": str(collaborator.role).lower(),
                    "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=token_delta),
                },
                secret_key,
                algorithm="HS256",
            )

            f = open(".token", "w")
            f.write(token)
            f.close()

            return token
        else:
            console.print("Collaborator not found", style="bold red")

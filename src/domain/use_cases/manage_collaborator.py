import jwt

from kink import di
from datetime import datetime, timedelta, timezone
from rich.console import Console

from src.infrastructure.repository.collaborator_repository import CollaboratorRepository

console = Console()


class ManageCollaborator:

    def login(self, email: str, password: str) -> str:
        """
        Login a collaborator

        Args:
            email (str): The collaborator email
            password (str): The collaborator password

        Returns:
            str: The token

        Raises:
            Exception: If an error occurs while logging in the collaborator
        """

        secret_key = di["secret_key"]
        token_delta = di["token_delta"]
        token_delta = int(token_delta)

        collaborator = CollaboratorRepository().login(email, password)

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

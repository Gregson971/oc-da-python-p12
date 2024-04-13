from sqlalchemy.orm import Session
from types import SimpleNamespace

from src.domain.use_cases.manage_manager import ManageManager


class Cli:
    def __init__(self, session: Session):
        self.session = session

    def run(self):
        print("Cli.run() executed")
        # Create a manager
        manager = ManageManager(self.session)
        manager.create_manager(
            SimpleNamespace(
                first_name="John",
                last_name="Doe",
                email="john@example.com",
                password="password",
                roles="manager",
            )
        )

        print("Cli.run() finished")

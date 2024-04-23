import getpass
import inquirer

from rich.console import Console
from types import SimpleNamespace

from src.domain.use_cases.manage_collaborator import ManageCollaborator

from src.infrastructure.services.database_connect import set_session
from src.infrastructure.services.get_token_payload import get_token_payload

from src.infrastructure.cli.manager_command import ManagerCommand
from src.infrastructure.cli.commercial_command import CommercialCommand
from src.infrastructure.cli.support_command import SupportCommand
from src.infrastructure.cli.admin_command import AdminCommand

console = Console()
session = set_session()


class MainMenu:

    def run(self):
        console.print("EpicEvents CRM", style="bold blue")
        console.print("Welcome to the EpicEvents CRM CLI\n", style="bold green")

        console.print("Main menu", style="bold blue")
        console.print("1. Login", style="bold green")
        console.print("2. Register", style="bold green")
        console.print("3. Show clients", style="bold green")
        console.print("4. Show contracts", style="bold green")
        console.print("5. Show events", style="bold green")
        console.print("6. Exit", style="bold green")

        option = int(input("Choose an option: "))

        if option == 1:
            self.login()
        elif option == 2:
            self.register()
        elif option == 3:
            self.get_clients()
        elif option == 4:
            self.get_contrats()
        elif option == 5:
            self.get_events()
        elif option == 6:
            self.exit()

    def login(self) -> None:
        """Login a collaborator."""

        email = input("Email: ")
        password = getpass.getpass("Password: ")

        collaborator = ManageCollaborator(session)
        collaborator.login(email, password)

        payload = get_token_payload()
        role = payload['role']

        console.print("Collaborator logged in successfully!", style="bold green")

        if role == 'manager':
            ManagerCommand().run()
        elif role == 'commercial':
            CommercialCommand().run()
        elif role == 'support':
            SupportCommand().run()
        elif role == 'admin':
            AdminCommand().run()

    def register(self) -> None:
        """Register a collaborator."""

        roles = [inquirer.List("role", message="Select a role", choices=["manager", "commercial", "support", "admin"])]

        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        role = inquirer.prompt(roles)["role"]
        password = getpass.getpass("Password: ")
        confirm_password = getpass.getpass("Confirm password: ")

        if password != confirm_password:
            console.print("Passwords do not match", style="bold red")
            return

        collaborator = ManageCollaborator(session)
        collaborator.register_collaborator(
            SimpleNamespace(
                first_name=first_name,
                last_name=last_name,
                email=email,
                role=role,
                password=password,
            )
        )

        console.print("Collaborator registered successfully!", style="bold green")

        if role == 'manager':
            ManagerCommand().run()
        elif role == 'commercial':
            CommercialCommand().run()
        elif role == 'support':
            SupportCommand().run()
        elif role == 'admin':
            AdminCommand().run()

    def get_clients(self):
        """Show clients."""
        pass

    def get_contrats(self):
        """Show contracts."""
        pass

    def get_events(self):
        """Show events."""
        pass

    def exit(self) -> None:
        console.print("Exiting...", style="bold blue")
        exit()

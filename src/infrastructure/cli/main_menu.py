import getpass

from kink import di
from rich.console import Console

from src.domain.use_cases.manage_collaborator import ManageCollaborator

from src.infrastructure.cli.manager_command import ManagerCommand
from src.infrastructure.cli.commercial_command import CommercialCommand
from src.infrastructure.cli.support_command import SupportCommand

console = Console()


class MainMenu:

    def run(self):
        console.print("\nEpicEvents CRM", style="bold blue")
        console.print("Welcome to the EpicEvents CRM CLI\n", style="bold green")

        try:
            payload = di["token_payload"]
            role = payload['role']
        except Exception:
            role = None
            self.show_main_menu()

        if role:
            self.redirect_to_role_command(role)

    def show_main_menu(self):
        console.print("Main menu", style="bold blue")
        console.print("1. Login", style="bold green")
        console.print("2. Exit", style="bold green")

        option = int(input("Choose an option: "))

        if option == 1:
            self.login()
        elif option == 2:
            self.exit()

    def login(self) -> None:
        """Login a collaborator."""

        email = input("Email: ")
        password = getpass.getpass("Password: ")

        collaborator = ManageCollaborator()
        collaborator.login(email, password)

        payload = di["token_payload"]
        role = payload['role']

        console.print("Collaborator logged in successfully!", style="bold green")

        self.redirect_to_role_command(role)

    def redirect_to_role_command(self, role: str) -> None:
        """Redirect to role command."""

        if role == 'manager':
            ManagerCommand().run()
        elif role == 'commercial':
            CommercialCommand().run()
        elif role == 'support':
            SupportCommand().run()

    def exit(self) -> None:
        console.print("Exiting...", style="bold blue")
        exit()

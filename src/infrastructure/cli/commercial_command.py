from rich.console import Console
from types import SimpleNamespace

from src.infrastructure.services.database_connect import set_session
from src.infrastructure.services.get_token_payload import get_token_payload
from src.infrastructure.services.remove_token import remove_token

from src.domain.use_cases.manage_commercial import ManageCommercial


console = Console()
session = set_session()
manage_commercial = ManageCommercial(session)


class CommercialCommand:

    def run(self):
        console.print("EpicEvents Commercial CRM", style="bold blue")
        console.print("Welcome to the EpicEvents CRM CLI\n", style="bold green")

        console.print("Main menu", style="bold blue")
        console.print("1. Create a client", style="bold green")
        console.print("2. Update a client", style="bold green")
        console.print("3. Update a contract", style="bold green")
        console.print("4. Show unsigned contracts", style="bold green")
        console.print("5. Show unpaid contracts", style="bold green")
        console.print("6. Create an event", style="bold green")
        console.print("7. Exit", style="bold green")
        console.print("8. Logout", style="bold green")

        option = int(input("Choose an option: "))

        if option == 1:
            self.create_client()
        elif option == 2:
            self.update_client()
        elif option == 3:
            self.update_contract()
        elif option == 4:
            self.get_unsigned_contracts()
        elif option == 5:
            self.get_unpaid_contracts()
        elif option == 6:
            self.create_event()
        elif option == 7:
            self.exit()
        elif option == 8:
            self.logout()

    def create_client(self):
        """Create a client."""
        payload = get_token_payload()

        information = input("Information: ")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        phone_number = input("Phone number: ")
        company_name = input("Company name: ")
        commercial_id = payload['id']

        manage_commercial.create_client(
            SimpleNamespace(
                information=information,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                company_name=company_name,
                commercial_id=commercial_id,
            )
        )

        console.print(f"Client {first_name} {last_name} created successfully!", style="bold green")
        self.run()

    def update_client(self):
        """Update a client."""

    def update_contract(self):
        """Update a contract."""
        pass

    def get_unsigned_contracts(self):
        """Show unsigned contracts."""
        pass

    def get_unpaid_contracts(self):
        """Show unpaid contracts."""
        pass

    def create_event(self):
        """Create an event."""
        pass

    def get_clients(self):
        """Show clients."""
        pass

    def get_contrats(self):
        """Show contracts."""
        pass

    def get_events(self):
        """Show events."""
        pass

    def logout(self):
        """Logout a collaborator."""
        remove_token()
        console.print("Collaborator logged out successfully!", style="bold green")
        self.exit()

    def exit(self) -> None:
        console.print("Exiting...", style="bold blue")
        exit()

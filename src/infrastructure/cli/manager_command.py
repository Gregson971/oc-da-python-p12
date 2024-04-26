import inquirer
import getpass

from rich.console import Console
from types import SimpleNamespace

from src.infrastructure.services.database_connect import set_session
from src.infrastructure.services.remove_token import remove_token

from src.domain.use_cases.manage_manager import ManageManager
from src.domain.use_cases.manage_collaborator import ManageCollaborator


console = Console()
session = set_session()
manageManager = ManageManager(session)


class ManagerCommand:

    def run(self):
        console.print("EpicEvents Manager CRM", style="bold blue")
        console.print("Welcome to the EpicEvents CRM CLI\n", style="bold green")

        console.print("Main menu", style="bold blue")
        console.print("1. Create a collaborator", style="bold green")
        console.print("2. Update manager", style="bold green")
        console.print("3. Delete manager", style="bold red")
        console.print("5. Update commercial", style="bold green")
        console.print("6. Delete commercial", style="bold red")
        console.print("8. Update support", style="bold green")
        console.print("9. Delete support", style="bold red")
        console.print("10. Create contract", style="bold green")
        console.print("11. Update contract", style="bold green")
        console.print("12. Show events with no assigned support", style="bold green")
        console.print("13. Update event", style="bold green")
        console.print("14. Exit", style="bold green")
        console.print("15. Logout", style="bold green")

        option = int(input("Choose an option: "))

        if option == 1:
            self.create_collaborator()
        elif option == 2:
            self.update_manager()
        elif option == 3:
            self.delete_manager()
        elif option == 4:
            self.update_commercial()
        elif option == 5:
            self.delete_commercial()
        elif option == 6:
            self.update_support()
        elif option == 7:
            self.delete_support()
        elif option == 8:
            self.create_contract()
        elif option == 9:
            self.update_contract()
        elif option == 10:
            self.get_events_with_no_assigned_support()
        elif option == 11:
            self.update_event()
        elif option == 12:
            self.exit()
        elif option == 13:
            self.logout()

    def get_collaborator_information(self):
        """Get collaborator information."""
        roles = [inquirer.List("role", message="Select a role", choices=["manager", "commercial", "support", "admin"])]

        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        role = inquirer.prompt(roles)["role"]
        password = getpass.getpass("Password: ")
        confirm_password = getpass.getpass("Confirm password: ")

        if password != confirm_password:
            console.print("Passwords do not match!", style="bold red")
            return

        return SimpleNamespace(
            first_name=first_name,
            last_name=last_name,
            email=email,
            role=role,
            password=password,
        )

    def create_collaborator(self):
        """Create collaborators."""
        collaborator_data = self.get_collaborator_information()

        collaborator = ManageCollaborator(session)
        collaborator.register_collaborator(collaborator_data)

        console.print(
            f"Collaborator: {collaborator_data.first_name} {collaborator_data.last_name} created successfully!",
            style="bold green",
        )

        self.run()

    def update_manager(self):
        """Update manager."""
        pass

    def delete_manager(self):
        """Delete manager."""
        pass

    def update_commercial(self):
        """Update commercial."""
        pass

    def delete_commercial(self):
        """Delete commercial."""
        pass

    def update_support(self):
        """Update support."""
        pass

    def delete_support(self):
        """Delete support."""
        pass

    def create_contract(self):
        """Create contract."""
        client_list = manageManager.get_clients()
        client_list = [(f"{client.first_name} {client.last_name}", client.id) for client in client_list]
        client_choices = [inquirer.List("client", message="Select a client", choices=client_list)]

        support_list = manageManager.get_supports()
        support_list = [(f"{support.first_name} {support.last_name}", support.id) for support in support_list]
        support_choices = [inquirer.List("support", message="Select a support", choices=support_list)]

        status_list = ["not-signed", "signed"]
        status_choices = [inquirer.List("status", message="Select a status", choices=status_list)]

        total_amount = float(input("Total amount: "))
        remaining_amount = float(input("Remaining amount: "))
        status = inquirer.prompt(status_choices)["status"]
        client_id = int(inquirer.prompt(client_choices)["client"])
        support_id = int(inquirer.prompt(support_choices)["support"])

        manageManager.create_contract(
            SimpleNamespace(
                total_amount=total_amount,
                remaining_amount=remaining_amount,
                status=status,
                client_id=client_id,
                support_id=support_id,
            )
        )

        self.run()

    def update_contract(self):
        """Update contract."""
        pass

    def get_events_with_no_assigned_support(self):
        """Get events with no assigned support."""
        pass

    def update_event(self):
        """Update event."""
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

    def exit(self):
        console.print("Exiting...", style="bold blue")
        exit()

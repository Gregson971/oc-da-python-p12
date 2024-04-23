from rich.console import Console
from types import SimpleNamespace

from src.infrastructure.services.database_connect import set_session

from src.domain.use_cases.manage_manager import ManageManager


console = Console()
session = set_session()
manageManager = ManageManager(session)


class ManagerCommand:

    def run(self):
        console.print("EpicEvents Manager CRM", style="bold blue")
        console.print("Welcome to the EpicEvents CRM CLI\n", style="bold green")

        console.print("Main menu", style="bold blue")
        console.print("1. Create manager", style="bold green")
        console.print("2. Update manager", style="bold green")
        console.print("3. Delete manager", style="bold red")
        console.print("4. Create commercial", style="bold green")
        console.print("5. Update commercial", style="bold green")
        console.print("6. Delete commercial", style="bold red")
        console.print("7. Create support", style="bold green")
        console.print("8. Update support", style="bold green")
        console.print("9. Delete support", style="bold red")
        console.print("10. Create contract", style="bold green")
        console.print("11. Update contract", style="bold green")
        console.print("12. Show events with no assigned support", style="bold green")
        console.print("13. Update event", style="bold green")
        console.print("14. Exit", style="bold green")

        option = int(input("Choose an option: "))

        if option == 1:
            self.create_manager()
        elif option == 2:
            self.update_manager()
        elif option == 3:
            self.delete_manager()
        elif option == 4:
            self.create_commercial()
        elif option == 5:
            self.update_commercial()
        elif option == 6:
            self.delete_commercial()
        elif option == 7:
            self.create_support()
        elif option == 8:
            self.update_support()
        elif option == 9:
            self.delete_support()
        elif option == 10:
            self.create_contract()
        elif option == 11:
            self.update_contract()
        elif option == 12:
            self.get_events_with_no_assigned_support()
        elif option == 13:
            self.update_event()
        elif option == 14:
            self.exit()

    def create_manager(self):
        """Create manager."""
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        password = input("Password: ")
        confirm_password = input("Confirm password: ")

        if password != confirm_password:
            console.print("Passwords do not match!", style="bold red")
            return

        manageManager.create_manager(
            SimpleNamespace(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )
        )
        console.print(f"Collaborator {first_name} {last_name} created successfully!", style="bold green")

    def update_manager(self):
        """Update manager."""
        pass

    def delete_manager(self):
        """Delete manager."""
        pass

    def create_commercial(self):
        """Create commercial."""
        pass

    def update_commercial(self):
        """Update commercial."""
        pass

    def delete_commercial(self):
        """Delete commercial."""
        pass

    def create_support(self):
        """Create support."""
        pass

    def update_support(self):
        """Update support."""
        pass

    def delete_support(self):
        """Delete support."""
        pass

    def create_contract(self):
        """Create contract."""
        pass

    def update_contract(self):
        """Update contract."""
        pass

    def get_events_with_no_assigned_support(self):
        """Get events with no assigned support."""
        pass

    def update_event(self):
        """Update event."""
        pass

    def exit(self):
        console.print("Exiting...", style="bold blue")
        exit()

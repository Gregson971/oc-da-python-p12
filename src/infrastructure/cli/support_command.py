from rich.console import Console

from src.infrastructure.services.remove_token import remove_token

console = Console()


class SupportCommand:

    def run(self):
        console.print("EpicEvents Support CRM", style="bold blue")
        console.print("Welcome to the EpicEvents CRM CLI\n", style="bold green")

        console.print("Main menu", style="bold blue")
        console.print("1. Show assigned events", style="bold green")
        console.print("2. Update event", style="bold green")
        console.print("3. Exit", style="bold green")
        console.print("4. Logout", style="bold green")

        option = int(input("Choose an option: "))

        if option == 1:
            self.get_assigned_events()
        elif option == 2:
            self.update_event()
        elif option == 3:
            self.exit()
        elif option == 4:
            self.logout()

    def get_assigned_events(self):
        """Show assigned events."""
        pass

    def update_event(self):
        """Update an event."""
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

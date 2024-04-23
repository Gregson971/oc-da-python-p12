from rich.console import Console

console = Console()


class SupportCommand:

    def run(self):
        console.print("EpicEvents Support CRM", style="bold blue")
        console.print("Welcome to the EpicEvents CRM CLI\n", style="bold green")

        console.print("Main menu", style="bold blue")
        console.print("1. Show assigned events", style="bold green")
        console.print("2. Update event", style="bold green")
        console.print("3. Exit", style="bold green")

    def get_assigned_events(self):
        """Show assigned events."""
        pass

    def update_event(self):
        """Update an event."""
        pass

    def exit(self) -> None:
        console.print("Exiting...", style="bold blue")
        exit()

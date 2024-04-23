from rich.console import Console

console = Console()


class AdminCommand:

    def run(self):
        console.print("EpicEvents Admin CRM", style="bold blue")
        console.print("Welcome to the EpicEvents CRM CLI\n", style="bold green")

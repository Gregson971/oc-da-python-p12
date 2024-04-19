# import jwt
import click
from rich.console import Console
from sqlalchemy.orm import Session

from types import SimpleNamespace

from src.domain.use_cases.manage_manager import ManageManager


console = Console()


class Cli:
    def __init__(self, session: Session):
        self.session = session

    @click.group()
    def run():
        """Run the CLI."""

        console.print("EpicEvents CRM", style="bold blue")
        console.print("Welcome to the EpicEvents CRM CLI", style="bold green")

    @run.command()
    @click.option("--first_name", "-fn", prompt="First name")
    @click.option("--last_name", "-ln", prompt="Last name")
    @click.option("--email", "-em", prompt="Email")
    @click.option("--password", "-pw", prompt="Password", hide_input=True, confirmation_prompt=True)
    @click.option(
        "--role", "-r", prompt="Role", type=click.Choice(["manager", "commercial", "support"], case_sensitive=True)
    )
    def create_collaborator(first_name: str, last_name: str, email: str, password: str, role: str) -> None:
        """As a manager, create a collaborator."""
        manager = ManageManager(self.session)
        manager.create_manager(
            SimpleNamespace(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                role=role,
            )
        )
        console.print(
            f"Collaborator {first_name} {last_name} created successfully with role {role}", style="bold green"
        )

    @run.command()
    def login():
        """Login a user."""

        print("Cli.login() executed")

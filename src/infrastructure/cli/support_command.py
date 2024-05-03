import inquirer

from rich.console import Console
from rich.table import Table
from types import SimpleNamespace

from src.infrastructure.services.database_connect import set_session
from src.infrastructure.services.remove_token import remove_token

from src.domain.use_cases.manage_support import ManageSupport

console = Console()
session = set_session()
manage_support = ManageSupport(session)


class SupportCommand:

    def run(self):
        console.print("\nEpicEvents Support CRM menu\n", style="bold blue")

        console.print("Main menu", style="bold blue")
        console.print("1. Show assigned events", style="bold green")
        console.print("2. Update event", style="bold green")
        console.print("3. Show clients", style="bold green")
        console.print("4. Show contracts", style="bold green")
        console.print("5. Show events", style="bold green")
        console.print("6. Exit", style="bold green")
        console.print("7. Logout", style="bold green")

        option_mapping = {
            1: self.get_assigned_events,
            2: self.update_event,
            3: self.get_clients,
            4: self.get_contratcs,
            5: self.get_events,
            6: self.exit,
            7: self.logout,
        }

        option = int(input("Choose an option: "))
        selected_method = option_mapping.get(option)

        if selected_method:
            selected_method()
        else:
            console.print("Invalid option selected.", style="bold red")

    def get_assigned_events(self):
        """Show assigned events."""

        assigned_events = manage_support.get_assigned_events()

        if not assigned_events:
            console.print("No assigned events", style="bold red")
            self.run()
        else:
            table = Table(title="Assigned events")
            table.add_column("Event ID")
            table.add_column("Event name")
            table.add_column("Event started date")
            table.add_column("Event ended date")
            table.add_column("Location")
            table.add_column("Attendees")
            table.add_column("Notes")
            table.add_column("Client")

            for event in assigned_events:
                table.add_row(
                    str(event.id),
                    event.name,
                    event.started_date,
                    event.ended_date,
                    event.location,
                    str(event.attendees),
                    event.notes,
                    event.client.first_name + " " + event.client.last_name,
                )

            console.print(table)
            self.run()

    def update_event(self):
        """Update an event."""

        event_list = manage_support.get_events()
        event_list = [(event.name, event.id) for event in event_list]
        event_choices = [inquirer.List("event", message="Select an event", choices=event_list)]

        event_id = int(inquirer.prompt(event_choices)["event"])
        event = manage_support.get_event(event_id)

        name = input(f"Name ({event.name}): ")
        location = input(f"Location ({event.location}): ")
        started_at = input(f"Started at ({event.started_at}): ")
        ended_at = input(f"Ended at ({event.ended_at}): ")
        attendees = input(f"Attendees ({event.attendees}): ")
        notes = input(f"Notes ({event.notes}): ")

        manage_support.update_event(
            SimpleNamespace(
                id=event_id,
                name=name,
                location=location,
                started_at=started_at,
                ended_at=ended_at,
                attendees=attendees,
                notes=notes,
            )
        )
        console.print("Event updated successfully!", style="bold green")
        self.run()

    def get_clients(self):
        """Show clients."""

        client_list = manage_support.get_clients()

        if not client_list:
            console.print("No clients found!", style="bold red")
            self.run()
        else:
            table = Table(title="Clients")
            table.add_column("First name", style="bold green")
            table.add_column("Last name", style="bold green")
            table.add_column("Email", style="bold green")
            table.add_column("Phone number", style="bold green")
            table.add_column("Company name", style="bold green")

            for client in client_list:
                table.add_row(
                    client.first_name, client.last_name, client.email, client.phone_number, client.company_name
                )

            console.print(table)
            self.run()

    def get_contratcs(self):
        """Show contracts."""

        contract_list = manage_support.get_contracts()

        if not contract_list:
            console.print("No contracts found!", style="bold red")
            self.run()
        else:
            table = Table(title="Contracts")
            table.add_column("Client", style="bold green")
            table.add_column("Total amount", style="bold green")
            table.add_column("Remaining amount", style="bold green")
            table.add_column("Status", style="bold green")

            for contract in contract_list:
                table.add_row(
                    contract.client.first_name + " " + contract.client.last_name,
                    str(contract.total_amount),
                    str(contract.remaining_amount),
                    str(contract.status),
                )

            console.print(table)
            self.run()

    def get_events(self):
        """Show events."""

        event_list = manage_support.get_events()

        if not event_list:
            console.print("No events found!", style="bold red")
            self.run()
        else:
            table = Table(title="Events")
            table.add_column("Name", style="bold green")
            table.add_column("Location", style="bold green")
            table.add_column("Started at", style="bold green")
            table.add_column("Ended at", style="bold green")
            table.add_column("Attendees", style="bold green")
            table.add_column("Notes", style="bold green")

            for event in event_list:
                table.add_row(
                    event.name, event.location, event.started_date, event.ended_date, event.attendees, event.notes
                )

            console.print(table)
            self.run()

    def logout(self):
        """Logout a collaborator."""
        remove_token()
        console.print("Collaborator logged out successfully!", style="bold green")
        self.exit()

    def exit(self) -> None:
        console.print("Exiting...", style="bold blue")
        exit()

import inquirer

from rich.console import Console
from rich.table import Table
from types import SimpleNamespace
from datetime import datetime
from dateutil.parser import parse as parse_date

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
        console.print("7. Show clients", style="bold green")
        console.print("8. Show contracts", style="bold green")
        console.print("9. Show events", style="bold green")
        console.print("10. Exit", style="bold green")
        console.print("11. Logout", style="bold green")

        option_mapping = {
            1: self.create_client,
            2: self.update_client,
            3: self.update_contract,
            4: self.get_unsigned_contracts,
            5: self.get_unpaid_contracts,
            6: self.create_event,
            7: self.get_clients,
            8: self.get_contrats,
            9: self.get_events,
            10: self.exit,
            11: self.logout,
        }

        option = int(input("Choose an option: "))
        selected_method = option_mapping.get(option)

        if selected_method:
            selected_method()
        else:
            console.print("Invalid option selected.", style="bold red")
            self.run()

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

        payload = get_token_payload()

        client_list = manage_commercial.get_clients()
        client_list = [
            (f"Client {client.first_name} {client.last_name}, Email {client.email}", client.id)
            for client in client_list
        ]
        client_choices = [inquirer.List("client", message="Select a client", choices=client_list)]

        client_id = int(inquirer.prompt(client_choices)["client"])
        client = manage_commercial.get_client(client_id)

        information = input(f"Information ({client.information}): ")
        first_name = input(f"First name ({client.first_name}): ")
        last_name = input(f"Last name ({client.last_name}): ")
        email = input(f"Email ({client.email}): ")
        phone_number = input(f"Phone number ({client.phone_number}): ")
        company_name = input(f"Company name ({client.company_name}): ")
        commercial_id = payload['id']

        manage_commercial.update_client(
            SimpleNamespace(
                id=client_id,
                information=information,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                company_name=company_name,
                commercial_id=commercial_id,
            )
        )
        console.print("Client updated successfully!", style="bold green")

    def update_contract(self):
        """Update a contract."""

        contract_list = manage_commercial.get_contracts()
        contract_list = [
            (f"Contract {contract.uniq_id}, Client {contract.client_id}", contract.id) for contract in contract_list
        ]
        contract_choices = [inquirer.List("contract", message="Select a contract", choices=contract_list)]

        contract_id = int(inquirer.prompt(contract_choices)["contract"])
        contract = manage_commercial.get_contract(contract_id)

        total_amount = float(input(f"Total amount ({contract.total_amount}): "))
        remaining_amount = float(input(f"Remaining amount ({contract.remaining_amount}): "))
        status = input(f"Status ({contract.status}): ")

        manage_commercial.update_contract(
            SimpleNamespace(
                id=contract_id,
                total_amount=total_amount,
                remaining_amount=remaining_amount,
                status=status,
            )
        )
        console.print("Contract updated successfully!", style="bold green")

    def get_unsigned_contracts(self):
        """Show unsigned contracts."""

        contract_list = manage_commercial.get_unsigned_contracts()

        if not contract_list:
            console.print("No unsigned contracts found.", style="bold red")
            self.run()
        else:
            table = Table(title="Unsigned Contracts")
            table.add_column("ID", style="bold blue")
            table.add_column("Total Amount", style="bold blue")
            table.add_column("Remaining Amount", style="bold blue")
            table.add_column("Status", style="bold blue")
            table.add_column("Client", style="bold blue")

            for contract in contract_list:
                table.add_row(
                    str(contract.id),
                    str(contract.total_amount),
                    str(contract.remaining_amount),
                    str(contract.status),
                    contract.client.first_name + " " + contract.client.last_name,
                )

            console.print(table)
            self.run()

    def get_unpaid_contracts(self):
        """Show unpaid contracts."""

        contract_list = manage_commercial.get_unpaid_contracts()

        if not contract_list:
            console.print("No unpaid contracts found.", style="bold red")
            self.run()
        else:
            table = Table(title="Unpaid Contracts")
            table.add_column("ID", style="bold blue")
            table.add_column("Total Amount", style="bold blue")
            table.add_column("Remaining Amount", style="bold blue")
            table.add_column("Status", style="bold blue")
            table.add_column("Client", style="bold blue")

            for contract in contract_list:
                table.add_row(
                    str(contract.id),
                    str(contract.total_amount),
                    str(contract.remaining_amount),
                    str(contract.status),
                    contract.client.first_name + " " + contract.client.last_name,
                )

            console.print(table)
            self.run()

    def create_event(self):
        """Create an event."""

        contract_list = manage_commercial.get_contracts()
        contract_list = [
            (
                f"Contract {contract.uniq_id}, Client {contract.client.first_name} {contract.client.last_name}",
                contract.id,
            )
            for contract in contract_list
        ]
        contract_choices = [inquirer.List("contract", message="Select a contract", choices=contract_list)]

        contract_id = int(inquirer.prompt(contract_choices)["contract"])
        contract = manage_commercial.get_contract(contract_id)
        support_id = int(contract.support_id)

        name = input("Name: ")
        location = input("Location: ")
        started_date = input("Started date (YYYY-MM-DD HH:MM): ")

        # Parse date and validate it is in the future and format is correct
        try:
            started_date = parse_date(started_date)

            if started_date < datetime.now():
                console.print("The started date must be in the future\n", style="bold red")
                self.run()
        except ValueError:
            console.print("Invalid date format. Please use the format YYYY-MM-DD HH:MM\n", style="bold red")
            self.run()

        ended_date = input("Ended date (YYYY-MM-DD HH:MM): ")

        # Parse date and validate it is in the future and format is correct
        try:
            ended_date = parse_date(ended_date)

            if ended_date < started_date:
                console.print("The ended date must be in the future\n", style="bold red")
                self.run()
        except ValueError:
            console.print("Invalid date format. Please use the format YYYY-MM-DD HH:MM\n", style="bold red")
            self.run()

        attendees = input("Attendees: ")
        notes = input("Notes: ")

        manage_commercial.create_event(
            SimpleNamespace(
                name=name,
                location=location,
                started_date=started_date,
                ended_date=ended_date,
                attendees=attendees,
                notes=notes,
                contract_id=contract_id,
                support_contact_id=support_id,
            )
        )

        console.print(f"Event {name} created successfully!", style="bold green")
        self.run()

    def get_clients(self):
        """Show clients."""

        client_list = manage_commercial.get_clients()

        if not client_list:
            console.print("No clients found.", style="bold red")
            self.run()
        else:
            table = Table(title="Clients")
            table.add_column("ID", style="bold blue")
            table.add_column("First Name", style="bold blue")
            table.add_column("Last Name", style="bold blue")
            table.add_column("Email", style="bold blue")
            table.add_column("Phone Number", style="bold blue")
            table.add_column("Company Name", style="bold blue")

            for client in client_list:
                table.add_row(
                    str(client.id),
                    client.first_name,
                    client.last_name,
                    client.email,
                    client.phone_number,
                    client.company_name,
                )

            console.print(table)
            self.run()

    def get_contrats(self):
        """Show contracts."""

        contract_list = manage_commercial.get_contracts()

        if not contract_list:
            console.print("No contracts found.", style="bold red")
            self.run()
        else:
            table = Table(title="Contracts")
            table.add_column("ID", style="bold blue")
            table.add_column("Total Amount", style="bold blue")
            table.add_column("Remaining Amount", style="bold blue")
            table.add_column("Status", style="bold blue")
            table.add_column("Client", style="bold blue")

            for contract in contract_list:
                table.add_row(
                    str(contract.id),
                    str(contract.total_amount),
                    str(contract.remaining_amount),
                    str(contract.status),
                    contract.client.first_name + " " + contract.client.last_name,
                )

            console.print(table)
            self.run()

    def get_events(self):
        """Show events."""

        event_list = manage_commercial.get_events()

        if not event_list:
            console.print("No events found.", style="bold red")
            self.run()
        else:
            table = Table(title="Events")
            table.add_column("Name", style="bold blue")
            table.add_column("Location", style="bold blue")
            table.add_column("Started at", style="bold blue")
            table.add_column("Ended at", style="bold blue")
            table.add_column("Attendees", style="bold blue")
            table.add_column("Notes", style="bold blue")
            table.add_column("Contract", style="bold blue")
            table.add_column("Client", style="bold blue")

            for event in event_list:
                table.add_row(
                    event.name,
                    event.location,
                    event.started_date.strftime("%m/%d/%Y, %H:%M:%S"),
                    event.ended_date.strftime("%m/%d/%Y, %H:%M:%S"),
                    str(event.attendees),
                    event.notes,
                    str(event.contract.uniq_id),
                    f"{event.contract.client.first_name} {event.contract.client.last_name}",
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

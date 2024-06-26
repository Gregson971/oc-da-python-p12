import inquirer
import getpass
import bcrypt

from rich.console import Console
from rich.table import Table
from types import SimpleNamespace
from sentry_sdk import capture_exception

from src.infrastructure.helpers.remove_token import remove_token
from src.infrastructure.helpers.validators import Validators

from src.domain.use_cases.manage_manager import ManageManager

console = Console()
manage_manager = ManageManager()


class ManagerCommand:

    def run(self):
        console.print("\nEpicEvents Manager CRM menu\n", style="bold blue")

        console.print("Main menu", style="bold blue")
        console.print("0. Show collaborators", style="bold green")
        console.print("1. Create a collaborator", style="bold green")
        console.print("2. Update manager", style="bold green")
        console.print("3. Delete manager", style="bold red")
        console.print("4. Update commercial", style="bold green")
        console.print("5. Delete commercial", style="bold red")
        console.print("6. Update support", style="bold green")
        console.print("7. Delete support", style="bold red")
        console.print("8. Create contract", style="bold green")
        console.print("9. Update contract", style="bold green")
        console.print("10. Show events with no assigned support", style="bold green")
        console.print("11. Update event", style="bold green")
        console.print("12. Show clients", style="bold green")
        console.print("13. Show contracts", style="bold green")
        console.print("14. Show events", style="bold green")
        console.print("15. Exit", style="bold green")
        console.print("16. Logout", style="bold green")

        option_mapping = {
            0: self.get_collaborators,
            1: self.create_collaborator,
            2: self.update_manager,
            3: self.delete_manager,
            4: self.update_commercial,
            5: self.delete_commercial,
            6: self.update_support,
            7: self.delete_support,
            8: self.create_contract,
            9: self.update_contract,
            10: self.get_events_with_no_assigned_support,
            11: self.update_event,
            12: self.get_clients,
            13: self.get_contratcs,
            14: self.get_events,
            15: self.exit,
            16: self.logout,
        }

        option = int(input("Choose an option: "))
        selected_method = option_mapping.get(option)

        if selected_method:
            selected_method()
        else:
            console.print("Invalid option selected.", style="bold red")
            self.run()

    def get_collaborator_information(self):
        """Get collaborator information."""

        roles = [inquirer.List("role", message="Select a role", choices=["manager", "commercial", "support"])]

        role = inquirer.prompt(roles)["role"]
        first_name = input("First name: ")
        last_name = input("Last name: ")

        try:
            email = input("Email: ")
            if not Validators.validate_email(email):
                console.print("Invalid email!", style="bold red")
                return
        except Exception as e:
            capture_exception(e)
            console.print(str(e), style="bold red")
            return

        try:
            password = getpass.getpass("Password: ")
            confirm_password = getpass.getpass("Confirm password: ")

            if not Validators.validate_password(password, confirm_password):
                console.print("Invalid password!", style="bold red")
                return
        except Exception as e:
            capture_exception(e)
            console.print(str(e), style="bold red")
            return

        # Hash the password using bcrypt
        hashed_password = bcrypt.hashpw(confirm_password.encode('utf-8'), bcrypt.gensalt())

        return SimpleNamespace(
            first_name=first_name,
            last_name=last_name,
            email=email,
            role=role,
            password=hashed_password,
        )

    def create_collaborator(self):
        """Create collaborators."""

        collaborator_data = self.get_collaborator_information()

        if collaborator_data is None:
            self.run()

        if collaborator_data.role == "manager":
            manage_manager.create_manager(collaborator_data)
        elif collaborator_data.role == "commercial":
            manage_manager.create_commercial(collaborator_data)
        elif collaborator_data.role == "support":
            manage_manager.create_support(collaborator_data)

        console.print(
            f"Collaborator: {collaborator_data.first_name} {collaborator_data.last_name} created successfully!",
            style="bold green",
        )

        self.run()

    def get_collaborators(self):
        """Show all collaborators."""

        collaborator_list = manage_manager.get_collaborators()

        if not collaborator_list:
            console.print("No collaborators found!", style="bold red")
            self.run()
        else:
            table = Table(title="Collaborators")
            table.add_column("First name", style="bold blue")
            table.add_column("Last name", style="bold blue")
            table.add_column("Email", style="bold blue")
            table.add_column("Role", style="bold blue")

            for collaborator in collaborator_list:
                table.add_row(
                    collaborator.first_name, collaborator.last_name, collaborator.email, str(collaborator.role)
                )

            console.print(table)
            self.run()

    def update_manager(self):
        """Update manager."""

        manager_list = manage_manager.get_managers()
        manager_list = [(f"{manager.first_name} {manager.last_name}", manager.id) for manager in manager_list]
        manager_choices = [inquirer.List("manager", message="Select a manager", choices=manager_list)]

        manager_id = int(inquirer.prompt(manager_choices)["manager"])
        manager = manage_manager.get_manager(manager_id)

        first_name = input(f"First name ({manager.first_name}): ") or manager.first_name
        last_name = input(f"Last name ({manager.last_name}): ") or manager.last_name
        email = input(f"Email ({manager.email}): ") or manager.email
        password = getpass.getpass("Password: ")
        confirm_password = getpass.getpass("Confirm password: ")

        if password != confirm_password:
            console.print("Passwords do not match!", style="bold red")
            return

        manage_manager.update_manager(
            manager_id,
            SimpleNamespace(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            ),
        )
        console.print("Manager updated successfully!", style="bold green")
        self.run()

    def delete_manager(self):
        """Delete manager."""

        manager_list = manage_manager.get_managers()
        manager_list = [(f"{manager.first_name} {manager.last_name}", manager.id) for manager in manager_list]
        manager_choices = [inquirer.List("manager", message="Select a manager", choices=manager_list)]

        manager_id = int(inquirer.prompt(manager_choices)["manager"])
        confirm = input("Are you sure you want to delete this manager? (y/n): ")

        if confirm.lower() != "y":
            console.print("Manager deletion cancelled!", style="bold red")
            self.run()
        else:
            manage_manager.delete_manager(manager_id)
            console.print("Manager deleted successfully!", style="bold green")
            self.run()

    def update_commercial(self):
        """Update commercial."""

        commercial_list = manage_manager.get_commercials()
        commercial_list = [
            (f"{commercial.first_name} {commercial.last_name}", commercial.id) for commercial in commercial_list
        ]
        commercial_choices = [inquirer.List("commercial", message="Select a commercial", choices=commercial_list)]

        commercial_id = int(inquirer.prompt(commercial_choices)["commercial"])
        commercial = manage_manager.get_commercial(commercial_id)

        first_name = input(f"First name ({commercial.first_name}): ") or commercial.first_name
        last_name = input(f"Last name ({commercial.last_name}): ") or commercial.last_name
        email = input(f"Email ({commercial.email}): ") or commercial.email
        password = getpass.getpass("Password: ")
        confirm_password = getpass.getpass("Confirm password: ")

        if password != confirm_password:
            console.print("Passwords do not match!", style="bold red")
            return

        manage_manager.update_commercial(
            commercial_id,
            SimpleNamespace(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            ),
        )
        console.print("Commercial updated successfully!", style="bold green")
        self.run()

    def delete_commercial(self):
        """Delete commercial."""

        commercial_list = manage_manager.get_commercials()
        commercial_list = [
            (f"{commercial.first_name} {commercial.last_name}", commercial.id) for commercial in commercial_list
        ]
        commercial_choices = [inquirer.List("commercial", message="Select a commercial", choices=commercial_list)]

        commercial_id = int(inquirer.prompt(commercial_choices)["commercial"])
        confirm = input("Are you sure you want to delete this commercial? (y/n): ")

        if confirm.lower() != "y":
            console.print("Commercial deletion cancelled!", style="bold red")
            self.run()
        else:
            manage_manager.delete_commercial(commercial_id)
            console.print("Commercial deleted successfully!", style="bold green")
            self.run()

    def update_support(self):
        """Update support."""

        support_list = manage_manager.get_supports()
        support_list = [(f"{support.first_name} {support.last_name}", support.id) for support in support_list]
        support_choices = [inquirer.List("support", message="Select a support", choices=support_list)]

        support_id = int(inquirer.prompt(support_choices)["support"])
        support = manage_manager.get_support(support_id)

        first_name = input(f"First name ({support.first_name}): ") or support.first_name
        last_name = input(f"Last name ({support.last_name}): ") or support.last_name
        email = input(f"Email ({support.email}): ") or support.email
        password = getpass.getpass("Password: ")
        confirm_password = getpass.getpass("Confirm password: ")

        if password != confirm_password:
            console.print("Passwords do not match!", style="bold red")
            return

        manage_manager.update_support(
            support_id,
            SimpleNamespace(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            ),
        )
        console.print("Support updated successfully!", style="bold green")
        self.run()

    def delete_support(self):
        """Delete support."""

        support_list = manage_manager.get_supports()
        support_list = [(f"{support.first_name} {support.last_name}", support.id) for support in support_list]
        support_choices = [inquirer.List("support", message="Select a support", choices=support_list)]

        support_id = int(inquirer.prompt(support_choices)["support"])
        confirm = input("Are you sure you want to delete this support? (y/n): ")

        if confirm.lower() != "y":
            console.print("Support deletion cancelled!", style="bold red")
            self.run()
        else:
            manage_manager.delete_support(support_id)
            console.print("Support deleted successfully!", style="bold green")
            self.run()

    def create_contract(self):
        """Create contract."""

        client_list = manage_manager.get_clients()
        client_list = [(f"{client.first_name} {client.last_name}", client.id) for client in client_list]
        client_choices = [inquirer.List("client", message="Select a client", choices=client_list)]

        support_list = manage_manager.get_supports()
        support_list = [(f"{support.first_name} {support.last_name}", support.id) for support in support_list]
        support_choices = [inquirer.List("support", message="Select a support", choices=support_list)]

        status_list = ["not-signed", "signed"]
        status_choices = [inquirer.List("status", message="Select a status", choices=status_list)]

        total_amount = float(input("Total amount: "))
        remaining_amount = float(input("Remaining amount: "))
        status = inquirer.prompt(status_choices)["status"]
        client_id = int(inquirer.prompt(client_choices)["client"])
        support_id = int(inquirer.prompt(support_choices)["support"])

        manage_manager.create_contract(
            SimpleNamespace(
                total_amount=total_amount,
                remaining_amount=remaining_amount,
                status=status,
                client_id=client_id,
                support_id=support_id,
            )
        )
        console.print("Contract created successfully!", style="bold green")
        self.run()

    def update_contract(self):
        """Update contract."""

        contract_list = manage_manager.get_contracts()
        contract_list = [
            (f"Contract {contract.uniq_id}, Client {contract.client_id}", contract.id) for contract in contract_list
        ]
        contract_choices = [inquirer.List("contract", message="Select a contract", choices=contract_list)]

        contract_id = int(inquirer.prompt(contract_choices)["contract"])
        contract = manage_manager.get_contract(contract_id)

        total_amount = float(input(f"Total amount ({contract.total_amount}): ") or contract.total_amount)
        remaining_amount = float(
            input(f"Remaining amount ({contract.remaining_amount}): ") or contract.remaining_amount
        )
        status = input(f"Status ({contract.status}): ") or contract.status

        manage_manager.update_contract(
            contract_id,
            SimpleNamespace(
                total_amount=total_amount,
                remaining_amount=remaining_amount,
                status=status,
            ),
        )
        console.print("Contract updated successfully!", style="bold green")

    def get_events_with_no_assigned_support(self):
        """Get events with no assigned support."""

        event_list = manage_manager.get_events_with_no_assigned_support()

        if not event_list:
            console.print("No events with no assigned support found!", style="bold red")
            self.run()
        else:
            table = Table(title="Events with no assigned support")
            table.add_column("Event ID", style="bold blue")
            table.add_column("Event", style="bold blue")
            table.add_column("Location", style="bold blue")
            table.add_column("Started at", style="bold blue")
            table.add_column("Ended at", style="bold blue")
            table.add_column("Attendees", style="bold blue")
            table.add_column("Notes", style="bold blue")
            table.add_column("Client")

            for event in event_list:
                table.add_row(
                    str(event.id),
                    event.name,
                    event.location,
                    event.started_date,
                    event.ended_date,
                    event.attendees,
                    event.notes,
                    event.client.first_name + " " + event.client.last_name,
                )

            console.print(table)
            self.run()

    def update_event(self):
        """Update event."""

        event_list = manage_manager.get_events()
        event_list = [(event.name, event.id) for event in event_list]
        event_choices = [inquirer.List("event", message="Select an event", choices=event_list)]

        event_id = int(inquirer.prompt(event_choices)["event"])
        event = manage_manager.get_event(event_id)

        name = input(f"Name ({event.name}): ") or event.name
        location = input(f"Location ({event.location}): ") or event.location
        started_at = input(f"Started at ({event.started_at}): ") or event.started_at
        ended_at = input(f"Ended at ({event.ended_at}): ") or event.ended_at
        attendees = input(f"Attendees ({event.attendees}): ") or event.attendees
        notes = input(f"Notes ({event.notes}): ") or event.notes

        manage_manager.update_event(
            event_id,
            SimpleNamespace(
                name=name,
                location=location,
                started_at=started_at,
                ended_at=ended_at,
                attendees=attendees,
                notes=notes,
            ),
        )
        console.print("Event updated successfully!", style="bold green")
        self.run()

    def get_clients(self):
        """Show clients."""

        client_list = manage_manager.get_clients()

        if not client_list:
            console.print("No clients found!", style="bold red")
            self.run()
        else:
            table = Table(title="Clients")
            table.add_column("First name", style="bold blue")
            table.add_column("Last name", style="bold blue")
            table.add_column("Email", style="bold blue")
            table.add_column("Phone number", style="bold blue")
            table.add_column("Company name", style="bold blue")

            for client in client_list:
                table.add_row(
                    client.first_name, client.last_name, client.email, client.phone_number, client.company_name
                )

            console.print(table)
            self.run()

    def get_contratcs(self):
        """Show contracts."""

        contract_list = manage_manager.get_contracts()

        if not contract_list:
            console.print("No contracts found!", style="bold red")
            self.run()
        else:
            table = Table(title="Contracts")
            table.add_column("ID", style="bold blue")
            table.add_column("Total amount", style="bold blue")
            table.add_column("Remaining amount", style="bold blue")
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

        event_list = manage_manager.get_events()

        if not event_list:
            console.print("No events found!", style="bold red")
            self.run()
        else:
            table = Table(title="Events")
            table.add_column("Name", style="bold blue")
            table.add_column("Location", style="bold blue")
            table.add_column("Started at", style="bold blue")
            table.add_column("Ended at", style="bold blue")
            table.add_column("Attendees", style="bold blue")
            table.add_column("Notes", style="bold blue")
            table.add_column("Contract ID", style="bold blue")
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

    def exit(self):
        console.print("Exiting...", style="bold blue")
        exit()

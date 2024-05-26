import getpass
import bcrypt
from kink import di
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from src.domain.entities.base import Base


def sample_db():
    # Get the password from the user input
    password = getpass.getpass("Enter the password which will be used for all collaborators and clients: ")
    confirm_password = getpass.getpass("Confirm the password: ")

    # Check if the passwords match
    if password != confirm_password:
        print("The passwords do not match.")
        return  # Prevent infinite recursion

    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(confirm_password.encode('utf-8'), bcrypt.gensalt())

    engine = di["engine"]

    # Create the tables
    Base.metadata.create_all(engine)

    # Create the session
    session = di[Session]

    # SQL commands
    sql_commands = """
    CREATE TABLE IF NOT EXISTS collaborators (
        id SERIAL PRIMARY KEY,
        first_name character varying(80) NOT NULL,
        last_name character varying(80) NOT NULL,
        email character varying(255) NOT NULL UNIQUE,
        password bytea NOT NULL,
        role character varying(255)
    );
    CREATE UNIQUE INDEX IF NOT EXISTS collaborators_email_key ON collaborators(email);

    CREATE TABLE IF NOT EXISTS commercials (
        id integer PRIMARY KEY REFERENCES collaborators(id)
    );

    CREATE TABLE IF NOT EXISTS managers (
        id integer PRIMARY KEY REFERENCES collaborators(id)
    );

    CREATE TABLE IF NOT EXISTS supports (
        id integer PRIMARY KEY REFERENCES collaborators(id)
    );

    CREATE TABLE IF NOT EXISTS clients (
        id SERIAL PRIMARY KEY,
        information character varying(80) NOT NULL,
        first_name character varying(80) NOT NULL,
        last_name character varying(80) NOT NULL,
        email character varying(255) NOT NULL UNIQUE,
        phone_number character varying(80) NOT NULL,
        company_name character varying(255) NOT NULL,
        created_date timestamp without time zone,
        updated_date timestamp without time zone,
        commercial_id integer NOT NULL REFERENCES commercials(id) ON DELETE CASCADE
    );
    CREATE UNIQUE INDEX IF NOT EXISTS clients_email_key ON clients(email);

    CREATE TABLE IF NOT EXISTS contracts (
        id SERIAL PRIMARY KEY,
        uniq_id uuid UNIQUE,
        total_amount double precision,
        remaining_amount double precision,
        created_date timestamp without time zone,
        status character varying(255),
        client_id integer NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
        support_id integer NOT NULL REFERENCES supports(id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS events (
        id SERIAL PRIMARY KEY,
        name character varying(80) NOT NULL,
        started_date timestamp without time zone NOT NULL,
        ended_date timestamp without time zone NOT NULL,
        location character varying(80) NOT NULL,
        attendees integer NOT NULL,
        notes character varying(255),
        contract_id integer NOT NULL REFERENCES contracts(id) ON DELETE CASCADE,
        support_contact_id integer REFERENCES supports(id)
    );
    """

    try:
        # Run the SQL commands
        session.execute(text(sql_commands))

        # Insert initial data
        insert_command = """
        INSERT INTO collaborators (first_name, last_name, email, password, role)
        VALUES (:first_name, :last_name, :email, :password, :role);

        INSERT INTO managers (id)
        VALUES ((SELECT id FROM collaborators WHERE email = :email));
        """
        session.execute(
            text(insert_command),
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "password": hashed_password,
                "role": "manager",
            },
        )

        # Commit the changes
        session.commit()

    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        # Close the session
        session.close()

    print("The samples table has been created successfully.")


if __name__ == "__main__":
    sample_db()

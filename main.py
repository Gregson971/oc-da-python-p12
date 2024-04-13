import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from src.domain.entities.base import Base
from src.infrastructure.views.cli import Cli


def main():
    # Load the environment variables
    load_dotenv()

    # Get the environment variable
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    # Create the connection string
    connection_string = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    # Create the engine
    engine = create_engine(connection_string)

    # Create the tables
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        cli = Cli(session)
        cli.run()


if __name__ == "__main__":
    main()
    print("main.py executed")

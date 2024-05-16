from os import getenv
from kink import di
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from src.infrastructure.helpers.get_token_payload import get_token_payload


def bootstrap_di() -> None:
    # Load the environment variables
    load_dotenv()

    # Get the environment variable
    di["db_user"] = getenv("DB_USER")
    di["db_password"] = getenv("DB_PASSWORD")
    di["db_host"] = getenv("DB_HOST")
    di["db_port"] = getenv("DB_PORT")
    di["db_name"] = getenv("DB_NAME")
    di["secret_key"] = getenv("SECRET_KEY")
    di["token_delta"] = getenv("TOKEN_DELTA")

    # Create the connection string
    di["connection_string"] = (
        f"postgresql+psycopg2://{di['db_user']}:{di['db_password']}@{di['db_host']}:{di['db_port']}/{di['db_name']}"
    )

    # Create the engine
    di["engine"] = lambda di: create_engine(di["connection_string"])

    # Create the session
    di[Session] = Session(di["engine"])

    # Get the token payload
    di["token_payload"] = lambda di: get_token_payload()

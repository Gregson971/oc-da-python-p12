import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


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


# Create the session
Session = sessionmaker(bind=engine)
session = Session()

# Connect to the database
with engine.connect() as connection:
    print("connected to the database")

# Close the session
session.close()
print("session closed")

# Close the engine
engine.dispose()
print("connection closed")

if __name__ == "__main__":
    print("main.py executed")

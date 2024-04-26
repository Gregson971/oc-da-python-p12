import os
import jwt

from dotenv import load_dotenv
from sentry_sdk import capture_exception


def get_token_payload() -> dict:
    """Get token payload."""
    try:
        secret_key = os.getenv("SECRET_KEY")
        f = open(".token", "r")
        token = f.read()
        f.close()

        load_dotenv()

        payload = jwt.decode(token, secret_key, algorithms=['HS256'])

    except jwt.ExpiredSignatureError as e:
        capture_exception(e)
        raise Exception("Token expired")
    except jwt.InvalidTokenError as e:
        capture_exception(e)
        raise Exception("Invalid token")

    return payload

import jwt

from kink import di
from sentry_sdk import capture_exception


def get_token_payload() -> dict:
    """Get token payload."""
    try:
        secret_key = di["secret_key"]
        f = open(".token", "r")
        token = f.read()
        f.close()

        payload = jwt.decode(token, secret_key, algorithms=['HS256'])

    except jwt.ExpiredSignatureError as e:
        capture_exception(e)
        raise Exception("Token expired")
    except jwt.InvalidTokenError as e:
        capture_exception(e)
        raise Exception("Invalid token")
    except FileNotFoundError as e:
        capture_exception(e)
        raise Exception(f"Token file not found, {e}")

    return payload

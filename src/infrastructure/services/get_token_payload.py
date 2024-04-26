import os
import jwt

from dotenv import load_dotenv


def get_token_payload() -> dict:
    """Get token payload."""
    try:
        secret_key = os.getenv("SECRET_KEY")
        f = open(".token", "r")
        token = f.read()
        f.close()

        load_dotenv()

        payload = jwt.decode(token, secret_key, algorithms=['HS256'])

    except jwt.ExpiredSignatureError:
        raise Exception("Token expired", 401)
    except jwt.InvalidTokenError:
        raise Exception("Invalid token", 401)

    return payload

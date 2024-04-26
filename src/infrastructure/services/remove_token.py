import os

from sentry_sdk import capture_exception


def remove_token():
    """Remove token."""
    try:
        os.remove(".token")
    except FileNotFoundError as e:
        capture_exception(e)
        raise Exception(f"Token file not found, {e}")
    except Exception as e:
        capture_exception(e)
        raise Exception(f"An error occurred while removing the token file: {e}")

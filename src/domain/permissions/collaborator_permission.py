import jwt

from kink import di
from sentry_sdk import capture_exception

ROLES = {
    'manager': [
        'create_collaborator',
        'update_collaborator',
        'delete_collaborator',
        'create_contract',
        'update_contract',
        'filter_events',
        'update_event',
    ],
    'commercial': [
        'create_client',
        'update_client',
        'create_client_contract',
        'update_client_contract',
        'filter_contracts',
        'create_event',
    ],
    'support': ['filter_events', 'update_event'],
    'admin': ['create_collaborator', 'update_collaborator', 'delete_collaborator'],
}


def check_permission(role, permission):
    return permission in ROLES.get(role, [])


def require_permission(permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                payload = di["token_payload"]
                role = payload['role']

                if not check_permission(role, permission):
                    raise PermissionError("Permission denied.")

                return func(*args, **kwargs)
            except jwt.ExpiredSignatureError as e:
                capture_exception(e)
                raise Exception("Token expired")
            except jwt.InvalidTokenError as e:
                capture_exception(e)
                raise Exception("Invalid token")
            except Exception as e:
                capture_exception(e)
                raise Exception(f"An error occurred while checking the permission: {e}")

        return wrapper

    return decorator

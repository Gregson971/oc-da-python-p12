from dotenv import load_dotenv

from src.infrastructure.services.get_token_payload import get_token_payload

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
    'commercial': ['create_client', 'update_client', 'update_client_contract', 'filter_contracts', 'create_event'],
    'support': ['filter_events', 'update_event'],
    'admin': ['create_collaborator', 'update_collaborator', 'delete_collaborator'],
}


def check_permission(role, permission):
    return permission in ROLES.get(role, [])


def require_permission(permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            load_dotenv()

            payload = get_token_payload()
            role = payload['role']

            if not check_permission(role, permission):
                raise PermissionError("Permission denied.")

            return func(*args, **kwargs)

        return wrapper

    return decorator

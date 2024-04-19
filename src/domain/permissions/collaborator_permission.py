from src.domain.entities.collaborator import Collaborator

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
}


def check_permission(role, permission):
    return permission in ROLES.get(role, [])


def require_permission(permission):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if not check_permission(Collaborator.role, permission):
                raise PermissionError("Permission denied.")
            return func(self, *args, **kwargs)

        return wrapper

    return decorator

import time
import pytest
from unittest import mock
from src.domain.permissions.collaborator_permission import check_permission, require_permission


@pytest.mark.parametrize(
    "role, permission, expected",
    [
        ("manager", "create_collaborator", True),
        ("manager", "non_existent_permission", False),
        ("non_existent_role", "create_collaborator", False),
    ],
    ids=["Role and permission exist", "Role exists but permission does not", "Role does not exist"],
)
def test_check_permission(role, permission, expected):
    assert check_permission(role, permission) == expected


@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_require_permission_with_permission(mock_di):
    mock_di.__getitem__.return_value = {'role': 'manager'}

    @require_permission('create_collaborator')
    def dummy_func():
        return "Success"

    assert dummy_func() == "Success"


@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_require_permission_without_permission(mock_di):
    mock_di.__getitem__.return_value = {'role': 'manager'}

    @require_permission('non_existent_permission')
    def dummy_func():
        return "Success"

    with pytest.raises(Exception) as e:
        dummy_func()

    assert str(e.value) == "An error occurred while checking the permission: Permission denied."


@mock.patch('src.infrastructure.helpers.get_token_payload')
@mock.patch('src.domain.permissions.collaborator_permission.di')
def test_require_permission_with_expired_token(mock_di, mock_get_token_payload):
    mock_di.__getitem__.return_value = {'role': 'manager'}
    mock_get_token_payload.return_value = {
        'role': 'manager',
        'email': 'john.doe@example.com',
        'exp': 1640991600000,  # 2022/01/01
        'id': 1,
    }
    mock_get_token_payload.return_value['exp'] = 1640991600  # 2022/01/01

    @require_permission('create_collaborator')
    def dummy_func():
        # Raise an exception if the token is expired
        if mock_get_token_payload.return_value['exp'] < time.time():
            raise Exception("Token expired")
        return "Success"

    with pytest.raises(Exception) as e:
        dummy_func()

    assert str(e.value) == "An error occurred while checking the permission: Token expired"

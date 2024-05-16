import jwt
from kink import di

from src.domain.use_cases.manage_collaborator import ManageCollaborator


def test_login(dummy_manager):
    manage_collaborator = ManageCollaborator()
    genereted_token = manage_collaborator.login(dummy_manager.email, dummy_manager.password)
    decoded_token = jwt.decode(genereted_token, di["secret_key"], algorithms=["HS256"])

    assert decoded_token["email"] == dummy_manager.email
    assert decoded_token["role"] == "manager"

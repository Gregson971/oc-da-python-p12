import re
from rich.console import Console

console = Console()


class Validators:
    """Class to validate"""

    @staticmethod
    def validate_email(email: str) -> bool:
        if re.match(r"[^@]+@[^@]+\.[^@]+", email) is None:
            raise ValueError("Invalid email address!")

        return True

    @staticmethod
    def validate_password(password: str, confirm_password: str) -> bool:
        if password != confirm_password:
            raise ValueError("Passwords do not match!")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long!")
        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter!")
        if not any(char.islower() for char in password):
            raise ValueError("Password must contain at least one lowercase letter!")
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one number!")
        if not any(not char.isalnum() for char in password):
            raise ValueError("Password must contain at least one special character!")

        return True

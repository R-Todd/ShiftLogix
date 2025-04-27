# app/ports/auth_service.py

from abc import ABC, abstractmethod

class AuthService(ABC):
    @abstractmethod
    def authenticate(self, email: str, password: str) -> str:
        """
        Return a JWT on success, or raise ValueError on failure.
        """
        ...

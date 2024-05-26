from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_utils import EmailType, PasswordType, ChoiceType
from sqlalchemy.orm import relationship

from .base import Base

ROLES = [("commercial", "Commercial"), ("support", "Support"), ("manager", "Manager")]


class Collaborator(Base):
    """Collaborator entity"""

    __tablename__ = "collaborators"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    email = Column(EmailType, nullable=False, unique=True)
    password = Column(PasswordType(schemes=['pbkdf2_sha512', 'md5_crypt'], deprecated=['md5_crypt']), nullable=False)
    role = Column(ChoiceType(ROLES), default="manager")

    def __repr__(self):
        return f"{self.__class__.__name__}, name: {self.first_name} {self.last_name}, email: {self.email}"


class Commercial(Collaborator):
    """Commercial entity, inherits from Collaborator"""

    __tablename__ = "commercials"

    id = Column(Integer, ForeignKey('collaborators.id'), primary_key=True)

    clients = relationship("Client", back_populates="commercial", passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__}, name: {self.first_name} {self.last_name}, email: {self.email}"


class Support(Collaborator):
    """Support entity, inherits from Collaborator"""

    __tablename__ = "supports"

    id = Column(Integer, ForeignKey('collaborators.id'), primary_key=True)

    contracts = relationship("Contract", back_populates="support", passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__}, name: {self.first_name} {self.last_name}, email: {self.email}"


class Manager(Collaborator):
    """Manager entity, inherits from Collaborator"""

    __tablename__ = "managers"

    id = Column(Integer, ForeignKey('collaborators.id'), primary_key=True)

    def __repr__(self):
        return f"{self.__class__.__name__}, name: {self.first_name} {self.last_name}, email: {self.email}"

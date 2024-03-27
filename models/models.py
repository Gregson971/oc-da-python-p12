from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy_utils import ChoiceType, EmailType, PasswordType, UUIDType
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

import uuid

Base = declarative_base()

ROLES = [('commercial', 'Commercial'), ('support', 'Support'), ('manager', 'Manager')]
STATUSES = [('signed', 'Signed'), ('not-signed', 'Not signed')]


class Collaborator(Base):
    __tablename__ = "collaborators"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(EmailType)
    password = Column(PasswordType(schemes=['pbkdf2_sha512', 'md5_crypt'], deprecated=['md5_crypt']))
    role = Column(ChoiceType(ROLES))

    def __repr__(self):
        return (
            f"Collaborator(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, "
            f"email={self.email}, password={self.password}, role={self.role})"
        )


class Commercial(Collaborator):
    __tablename__ = "commercials"

    collaborator_id = Column(Integer, ForeignKey('collaborators.id'), primary_key=True)

    clients = relationship("Client", back_populates="commercial")


class Support(Collaborator):
    __tablename__ = "supports"

    collaborator_id = Column(Integer, ForeignKey('collaborators.id'), primary_key=True)


class Manager(Collaborator):
    __tablename__ = "managers"

    collaborator_id = Column(Integer, ForeignKey('collaborators.id'), primary_key=True)


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    information = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    full_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    company_name = Column(String)
    created_date = Column(Date)  # First contact date
    updated_date = Column(Date)
    commercial_id = Column(Integer, ForeignKey('commercials.collaborator_id'))

    commercial = relationship("Commercial", back_populates="clients")

    def __repr__(self):
        return (
            f"Client(id={self.id}, information={self.information}, first_name={self.first_name}, "
            f"last_name={self.last_name}, full_name={self.full_name}, email={self.email}, "
            f"phone_number={self.phone_number}, company_name={self.company_name}, "
            f"created_date={self.created_date}, updated_date={self.updated_date}, "
            f"commercial_id={self.commercial_id})"
        )


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True)
    uniq_id = Column(UUIDType(binary=False), default=uuid.uuid4)
    client_id = Column(Integer, ForeignKey('clients.id'))
    commercial_id = Column(Integer, ForeignKey('commercials.collaborator_id'))
    total_amount = Column(Float)
    remaining_amount = Column(Float)
    created_date = Column(Date)
    status = Column(ChoiceType(STATUSES))

    client = relationship("Client")
    commercial = relationship("Commercial")

    def __repr__(self):
        return (
            f"Contract(id={self.id}, uniq_id={self.uniq_id}, client_id={self.client_id}, "
            f"commercial_id={self.commercial_id}, total_amount={self.total_amount}, "
            f"remaining_amount={self.remaining_amount}, created_date={self.created_date}, "
            f"status={self.status})"
        )


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    contract_id = Column(Integer, ForeignKey('contracts.id'))
    client_id = Column(Integer, ForeignKey('clients.id'))
    started_date = Column(Date)
    ended_date = Column(Date)
    support_contact_id = Column(Integer, ForeignKey('supports.collaborator_id'))
    location = Column(String)
    attendees = Column(Integer)
    notes = Column(String)

    contract = relationship("Contract")
    client = relationship("Client")
    support_contact = relationship("Support")

    def __repr__(self):
        return (
            f"Event(id={self.id}, contract_id={self.contract_id}, client_id={self.client_id}, "
            f"started_date={self.started_date}, ended_date={self.ended_date}, "
            f"support_contact_id={self.support_contact_id}, location={self.location}, "
            f"attendees={self.attendees}, notes={self.notes})"
        )

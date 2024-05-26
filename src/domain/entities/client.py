from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Client(Base):
    """Client entity"""

    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    information = Column(String(80), nullable=False)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    created_date = Column(DateTime, default=datetime.now(timezone.utc))
    updated_date = Column(DateTime, onupdate=datetime.now(timezone.utc))
    commercial_id = Column(Integer, ForeignKey('commercials.id', ondelete="CASCADE"), nullable=False, index=True)

    commercial = relationship("Commercial", back_populates="clients")
    contract = relationship("Contract", back_populates="client", uselist=False, passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__}, name: {self.first_name} {self.last_name}, email: {self.email}"

from datetime import datetime, timezone
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy_utils import ChoiceType, UUIDType
from sqlalchemy.orm import relationship

from .base import Base

import uuid

STATUSES = [('signed', 'Signed'), ('not-signed', 'Not signed')]


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uniq_id = Column(UUIDType(binary=False), default=uuid.uuid4)
    total_amount = Column(Float)
    remaining_amount = Column(Float)
    created_date = Column(DateTime, default=datetime.now(timezone.utc))
    status = Column(ChoiceType(STATUSES))
    client_id = Column(Integer, ForeignKey('clients.id', ondelete="CASCADE"), nullable=False, index=True, unique=True)
    support_id = Column(Integer, ForeignKey('supports.id', ondelete="CASCADE"), nullable=False, index=True)

    client = relationship("Client", back_populates="contract")
    support = relationship("Support", back_populates="contracts")
    event = relationship("Event", back_populates="contract", uselist=False, passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__}, status: {self.status}, total_amount: {self.total_amount}"

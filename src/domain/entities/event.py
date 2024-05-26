from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Event(Base):
    """Event entity"""

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    started_date = Column(DateTime, nullable=False, default=None)
    ended_date = Column(DateTime, nullable=False, default=None)
    location = Column(String(80), nullable=False)
    attendees = Column(Integer, nullable=False)
    notes = Column(String(255))
    contract_id = Column(
        Integer, ForeignKey('contracts.id', ondelete="CASCADE"), nullable=False, index=True, unique=True
    )
    support_contact_id = Column(Integer, ForeignKey('supports.id'))

    contract = relationship("Contract", back_populates="event", uselist=False, passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__}, name: {self.name}, location: {self.location}, attendees: {self.attendees}"

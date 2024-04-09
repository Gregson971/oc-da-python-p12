from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    started_date = Column(DateTime, default=None)
    ended_date = Column(DateTime, default=None)
    location = Column(String)
    attendees = Column(Integer)
    notes = Column(String)
    contract_id = Column(
        Integer, ForeignKey('contracts.id', ondelete="CASCADE"), nullable=False, index=True, unique=True
    )
    support_contact_id = Column(Integer, ForeignKey('supports.id'))

    contract = relationship("Contract", back_populates="event", uselist=False, passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__}, location: {self.location}, attendees: {self.attendees}"

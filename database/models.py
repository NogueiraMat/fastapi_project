import uuid
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from database.database import Base

class Characters(Base):
    __tablename__ = "characters"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    bounty = Column(Integer)
    nickname = Column(String)
    primary_color = Column(String)
    secondary_color = Column(String)
    crew_id = Column(UUID(as_uuid=True), ForeignKey('crews.id'))

    crews = relationship("Crew", back_populates="characters")

class Crew(Base):
    __tablename__ = "crews"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, index=True)
    ship = Column(String)

    characters = relationship("Characters", back_populates="crews")
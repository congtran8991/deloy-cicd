from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.core.database import Base


class Item(Base):
    """Example model - an Item with basic fields."""

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(String(500), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Item(id={self.id}, title='{self.title}')>"

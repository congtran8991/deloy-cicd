"""
Generic CRUD utility helpers.
"""

from typing import Any, Optional, Type, TypeVar

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.core.database import Base

ModelType = TypeVar("ModelType", bound=Base)


def get_or_404(db: Session, model: Type[ModelType], obj_id: int) -> ModelType:
    """Fetch a record by primary key or raise a 404 error."""
    obj = db.query(model).filter(model.id == obj_id).first()
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{model.__name__} with id {obj_id} not found",
        )
    return obj


def paginate(
    db: Session,
    model: Type[ModelType],
    skip: int = 0,
    limit: int = 100,
    filters: Optional[list] = None,
) -> list[ModelType]:
    """Return a paginated & filtered list of records."""
    query = db.query(model)
    if filters:
        for condition in filters:
            query = query.filter(condition)
    return query.offset(skip).limit(limit).all()

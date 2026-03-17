from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.api.v1.schemas.item import ItemCreate, ItemResponse, ItemUpdate
from app.constants.common import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE
from app.utils import item_service

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/", response_model=list[ItemResponse])
def list_items(
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(
        DEFAULT_PAGE_SIZE,
        ge=1,
        le=MAX_PAGE_SIZE,
        description="Number of items to return",
    ),
    is_active: Optional[bool] = Query(None, description="Filter by active status"),
    db: Session = Depends(get_db),
):
    """Retrieve a list of items with pagination and optional filtering."""
    return item_service.get_items(db, skip=skip, limit=limit, is_active=is_active)


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    """Retrieve a single item by its ID."""
    return item_service.get_item(db, item_id)


@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item_in: ItemCreate, db: Session = Depends(get_db)):
    """Create a new item."""
    return item_service.create_item(db, item_in)


@router.patch("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item_in: ItemUpdate, db: Session = Depends(get_db)):
    """Partially update an item."""
    return item_service.update_item(db, item_id, item_in)


@router.delete("/{item_id}", response_model=ItemResponse)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Delete an item by its ID."""
    return item_service.delete_item(db, item_id)

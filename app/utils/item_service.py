from typing import Optional

from sqlalchemy.orm import Session

from app.api.v1.schemas.item import ItemCreate, ItemUpdate
from app.models.item import Item
from app.utils.crud import get_or_404, paginate


def get_items(
    db: Session, skip: int = 0, limit: int = 100, is_active: Optional[bool] = None
) -> list[Item]:
    """Get a list of items with optional filtering."""
    filters = []
    if is_active is not None:
        filters.append(Item.is_active == is_active)
    return paginate(db, Item, skip=skip, limit=limit, filters=filters)


def get_item(db: Session, item_id: int) -> Item:
    """Get a single item by ID, or raise 404."""
    return get_or_404(db, Item, item_id)


def create_item(db: Session, item_in: ItemCreate) -> Item:
    """Create a new item."""
    db_item = Item(**item_in.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, item_id: int, item_in: ItemUpdate) -> Item:
    """Update an existing item (partial update)."""
    db_item = get_or_404(db, Item, item_id)
    update_data = item_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_item, field, value)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int) -> Item:
    """Delete an item by ID."""
    db_item = get_or_404(db, Item, item_id)
    db.delete(db_item)
    db.commit()
    return db_item

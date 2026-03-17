from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.constants.common import TITLE_MAX_LENGTH, DESCRIPTION_MAX_LENGTH


class ItemBase(BaseModel):
    """Shared properties for Item."""

    title: str = Field(
        ..., min_length=1, max_length=TITLE_MAX_LENGTH, examples=["My Item"]
    )
    description: Optional[str] = Field(
        None, max_length=DESCRIPTION_MAX_LENGTH, examples=["A detailed description"]
    )


class ItemCreate(ItemBase):
    """Properties required to create an Item."""

    pass


class ItemUpdate(BaseModel):
    """Properties allowed to update on an Item (all optional)."""

    title: Optional[str] = Field(None, min_length=1, max_length=TITLE_MAX_LENGTH)
    description: Optional[str] = Field(None, max_length=DESCRIPTION_MAX_LENGTH)
    is_active: Optional[bool] = None


class ItemResponse(ItemBase):
    """Properties returned to the client."""

    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

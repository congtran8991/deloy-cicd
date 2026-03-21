"""
Application-wide constants.
"""

from enum import Enum


# Pagination defaults
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# String length limits
TITLE_MAX_LENGTH = 255
DESCRIPTION_MAX_LENGTH = 500


class SortOrder(str, Enum):
    """Sort order options."""

    ASC = "asc"
    DESC = "desc"


class ItemStatus(str, Enum):
    """Item status options."""

    ACTIVE = "active"
    INACTIVE = "inactive"

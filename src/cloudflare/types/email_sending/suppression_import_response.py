# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SuppressionImportResponse", "Item"]


class Item(BaseModel):
    index: int
    """Zero-based index of this item in the request body."""

    status: Literal["processed", "invalid", "error", "skipped"]
    """Outcome for this item."""

    id: Optional[str] = None
    """The created or promoted suppression's identifier.

    Present when `status` is `processed`.
    """

    email: Optional[str] = None
    """The submitted email address for this item."""

    error: Optional[str] = None
    """Human-readable error message.

    Present when `status` is `invalid`, `error`, or `skipped`.
    """


class SuppressionImportResponse(BaseModel):
    deduplicated: int
    """
    Number of items dropped because their email address repeated an earlier item in
    this request. Counted once and excluded from `items`.
    """

    errors: int
    """Number of items that failed to import due to an unexpected error."""

    invalid: int
    """Number of items with an invalid email address."""

    items: List[Item]
    """Per-item results, in the same order as the request body."""

    processed: int
    """Number of items successfully created or promoted."""

    skipped: int
    """
    Number of items skipped because the existing suppression is not customer-managed
    (for example, a read-only policy suppression).
    """

    total: int
    """Total number of items in the request body, including duplicates."""

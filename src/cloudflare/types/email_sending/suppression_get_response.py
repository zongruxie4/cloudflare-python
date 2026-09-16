# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SuppressionGetResponse"]


class SuppressionGetResponse(BaseModel):
    id: str
    """Unique identifier for this suppression."""

    created_at: datetime
    """When the suppression was created."""

    email: str
    """The suppressed email address."""

    expires_at: Optional[datetime] = None
    """When the suppression expires. Null for a permanent suppression."""

    read_only: bool
    """Whether clients may mutate this suppression.

    This is determined by the server and must not be inferred from `reason`.
    """

    reason: str
    """
    Why the address is suppressed: `manual`, `complaint`, `hard_bounce`,
    `soft_bounce`, or `policy`.
    """

    note: Optional[str] = None
    """Advisory note for this suppression, if any."""

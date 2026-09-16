# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SuppressionCreateParams"]


class SuppressionCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID."""

    email: Required[str]
    """The email address to suppress."""

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Expiration timestamp for the suppression.

    Omit or set to null for a permanent suppression that never expires.
    """

    note: str
    """Advisory note for this suppression. Not enforced or validated beyond length."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SuppressionImportParams", "Item"]


class SuppressionImportParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID."""

    items: Required[Iterable[Item]]
    """Suppressions to import.

    Items with a duplicate email address are deduplicated before processing.
    """


class Item(TypedDict, total=False):
    email: Required[str]
    """The email address to suppress."""

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Expiration timestamp for the suppression.

    Omit or set to null for a permanent suppression that never expires.
    """

    note: str
    """Advisory note for this suppression. Not enforced or validated beyond length."""

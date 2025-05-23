# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..hostname import Hostname
from ..redirect import Redirect
from ...._models import BaseModel

__all__ = ["ItemGetResponse", "UnionMember0", "UnionMember1"]


class UnionMember0(BaseModel):
    id: Optional[str] = None
    """The unique ID of the list."""

    asn: Optional[int] = None
    """Defines a non-negative 32 bit integer."""

    comment: Optional[str] = None
    """Defines an informative summary of the list item."""

    created_on: Optional[str] = None
    """The RFC 3339 timestamp of when the item was created."""

    hostname: Optional[Hostname] = None
    """
    Valid characters for hostnames are ASCII(7) letters from a to z, the digits from
    0 to 9, wildcards (\\**), and the hyphen (-).
    """

    ip: Optional[str] = None
    """An IPv4 address, an IPv4 CIDR, or an IPv6 CIDR.

    IPv6 CIDRs are limited to a maximum of /64.
    """

    modified_on: Optional[str] = None
    """The RFC 3339 timestamp of when the item was last modified."""

    redirect: Optional[Redirect] = None
    """The definition of the redirect."""


class UnionMember1(BaseModel):
    id: Optional[str] = None
    """The unique ID of the list."""

    asn: Optional[int] = None
    """Defines a non-negative 32 bit integer."""

    comment: Optional[str] = None
    """Defines an informative summary of the list item."""

    created_on: Optional[str] = None
    """The RFC 3339 timestamp of when the item was created."""

    hostname: Optional[Hostname] = None
    """
    Valid characters for hostnames are ASCII(7) letters from a to z, the digits from
    0 to 9, wildcards (\\**), and the hyphen (-).
    """

    ip: Optional[str] = None
    """An IPv4 address, an IPv4 CIDR, or an IPv6 CIDR.

    IPv6 CIDRs are limited to a maximum of /64.
    """

    modified_on: Optional[str] = None
    """The RFC 3339 timestamp of when the item was last modified."""

    redirect: Optional[Redirect] = None
    """The definition of the redirect."""


ItemGetResponse: TypeAlias = Union[UnionMember0, UnionMember1]

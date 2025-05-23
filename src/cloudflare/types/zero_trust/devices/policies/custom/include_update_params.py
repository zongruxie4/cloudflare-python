# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ...split_tunnel_include_param import SplitTunnelIncludeParam

__all__ = ["IncludeUpdateParams"]


class IncludeUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    body: Required[Iterable[SplitTunnelIncludeParam]]

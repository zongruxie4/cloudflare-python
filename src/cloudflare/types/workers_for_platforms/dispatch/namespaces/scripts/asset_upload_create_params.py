# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["AssetUploadCreateParams", "Manifest"]


class AssetUploadCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    dispatch_namespace: Required[str]
    """Name of the Workers for Platforms dispatch namespace."""

    manifest: Required[Dict[str, Manifest]]
    """A manifest ([path]: {hash, size}) map of files to upload.

    As an example, `/blog/hello-world.html` would be a valid path key.
    """


class Manifest(TypedDict, total=False):
    hash: Required[str]
    """The hash of the file."""

    size: Required[int]
    """The size of the file in bytes."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cache import (
    SmartTieredCacheGetResponse,
    SmartTieredCacheEditResponse,
    SmartTieredCacheDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSmartTieredCache:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        smart_tiered_cache = client.cache.smart_tiered_cache.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SmartTieredCacheDeleteResponse], smart_tiered_cache, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cache.smart_tiered_cache.with_raw_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_tiered_cache = response.parse()
        assert_matches_type(Optional[SmartTieredCacheDeleteResponse], smart_tiered_cache, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cache.smart_tiered_cache.with_streaming_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_tiered_cache = response.parse()
            assert_matches_type(Optional[SmartTieredCacheDeleteResponse], smart_tiered_cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.smart_tiered_cache.with_raw_response.delete(
                zone_id="",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        smart_tiered_cache = client.cache.smart_tiered_cache.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )
        assert_matches_type(Optional[SmartTieredCacheEditResponse], smart_tiered_cache, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.cache.smart_tiered_cache.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_tiered_cache = response.parse()
        assert_matches_type(Optional[SmartTieredCacheEditResponse], smart_tiered_cache, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.cache.smart_tiered_cache.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_tiered_cache = response.parse()
            assert_matches_type(Optional[SmartTieredCacheEditResponse], smart_tiered_cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.smart_tiered_cache.with_raw_response.edit(
                zone_id="",
                value="on",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        smart_tiered_cache = client.cache.smart_tiered_cache.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SmartTieredCacheGetResponse], smart_tiered_cache, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cache.smart_tiered_cache.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_tiered_cache = response.parse()
        assert_matches_type(Optional[SmartTieredCacheGetResponse], smart_tiered_cache, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cache.smart_tiered_cache.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_tiered_cache = response.parse()
            assert_matches_type(Optional[SmartTieredCacheGetResponse], smart_tiered_cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.smart_tiered_cache.with_raw_response.get(
                zone_id="",
            )


class TestAsyncSmartTieredCache:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        smart_tiered_cache = await async_client.cache.smart_tiered_cache.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SmartTieredCacheDeleteResponse], smart_tiered_cache, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.smart_tiered_cache.with_raw_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_tiered_cache = await response.parse()
        assert_matches_type(Optional[SmartTieredCacheDeleteResponse], smart_tiered_cache, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.smart_tiered_cache.with_streaming_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_tiered_cache = await response.parse()
            assert_matches_type(Optional[SmartTieredCacheDeleteResponse], smart_tiered_cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.smart_tiered_cache.with_raw_response.delete(
                zone_id="",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        smart_tiered_cache = await async_client.cache.smart_tiered_cache.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )
        assert_matches_type(Optional[SmartTieredCacheEditResponse], smart_tiered_cache, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.smart_tiered_cache.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_tiered_cache = await response.parse()
        assert_matches_type(Optional[SmartTieredCacheEditResponse], smart_tiered_cache, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.smart_tiered_cache.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_tiered_cache = await response.parse()
            assert_matches_type(Optional[SmartTieredCacheEditResponse], smart_tiered_cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.smart_tiered_cache.with_raw_response.edit(
                zone_id="",
                value="on",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        smart_tiered_cache = await async_client.cache.smart_tiered_cache.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SmartTieredCacheGetResponse], smart_tiered_cache, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.smart_tiered_cache.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_tiered_cache = await response.parse()
        assert_matches_type(Optional[SmartTieredCacheGetResponse], smart_tiered_cache, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.smart_tiered_cache.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_tiered_cache = await response.parse()
            assert_matches_type(Optional[SmartTieredCacheGetResponse], smart_tiered_cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.smart_tiered_cache.with_raw_response.get(
                zone_id="",
            )

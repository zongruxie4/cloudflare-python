# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.email_routing import Settings

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmailRouting:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_disable(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            email_routing = client.email_routing.disable(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(Optional[Settings], email_routing, path=["response"])

    @parametrize
    def test_raw_response_disable(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.email_routing.with_raw_response.disable(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_routing = response.parse()
        assert_matches_type(Optional[Settings], email_routing, path=["response"])

    @parametrize
    def test_streaming_response_disable(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.email_routing.with_streaming_response.disable(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                email_routing = response.parse()
                assert_matches_type(Optional[Settings], email_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_disable(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.email_routing.with_raw_response.disable(
                    zone_id="",
                    body={},
                )

    @parametrize
    def test_method_enable(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            email_routing = client.email_routing.enable(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(Optional[Settings], email_routing, path=["response"])

    @parametrize
    def test_raw_response_enable(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.email_routing.with_raw_response.enable(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_routing = response.parse()
        assert_matches_type(Optional[Settings], email_routing, path=["response"])

    @parametrize
    def test_streaming_response_enable(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.email_routing.with_streaming_response.enable(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                email_routing = response.parse()
                assert_matches_type(Optional[Settings], email_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_enable(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.email_routing.with_raw_response.enable(
                    zone_id="",
                    body={},
                )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        email_routing = client.email_routing.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Settings], email_routing, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.email_routing.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_routing = response.parse()
        assert_matches_type(Optional[Settings], email_routing, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.email_routing.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_routing = response.parse()
            assert_matches_type(Optional[Settings], email_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.email_routing.with_raw_response.get(
                zone_id="",
            )


class TestAsyncEmailRouting:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_disable(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            email_routing = await async_client.email_routing.disable(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(Optional[Settings], email_routing, path=["response"])

    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.email_routing.with_raw_response.disable(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_routing = await response.parse()
        assert_matches_type(Optional[Settings], email_routing, path=["response"])

    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.email_routing.with_streaming_response.disable(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                email_routing = await response.parse()
                assert_matches_type(Optional[Settings], email_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_disable(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.email_routing.with_raw_response.disable(
                    zone_id="",
                    body={},
                )

    @parametrize
    async def test_method_enable(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            email_routing = await async_client.email_routing.enable(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(Optional[Settings], email_routing, path=["response"])

    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.email_routing.with_raw_response.enable(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_routing = await response.parse()
        assert_matches_type(Optional[Settings], email_routing, path=["response"])

    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.email_routing.with_streaming_response.enable(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                email_routing = await response.parse()
                assert_matches_type(Optional[Settings], email_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_enable(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.email_routing.with_raw_response.enable(
                    zone_id="",
                    body={},
                )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        email_routing = await async_client.email_routing.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Settings], email_routing, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_routing.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_routing = await response.parse()
        assert_matches_type(Optional[Settings], email_routing, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_routing.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_routing = await response.parse()
            assert_matches_type(Optional[Settings], email_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.email_routing.with_raw_response.get(
                zone_id="",
            )

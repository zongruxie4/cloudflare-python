# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from .items import (
    ItemsResource,
    AsyncItemsResource,
    ItemsResourceWithRawResponse,
    AsyncItemsResourceWithRawResponse,
    ItemsResourceWithStreamingResponse,
    AsyncItemsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....types.rules import list_create_params, list_update_params
from ...._base_client import make_request_options
from .bulk_operations import (
    BulkOperationsResource,
    AsyncBulkOperationsResource,
    BulkOperationsResourceWithRawResponse,
    AsyncBulkOperationsResourceWithRawResponse,
    BulkOperationsResourceWithStreamingResponse,
    AsyncBulkOperationsResourceWithStreamingResponse,
)
from ....types.rules.list_get_response import ListGetResponse
from ....types.rules.list_list_response import ListListResponse
from ....types.rules.list_create_response import ListCreateResponse
from ....types.rules.list_delete_response import ListDeleteResponse
from ....types.rules.list_update_response import ListUpdateResponse

__all__ = ["ListsResource", "AsyncListsResource"]


class ListsResource(SyncAPIResource):
    @cached_property
    def bulk_operations(self) -> BulkOperationsResource:
        return BulkOperationsResource(self._client)

    @cached_property
    def items(self) -> ItemsResource:
        return ItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ListsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        kind: Literal["ip", "redirect", "hostname", "asn"],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListCreateResponse:
        """
        Creates a new list of the specified type.

        Args:
          account_id: Defines an identifier.

          kind: The type of the list. Each type supports specific list items (IP addresses,
              ASNs, hostnames or redirects).

          name: An informative name for the list. Use this name in filter and rule expressions.

          description: An informative summary of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            ListCreateResponse,
            self._post(
                f"/accounts/{account_id}/rules/lists",
                body=maybe_transform(
                    {
                        "kind": kind,
                        "name": name,
                        "description": description,
                    },
                    list_create_params.ListCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ListCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ListCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update(
        self,
        list_id: str,
        *,
        account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListUpdateResponse:
        """
        Updates the description of a list.

        Args:
          account_id: Defines an identifier.

          list_id: The unique ID of the list.

          description: An informative summary of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return cast(
            ListUpdateResponse,
            self._put(
                f"/accounts/{account_id}/rules/lists/{list_id}",
                body=maybe_transform({"description": description}, list_update_params.ListUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ListUpdateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ListUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListListResponse:
        """
        Fetches all lists in the account.

        Args:
          account_id: Defines an identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            ListListResponse,
            self._get(
                f"/accounts/{account_id}/rules/lists",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ListListResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ListListResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        list_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListDeleteResponse:
        """
        Deletes a specific list and all its items.

        Args:
          account_id: Defines an identifier.

          list_id: The unique ID of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return cast(
            ListDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/rules/lists/{list_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ListDeleteResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ListDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        list_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListGetResponse:
        """
        Fetches the details of a list.

        Args:
          account_id: Defines an identifier.

          list_id: The unique ID of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return cast(
            ListGetResponse,
            self._get(
                f"/accounts/{account_id}/rules/lists/{list_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ListGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ListGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncListsResource(AsyncAPIResource):
    @cached_property
    def bulk_operations(self) -> AsyncBulkOperationsResource:
        return AsyncBulkOperationsResource(self._client)

    @cached_property
    def items(self) -> AsyncItemsResource:
        return AsyncItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncListsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        kind: Literal["ip", "redirect", "hostname", "asn"],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListCreateResponse:
        """
        Creates a new list of the specified type.

        Args:
          account_id: Defines an identifier.

          kind: The type of the list. Each type supports specific list items (IP addresses,
              ASNs, hostnames or redirects).

          name: An informative name for the list. Use this name in filter and rule expressions.

          description: An informative summary of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            ListCreateResponse,
            await self._post(
                f"/accounts/{account_id}/rules/lists",
                body=await async_maybe_transform(
                    {
                        "kind": kind,
                        "name": name,
                        "description": description,
                    },
                    list_create_params.ListCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ListCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ListCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update(
        self,
        list_id: str,
        *,
        account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListUpdateResponse:
        """
        Updates the description of a list.

        Args:
          account_id: Defines an identifier.

          list_id: The unique ID of the list.

          description: An informative summary of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return cast(
            ListUpdateResponse,
            await self._put(
                f"/accounts/{account_id}/rules/lists/{list_id}",
                body=await async_maybe_transform({"description": description}, list_update_params.ListUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ListUpdateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ListUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListListResponse:
        """
        Fetches all lists in the account.

        Args:
          account_id: Defines an identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            ListListResponse,
            await self._get(
                f"/accounts/{account_id}/rules/lists",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ListListResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ListListResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        list_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListDeleteResponse:
        """
        Deletes a specific list and all its items.

        Args:
          account_id: Defines an identifier.

          list_id: The unique ID of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return cast(
            ListDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/rules/lists/{list_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ListDeleteResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ListDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        list_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListGetResponse:
        """
        Fetches the details of a list.

        Args:
          account_id: Defines an identifier.

          list_id: The unique ID of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return cast(
            ListGetResponse,
            await self._get(
                f"/accounts/{account_id}/rules/lists/{list_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ListGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ListGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ListsResourceWithRawResponse:
    def __init__(self, lists: ListsResource) -> None:
        self._lists = lists

        self.create = to_raw_response_wrapper(
            lists.create,
        )
        self.update = to_raw_response_wrapper(
            lists.update,
        )
        self.list = to_raw_response_wrapper(
            lists.list,
        )
        self.delete = to_raw_response_wrapper(
            lists.delete,
        )
        self.get = to_raw_response_wrapper(
            lists.get,
        )

    @cached_property
    def bulk_operations(self) -> BulkOperationsResourceWithRawResponse:
        return BulkOperationsResourceWithRawResponse(self._lists.bulk_operations)

    @cached_property
    def items(self) -> ItemsResourceWithRawResponse:
        return ItemsResourceWithRawResponse(self._lists.items)


class AsyncListsResourceWithRawResponse:
    def __init__(self, lists: AsyncListsResource) -> None:
        self._lists = lists

        self.create = async_to_raw_response_wrapper(
            lists.create,
        )
        self.update = async_to_raw_response_wrapper(
            lists.update,
        )
        self.list = async_to_raw_response_wrapper(
            lists.list,
        )
        self.delete = async_to_raw_response_wrapper(
            lists.delete,
        )
        self.get = async_to_raw_response_wrapper(
            lists.get,
        )

    @cached_property
    def bulk_operations(self) -> AsyncBulkOperationsResourceWithRawResponse:
        return AsyncBulkOperationsResourceWithRawResponse(self._lists.bulk_operations)

    @cached_property
    def items(self) -> AsyncItemsResourceWithRawResponse:
        return AsyncItemsResourceWithRawResponse(self._lists.items)


class ListsResourceWithStreamingResponse:
    def __init__(self, lists: ListsResource) -> None:
        self._lists = lists

        self.create = to_streamed_response_wrapper(
            lists.create,
        )
        self.update = to_streamed_response_wrapper(
            lists.update,
        )
        self.list = to_streamed_response_wrapper(
            lists.list,
        )
        self.delete = to_streamed_response_wrapper(
            lists.delete,
        )
        self.get = to_streamed_response_wrapper(
            lists.get,
        )

    @cached_property
    def bulk_operations(self) -> BulkOperationsResourceWithStreamingResponse:
        return BulkOperationsResourceWithStreamingResponse(self._lists.bulk_operations)

    @cached_property
    def items(self) -> ItemsResourceWithStreamingResponse:
        return ItemsResourceWithStreamingResponse(self._lists.items)


class AsyncListsResourceWithStreamingResponse:
    def __init__(self, lists: AsyncListsResource) -> None:
        self._lists = lists

        self.create = async_to_streamed_response_wrapper(
            lists.create,
        )
        self.update = async_to_streamed_response_wrapper(
            lists.update,
        )
        self.list = async_to_streamed_response_wrapper(
            lists.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            lists.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            lists.get,
        )

    @cached_property
    def bulk_operations(self) -> AsyncBulkOperationsResourceWithStreamingResponse:
        return AsyncBulkOperationsResourceWithStreamingResponse(self._lists.bulk_operations)

    @cached_property
    def items(self) -> AsyncItemsResourceWithStreamingResponse:
        return AsyncItemsResourceWithStreamingResponse(self._lists.items)

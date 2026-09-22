# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ConsumerUpdateParams",
    "MqWorkerConsumerRequest",
    "MqWorkerConsumerRequestSettings",
    "MqHTTPConsumerRequest",
    "MqHTTPConsumerRequestSettings",
    "MqNotificationConsumerRequest",
    "MqNotificationConsumerRequestSettings",
    "MqNotificationConsumerRequestSettingsUnionMember0",
    "MqNotificationConsumerRequestSettingsUnionMember0Email",
    "MqNotificationConsumerRequestSettingsUnionMember0Pagerduty",
    "MqNotificationConsumerRequestSettingsUnionMember0Webhook",
    "MqNotificationConsumerRequestSettingsUnionMember1",
    "MqNotificationConsumerRequestSettingsUnionMember1Webhook",
    "MqNotificationConsumerRequestSettingsUnionMember1Email",
    "MqNotificationConsumerRequestSettingsUnionMember1Pagerduty",
    "MqNotificationConsumerRequestSettingsUnionMember2",
    "MqNotificationConsumerRequestSettingsUnionMember2Pagerduty",
    "MqNotificationConsumerRequestSettingsUnionMember2Email",
    "MqNotificationConsumerRequestSettingsUnionMember2Webhook",
]


class MqWorkerConsumerRequest(TypedDict, total=False):
    account_id: Required[str]
    """A Resource identifier."""

    queue_id: Required[str]
    """A Resource identifier."""

    script_name: Required[str]
    """Name of a Worker"""

    type: Required[Literal["worker"]]

    dead_letter_queue: str

    settings: MqWorkerConsumerRequestSettings


class MqWorkerConsumerRequestSettings(TypedDict, total=False):
    batch_size: float
    """The maximum number of messages to include in a batch."""

    max_concurrency: float
    """Maximum number of concurrent consumers that may consume from this Queue.

    Set to `null` to automatically opt in to the platform's maximum (recommended).
    """

    max_retries: float
    """The maximum number of retries"""

    max_wait_time_ms: float
    """
    The number of milliseconds to wait for a batch to fill up before attempting to
    deliver it
    """

    retry_delay: float
    """
    The number of seconds to delay before making the message available for another
    attempt.
    """


class MqHTTPConsumerRequest(TypedDict, total=False):
    account_id: Required[str]
    """A Resource identifier."""

    queue_id: Required[str]
    """A Resource identifier."""

    type: Required[Literal["http_pull"]]

    dead_letter_queue: str

    settings: MqHTTPConsumerRequestSettings


class MqHTTPConsumerRequestSettings(TypedDict, total=False):
    batch_size: float
    """The maximum number of messages to include in a batch."""

    max_retries: float
    """The maximum number of retries"""

    retry_delay: float
    """
    The number of seconds to delay before making the message available for another
    attempt.
    """

    visibility_timeout_ms: float
    """The number of milliseconds that a message is exclusively leased.

    After the timeout, the message becomes available for another attempt.
    """


class MqNotificationConsumerRequest(TypedDict, total=False):
    account_id: Required[str]
    """A Resource identifier."""

    queue_id: Required[str]
    """A Resource identifier."""

    settings: Required[MqNotificationConsumerRequestSettings]
    """Notification destinations for a Queue.

    At least one email, webhook, or PagerDuty destination is required.
    """

    type: Required[Literal["notification"]]

    dead_letter_queue: str


class MqNotificationConsumerRequestSettingsUnionMember0Email(TypedDict, total=False):
    id: Required[str]
    """The email address."""


class MqNotificationConsumerRequestSettingsUnionMember0Pagerduty(TypedDict, total=False):
    id: Required[str]
    """UUID."""


class MqNotificationConsumerRequestSettingsUnionMember0Webhook(TypedDict, total=False):
    id: Required[str]
    """UUID."""


class MqNotificationConsumerRequestSettingsUnionMember0(TypedDict, total=False):
    email: Required[Iterable[MqNotificationConsumerRequestSettingsUnionMember0Email]]

    pagerduty: Iterable[MqNotificationConsumerRequestSettingsUnionMember0Pagerduty]
    """PagerDuty notification destinations."""

    webhooks: Iterable[MqNotificationConsumerRequestSettingsUnionMember0Webhook]
    """Webhook notification destinations."""


class MqNotificationConsumerRequestSettingsUnionMember1Webhook(TypedDict, total=False):
    id: Required[str]
    """UUID."""


class MqNotificationConsumerRequestSettingsUnionMember1Email(TypedDict, total=False):
    id: Required[str]
    """The email address."""


class MqNotificationConsumerRequestSettingsUnionMember1Pagerduty(TypedDict, total=False):
    id: Required[str]
    """UUID."""


class MqNotificationConsumerRequestSettingsUnionMember1(TypedDict, total=False):
    webhooks: Required[Iterable[MqNotificationConsumerRequestSettingsUnionMember1Webhook]]

    email: Iterable[MqNotificationConsumerRequestSettingsUnionMember1Email]
    """Email notification destinations."""

    pagerduty: Iterable[MqNotificationConsumerRequestSettingsUnionMember1Pagerduty]
    """PagerDuty notification destinations."""


class MqNotificationConsumerRequestSettingsUnionMember2Pagerduty(TypedDict, total=False):
    id: Required[str]
    """UUID."""


class MqNotificationConsumerRequestSettingsUnionMember2Email(TypedDict, total=False):
    id: Required[str]
    """The email address."""


class MqNotificationConsumerRequestSettingsUnionMember2Webhook(TypedDict, total=False):
    id: Required[str]
    """UUID."""


class MqNotificationConsumerRequestSettingsUnionMember2(TypedDict, total=False):
    pagerduty: Required[Iterable[MqNotificationConsumerRequestSettingsUnionMember2Pagerduty]]

    email: Iterable[MqNotificationConsumerRequestSettingsUnionMember2Email]
    """Email notification destinations."""

    webhooks: Iterable[MqNotificationConsumerRequestSettingsUnionMember2Webhook]
    """Webhook notification destinations."""


MqNotificationConsumerRequestSettings: TypeAlias = Union[
    MqNotificationConsumerRequestSettingsUnionMember0,
    MqNotificationConsumerRequestSettingsUnionMember1,
    MqNotificationConsumerRequestSettingsUnionMember2,
]

ConsumerUpdateParams: TypeAlias = Union[MqWorkerConsumerRequest, MqHTTPConsumerRequest, MqNotificationConsumerRequest]

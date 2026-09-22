# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "Consumer",
    "MqWorkerConsumerResponse",
    "MqWorkerConsumerResponseSettings",
    "MqHTTPConsumerResponse",
    "MqHTTPConsumerResponseSettings",
    "MqNotificationConsumerResponse",
    "MqNotificationConsumerResponseSettings",
    "MqNotificationConsumerResponseSettingsUnionMember0",
    "MqNotificationConsumerResponseSettingsUnionMember0Email",
    "MqNotificationConsumerResponseSettingsUnionMember0Pagerduty",
    "MqNotificationConsumerResponseSettingsUnionMember0Webhook",
    "MqNotificationConsumerResponseSettingsUnionMember1",
    "MqNotificationConsumerResponseSettingsUnionMember1Webhook",
    "MqNotificationConsumerResponseSettingsUnionMember1Email",
    "MqNotificationConsumerResponseSettingsUnionMember1Pagerduty",
    "MqNotificationConsumerResponseSettingsUnionMember2",
    "MqNotificationConsumerResponseSettingsUnionMember2Pagerduty",
    "MqNotificationConsumerResponseSettingsUnionMember2Email",
    "MqNotificationConsumerResponseSettingsUnionMember2Webhook",
]


class MqWorkerConsumerResponseSettings(BaseModel):
    batch_size: Optional[float] = None
    """The maximum number of messages to include in a batch."""

    max_concurrency: Optional[float] = None
    """Maximum number of concurrent consumers that may consume from this Queue.

    Set to `null` to automatically opt in to the platform's maximum (recommended).
    """

    max_retries: Optional[float] = None
    """The maximum number of retries"""

    max_wait_time_ms: Optional[float] = None
    """
    The number of milliseconds to wait for a batch to fill up before attempting to
    deliver it
    """

    retry_delay: Optional[float] = None
    """
    The number of seconds to delay before making the message available for another
    attempt.
    """


class MqWorkerConsumerResponse(BaseModel):
    consumer_id: Optional[str] = None
    """A Resource identifier."""

    created_on: Optional[datetime] = None

    dead_letter_queue: Optional[str] = None
    """Name of the dead letter queue, or empty string if not configured"""

    queue_name: Optional[str] = None

    script_name: Optional[str] = None
    """Name of a Worker"""

    settings: Optional[MqWorkerConsumerResponseSettings] = None

    type: Optional[Literal["worker"]] = None


class MqHTTPConsumerResponseSettings(BaseModel):
    batch_size: Optional[float] = None
    """The maximum number of messages to include in a batch."""

    max_retries: Optional[float] = None
    """The maximum number of retries"""

    retry_delay: Optional[float] = None
    """
    The number of seconds to delay before making the message available for another
    attempt.
    """

    visibility_timeout_ms: Optional[float] = None
    """The number of milliseconds that a message is exclusively leased.

    After the timeout, the message becomes available for another attempt.
    """


class MqHTTPConsumerResponse(BaseModel):
    consumer_id: Optional[str] = None
    """A Resource identifier."""

    created_on: Optional[datetime] = None

    dead_letter_queue: Optional[str] = None
    """Name of the dead letter queue, or empty string if not configured"""

    queue_name: Optional[str] = None

    settings: Optional[MqHTTPConsumerResponseSettings] = None

    type: Optional[Literal["http_pull"]] = None


class MqNotificationConsumerResponseSettingsUnionMember0Email(BaseModel):
    id: str
    """The email address."""


class MqNotificationConsumerResponseSettingsUnionMember0Pagerduty(BaseModel):
    id: str
    """UUID."""


class MqNotificationConsumerResponseSettingsUnionMember0Webhook(BaseModel):
    id: str
    """UUID."""


class MqNotificationConsumerResponseSettingsUnionMember0(BaseModel):
    email: List[MqNotificationConsumerResponseSettingsUnionMember0Email]

    pagerduty: Optional[List[MqNotificationConsumerResponseSettingsUnionMember0Pagerduty]] = None
    """PagerDuty notification destinations."""

    webhooks: Optional[List[MqNotificationConsumerResponseSettingsUnionMember0Webhook]] = None
    """Webhook notification destinations."""


class MqNotificationConsumerResponseSettingsUnionMember1Webhook(BaseModel):
    id: str
    """UUID."""


class MqNotificationConsumerResponseSettingsUnionMember1Email(BaseModel):
    id: str
    """The email address."""


class MqNotificationConsumerResponseSettingsUnionMember1Pagerduty(BaseModel):
    id: str
    """UUID."""


class MqNotificationConsumerResponseSettingsUnionMember1(BaseModel):
    webhooks: List[MqNotificationConsumerResponseSettingsUnionMember1Webhook]

    email: Optional[List[MqNotificationConsumerResponseSettingsUnionMember1Email]] = None
    """Email notification destinations."""

    pagerduty: Optional[List[MqNotificationConsumerResponseSettingsUnionMember1Pagerduty]] = None
    """PagerDuty notification destinations."""


class MqNotificationConsumerResponseSettingsUnionMember2Pagerduty(BaseModel):
    id: str
    """UUID."""


class MqNotificationConsumerResponseSettingsUnionMember2Email(BaseModel):
    id: str
    """The email address."""


class MqNotificationConsumerResponseSettingsUnionMember2Webhook(BaseModel):
    id: str
    """UUID."""


class MqNotificationConsumerResponseSettingsUnionMember2(BaseModel):
    pagerduty: List[MqNotificationConsumerResponseSettingsUnionMember2Pagerduty]

    email: Optional[List[MqNotificationConsumerResponseSettingsUnionMember2Email]] = None
    """Email notification destinations."""

    webhooks: Optional[List[MqNotificationConsumerResponseSettingsUnionMember2Webhook]] = None
    """Webhook notification destinations."""


MqNotificationConsumerResponseSettings: TypeAlias = Union[
    MqNotificationConsumerResponseSettingsUnionMember0,
    MqNotificationConsumerResponseSettingsUnionMember1,
    MqNotificationConsumerResponseSettingsUnionMember2,
]


class MqNotificationConsumerResponse(BaseModel):
    consumer_id: Optional[str] = None
    """A Resource identifier."""

    created_on: Optional[datetime] = None

    dead_letter_queue: Optional[str] = None
    """Name of the dead letter queue, or empty string if not configured."""

    queue_name: Optional[str] = None

    settings: Optional[MqNotificationConsumerResponseSettings] = None
    """Notification destinations for a Queue.

    At least one email, webhook, or PagerDuty destination is required.
    """

    type: Optional[Literal["notification"]] = None


Consumer: TypeAlias = Annotated[
    Union[MqWorkerConsumerResponse, MqHTTPConsumerResponse, MqNotificationConsumerResponse],
    PropertyInfo(discriminator="type"),
]

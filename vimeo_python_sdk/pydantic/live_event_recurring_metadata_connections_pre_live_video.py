# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from vimeo_python_sdk.pydantic.live_event_recurring_metadata_connections_pre_live_video_options import LiveEventRecurringMetadataConnectionsPreLiveVideoOptions

class LiveEventRecurringMetadataConnectionsPreLiveVideo(BaseModel):
    options: LiveEventRecurringMetadataConnectionsPreLiveVideoOptions = Field(alias='options')

    # The status of the pre-live video's RTMP link.  Option descriptions:  * `pending` - Vimeo is working on setting up the connection.  * `ready` - Resources have been provisioned for the event.  * `streaming` - Live video is currently streaming to the RTMP link.  * `unavailable` - The connection is ready, but streaming to the RTMP link has not yet begun. 
    status: Literal["pending", "ready", "streaming", "unavailable"] = Field(alias='status')

    # The API URI that resolves to the connection data.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

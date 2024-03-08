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

from vimeo_python_sdk.type.live_event_session_status_archive import LiveEventSessionStatusArchive
from vimeo_python_sdk.type.live_event_session_status_ingest import LiveEventSessionStatusIngest
from vimeo_python_sdk.type.live_event_session_status_metering import LiveEventSessionStatusMetering

class RequiredLiveEventSessionStatus(TypedDict):
    archive: LiveEventSessionStatusArchive

    # Whether the current user can manage the event.
    can_manage: bool

    # The ID of the live video.
    id: typing.Union[int, float]

    ingest: LiveEventSessionStatusIngest

    metering: LiveEventSessionStatusMetering

    # The status of the live event.  Option descriptions:  * `ended` - The live event has ended.  * `started` - The live event has started. 
    status: typing.Optional[str]

    # The stream mode of the event.  Option descriptions:  * `live` - The stream is live playback.  * `record` - The stream is in record mode.  * `simulive` - The stream is scheduled media playback. 
    stream_mode: str

class OptionalLiveEventSessionStatus(TypedDict, total=False):
    pass

class LiveEventSessionStatus(RequiredLiveEventSessionStatus, OptionalLiveEventSessionStatus):
    pass

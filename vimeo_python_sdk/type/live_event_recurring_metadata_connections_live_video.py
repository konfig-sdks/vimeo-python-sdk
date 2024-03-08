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

from vimeo_python_sdk.type.live_event_recurring_metadata_connections_live_video_options import LiveEventRecurringMetadataConnectionsLiveVideoOptions

class RequiredLiveEventRecurringMetadataConnectionsLiveVideo(TypedDict):
    options: LiveEventRecurringMetadataConnectionsLiveVideoOptions

    # The status of the live video's RTMP link.  Option descriptions:  * `streaming` - The stream is open and receiving content. 
    status: str

    # The API URI that resolves to the connection data.
    uri: str

class OptionalLiveEventRecurringMetadataConnectionsLiveVideo(TypedDict, total=False):
    pass

class LiveEventRecurringMetadataConnectionsLiveVideo(RequiredLiveEventRecurringMetadataConnectionsLiveVideo, OptionalLiveEventRecurringMetadataConnectionsLiveVideo):
    pass

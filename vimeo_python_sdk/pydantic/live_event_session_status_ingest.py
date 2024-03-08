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


class LiveEventSessionStatusIngest(BaseModel):
    # The protocol used for this session.  Option descriptions:  * `dash` - The protocol is DASH.  * `rtmp` - The protocol is RTMP.  * `simple_live` - The protocol is Simplelive.  * `studio_cloud` - The protocol is StudioCloud.  * `unknown` - The protocol is unknown or not set.  * `webrtc` - The protocol is WebRTC. 
    encoder_type: Literal["dash", "rtmp", "simple_live", "studio_cloud", "unknown", "webrtc"] = Field(alias='encoder_type')

    # The timestamp in UTC format when the live stream ended.
    end_time: typing.Optional[typing.Union[int, float]] = Field(alias='end_time')

    # The height of the live video in pixels.
    height: typing.Optional[typing.Union[int, float]] = Field(alias='height')

    # Whether the session is using RTMP.
    is_rtmp_session: bool = Field(alias='is_rtmp_session')

    # Whether the stream is scheduled media playback.
    is_scheduled_playback: typing.Optional[bool] = Field(alias='is_scheduled_playback')

    # The time in ISO 8601 format when the RTMP expires.
    rtmp_expires_at: typing.Optional[str] = Field(alias='rtmp_expires_at')

    # The upstream RTMP link. Send your live content to this link to create a live video on the event.
    rtmp_link: typing.Optional[str] = Field(alias='rtmp_link')

    # The upstream RTMPS link. Send your live content to this secure link to create a live video on the event.
    rtmps_link: typing.Optional[str] = Field(alias='rtmps_link')

    # The scheduled start time of the live video in ISO 8601 format.
    scheduled_start_time: typing.Optional[str] = Field(alias='scheduled_start_time')

    # The session ID.
    session_id: typing.Optional[str] = Field(alias='session_id')

    # The timestamp in UTC format when the live video started.
    start_time: typing.Optional[typing.Union[int, float]] = Field(alias='start_time')

    # The ingest status of the live video.  Option descriptions:  * `0` - There’s a live video, but no RMTP URL or key.  * `1` - There’s an RMTP URL and key, but the machine is provisioning.  * `2` - There’s an RMTP URL and key, and the machine is provisioned, but the stream hasn’t started yet.  * `3` - There’s an RMTP URL and key, and the machine is provisioned, but the stream didn’t start before the machine timed out.  * `4` - The stream has started and is currently underway.  * `5` - The stream has ended. 
    status: Literal["0", "1", "2", "3", "4", "5"] = Field(alias='status')

    # The reason why the stream ended. If the stream hasn't ended, this field is empty.
    stream_ended_reason: typing.Optional[typing.Union[int, float]] = Field(alias='stream_ended_reason')

    # The stream key used in conjunction with the RTMP and RTMPS links.
    stream_key: typing.Optional[str] = Field(alias='stream_key')

    # The width of the live video in pixels.
    width: typing.Optional[typing.Union[int, float]] = Field(alias='width')
    class Config:
        arbitrary_types_allowed = True

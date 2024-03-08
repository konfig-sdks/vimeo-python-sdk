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

from vimeo_python_sdk.pydantic.live_event_schedule_weekdays import LiveEventScheduleWeekdays

class LiveEventSchedule(BaseModel):
    # The schedule of the live event.  Option descriptions:  * `single` - The event is live only once.  * `weekly` - The event is live on a recurring weekly basis. 
    type: Literal["single", "weekly"] = Field(alias='type')

    # When **schedule.type** is `weekly`, the time in ISO 8601 format when the event is expected to be live.
    daily_time: typing.Optional[str] = Field(None, alias='daily_time')

    # The time in ISO 8601 format when the live event is expected to end.
    end_time: typing.Optional[str] = Field(None, alias='end_time')

    # The recurrence rule for the event's schedule according to [RFC 5545](https://datatracker.ietf.org/doc/html/rfc5545).
    rrule: typing.Optional[str] = Field(None, alias='rrule')

    # When **schedule.type** is `weekly`, the time in ISO 8601 format when the first occurrence of the event is expected to be live.
    scheduled_time: typing.Optional[str] = Field(None, alias='scheduled_time')

    # The time in ISO 8601 format when the live event is expected to be live.
    start_time: typing.Optional[str] = Field(None, alias='start_time')

    # The time zone of the live event.
    time_zone: typing.Optional[str] = Field(None, alias='time_zone')

    weekdays: typing.Optional[LiveEventScheduleWeekdays] = Field(None, alias='weekdays')
    class Config:
        arbitrary_types_allowed = True

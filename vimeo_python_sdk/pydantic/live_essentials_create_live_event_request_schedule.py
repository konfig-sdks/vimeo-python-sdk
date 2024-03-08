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

from vimeo_python_sdk.pydantic.live_essentials_create_live_event_request_schedule_weekdays import LiveEssentialsCreateLiveEventRequestScheduleWeekdays

class LiveEssentialsCreateLiveEventRequestSchedule(BaseModel):
    # The time in ISO 8601 format when the event is expected to be live, with the zero UTC offset `Z`. This parameter is required when **schedule.type** is `weekly`.
    daily_time: typing.Optional[str] = Field(None, alias='daily_time')

    # How often the event is expected to be live.  Option descriptions:  * `single` - The event is live one time only.  * `weekly` - The event is live on a weekly basis. 
    type: typing.Optional[Literal["single", "weekly"]] = Field(None, alias='type')

    weekdays: typing.Optional[LiveEssentialsCreateLiveEventRequestScheduleWeekdays] = Field(None, alias='weekdays')
    class Config:
        arbitrary_types_allowed = True

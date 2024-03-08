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

from vimeo_python_sdk.pydantic.webinar_schedule_weekdays import WebinarScheduleWeekdays

class WebinarSchedule(BaseModel):
    # The time in ISO 8601 format at which the webinar is expected to be live when **schedule.type** is `weekly`.
    daily_time: str = Field(alias='daily_time')

    # The date in ISO 8601 format on which the webinar is expected to end. This field applies when **schedule.type** is `single`.
    end_time: str = Field(alias='end_time')

    # The date in ISO 8601 format on which the first occurrence of the webinar is expected to be live when **schedule.type** is `weekly`.
    scheduled_time: typing.Optional[str] = Field(alias='scheduled_time')

    # The date in ISO 8601 format on which the webinar is expected to be live when **schedule.type** is `single`.
    start_time: str = Field(alias='start_time')

    # The schedule of the webinar.  Option descriptions:  * `single` - The webinar is live only once.  * `weekly` - The webinar is live on a recurring weekly basis. 
    type: Literal["single", "weekly"] = Field(alias='type')

    weekdays: WebinarScheduleWeekdays = Field(alias='weekdays')
    class Config:
        arbitrary_types_allowed = True

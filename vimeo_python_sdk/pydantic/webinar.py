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

from vimeo_python_sdk.pydantic.email_capture_form import EmailCaptureForm
from vimeo_python_sdk.pydantic.user import User
from vimeo_python_sdk.pydantic.webinar_edit import WebinarEdit
from vimeo_python_sdk.pydantic.webinar_email_provider_list import WebinarEmailProviderList
from vimeo_python_sdk.pydantic.webinar_email_quota import WebinarEmailQuota
from vimeo_python_sdk.pydantic.webinar_email_settings import WebinarEmailSettings
from vimeo_python_sdk.pydantic.webinar_events import WebinarEvents
from vimeo_python_sdk.pydantic.webinar_metadata import WebinarMetadata
from vimeo_python_sdk.pydantic.webinar_privacy import WebinarPrivacy
from vimeo_python_sdk.pydantic.webinar_registration_data import WebinarRegistrationData
from vimeo_python_sdk.pydantic.webinar_schedule import WebinarSchedule

class Webinar(BaseModel):
    # The title of the webinar.
    title: typing.Optional[str] = Field(alias='title')

    # The description of the webinar.
    description: typing.Optional[str] = Field(alias='description')

    # The time in ISO 8601 format when the webinar was completed.
    completed_on: str = Field(alias='completed_on')

    # The time in ISO 8601 format when the webinar was created.
    created_time: str = Field(alias='created_time')

    edit: WebinarEdit = Field(alias='edit')

    email_provider_list: WebinarEmailProviderList = Field(alias='email_provider_list')

    email_quota: WebinarEmailQuota = Field(alias='email_quota')

    # The settings for emails that are sent about the webinar.
    email_settings: WebinarEmailSettings = Field(alias='email_settings')

    events: WebinarEvents = Field(alias='events')

    # Whether polls are associated with the webinar.
    has_polls: bool = Field(alias='has_polls')

    metadata: WebinarMetadata = Field(alias='metadata')

    # The time in ISO 8601 format when the webinar was modified.
    modified_on: str = Field(alias='modified_on')

    # The date in ISO 8601 format on which the next occurrence of the webinar is expected to be live.
    next_occurrence_time: typing.Optional[str] = Field(alias='next_occurrence_time')

    # The password used to access the videos generated by streaming to the webinar event.
    password: typing.Optional[str] = Field(alias='password')

    privacy: WebinarPrivacy = Field(alias='privacy')

    registration_data: WebinarRegistrationData = Field(alias='registration_data')

    # The registration form settings associated with the webinar.
    registration_form: EmailCaptureForm = Field(alias='registration_form')

    schedule: WebinarSchedule = Field(alias='schedule')

    # The status of the webinar.  Option descriptions:  * `ended` - The webinar has ended.  * `started` - The webinar has started. 
    status: Literal["ended", "started"] = Field(alias='status')

    # The time zone used in resolving the timestamps that are included in the automatically generated video titles for the webinar.
    time_zone: str = Field(alias='time_zone')

    # The webinar's canonical relative URI.
    uri: str = Field(alias='uri')

    # The owner of the webinar.
    user: User = Field(alias='user')
    class Config:
        arbitrary_types_allowed = True

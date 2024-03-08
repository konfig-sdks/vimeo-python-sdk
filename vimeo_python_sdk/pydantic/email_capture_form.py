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

from vimeo_python_sdk.pydantic.email_capture_form_custom_fields import EmailCaptureFormCustomFields
from vimeo_python_sdk.pydantic.email_capture_form_email_lists import EmailCaptureFormEmailLists
from vimeo_python_sdk.pydantic.email_capture_form_hidden_fields import EmailCaptureFormHiddenFields

class EmailCaptureForm(BaseModel):
    # The ID of the video associated with the form. If there is no associated video, the value of this field is `-1`.
    clip_id: typing.Union[int, float] = Field(alias='clip_id')

    # The time in ISO 8601 format when the form was created.
    created_time: str = Field(alias='created_time')

    custom_fields: EmailCaptureFormCustomFields = Field(alias='custom_fields')

    # The ID of the logo image to display on the form.
    custom_logo: typing.Union[int, float] = Field(alias='custom_logo')

    # The message to display on the form.
    custom_message: str = Field(alias='custom_message')

    email_lists: EmailCaptureFormEmailLists = Field(alias='email_lists')

    hidden_fields: EmailCaptureFormHiddenFields = Field(alias='hidden_fields')

    # The ID of the email capture form.
    id: typing.Union[int, float] = Field(alias='id')

    # When the form appears relative to the video playback.  Option descriptions:  * `after-video` - The form appears immediately after the video ends.  * `before-video` - The form appears before the video begins.  * `during-video` - The form appears during the video at the time specified by the **timecode** field. 
    position: Literal["after-video", "before-video", "during-video"] = Field(alias='position')

    # The URL of the privacy policy related to the form.
    privacy_policy: str = Field(alias='privacy_policy')

    # Whether the user can skip the form.
    skippable: bool = Field(alias='skippable')

    # The timecode for when the form appears. This field is used when the value of **position** is `during-video`.
    timecode: str = Field(alias='timecode')

    # The canonical relative URI of the video's email capture form.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

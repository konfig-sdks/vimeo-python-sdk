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


class WebinarEmailContent(BaseModel):
    # The HTML body of the email.
    body: str = Field(alias='body')

    # The target link for the call-to-action button in the email.
    button_link: str = Field(alias='button_link')

    # The text for the call-to-action button in the email.
    button_text: str = Field(alias='button_text')

    # The HTML header section of the email.
    header: str = Field(alias='header')

    # The time in ISO 8601 format when the webinar email content was updated.
    modified_time: str = Field(alias='modified_time')

    # The HTML subject of the email.
    subject: str = Field(alias='subject')

    # The email type for which the content was customized.  Option descriptions:  * `email_event_reminder_24_hrs` - The webinar reminder email, which goes out 24 hours before the event.  * `email_post_event_thank_you` - The webinar post-event thank-you email.  * `email_registration_confirmation` - The webinar registration confirmation email. 
    type: Literal["email_event_reminder_24_hrs", "email_post_event_thank_you", "email_registration_confirmation"] = Field(alias='type')

    # Whether to show the calendar in the email.
    use_calender: bool = Field(alias='use_calender')

    # Whether to include a custom link in emails that are sent about the webinar.
    use_custom_link: bool = Field(alias='use_custom_link')
    class Config:
        arbitrary_types_allowed = True

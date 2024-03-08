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


class RequiredUpdateWebinarRequestEmailSettingsEmailPreferences(TypedDict):
    pass

class OptionalUpdateWebinarRequestEmailSettingsEmailPreferences(TypedDict, total=False):
    # Whether to send a reminder email 15 minutes before the webinar starts. _This field is deprecated._
    email_event_reminder_15_min: bool

    # Whether to send a reminder email 1 hour before the webinar starts. _This field is deprecated._
    email_event_reminder_1_hrs: bool

    # Whether to send a reminder email 24 hours before the webinar starts. _This field is deprecated._
    email_event_reminder_24_hrs: bool

    # Whether to send post-event thank-you emails to no-shows. _This field is deprecated._
    email_post_event_no_show_thank_you: bool

    # Whether to send post-event thank-you emails. _This field is deprecated._
    email_post_event_thank_you: bool

    # Whether to send a registration confirmation email after webinar registration. _This field is deprecated._
    email_registration_confirmation: bool

class UpdateWebinarRequestEmailSettingsEmailPreferences(RequiredUpdateWebinarRequestEmailSettingsEmailPreferences, OptionalUpdateWebinarRequestEmailSettingsEmailPreferences):
    pass

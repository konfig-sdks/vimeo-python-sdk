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

from vimeo_python_sdk.pydantic.webinar_emails_customize_preferences_request_email_preferences import WebinarEmailsCustomizePreferencesRequestEmailPreferences

class WebinarEmailsCustomizePreferencesRequest(BaseModel):
    # The accent color scheme for emails that are sent about the webinar.
    accent_color: typing.Optional[str] = Field(None, alias='accent_color')

    # The custom link for emails that are sent about the webinar.
    custom_link: typing.Optional[str] = Field(None, alias='custom_link')

    # The email customization details for the webinar reminder email, which goes out 24 hours before the event.
    email_event_reminder_24_hrs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='email_event_reminder_24_hrs')

    # The email customization details for the webinar post-event thank-you email.
    email_post_event_thank_you: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='email_post_event_thank_you')

    email_preferences: typing.Optional[WebinarEmailsCustomizePreferencesRequestEmailPreferences] = Field(None, alias='email_preferences')

    # The email customization details for the webinar registration confirmation email.
    email_registration_confirmation: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='email_registration_confirmation')

    # The name of the sender for emails that are sent about the webinar.
    from_: typing.Optional[str] = Field(None, alias='from')

    # The URI of the logo image to include in emails that are sent about the webinar.
    logo_uri: typing.Optional[str] = Field(None, alias='logo_uri')

    # The sender's reply email address.
    reply_email: typing.Optional[str] = Field(None, alias='reply_email')

    # The sender's physical address.
    sender_address: typing.Optional[str] = Field(None, alias='sender_address')

    # The URL of the sender's privacy policy.
    sender_policy_url: typing.Optional[str] = Field(None, alias='sender_policy_url')

    # Whether to include a custom link in emails that are sent about the webinar.
    use_custom_link: typing.Optional[bool] = Field(None, alias='use_custom_link')

    # Whether to include a reply link in the footer of emails that are sent about the webinar.
    use_reply_email: typing.Optional[bool] = Field(None, alias='use_reply_email')

    # Whether to include the sender's physical address in the footer of emails that are sent about the webinar.
    use_sender_address: typing.Optional[bool] = Field(None, alias='use_sender_address')

    # Whether to include the URL of the sender's privacy policy in the footer of emails that are sent about the webinar.
    use_sender_policy_url: typing.Optional[bool] = Field(None, alias='use_sender_policy_url')
    class Config:
        arbitrary_types_allowed = True

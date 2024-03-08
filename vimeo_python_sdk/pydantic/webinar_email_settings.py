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

from vimeo_python_sdk.pydantic.picture import Picture
from vimeo_python_sdk.pydantic.user import User
from vimeo_python_sdk.pydantic.webinar_email_settings_email_event_reminder24_hrs import WebinarEmailSettingsEmailEventReminder24Hrs
from vimeo_python_sdk.pydantic.webinar_email_settings_email_post_event_thank_you import WebinarEmailSettingsEmailPostEventThankYou
from vimeo_python_sdk.pydantic.webinar_email_settings_email_preferences import WebinarEmailSettingsEmailPreferences
from vimeo_python_sdk.pydantic.webinar_email_settings_email_registration_confirmation import WebinarEmailSettingsEmailRegistrationConfirmation

class WebinarEmailSettings(BaseModel):
    # The accent color scheme for emails that are sent about the webinar.
    accent_color: str = Field(alias='accent_color')

    # The custom link for emails that are sent about the webinar.
    custom_link: typing.Optional[str] = Field(alias='custom_link')

    email_event_reminder_24_hrs: WebinarEmailSettingsEmailEventReminder24Hrs = Field(alias='email_event_reminder_24_hrs')

    email_post_event_thank_you: WebinarEmailSettingsEmailPostEventThankYou = Field(alias='email_post_event_thank_you')

    email_preferences: WebinarEmailSettingsEmailPreferences = Field(alias='email_preferences')

    email_registration_confirmation: WebinarEmailSettingsEmailRegistrationConfirmation = Field(alias='email_registration_confirmation')

    # The time in ISO 8601 format when the follow-up email was sent.
    follow_up_send_on: str = Field(alias='follow_up_send_on')

    # The user who manually triggered the follow-up email.
    follow_up_sender: User = Field(alias='follow_up_sender')

    # The name of the sender for emails that are sent about the webinar.
    from_: str = Field(alias='from')

    # The URI of the logo image to include in emails that are sent about the webinar.
    logo_uri: typing.Optional[str] = Field(alias='logo_uri')

    # The logo to include in emails that are sent about the webinar.
    pictures: Picture = Field(alias='pictures')

    # The sender's reply email address.
    reply_email: typing.Optional[str] = Field(alias='reply_email')

    # The sender's physical address.
    sender_address: typing.Optional[str] = Field(alias='sender_address')

    # The URL of the sender's privacy policy.
    sender_policy_url: typing.Optional[str] = Field(alias='sender_policy_url')

    # Whether to include a custom link in emails that are sent about the webinar.
    use_custom_link: bool = Field(alias='use_custom_link')

    # Whether to include a reply link in the footer of emails that are sent about the webinar.
    use_reply_email: bool = Field(alias='use_reply_email')

    # Whether to include the sender's physical address in the footer of emails that are sent about the webinar.
    use_sender_address: bool = Field(alias='use_sender_address')

    # Whether to include the URL of the sender's privacy policy in the footer of emails that are sent about the webinar.
    use_sender_policy_url: bool = Field(alias='use_sender_policy_url')
    class Config:
        arbitrary_types_allowed = True

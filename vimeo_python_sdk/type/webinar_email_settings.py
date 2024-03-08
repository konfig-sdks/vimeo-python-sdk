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

from vimeo_python_sdk.type.picture import Picture
from vimeo_python_sdk.type.user import User
from vimeo_python_sdk.type.webinar_email_settings_email_event_reminder24_hrs import WebinarEmailSettingsEmailEventReminder24Hrs
from vimeo_python_sdk.type.webinar_email_settings_email_post_event_thank_you import WebinarEmailSettingsEmailPostEventThankYou
from vimeo_python_sdk.type.webinar_email_settings_email_preferences import WebinarEmailSettingsEmailPreferences
from vimeo_python_sdk.type.webinar_email_settings_email_registration_confirmation import WebinarEmailSettingsEmailRegistrationConfirmation

RequiredWebinarEmailSettings = TypedDict("RequiredWebinarEmailSettings", {
    # The accent color scheme for emails that are sent about the webinar.
    "accent_color": str,

    # The custom link for emails that are sent about the webinar.
    "custom_link": typing.Optional[str],

    "email_event_reminder_24_hrs": WebinarEmailSettingsEmailEventReminder24Hrs,

    "email_post_event_thank_you": WebinarEmailSettingsEmailPostEventThankYou,

    "email_preferences": WebinarEmailSettingsEmailPreferences,

    "email_registration_confirmation": WebinarEmailSettingsEmailRegistrationConfirmation,

    # The time in ISO 8601 format when the follow-up email was sent.
    "follow_up_send_on": str,

    # The user who manually triggered the follow-up email.
    "follow_up_sender": User,

    # The name of the sender for emails that are sent about the webinar.
    "from": str,

    # The URI of the logo image to include in emails that are sent about the webinar.
    "logo_uri": typing.Optional[str],

    # The logo to include in emails that are sent about the webinar.
    "pictures": Picture,

    # The sender's reply email address.
    "reply_email": typing.Optional[str],

    # The sender's physical address.
    "sender_address": typing.Optional[str],

    # The URL of the sender's privacy policy.
    "sender_policy_url": typing.Optional[str],

    # Whether to include a custom link in emails that are sent about the webinar.
    "use_custom_link": bool,

    # Whether to include a reply link in the footer of emails that are sent about the webinar.
    "use_reply_email": bool,

    # Whether to include the sender's physical address in the footer of emails that are sent about the webinar.
    "use_sender_address": bool,

    # Whether to include the URL of the sender's privacy policy in the footer of emails that are sent about the webinar.
    "use_sender_policy_url": bool,
    })

OptionalWebinarEmailSettings = TypedDict("OptionalWebinarEmailSettings", {
    }, total=False)

class WebinarEmailSettings(RequiredWebinarEmailSettings, OptionalWebinarEmailSettings):
    pass

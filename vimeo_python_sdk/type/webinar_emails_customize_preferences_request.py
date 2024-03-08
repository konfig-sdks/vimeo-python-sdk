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

from vimeo_python_sdk.type.webinar_emails_customize_preferences_request_email_preferences import WebinarEmailsCustomizePreferencesRequestEmailPreferences

RequiredWebinarEmailsCustomizePreferencesRequest = TypedDict("RequiredWebinarEmailsCustomizePreferencesRequest", {
    })

OptionalWebinarEmailsCustomizePreferencesRequest = TypedDict("OptionalWebinarEmailsCustomizePreferencesRequest", {
    # The accent color scheme for emails that are sent about the webinar.
    "accent_color": str,

    # The custom link for emails that are sent about the webinar.
    "custom_link": str,

    # The email customization details for the webinar reminder email, which goes out 24 hours before the event.
    "email_event_reminder_24_hrs": typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],

    # The email customization details for the webinar post-event thank-you email.
    "email_post_event_thank_you": typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],

    "email_preferences": WebinarEmailsCustomizePreferencesRequestEmailPreferences,

    # The email customization details for the webinar registration confirmation email.
    "email_registration_confirmation": typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],

    # The name of the sender for emails that are sent about the webinar.
    "from": str,

    # The URI of the logo image to include in emails that are sent about the webinar.
    "logo_uri": str,

    # The sender's reply email address.
    "reply_email": str,

    # The sender's physical address.
    "sender_address": str,

    # The URL of the sender's privacy policy.
    "sender_policy_url": str,

    # Whether to include a custom link in emails that are sent about the webinar.
    "use_custom_link": bool,

    # Whether to include a reply link in the footer of emails that are sent about the webinar.
    "use_reply_email": bool,

    # Whether to include the sender's physical address in the footer of emails that are sent about the webinar.
    "use_sender_address": bool,

    # Whether to include the URL of the sender's privacy policy in the footer of emails that are sent about the webinar.
    "use_sender_policy_url": bool,
    }, total=False)

class WebinarEmailsCustomizePreferencesRequest(RequiredWebinarEmailsCustomizePreferencesRequest, OptionalWebinarEmailsCustomizePreferencesRequest):
    pass

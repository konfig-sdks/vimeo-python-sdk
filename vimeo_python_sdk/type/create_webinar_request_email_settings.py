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

from vimeo_python_sdk.type.create_webinar_request_email_settings_email_preferences import CreateWebinarRequestEmailSettingsEmailPreferences

RequiredCreateWebinarRequestEmailSettings = TypedDict("RequiredCreateWebinarRequestEmailSettings", {
    })

OptionalCreateWebinarRequestEmailSettings = TypedDict("OptionalCreateWebinarRequestEmailSettings", {
    # The accent color scheme for emails that are sent about the webinar. _This field is deprecated._
    "accent_color": str,

    # The custom link for emails that are sent about the webinar. _This field is deprecated._
    "custom_link": str,

    "email_preferences": CreateWebinarRequestEmailSettingsEmailPreferences,

    # The name of the sender for emails that are sent about the webinar. _This field is deprecated._
    "from": str,

    # The URI of the logo image to include in emails that are sent about the webinar. _This field is deprecated._
    "logo_uri": str,

    # The sender's reply email address. _This field is deprecated._
    "reply_email": str,

    # The sender's physical address. _This field is deprecated._
    "sender_address": str,

    # The URL of the sender's privacy policy. _This field is deprecated._
    "sender_policy_url": str,

    # Whether to include a custom link in emails that are sent about the webinar. _This field is deprecated._
    "use_custom_link": bool,

    # Whether to include a reply link in the footer of emails that are sent about the webinar. _This field is deprecated._
    "use_reply_email": bool,

    # Whether to include the sender's physical address in the footer of emails that are sent about the webinar. _This field is deprecated._
    "use_sender_address": bool,

    # Whether to include the URL of the sender's privacy policy in the footer of emails that are sent about the webinar. _This field is deprecated._
    "use_sender_policy_url": bool,
    }, total=False)

class CreateWebinarRequestEmailSettings(RequiredCreateWebinarRequestEmailSettings, OptionalCreateWebinarRequestEmailSettings):
    pass

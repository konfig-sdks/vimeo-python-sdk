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

from vimeo_python_sdk.pydantic.webinar_essentials_create_webinar_request_email_settings_email_preferences import WebinarEssentialsCreateWebinarRequestEmailSettingsEmailPreferences

class WebinarEssentialsCreateWebinarRequestEmailSettings(BaseModel):
    # The accent color scheme for emails that are sent about the webinar. _This field is deprecated._
    accent_color: typing.Optional[str] = Field(None, alias='accent_color')

    # The custom link for emails that are sent about the webinar. _This field is deprecated._
    custom_link: typing.Optional[str] = Field(None, alias='custom_link')

    email_preferences: typing.Optional[WebinarEssentialsCreateWebinarRequestEmailSettingsEmailPreferences] = Field(None, alias='email_preferences')

    # The name of the sender for emails that are sent about the webinar. _This field is deprecated._
    from_: typing.Optional[str] = Field(None, alias='from')

    # The URI of the logo image to include in emails that are sent about the webinar. _This field is deprecated._
    logo_uri: typing.Optional[str] = Field(None, alias='logo_uri')

    # The sender's reply email address. _This field is deprecated._
    reply_email: typing.Optional[str] = Field(None, alias='reply_email')

    # The sender's physical address. _This field is deprecated._
    sender_address: typing.Optional[str] = Field(None, alias='sender_address')

    # The URL of the sender's privacy policy. _This field is deprecated._
    sender_policy_url: typing.Optional[str] = Field(None, alias='sender_policy_url')

    # Whether to include a custom link in emails that are sent about the webinar. _This field is deprecated._
    use_custom_link: typing.Optional[bool] = Field(None, alias='use_custom_link')

    # Whether to include a reply link in the footer of emails that are sent about the webinar. _This field is deprecated._
    use_reply_email: typing.Optional[bool] = Field(None, alias='use_reply_email')

    # Whether to include the sender's physical address in the footer of emails that are sent about the webinar. _This field is deprecated._
    use_sender_address: typing.Optional[bool] = Field(None, alias='use_sender_address')

    # Whether to include the URL of the sender's privacy policy in the footer of emails that are sent about the webinar. _This field is deprecated._
    use_sender_policy_url: typing.Optional[bool] = Field(None, alias='use_sender_policy_url')
    class Config:
        arbitrary_types_allowed = True

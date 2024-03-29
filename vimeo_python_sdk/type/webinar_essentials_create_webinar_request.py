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

from vimeo_python_sdk.type.webinar_essentials_create_webinar_request_email_settings import WebinarEssentialsCreateWebinarRequestEmailSettings
from vimeo_python_sdk.type.webinar_essentials_create_webinar_request_privacy import WebinarEssentialsCreateWebinarRequestPrivacy
from vimeo_python_sdk.type.webinar_essentials_create_webinar_request_schedule import WebinarEssentialsCreateWebinarRequestSchedule

class RequiredWebinarEssentialsCreateWebinarRequest(TypedDict):
    # The title of the webinar.
    title: str

class OptionalWebinarEssentialsCreateWebinarRequest(TypedDict, total=False):
    # The description of the webinar.
    description: str

    email_settings: WebinarEssentialsCreateWebinarRequestEmailSettings

    # The URI of the webinar's folder.
    folder_uri: typing.Union[int, float]

    # The password when **privacy.view** is `password`. Anyone with the password can view the videos generated by streaming to the webinar event.
    password: str

    privacy: WebinarEssentialsCreateWebinarRequestPrivacy

    schedule: WebinarEssentialsCreateWebinarRequestSchedule

    # The time zone used in resolving the timestamps that are included in the automatically generated video titles for the webinar.
    time_zone: str

class WebinarEssentialsCreateWebinarRequest(RequiredWebinarEssentialsCreateWebinarRequest, OptionalWebinarEssentialsCreateWebinarRequest):
    pass

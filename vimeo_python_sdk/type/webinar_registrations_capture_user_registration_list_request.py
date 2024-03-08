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

from vimeo_python_sdk.type.webinar_registrations_capture_user_registration_list_request_registrants import WebinarRegistrationsCaptureUserRegistrationListRequestRegistrants

class RequiredWebinarRegistrationsCaptureUserRegistrationListRequest(TypedDict):
    pass

class OptionalWebinarRegistrationsCaptureUserRegistrationListRequest(TypedDict, total=False):
    registrants: WebinarRegistrationsCaptureUserRegistrationListRequestRegistrants

class WebinarRegistrationsCaptureUserRegistrationListRequest(RequiredWebinarRegistrationsCaptureUserRegistrationListRequest, OptionalWebinarRegistrationsCaptureUserRegistrationListRequest):
    pass

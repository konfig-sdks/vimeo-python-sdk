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

from vimeo_python_sdk.type.webinar_email_content import WebinarEmailContent

class RequiredWebinarEmailSettingsEmailRegistrationConfirmation(TypedDict):
    # The email custom details for the webinar registration confirmation email.
    custom: WebinarEmailContent

    # The email default details for the webinar registration confirmation email.
    default: WebinarEmailContent

class OptionalWebinarEmailSettingsEmailRegistrationConfirmation(TypedDict, total=False):
    pass

class WebinarEmailSettingsEmailRegistrationConfirmation(RequiredWebinarEmailSettingsEmailRegistrationConfirmation, OptionalWebinarEmailSettingsEmailRegistrationConfirmation):
    pass

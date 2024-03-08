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

from vimeo_python_sdk.pydantic.webinar_email_content import WebinarEmailContent

class WebinarEmailSettingsEmailRegistrationConfirmation(BaseModel):
    # The email custom details for the webinar registration confirmation email.
    custom: WebinarEmailContent = Field(alias='custom')

    # The email default details for the webinar registration confirmation email.
    default: WebinarEmailContent = Field(alias='default')
    class Config:
        arbitrary_types_allowed = True

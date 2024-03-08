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


class WebinarRegistrationsCaptureUserRegistrationListRequest1RegistrantsItem(BaseModel):
    # The registrant's other submitted fields.
    data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='data')

    # The registrant's email address.
    email: typing.Optional[str] = Field(None, alias='email')

    # The registrant's first name.
    first_name: typing.Optional[str] = Field(None, alias='first_name')

    # The registrant's last name.
    last_name: typing.Optional[str] = Field(None, alias='last_name')
    class Config:
        arbitrary_types_allowed = True

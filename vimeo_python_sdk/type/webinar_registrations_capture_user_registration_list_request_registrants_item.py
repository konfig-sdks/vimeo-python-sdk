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


class RequiredWebinarRegistrationsCaptureUserRegistrationListRequestRegistrantsItem(TypedDict):
    pass

class OptionalWebinarRegistrationsCaptureUserRegistrationListRequestRegistrantsItem(TypedDict, total=False):
    # The registrant's other submitted fields.
    data: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The registrant's email address.
    email: str

    # The registrant's first name.
    first_name: str

    # The registrant's last name.
    last_name: str

class WebinarRegistrationsCaptureUserRegistrationListRequestRegistrantsItem(RequiredWebinarRegistrationsCaptureUserRegistrationListRequestRegistrantsItem, OptionalWebinarRegistrationsCaptureUserRegistrationListRequestRegistrantsItem):
    pass

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

from vimeo_python_sdk.type.webinar_registrant_analytics import WebinarRegistrantAnalytics

class RequiredWebinarRegistrant(TypedDict):
    analytics: WebinarRegistrantAnalytics

    # The date in Unix time when the registrant's account was created.
    created_on: typing.Union[int, float]

    # The values of all other fields as submitted on the webinar registration form.
    data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    # The registrant's email address as submitted on the webinar registration form.
    email: str

    # The registrant's first name as submitted on the webinar registration form.
    first_name: typing.Optional[str]

    # The registrant's attended status for the webinar.  Option descriptions:  * `B` - The registrant has been blocked from attending the webinar.  * `N` - The registrant has not attended the webinar.  * `Y` - The registrant has attended the webinar. 
    has_attended: str

    # Whether the registrant's viewing status for the webinar is blocked.
    is_blocked: bool

    # The registrant's last name as submitted on the webinar registration form.
    last_name: typing.Optional[str]

    # The web address where the registration form was submitted.
    referrer: typing.Optional[str]

    # Details about the source from which the registrant's account was created.
    source_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    # The source from which the registrant's account was created.
    source_type: typing.Optional[str]

    # The API URL to return the webinar registrant's account.
    uri: str

class OptionalWebinarRegistrant(TypedDict, total=False):
    pass

class WebinarRegistrant(RequiredWebinarRegistrant, OptionalWebinarRegistrant):
    pass

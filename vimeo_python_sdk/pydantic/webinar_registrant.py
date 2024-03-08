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

from vimeo_python_sdk.pydantic.webinar_registrant_analytics import WebinarRegistrantAnalytics

class WebinarRegistrant(BaseModel):
    analytics: WebinarRegistrantAnalytics = Field(alias='analytics')

    # The date in Unix time when the registrant's account was created.
    created_on: typing.Union[int, float] = Field(alias='created_on')

    # The values of all other fields as submitted on the webinar registration form.
    data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(alias='data')

    # The registrant's email address as submitted on the webinar registration form.
    email: str = Field(alias='email')

    # The registrant's first name as submitted on the webinar registration form.
    first_name: typing.Optional[str] = Field(alias='first_name')

    # The registrant's attended status for the webinar.  Option descriptions:  * `B` - The registrant has been blocked from attending the webinar.  * `N` - The registrant has not attended the webinar.  * `Y` - The registrant has attended the webinar. 
    has_attended: Literal["B", "N", "Y"] = Field(alias='has_attended')

    # Whether the registrant's viewing status for the webinar is blocked.
    is_blocked: bool = Field(alias='is_blocked')

    # The registrant's last name as submitted on the webinar registration form.
    last_name: typing.Optional[str] = Field(alias='last_name')

    # The web address where the registration form was submitted.
    referrer: typing.Optional[str] = Field(alias='referrer')

    # Details about the source from which the registrant's account was created.
    source_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(alias='source_details')

    # The source from which the registrant's account was created.
    source_type: typing.Optional[str] = Field(alias='source_type')

    # The API URL to return the webinar registrant's account.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

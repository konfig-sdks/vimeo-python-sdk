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

from vimeo_python_sdk.pydantic.webinar_email_provider_list_item_list import WebinarEmailProviderListItemList
from vimeo_python_sdk.pydantic.webinar_email_provider_list_item_provider import WebinarEmailProviderListItemProvider

class WebinarEmailProviderListItem(BaseModel):
    # Whether the connection is active.
    is_active: bool = Field(alias='is_active')

    # The most recent sync date of the provider list.
    last_import_time: typing.Optional[str] = Field(alias='last_import_time')

    list_: WebinarEmailProviderListItemList = Field(alias='list')

    provider: WebinarEmailProviderListItemProvider = Field(alias='provider')
    class Config:
        arbitrary_types_allowed = True

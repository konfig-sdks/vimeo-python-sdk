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


class EmailCaptureFormEmailListsItem(BaseModel):
    # The ID of the email capture form.
    form_id: typing.Union[int, float] = Field(alias='form_id')

    # The ID of the mailing list in the third-party email service provider's system.
    list_id: str = Field(alias='list_id')

    # A third-party email service provider.  Option descriptions:  * `1` - The provider is Mailchimp.  * `2` - The provider is Campaign Monitor.  * `3` - The provider is Constant Contact.  * `4` - The provider is Infusionsoft.  * `5` - The provider is HubSpot.  * `6` - The provider is Constant Contact V3.  * `7` - The provider is Marketo. 
    provider_id: Literal["1", "2", "3", "4", "5", "6", "7"] = Field(alias='provider_id')

    # The name of the mailing list in the third-party email service provider's system.
    list_name: typing.Optional[str] = Field(None, alias='list_name')
    class Config:
        arbitrary_types_allowed = True

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

from vimeo_python_sdk.pydantic.live_embed_privacy_embed_event_on_domains_request2_allowed_domains import LiveEmbedPrivacyEmbedEventOnDomainsRequest2AllowedDomains

class LiveEmbedPrivacyEmbedEventOnDomainsRequest2(BaseModel):
    allowed_domains: typing.Optional[LiveEmbedPrivacyEmbedEventOnDomainsRequest2AllowedDomains] = Field(None, alias='allowed_domains')
    class Config:
        arbitrary_types_allowed = True

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

from vimeo_python_sdk.type.live_embed_privacy_embed_event_on_domains_request1_allowed_domains import LiveEmbedPrivacyEmbedEventOnDomainsRequest1AllowedDomains

class RequiredLiveEmbedPrivacyEmbedEventOnDomainsRequest1(TypedDict):
    pass

class OptionalLiveEmbedPrivacyEmbedEventOnDomainsRequest1(TypedDict, total=False):
    allowed_domains: LiveEmbedPrivacyEmbedEventOnDomainsRequest1AllowedDomains

class LiveEmbedPrivacyEmbedEventOnDomainsRequest1(RequiredLiveEmbedPrivacyEmbedEventOnDomainsRequest1, OptionalLiveEmbedPrivacyEmbedEventOnDomainsRequest1):
    pass

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

from vimeo_python_sdk.type.webinar_event_embed_logos_custom import WebinarEventEmbedLogosCustom

class RequiredWebinarEventEmbedLogos(TypedDict):
    custom: WebinarEventEmbedLogosCustom

    # Whether the Vimeo logo appears in the embeddable player for the video.
    vimeo: bool

class OptionalWebinarEventEmbedLogos(TypedDict, total=False):
    pass

class WebinarEventEmbedLogos(RequiredWebinarEventEmbedLogos, OptionalWebinarEventEmbedLogos):
    pass

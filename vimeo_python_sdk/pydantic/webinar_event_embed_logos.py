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

from vimeo_python_sdk.pydantic.webinar_event_embed_logos_custom import WebinarEventEmbedLogosCustom

class WebinarEventEmbedLogos(BaseModel):
    custom: WebinarEventEmbedLogosCustom = Field(alias='custom')

    # Whether the Vimeo logo appears in the embeddable player for the video.
    vimeo: bool = Field(alias='vimeo')
    class Config:
        arbitrary_types_allowed = True
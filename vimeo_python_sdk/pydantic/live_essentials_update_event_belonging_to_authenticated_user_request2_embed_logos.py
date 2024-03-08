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

from vimeo_python_sdk.pydantic.live_essentials_update_event_belonging_to_authenticated_user_request2_embed_logos_custom import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2EmbedLogosCustom

class LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2EmbedLogos(BaseModel):
    custom: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2EmbedLogosCustom] = Field(None, alias='custom')

    # Whether to show the Vimeo logo on the embed player.
    vimeo: typing.Optional[bool] = Field(None, alias='vimeo')
    class Config:
        arbitrary_types_allowed = True

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

from vimeo_python_sdk.pydantic.create_vod_request_episodes_buy import CreateVodRequestEpisodesBuy
from vimeo_python_sdk.pydantic.create_vod_request_episodes_rent import CreateVodRequestEpisodesRent

class CreateVodRequestEpisodes(BaseModel):
    buy: typing.Optional[CreateVodRequestEpisodesBuy] = Field(None, alias='buy')

    rent: typing.Optional[CreateVodRequestEpisodesRent] = Field(None, alias='rent')
    class Config:
        arbitrary_types_allowed = True

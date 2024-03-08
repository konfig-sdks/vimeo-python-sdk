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

from vimeo_python_sdk.pydantic.on_demand_videos_add_video_to_page_request_buy_price import OnDemandVideosAddVideoToPageRequestBuyPrice

class OnDemandVideosAddVideoToPageRequestBuy(BaseModel):
    price: typing.Optional[OnDemandVideosAddVideoToPageRequestBuyPrice] = Field(None, alias='price')
    class Config:
        arbitrary_types_allowed = True

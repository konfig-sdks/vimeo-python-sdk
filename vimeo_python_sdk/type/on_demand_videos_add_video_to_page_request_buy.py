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

from vimeo_python_sdk.type.on_demand_videos_add_video_to_page_request_buy_price import OnDemandVideosAddVideoToPageRequestBuyPrice

class RequiredOnDemandVideosAddVideoToPageRequestBuy(TypedDict):
    pass

class OptionalOnDemandVideosAddVideoToPageRequestBuy(TypedDict, total=False):
    price: OnDemandVideosAddVideoToPageRequestBuyPrice

class OnDemandVideosAddVideoToPageRequestBuy(RequiredOnDemandVideosAddVideoToPageRequestBuy, OptionalOnDemandVideosAddVideoToPageRequestBuy):
    pass

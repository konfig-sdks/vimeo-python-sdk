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

from vimeo_python_sdk.type.on_demand_essentials_create_page_request_buy_price import OnDemandEssentialsCreatePageRequestBuyPrice

class RequiredOnDemandEssentialsCreatePageRequestBuy(TypedDict):
    pass

class OptionalOnDemandEssentialsCreatePageRequestBuy(TypedDict, total=False):
    # Whether the video can be purchased. This parameter is required when **rent.active** is `false`.
    active: bool

    # Whether people who buy the video can download it. To use this parameter, **type** must be `film`.
    download: bool

    price: OnDemandEssentialsCreatePageRequestBuyPrice

class OnDemandEssentialsCreatePageRequestBuy(RequiredOnDemandEssentialsCreatePageRequestBuy, OptionalOnDemandEssentialsCreatePageRequestBuy):
    pass

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

from vimeo_python_sdk.pydantic.on_demand_promotion_metadata import OnDemandPromotionMetadata

class OnDemandPromotion(BaseModel):
    # The type of access that the promotion grants.  Option descriptions:  * `default` - The promotion grants discounts on existing product offerings.  * `vip` - The promotion grants free access to On Demand content before it's released, or to access types that aren't part of the existing product offerings. 
    access_type: Literal["default", "vip"] = Field(alias='access_type')

    # The type of discount that the promotion provides.  Option descriptions:  * `dollars` - The promotion discounts a fixed amount from the full purchase price.  * `free` - The promotion discounts the full purchase price. When **access_type** is `vip`, **discount_type** is always `free`.  * `percent` - The promotion discounts a percentage of the full purchase price. 
    discount_type: Literal["dollars", "free", "percent"] = Field(alias='discount_type')

    # Whether the promotion grants download access to On Demand content.
    download: bool = Field(alias='download')

    # The prefix string for batch codes, or the null value for single codes.
    label: typing.Optional[str] = Field(alias='label')

    metadata: OnDemandPromotionMetadata = Field(alias='metadata')

    # When **discount_type** is `percent`, the percentage amount that is deducted from the product price.
    percent_off: typing.Union[int, float] = Field(alias='percent_off')

    # The type of product to which the promotion can be applied. Only the `buy` and `rent` options are available when **access_type** is `vip`.  Option descriptions:  * `any` - The promotion can be applied to any product.  * `buy` - The promotion can be applied to a buyable single video.  * `buy_episode` - The promotion can be applied to a buyable single episode.  * `rent` - The promotion can be applied to a rentable single video.  * `rent_episode` - The promotion can be applied to a rentable single episode.  * `subscribe` - The promotion can be applied to a subscription. 
    product_type: Literal["any", "buy", "buy_episode", "rent", "rent_episode", "subscribe"] = Field(alias='product_type')

    # The amount of time that the user has access to the On Demand content after redeeming a promo code.  Option descriptions:  * `1_week` - Access lasts for one week.  * `1_year` - Access lasts for one year.  * `24_hour` - Access lasts for 24 hours.  * `30_days` - Access lasts for 30 days.  * `3_month` - Access lasts for three months.  * `48_hour` - Access lasts for 48 hours.  * `6_month` - Access lasts for six months.  * `72_hour` - Access lasts for 72 hours. 
    stream_period: Literal["1_week", "1_year", "24_hour", "30_days", "3_month", "48_hour", "6_month", "72_hour"] = Field(alias='stream_period')

    # When **type** is `single`, the total number of times that the promotion can be used. When **type** is `batch` or `batch_prefix`, the total number of promo codes that have been generated.
    total: typing.Union[int, float] = Field(alias='total')

    # The way in which the promotion generates promo codes.  Option descriptions:  * `batch` - The promotion provides a unique promo code for each user.  * `batch_prefix` - Like `batch`, except that all codes have a similar prefix string. _This option is deprecated, yet it may still appear for some users._  * `single` - The promotion provides a single promo code for all users. 
    type: Literal["batch", "batch_prefix", "single"] = Field(alias='type')

    # The promotion's canonical relative URI.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

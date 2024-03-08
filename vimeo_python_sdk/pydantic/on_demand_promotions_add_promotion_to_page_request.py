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


class OnDemandPromotionsAddPromotionToPageRequest(BaseModel):
    # Whether the promotion grants download access to On Demand content. This field is required only when the download access hasn't been defined in the On Demand container, or when **access_type** is `vip` or **product_type** is `buy`.
    download: bool = Field(alias='download')

    # The amount of time for which the user can access On Demand content upon redeeming a promotion code. This parameter is required only when the streaming period isn't defined in the On Demand container, or when creating promotions where **access_type** is `vip` or **product_type** is `rent`.  Option descriptions:  * `1_week` - The user can access On Demand content for a maximum of 1 week after redeeming a promotion code.  * `1_year` - The user can access On Demand content for a maximum of 1 year after redeeming a promotion code.  * `24_hour` - The user can access On Demand content for a maximum of 24 hours after redeeming a promotion code.  * `30_day` - The user can access On Demand content for a maximum of 30 days after redeeming a promotion code.  * `3_month` - The user can access On Demand content for a maximum of 3 months after redeeming a promotion code.  * `48_hour` - The user can access On Demand content for a maximum of 48 hours after redeeming a promotion code.  * `6_month` - The user can access On Demand content for a maximum of 6 months after redeeming a promotion code.  * `72_hour` - The user can access On Demand content for a maximum of 72 hours after redeeming a promotion code. 
    stream_period: Literal["1_week", "1_year", "24_hour", "30_day", "3_month", "48_hour", "6_month", "72_hour"] = Field(alias='stream_period')

    # When **type** is `batch`, the total number of promotions to generate. When **type** is `single`, the total number of uses of the promotion.
    total: typing.Union[int, float] = Field(alias='total')

    # The type of the promotion. When **access_type** is `vip`, the value for this parameter must be `batch`.  Option descriptions:  * `batch` - The promotion type that generates many random codes to use one time each.  * `single` - The promotion type that generates one code to use many times. 
    type: Literal["batch", "single"] = Field(alias='type')

    # The promotion access type, which is a purchase option that isn't available in the On Demand container. Use the **download** and **stream_period** parameters to define additional characteristics for the `vip` type.  Option descriptions:  * `default` - The promotion grants a discount on the existing purchase options for an On Demand container.  * `vip` - The promotion grants free access to On Demand content before it's released. 
    access_type: typing.Optional[Literal["default", "vip"]] = Field(None, alias='access_type')

    # The promotion code. This parameter is ignored when the promotion type is `batch`.
    code: typing.Optional[str] = Field(None, alias='code')

    # The type of discount offered by the promotion code. When **access_type** is `vip`, the value of this parameter must be `free`.  Option descriptions:  * `free` - The discount reduces the price to zero.  * `percent` - The discount reduces the price by the percentage defined in the **percent_off** parameter. 
    discount_type: typing.Optional[Literal["free", "percent"]] = Field(None, alias='discount_type')

    # The time at which the promotion period ends. If this parameter has no value, the promotion never expires.
    end_time: typing.Optional[str] = Field(None, alias='end_time')

    # The description of the promotion when the promotion type is `batch`. This parameter is ignored when the promotion type is `single`.
    label: typing.Optional[str] = Field(None, alias='label')

    # The percentage of the discount. This parameter is applicable only when **discount_type** is `percent`.
    percent_off: typing.Optional[typing.Union[int, float]] = Field(None, alias='percent_off')

    # The type of transaction to which the promotion applies. When **access_type** is `default`, the default value is `any`. When **access_type** is `vip`, the default value is `rent` and the only valid product types are `buy` and `rent`.  Option descriptions:  * `any` - The promotion applies to any transaction.  * `buy` - The promotion applies only to purchased products.  * `buy_episode` - The promotion applies only to purchased episodes.  * `rent` - The promotion applies only to rented products.  * `rent_episode` - The promotion applies only to rented episodes.  * `subscribe` - The promotion applies only to subscriptions. 
    product_type: typing.Optional[Literal["any", "buy", "buy_episode", "rent", "rent_episode", "subscribe"]] = Field(None, alias='product_type')

    # The time at which the promotion period starts. If this parameter has no value, the start time defaults to the time at which the promotion was created.
    start_time: typing.Optional[str] = Field(None, alias='start_time')
    class Config:
        arbitrary_types_allowed = True

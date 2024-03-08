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

from vimeo_python_sdk.pydantic.subscription_plans_currency import SubscriptionPlansCurrency
from vimeo_python_sdk.pydantic.subscription_plans_discount import SubscriptionPlansDiscount
from vimeo_python_sdk.pydantic.subscription_plans_metadata import SubscriptionPlansMetadata
from vimeo_python_sdk.pydantic.subscription_plans_price import SubscriptionPlansPrice
from vimeo_python_sdk.pydantic.subscription_plans_promotion import SubscriptionPlansPromotion

class SubscriptionPlans(BaseModel):
    currency: SubscriptionPlansCurrency = Field(alias='currency')

    discount: SubscriptionPlansDiscount = Field(alias='discount')

    # The SKU of the plan.
    id: typing.Union[int, float] = Field(alias='id')

    metadata: SubscriptionPlansMetadata = Field(alias='metadata')

    # The name of the plan.
    name: str = Field(alias='name')

    price: SubscriptionPlansPrice = Field(alias='price')

    promotion: SubscriptionPlansPromotion = Field(alias='promotion')

    # The plan type.  Option descriptions:  * `advanced` - The plan type is Vimeo Advanced.  * `basic` - The plan type is Vimeo Basic.  * `business` - The plan type is Vimeo Business.  * `enterprise` - The plan type is Vimeo Enterprise.  * `free` - The plan type is Vimeo Free.  * `livePremium` - The plan type is Vimeo Premium.  * `ott` - The plan type is Vimeo OTT.  * `plus` - The plan type is Vimeo Plus.  * `pro` - The plan type is Vimeo Pro.  * `proUnlimited` - The plan type is Vimeo Pro Unlimited.  * `standard` - The plan type is Vimeo Standard.  * `starter` - The plan type is Vimeo Starter. 
    tier: Literal["advanced", "basic", "business", "enterprise", "free", "livePremium", "ott", "plus", "pro", "proUnlimited", "standard", "starter"] = Field(alias='tier')

    # The URI of the plan.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

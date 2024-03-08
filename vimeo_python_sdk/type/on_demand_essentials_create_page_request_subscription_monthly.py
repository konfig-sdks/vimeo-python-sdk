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

from vimeo_python_sdk.type.on_demand_essentials_create_page_request_subscription_monthly_price import OnDemandEssentialsCreatePageRequestSubscriptionMonthlyPrice

class RequiredOnDemandEssentialsCreatePageRequestSubscriptionMonthly(TypedDict):
    pass

class OptionalOnDemandEssentialsCreatePageRequestSubscriptionMonthly(TypedDict, total=False):
    # Whether a monthly subscription is active. This parameter is required when **rent.active** and **buy.active** are `false`.
    active: bool

    price: OnDemandEssentialsCreatePageRequestSubscriptionMonthlyPrice

class OnDemandEssentialsCreatePageRequestSubscriptionMonthly(RequiredOnDemandEssentialsCreatePageRequestSubscriptionMonthly, OptionalOnDemandEssentialsCreatePageRequestSubscriptionMonthly):
    pass

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

from vimeo_python_sdk.type.disabled_video_properties_duplicate_reasons import DisabledVideoPropertiesDuplicateReasons

class RequiredDisabledVideoPropertiesDuplicate(TypedDict):
    # The relative link to upgrade to duplication.
    enable_link: str

    # The path to the duplicate object in the video response.
    key_path: str

    # The capability required to activate duplication.  Option descriptions:  * `basic` - The user must have at least a Vimeo Basic account.  * `business` - The user must have at least a Vimeo Business account.  * `enterprise` - The user must have at least a Vimeo Enterprise account.  * `live_business` - The user must have at least a Vimeo Business Live account.  * `live_premium` - The user must have at least a Vimeo Premium account.  * `live_pro` - The user must have at least a Vimeo Pro Live account.  * `plus` - The user must have at least a Vimeo Plus account.  * `pro` - The user must have at least a Vimeo Pro account.  * `pro_unlimited` - The user must have at least a Vimeo Pro Unlimited account.  * `producer` - The user must have at least a Vimeo Producer account. 
    min_tier_for_capability: str

    reasons: DisabledVideoPropertiesDuplicateReasons

class OptionalDisabledVideoPropertiesDuplicate(TypedDict, total=False):
    pass

class DisabledVideoPropertiesDuplicate(RequiredDisabledVideoPropertiesDuplicate, OptionalDisabledVideoPropertiesDuplicate):
    pass

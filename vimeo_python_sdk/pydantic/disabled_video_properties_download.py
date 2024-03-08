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

from vimeo_python_sdk.pydantic.disabled_video_properties_download_reasons import DisabledVideoPropertiesDownloadReasons

class DisabledVideoPropertiesDownload(BaseModel):
    # The relative link to upgrade downloads.
    enable_link: str = Field(alias='enable_link')

    # The path to the download object in the video response.
    key_path: str = Field(alias='key_path')

    # The capability required to activate downloads.  Option descriptions:  * `basic` - The user must have at least a Vimeo Basic account.  * `business` - The user must have at least a Vimeo Business account.  * `enterprise` - The user must have at least a Vimeo Enterprise account.  * `live_business` - The user must have at least a Vimeo Business Live account.  * `live_premium` - The user must have at least a Vimeo Premium account.  * `live_pro` - The user must have at least a Vimeo Pro Live account.  * `plus` - The user must have at least a Vimeo Plus account.  * `pro` - The user must have at least a Vimeo Pro account.  * `pro_unlimited` - The user must have at least a Vimeo Pro Unlimited account.  * `producer` - The user must have at least a Vimeo Producer account. 
    min_tier_for_capability: Literal["basic", "business", "enterprise", "live_business", "live_premium", "live_pro", "plus", "pro", "pro_unlimited", "producer"] = Field(alias='min_tier_for_capability')

    reasons: DisabledVideoPropertiesDownloadReasons = Field(alias='reasons')
    class Config:
        arbitrary_types_allowed = True

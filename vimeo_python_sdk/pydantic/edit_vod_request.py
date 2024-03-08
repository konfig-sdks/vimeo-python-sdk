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

from vimeo_python_sdk.pydantic.edit_vod_request_preorder import EditVodRequestPreorder
from vimeo_python_sdk.pydantic.edit_vod_request_publish import EditVodRequestPublish

class EditVodRequest(BaseModel):
    # The custom string to use in the Vimeo URL of the On Demand page.
    link: typing.Optional[str] = Field(None, alias='link')

    preorder: typing.Optional[EditVodRequestPreorder] = Field(None, alias='preorder')

    publish: typing.Optional[EditVodRequestPublish] = Field(None, alias='publish')

    # Whether to publish the On Demand page automatically after all videos have finished transcoding.
    publish_when_ready: typing.Optional[bool] = Field(None, alias='publish_when_ready')
    class Config:
        arbitrary_types_allowed = True

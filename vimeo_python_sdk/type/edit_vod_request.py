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

from vimeo_python_sdk.type.edit_vod_request_preorder import EditVodRequestPreorder
from vimeo_python_sdk.type.edit_vod_request_publish import EditVodRequestPublish

class RequiredEditVodRequest(TypedDict):
    pass

class OptionalEditVodRequest(TypedDict, total=False):
    # The custom string to use in the Vimeo URL of the On Demand page.
    link: str

    preorder: EditVodRequestPreorder

    publish: EditVodRequestPublish

    # Whether to publish the On Demand page automatically after all videos have finished transcoding.
    publish_when_ready: bool

class EditVodRequest(RequiredEditVodRequest, OptionalEditVodRequest):
    pass

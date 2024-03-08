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

from vimeo_python_sdk.type.upload_video_request_embed_logos_custom import UploadVideoRequestEmbedLogosCustom

class RequiredUploadVideoRequestEmbedLogos(TypedDict):
    pass

class OptionalUploadVideoRequestEmbedLogos(TypedDict, total=False):
    custom: UploadVideoRequestEmbedLogosCustom

    # Whether to show the Vimeo logo on the embeddable player.
    vimeo: bool

class UploadVideoRequestEmbedLogos(RequiredUploadVideoRequestEmbedLogos, OptionalUploadVideoRequestEmbedLogos):
    pass

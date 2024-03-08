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

from vimeo_python_sdk.type.upload_video_request_embed_buttons import UploadVideoRequestEmbedButtons
from vimeo_python_sdk.type.upload_video_request_embed_end_screen import UploadVideoRequestEmbedEndScreen
from vimeo_python_sdk.type.upload_video_request_embed_logos import UploadVideoRequestEmbedLogos
from vimeo_python_sdk.type.upload_video_request_embed_title import UploadVideoRequestEmbedTitle

class RequiredUploadVideoRequestEmbed(TypedDict):
    pass

class OptionalUploadVideoRequestEmbed(TypedDict, total=False):
    title: UploadVideoRequestEmbedTitle

    buttons: UploadVideoRequestEmbedButtons

    # The main color of the embeddable player.
    color: str

    end_screen: UploadVideoRequestEmbedEndScreen

    logos: UploadVideoRequestEmbedLogos

    # Whether to show the playbar on the embeddable player.
    playbar: bool

    # Whether to show the volume selector on the embeddable player.
    volume: bool

class UploadVideoRequestEmbed(RequiredUploadVideoRequestEmbed, OptionalUploadVideoRequestEmbed):
    pass

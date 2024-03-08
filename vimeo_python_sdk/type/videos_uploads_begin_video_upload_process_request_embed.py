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

from vimeo_python_sdk.type.videos_uploads_begin_video_upload_process_request_embed_buttons import VideosUploadsBeginVideoUploadProcessRequestEmbedButtons
from vimeo_python_sdk.type.videos_uploads_begin_video_upload_process_request_embed_end_screen import VideosUploadsBeginVideoUploadProcessRequestEmbedEndScreen
from vimeo_python_sdk.type.videos_uploads_begin_video_upload_process_request_embed_logos import VideosUploadsBeginVideoUploadProcessRequestEmbedLogos
from vimeo_python_sdk.type.videos_uploads_begin_video_upload_process_request_embed_title import VideosUploadsBeginVideoUploadProcessRequestEmbedTitle

class RequiredVideosUploadsBeginVideoUploadProcessRequestEmbed(TypedDict):
    pass

class OptionalVideosUploadsBeginVideoUploadProcessRequestEmbed(TypedDict, total=False):
    title: VideosUploadsBeginVideoUploadProcessRequestEmbedTitle

    buttons: VideosUploadsBeginVideoUploadProcessRequestEmbedButtons

    # The main color of the embeddable player.
    color: str

    end_screen: VideosUploadsBeginVideoUploadProcessRequestEmbedEndScreen

    logos: VideosUploadsBeginVideoUploadProcessRequestEmbedLogos

    # Whether to show the playbar on the embeddable player.
    playbar: bool

    # Whether to show the volume selector on the embeddable player.
    volume: bool

class VideosUploadsBeginVideoUploadProcessRequestEmbed(RequiredVideosUploadsBeginVideoUploadProcessRequestEmbed, OptionalVideosUploadsBeginVideoUploadProcessRequestEmbed):
    pass

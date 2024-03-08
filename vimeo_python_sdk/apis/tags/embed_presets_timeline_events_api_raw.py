# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.videos_video_id_timelinethumbnails.post import AddThumbnailToVideoRaw
from vimeo_python_sdk.paths.videos_video_id_timelinethumbnails_thumbnail_id.get import GetSingleThumbnailRaw


class EmbedPresetsTimelineEventsApiRaw(
    AddThumbnailToVideoRaw,
    GetSingleThumbnailRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
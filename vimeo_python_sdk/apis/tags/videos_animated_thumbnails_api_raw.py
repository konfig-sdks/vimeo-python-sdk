# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.videos_video_id_animated_thumbsets.post import CreateSetRaw
from vimeo_python_sdk.paths.videos_video_id_animated_thumbsets_picture_id.delete import DeleteSetRaw
from vimeo_python_sdk.paths.videos_video_id_animated_thumbsets.get import GetAllSetsRaw
from vimeo_python_sdk.paths.videos_video_id_animated_thumbsets_picture_id_status.get import GetStatusOfSetRaw
from vimeo_python_sdk.paths.videos_video_id_animated_thumbsets_picture_id.get import SpecificSetGetRaw


class VideosAnimatedThumbnailsApiRaw(
    CreateSetRaw,
    DeleteSetRaw,
    GetAllSetsRaw,
    GetStatusOfSetRaw,
    SpecificSetGetRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
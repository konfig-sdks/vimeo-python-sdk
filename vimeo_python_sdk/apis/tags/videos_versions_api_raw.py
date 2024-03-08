# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.videos_video_id_versions.post import AddVideoVersionRaw
from vimeo_python_sdk.paths.videos_video_id_versions_version_id.delete import DeleteVideoVersionRaw
from vimeo_python_sdk.paths.videos_video_id_versions_version_id.patch import EditVideoVersionRaw
from vimeo_python_sdk.paths.channels_channel_id_videos_video_id_versions.get import GetAllVideoVersionsRaw
from vimeo_python_sdk.paths.videos_video_id_versions.get import GetAllVideoVersions0Raw
from vimeo_python_sdk.paths.videos_video_id_versions_version_id.get import GetSpecificVersionRaw


class VideosVersionsApiRaw(
    AddVideoVersionRaw,
    DeleteVideoVersionRaw,
    EditVideoVersionRaw,
    GetAllVideoVersionsRaw,
    GetAllVideoVersions0Raw,
    GetSpecificVersionRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
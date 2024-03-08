# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.groups_group_id_videos_video_id.put import AddToGroupRaw
from vimeo_python_sdk.paths.groups_group_id_videos.get import GetAllGroupVideosRaw
from vimeo_python_sdk.paths.groups_group_id_videos_video_id.get import GetSingleVideoRaw
from vimeo_python_sdk.paths.groups_group_id_videos_video_id.delete import RemoveFromGroupRaw


class GroupsVideosApiRaw(
    AddToGroupRaw,
    GetAllGroupVideosRaw,
    GetSingleVideoRaw,
    RemoveFromGroupRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
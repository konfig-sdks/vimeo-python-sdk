# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.groups_group_id_videos_video_id.put import AddToGroup
from vimeo_python_sdk.paths.groups_group_id_videos.get import GetAllGroupVideos
from vimeo_python_sdk.paths.groups_group_id_videos_video_id.get import GetSingleVideo
from vimeo_python_sdk.paths.groups_group_id_videos_video_id.delete import RemoveFromGroup
from vimeo_python_sdk.apis.tags.groups_videos_api_raw import GroupsVideosApiRaw


class GroupsVideosApi(
    AddToGroup,
    GetAllGroupVideos,
    GetSingleVideo,
    RemoveFromGroup,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: GroupsVideosApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = GroupsVideosApiRaw(api_client)
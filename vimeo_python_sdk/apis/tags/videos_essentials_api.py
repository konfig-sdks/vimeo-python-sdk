# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.users_user_id_appearances.get import Appearances
from vimeo_python_sdk.paths.users_user_id_videos_video_id.get import CheckUserOwnership
from vimeo_python_sdk.paths.me_videos_video_id.get import CheckUserOwnsVideo
from vimeo_python_sdk.paths.me_videos.delete import DeleteUserVideos
from vimeo_python_sdk.paths.me_videos.get import GetAllUserVideos
from vimeo_python_sdk.paths.me_appearances.get import GetUserAppearances
from vimeo_python_sdk.paths.videos_video_id.get import Video
from vimeo_python_sdk.paths.videos_video_id.delete import Video0
from vimeo_python_sdk.paths.videos_video_id.patch import Video1
from vimeo_python_sdk.paths.users_user_id_videos.get import Videos
from vimeo_python_sdk.paths.users_user_id_videos.delete import Videos0
from vimeo_python_sdk.paths.videos.get import Videos1
from vimeo_python_sdk.apis.tags.videos_essentials_api_raw import VideosEssentialsApiRaw


class VideosEssentialsApi(
    Appearances,
    CheckUserOwnership,
    CheckUserOwnsVideo,
    DeleteUserVideos,
    GetAllUserVideos,
    GetUserAppearances,
    Video,
    Video0,
    Video1,
    Videos,
    Videos0,
    Videos1,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: VideosEssentialsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = VideosEssentialsApiRaw(api_client)

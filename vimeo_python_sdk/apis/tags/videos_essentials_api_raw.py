# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.users_user_id_appearances.get import AppearancesRaw
from vimeo_python_sdk.paths.users_user_id_videos_video_id.get import CheckUserOwnershipRaw
from vimeo_python_sdk.paths.me_videos_video_id.get import CheckUserOwnsVideoRaw
from vimeo_python_sdk.paths.me_videos.delete import DeleteUserVideosRaw
from vimeo_python_sdk.paths.me_videos.get import GetAllUserVideosRaw
from vimeo_python_sdk.paths.me_appearances.get import GetUserAppearancesRaw
from vimeo_python_sdk.paths.videos_video_id.get import VideoRaw
from vimeo_python_sdk.paths.videos_video_id.delete import Video0Raw
from vimeo_python_sdk.paths.videos_video_id.patch import Video1Raw
from vimeo_python_sdk.paths.users_user_id_videos.get import VideosRaw
from vimeo_python_sdk.paths.users_user_id_videos.delete import Videos0Raw
from vimeo_python_sdk.paths.videos.get import Videos1Raw


class VideosEssentialsApiRaw(
    AppearancesRaw,
    CheckUserOwnershipRaw,
    CheckUserOwnsVideoRaw,
    DeleteUserVideosRaw,
    GetAllUserVideosRaw,
    GetUserAppearancesRaw,
    VideoRaw,
    Video0Raw,
    Video1Raw,
    VideosRaw,
    Videos0Raw,
    Videos1Raw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

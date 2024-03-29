# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.me_likes_video_id.get import CheckUserLikedVideo
from vimeo_python_sdk.paths.users_user_id_likes_video_id.get import CheckVideoLikedByUser
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_likes.get import GetAllUserLikes
from vimeo_python_sdk.paths.me_likes.get import GetUserLikedVideos
from vimeo_python_sdk.paths.videos_video_id_likes.get import GetUserLikes
from vimeo_python_sdk.paths.channels_channel_id_videos_video_id_likes.get import GetUsersWhoLikedVideo
from vimeo_python_sdk.paths.me_likes_video_id.put import LikeVideo
from vimeo_python_sdk.paths.users_user_id_likes.get import Likes
from vimeo_python_sdk.paths.me_likes_video_id.delete import UnlikeVideo
from vimeo_python_sdk.paths.users_user_id_likes_video_id.put import Video
from vimeo_python_sdk.paths.users_user_id_likes_video_id.delete import Video0
from vimeo_python_sdk.apis.tags.likes_essentials_api_raw import LikesEssentialsApiRaw


class LikesEssentialsApi(
    CheckUserLikedVideo,
    CheckVideoLikedByUser,
    GetAllUserLikes,
    GetUserLikedVideos,
    GetUserLikes,
    GetUsersWhoLikedVideo,
    LikeVideo,
    Likes,
    UnlikeVideo,
    Video,
    Video0,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: LikesEssentialsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = LikesEssentialsApiRaw(api_client)

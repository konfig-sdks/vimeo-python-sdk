# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.me_watched_videos.delete import DeleteEntireWatchHistory
from vimeo_python_sdk.paths.me_watched_videos_video_id.delete import DeleteSpecificVideo
from vimeo_python_sdk.paths.me_watched_videos.get import GetWatchedVideos
from vimeo_python_sdk.apis.tags.users_watch_history_api_raw import UsersWatchHistoryApiRaw


class UsersWatchHistoryApi(
    DeleteEntireWatchHistory,
    DeleteSpecificVideo,
    GetWatchedVideos,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UsersWatchHistoryApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UsersWatchHistoryApiRaw(api_client)
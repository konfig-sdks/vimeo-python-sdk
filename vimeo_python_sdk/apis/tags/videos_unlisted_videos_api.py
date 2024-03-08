# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.channels_channel_id_videos_video_id_privacy_users.put import GrantAccessToUsers
from vimeo_python_sdk.paths.videos_video_id_privacy_users.put import GrantAccessToUsers0
from vimeo_python_sdk.paths.videos_video_id_privacy_users_user_id.put import GrantUserAccess
from vimeo_python_sdk.paths.channels_channel_id_videos_video_id_privacy_users.get import ListAccessibleUsers
from vimeo_python_sdk.paths.videos_video_id_privacy_users.get import ListAccessibleUsers0
from vimeo_python_sdk.paths.videos_video_id_privacy_users_user_id.delete import RestrictUserAccess
from vimeo_python_sdk.apis.tags.videos_unlisted_videos_api_raw import VideosUnlistedVideosApiRaw


class VideosUnlistedVideosApi(
    GrantAccessToUsers,
    GrantAccessToUsers0,
    GrantUserAccess,
    ListAccessibleUsers,
    ListAccessibleUsers0,
    RestrictUserAccess,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: VideosUnlistedVideosApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = VideosUnlistedVideosApiRaw(api_client)
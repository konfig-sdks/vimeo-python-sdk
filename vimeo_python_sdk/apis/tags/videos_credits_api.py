# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.videos_video_id_credits.post import AddUserCredit
from vimeo_python_sdk.paths.channels_channel_id_videos_video_id_credits.post import AddUserCreditInVideo
from vimeo_python_sdk.paths.videos_video_id_credits_credit_id.delete import DeleteUserCredit
from vimeo_python_sdk.paths.videos_video_id_credits_credit_id.patch import EditUserCreditInVideo
from vimeo_python_sdk.paths.channels_channel_id_videos_video_id_credits.get import GetAllCreditedUsersInVideo
from vimeo_python_sdk.paths.videos_video_id_credits.get import GetAllCreditedUsersInVideo0
from vimeo_python_sdk.paths.videos_video_id_credits_credit_id.get import GetSpecificCreditedUser
from vimeo_python_sdk.paths.videos_video_id_credits_available_users.get import Users
from vimeo_python_sdk.apis.tags.videos_credits_api_raw import VideosCreditsApiRaw


class VideosCreditsApi(
    AddUserCredit,
    AddUserCreditInVideo,
    DeleteUserCredit,
    EditUserCreditInVideo,
    GetAllCreditedUsersInVideo,
    GetAllCreditedUsersInVideo0,
    GetSpecificCreditedUser,
    Users,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: VideosCreditsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = VideosCreditsApiRaw(api_client)

# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.videos_video_id_credits.post import AddUserCreditRaw
from vimeo_python_sdk.paths.channels_channel_id_videos_video_id_credits.post import AddUserCreditInVideoRaw
from vimeo_python_sdk.paths.videos_video_id_credits_credit_id.delete import DeleteUserCreditRaw
from vimeo_python_sdk.paths.videos_video_id_credits_credit_id.patch import EditUserCreditInVideoRaw
from vimeo_python_sdk.paths.channels_channel_id_videos_video_id_credits.get import GetAllCreditedUsersInVideoRaw
from vimeo_python_sdk.paths.videos_video_id_credits.get import GetAllCreditedUsersInVideo0Raw
from vimeo_python_sdk.paths.videos_video_id_credits_credit_id.get import GetSpecificCreditedUserRaw
from vimeo_python_sdk.paths.videos_video_id_credits_available_users.get import UsersRaw


class VideosCreditsApiRaw(
    AddUserCreditRaw,
    AddUserCreditInVideoRaw,
    DeleteUserCreditRaw,
    EditUserCreditInVideoRaw,
    GetAllCreditedUsersInVideoRaw,
    GetAllCreditedUsersInVideo0Raw,
    GetSpecificCreditedUserRaw,
    UsersRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
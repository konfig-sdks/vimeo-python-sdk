# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.users_user_id_following_follow_user_id.get import CheckFollowingStatus
from vimeo_python_sdk.paths.me_following_follow_user_id.get import CheckFollowingUser
from vimeo_python_sdk.paths.me_following.post import FollowMultipleUsers
from vimeo_python_sdk.paths.me_following_follow_user_id.put import FollowSpecificUser
from vimeo_python_sdk.paths.users_user_id_followers.get import Followers
from vimeo_python_sdk.paths.me_followers.get import ListAll
from vimeo_python_sdk.paths.users_user_id_following.get import ListOfFollowedUsers
from vimeo_python_sdk.paths.me_following.get import ListOfFollowingUsers
from vimeo_python_sdk.paths.me_following_follow_user_id.delete import StopFollowingUser
from vimeo_python_sdk.paths.users_user_id_following_follow_user_id.put import User
from vimeo_python_sdk.paths.users_user_id_following_follow_user_id.delete import User0
from vimeo_python_sdk.paths.users_user_id_following.post import Users
from vimeo_python_sdk.apis.tags.users_followers_api_raw import UsersFollowersApiRaw


class UsersFollowersApi(
    CheckFollowingStatus,
    CheckFollowingUser,
    FollowMultipleUsers,
    FollowSpecificUser,
    Followers,
    ListAll,
    ListOfFollowedUsers,
    ListOfFollowingUsers,
    StopFollowingUser,
    User,
    User0,
    Users,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UsersFollowersApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UsersFollowersApiRaw(api_client)

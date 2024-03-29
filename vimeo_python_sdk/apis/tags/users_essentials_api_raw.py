# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.me.patch import EditVimeoAccountRaw
from vimeo_python_sdk.paths.me.get import GetUserRaw
from vimeo_python_sdk.paths.users_user_id.get import UserRaw
from vimeo_python_sdk.paths.users_user_id.patch import User0Raw


class UsersEssentialsApiRaw(
    EditVimeoAccountRaw,
    GetUserRaw,
    UserRaw,
    User0Raw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.users_user_id_feed.get import Feed
from vimeo_python_sdk.paths.me_feed.get import GetUserFeedVideos
from vimeo_python_sdk.apis.tags.users_feeds_api_raw import UsersFeedsApiRaw


class UsersFeedsApi(
    Feed,
    GetUserFeedVideos,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UsersFeedsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UsersFeedsApiRaw(api_client)
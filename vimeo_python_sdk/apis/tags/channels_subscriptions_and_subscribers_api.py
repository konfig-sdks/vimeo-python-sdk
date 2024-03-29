# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.me_channels_channel_id.get import CheckIfUserFollowsChannel
from vimeo_python_sdk.paths.users_user_id_channels_channel_id.get import CheckUserFollowsChannel
from vimeo_python_sdk.paths.channels_channel_id_users.get import ListChannelFollowers
from vimeo_python_sdk.paths.users_user_id_channels_channel_id.put import SubscribeToChannel
from vimeo_python_sdk.paths.me_channels_channel_id.put import SubscribeUserToChannel
from vimeo_python_sdk.paths.me_channels_channel_id.delete import UnsubscribeUserFromChannel
from vimeo_python_sdk.paths.users_user_id_channels_channel_id.delete import UnsubscribeUserFromChannel0
from vimeo_python_sdk.apis.tags.channels_subscriptions_and_subscribers_api_raw import ChannelsSubscriptionsAndSubscribersApiRaw


class ChannelsSubscriptionsAndSubscribersApi(
    CheckIfUserFollowsChannel,
    CheckUserFollowsChannel,
    ListChannelFollowers,
    SubscribeToChannel,
    SubscribeUserToChannel,
    UnsubscribeUserFromChannel,
    UnsubscribeUserFromChannel0,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ChannelsSubscriptionsAndSubscribersApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ChannelsSubscriptionsAndSubscribersApiRaw(api_client)

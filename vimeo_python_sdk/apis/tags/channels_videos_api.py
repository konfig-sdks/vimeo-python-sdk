# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.channels_channel_id_videos.put import AddMultipleToChannel
from vimeo_python_sdk.paths.channels_channel_id_videos_video_id.put import AddVideoToChannel
from vimeo_python_sdk.paths.videos_video_id_available_channels.get import GetAccessibleChannels
from vimeo_python_sdk.paths.channels_channel_id_videos_video_id.get import GetSpecificVideoInChannel
from vimeo_python_sdk.paths.channels_channel_id_videos.get import ListInChannel
from vimeo_python_sdk.paths.channels_channel_id_videos.delete import RemoveMultipleFromChannel
from vimeo_python_sdk.paths.channels_channel_id_videos_video_id.delete import RemoveSpecificVideo
from vimeo_python_sdk.apis.tags.channels_videos_api_raw import ChannelsVideosApiRaw


class ChannelsVideosApi(
    AddMultipleToChannel,
    AddVideoToChannel,
    GetAccessibleChannels,
    GetSpecificVideoInChannel,
    ListInChannel,
    RemoveMultipleFromChannel,
    RemoveSpecificVideo,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ChannelsVideosApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ChannelsVideosApiRaw(api_client)
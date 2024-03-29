# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.me_live_events_live_event_id_m3u8_playback.get import GetUrlRaw
from vimeo_python_sdk.paths.users_user_id_live_events_live_event_id_m3u8_playback.get import GetUrlForEventStreamRaw


class LiveEventM3U8PlaybackApiRaw(
    GetUrlRaw,
    GetUrlForEventStreamRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

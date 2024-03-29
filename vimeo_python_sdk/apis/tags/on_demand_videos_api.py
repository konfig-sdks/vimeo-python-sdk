# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_videos_video_id.put import AddVideoToPage
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_videos.get import GetAllVideos
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_videos_video_id.delete import RemoveFromPage
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_videos_video_id.get import SpecificVideoGet
from vimeo_python_sdk.apis.tags.on_demand_videos_api_raw import OnDemandVideosApiRaw


class OnDemandVideosApi(
    AddVideoToPage,
    GetAllVideos,
    RemoveFromPage,
    SpecificVideoGet,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: OnDemandVideosApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = OnDemandVideosApiRaw(api_client)

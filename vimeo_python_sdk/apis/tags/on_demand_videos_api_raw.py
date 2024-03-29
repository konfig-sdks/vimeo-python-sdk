# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_videos_video_id.put import AddVideoToPageRaw
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_videos.get import GetAllVideosRaw
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_videos_video_id.delete import RemoveFromPageRaw
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_videos_video_id.get import SpecificVideoGetRaw


class OnDemandVideosApiRaw(
    AddVideoToPageRaw,
    GetAllVideosRaw,
    RemoveFromPageRaw,
    SpecificVideoGetRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

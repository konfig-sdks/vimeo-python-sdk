# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.videos_video_id_categories.get import GetAllVideoCategories
from vimeo_python_sdk.paths.categories_category_videos_video_id.get import GetVideoInCategory
from vimeo_python_sdk.paths.categories_category_videos.get import ListVideosInCategory
from vimeo_python_sdk.paths.videos_video_id_categories.put import SetVideoCategories
from vimeo_python_sdk.apis.tags.categories_videos_api_raw import CategoriesVideosApiRaw


class CategoriesVideosApi(
    GetAllVideoCategories,
    GetVideoInCategory,
    ListVideosInCategory,
    SetVideoCategories,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CategoriesVideosApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CategoriesVideosApiRaw(api_client)
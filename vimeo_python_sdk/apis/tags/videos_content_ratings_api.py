# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.contentratings.get import GetAllContentRatings
from vimeo_python_sdk.apis.tags.videos_content_ratings_api_raw import VideosContentRatingsApiRaw


class VideosContentRatingsApi(
    GetAllContentRatings,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: VideosContentRatingsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = VideosContentRatingsApiRaw(api_client)

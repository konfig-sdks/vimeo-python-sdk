# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_pictures.post import AddPosterToPage
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_pictures.get import GetOnDemandPagePosters
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_pictures_poster_id.get import GetSpecificPoster
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_pictures_poster_id.patch import UpdatePoster
from vimeo_python_sdk.apis.tags.on_demand_posters_api_raw import OnDemandPostersApiRaw


class OnDemandPostersApi(
    AddPosterToPage,
    GetOnDemandPagePosters,
    GetSpecificPoster,
    UpdatePoster,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: OnDemandPostersApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = OnDemandPostersApiRaw(api_client)

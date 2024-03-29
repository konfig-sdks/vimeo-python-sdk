# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_pictures.post import AddPosterToPageRaw
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_pictures.get import GetOnDemandPagePostersRaw
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_pictures_poster_id.get import GetSpecificPosterRaw
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_pictures_poster_id.patch import UpdatePosterRaw


class OnDemandPostersApiRaw(
    AddPosterToPageRaw,
    GetOnDemandPagePostersRaw,
    GetSpecificPosterRaw,
    UpdatePosterRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

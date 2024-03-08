# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_regions.put import AddMultipleRaw
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_regions_country.put import AddRegionToPageRaw
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_regions.get import GetAllRaw
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_regions_country.get import GetSpecificRegionRaw
from vimeo_python_sdk.paths.ondemand_regions_country.get import RegionRaw
from vimeo_python_sdk.paths.ondemand_regions.get import RegionsRaw
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_regions.delete import RemoveMultipleRaw
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_regions_country.delete import RemoveSpecificRegionRaw


class OnDemandRegionsApiRaw(
    AddMultipleRaw,
    AddRegionToPageRaw,
    GetAllRaw,
    GetSpecificRegionRaw,
    RegionRaw,
    RegionsRaw,
    RemoveMultipleRaw,
    RemoveSpecificRegionRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

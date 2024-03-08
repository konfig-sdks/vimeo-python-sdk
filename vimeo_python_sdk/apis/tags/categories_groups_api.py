# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.categories_category_groups.get import GetAllGroups
from vimeo_python_sdk.apis.tags.categories_groups_api_raw import CategoriesGroupsApiRaw


class CategoriesGroupsApi(
    GetAllGroups,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CategoriesGroupsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CategoriesGroupsApiRaw(api_client)

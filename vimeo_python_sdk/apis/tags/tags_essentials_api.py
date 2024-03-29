# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.tags_word.get import Tag
from vimeo_python_sdk.apis.tags.tags_essentials_api_raw import TagsEssentialsApiRaw


class TagsEssentialsApi(
    Tag,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TagsEssentialsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TagsEssentialsApiRaw(api_client)

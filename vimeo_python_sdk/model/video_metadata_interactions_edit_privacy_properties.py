# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from vimeo_python_sdk import schemas  # noqa: F401


class VideoMetadataInteractionsEditPrivacyProperties(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    An array of suggested fields to be used for this interaction.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['VideoMetadataInteractionsEditPrivacyPropertiesItem']:
            return VideoMetadataInteractionsEditPrivacyPropertiesItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['VideoMetadataInteractionsEditPrivacyPropertiesItem'], typing.List['VideoMetadataInteractionsEditPrivacyPropertiesItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'VideoMetadataInteractionsEditPrivacyProperties':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'VideoMetadataInteractionsEditPrivacyPropertiesItem':
        return super().__getitem__(i)

from vimeo_python_sdk.model.video_metadata_interactions_edit_privacy_properties_item import VideoMetadataInteractionsEditPrivacyPropertiesItem

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


class VideosShowcasesAddToMultipleShowcasesRequestRemove(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    The array of showcases to remove the video from. Specify these with a batch request; see our [Using Common Formats and Parameters](https://developer.vimeo.com/api/common-formats#working-with-batch-requests) guide for more information.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['VideosShowcasesAddToMultipleShowcasesRequestRemoveItem']:
            return VideosShowcasesAddToMultipleShowcasesRequestRemoveItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['VideosShowcasesAddToMultipleShowcasesRequestRemoveItem'], typing.List['VideosShowcasesAddToMultipleShowcasesRequestRemoveItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'VideosShowcasesAddToMultipleShowcasesRequestRemove':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'VideosShowcasesAddToMultipleShowcasesRequestRemoveItem':
        return super().__getitem__(i)

from vimeo_python_sdk.model.videos_showcases_add_to_multiple_showcases_request_remove_item import VideosShowcasesAddToMultipleShowcasesRequestRemoveItem
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


class DisabledVideoPropertiesEmbedPresetsReasons(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    The reasons why embed presets are disabled for the video.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['DisabledVideoPropertiesEmbedPresetsReasonsItem']:
            return DisabledVideoPropertiesEmbedPresetsReasonsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['DisabledVideoPropertiesEmbedPresetsReasonsItem'], typing.List['DisabledVideoPropertiesEmbedPresetsReasonsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DisabledVideoPropertiesEmbedPresetsReasons':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'DisabledVideoPropertiesEmbedPresetsReasonsItem':
        return super().__getitem__(i)

from vimeo_python_sdk.model.disabled_video_properties_embed_presets_reasons_item import DisabledVideoPropertiesEmbedPresetsReasonsItem
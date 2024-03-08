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


class LiveEventRecurringEmbedLogos(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A collection of information about the logo in the corner of the embeddable player.
    """


    class MetaOapg:
        required = {
            "vimeo",
            "custom",
        }
        
        class properties:
        
            @staticmethod
            def custom() -> typing.Type['LiveEventRecurringEmbedLogosCustom']:
                return LiveEventRecurringEmbedLogosCustom
            vimeo = schemas.BoolSchema
            __annotations__ = {
                "custom": custom,
                "vimeo": vimeo,
            }
    
    vimeo: MetaOapg.properties.vimeo
    custom: 'LiveEventRecurringEmbedLogosCustom'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom"]) -> 'LiveEventRecurringEmbedLogosCustom': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vimeo"]) -> MetaOapg.properties.vimeo: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["custom", "vimeo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom"]) -> 'LiveEventRecurringEmbedLogosCustom': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vimeo"]) -> MetaOapg.properties.vimeo: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["custom", "vimeo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        vimeo: typing.Union[MetaOapg.properties.vimeo, bool, ],
        custom: 'LiveEventRecurringEmbedLogosCustom',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LiveEventRecurringEmbedLogos':
        return super().__new__(
            cls,
            *args,
            vimeo=vimeo,
            custom=custom,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.live_event_recurring_embed_logos_custom import LiveEventRecurringEmbedLogosCustom

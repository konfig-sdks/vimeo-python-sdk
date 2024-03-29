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


class OnDemandPageColors(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The first and second colors of the On Demand page.
    """


    class MetaOapg:
        required = {
            "secondary",
            "primary",
        }
        
        class properties:
            primary = schemas.StrSchema
            secondary = schemas.StrSchema
            __annotations__ = {
                "primary": primary,
                "secondary": secondary,
            }
    
    secondary: MetaOapg.properties.secondary
    primary: MetaOapg.properties.primary
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary"]) -> MetaOapg.properties.primary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secondary"]) -> MetaOapg.properties.secondary: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["primary", "secondary", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary"]) -> MetaOapg.properties.primary: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secondary"]) -> MetaOapg.properties.secondary: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["primary", "secondary", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        secondary: typing.Union[MetaOapg.properties.secondary, str, ],
        primary: typing.Union[MetaOapg.properties.primary, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OnDemandPageColors':
        return super().__new__(
            cls,
            *args,
            secondary=secondary,
            primary=primary,
            _configuration=_configuration,
            **kwargs,
        )

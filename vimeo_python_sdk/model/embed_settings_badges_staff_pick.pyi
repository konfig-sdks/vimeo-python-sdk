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


class EmbedSettingsBadgesStaffPick(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "normal",
            "best_of_the_month",
            "best_of_the_year",
            "premiere",
        }
        
        class properties:
            best_of_the_month = schemas.BoolSchema
            best_of_the_year = schemas.BoolSchema
            normal = schemas.BoolSchema
            premiere = schemas.BoolSchema
            __annotations__ = {
                "best_of_the_month": best_of_the_month,
                "best_of_the_year": best_of_the_year,
                "normal": normal,
                "premiere": premiere,
            }
    
    normal: MetaOapg.properties.normal
    best_of_the_month: MetaOapg.properties.best_of_the_month
    best_of_the_year: MetaOapg.properties.best_of_the_year
    premiere: MetaOapg.properties.premiere
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["best_of_the_month"]) -> MetaOapg.properties.best_of_the_month: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["best_of_the_year"]) -> MetaOapg.properties.best_of_the_year: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normal"]) -> MetaOapg.properties.normal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["premiere"]) -> MetaOapg.properties.premiere: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["best_of_the_month", "best_of_the_year", "normal", "premiere", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["best_of_the_month"]) -> MetaOapg.properties.best_of_the_month: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["best_of_the_year"]) -> MetaOapg.properties.best_of_the_year: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normal"]) -> MetaOapg.properties.normal: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["premiere"]) -> MetaOapg.properties.premiere: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["best_of_the_month", "best_of_the_year", "normal", "premiere", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        normal: typing.Union[MetaOapg.properties.normal, bool, ],
        best_of_the_month: typing.Union[MetaOapg.properties.best_of_the_month, bool, ],
        best_of_the_year: typing.Union[MetaOapg.properties.best_of_the_year, bool, ],
        premiere: typing.Union[MetaOapg.properties.premiere, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmbedSettingsBadgesStaffPick':
        return super().__new__(
            cls,
            *args,
            normal=normal,
            best_of_the_month=best_of_the_month,
            best_of_the_year=best_of_the_year,
            premiere=premiere,
            _configuration=_configuration,
            **kwargs,
        )

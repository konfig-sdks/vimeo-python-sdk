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


class LiveEventEmbedColors(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A collection of information about player colors.
    """


    class MetaOapg:
        required = {
            "color_three",
            "color_two",
            "color_four",
            "color_one",
        }
        
        class properties:
            color_four = schemas.StrSchema
            color_one = schemas.StrSchema
            color_three = schemas.StrSchema
            color_two = schemas.StrSchema
            __annotations__ = {
                "color_four": color_four,
                "color_one": color_one,
                "color_three": color_three,
                "color_two": color_two,
            }
    
    color_three: MetaOapg.properties.color_three
    color_two: MetaOapg.properties.color_two
    color_four: MetaOapg.properties.color_four
    color_one: MetaOapg.properties.color_one
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color_four"]) -> MetaOapg.properties.color_four: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color_one"]) -> MetaOapg.properties.color_one: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color_three"]) -> MetaOapg.properties.color_three: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color_two"]) -> MetaOapg.properties.color_two: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["color_four", "color_one", "color_three", "color_two", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color_four"]) -> MetaOapg.properties.color_four: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color_one"]) -> MetaOapg.properties.color_one: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color_three"]) -> MetaOapg.properties.color_three: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color_two"]) -> MetaOapg.properties.color_two: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["color_four", "color_one", "color_three", "color_two", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        color_three: typing.Union[MetaOapg.properties.color_three, str, ],
        color_two: typing.Union[MetaOapg.properties.color_two, str, ],
        color_four: typing.Union[MetaOapg.properties.color_four, str, ],
        color_one: typing.Union[MetaOapg.properties.color_one, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LiveEventEmbedColors':
        return super().__new__(
            cls,
            *args,
            color_three=color_three,
            color_two=color_two,
            color_four=color_four,
            color_one=color_one,
            _configuration=_configuration,
            **kwargs,
        )
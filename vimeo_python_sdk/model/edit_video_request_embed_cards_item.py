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


class EditVideoRequestEmbedCardsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            display_time = schemas.NumberSchema
            headline = schemas.StrSchema
            id = schemas.StrSchema
            image_url = schemas.StrSchema
            teaser = schemas.StrSchema
            timecode = schemas.NumberSchema
            url = schemas.StrSchema
            __annotations__ = {
                "display_time": display_time,
                "headline": headline,
                "id": id,
                "image_url": image_url,
                "teaser": teaser,
                "timecode": timecode,
                "url": url,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_time"]) -> MetaOapg.properties.display_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["headline"]) -> MetaOapg.properties.headline: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_url"]) -> MetaOapg.properties.image_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["teaser"]) -> MetaOapg.properties.teaser: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timecode"]) -> MetaOapg.properties.timecode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["display_time", "headline", "id", "image_url", "teaser", "timecode", "url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_time"]) -> typing.Union[MetaOapg.properties.display_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["headline"]) -> typing.Union[MetaOapg.properties.headline, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_url"]) -> typing.Union[MetaOapg.properties.image_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["teaser"]) -> typing.Union[MetaOapg.properties.teaser, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timecode"]) -> typing.Union[MetaOapg.properties.timecode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["display_time", "headline", "id", "image_url", "teaser", "timecode", "url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        display_time: typing.Union[MetaOapg.properties.display_time, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        headline: typing.Union[MetaOapg.properties.headline, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        image_url: typing.Union[MetaOapg.properties.image_url, str, schemas.Unset] = schemas.unset,
        teaser: typing.Union[MetaOapg.properties.teaser, str, schemas.Unset] = schemas.unset,
        timecode: typing.Union[MetaOapg.properties.timecode, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EditVideoRequestEmbedCardsItem':
        return super().__new__(
            cls,
            *args,
            display_time=display_time,
            headline=headline,
            id=id,
            image_url=image_url,
            teaser=teaser,
            timecode=timecode,
            url=url,
            _configuration=_configuration,
            **kwargs,
        )

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


class Chapter(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "thumbnails",
            "title",
            "uri",
            "timecode",
        }
        
        class properties:
            
            
            class title(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'title':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class thumbnails(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Picture']:
                        return Picture
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Picture'], typing.List['Picture']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'thumbnails':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Picture':
                    return super().__getitem__(i)
            
            
            class timecode(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'timecode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            uri = schemas.StrSchema
            active_thumbnail_uri = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "thumbnails": thumbnails,
                "timecode": timecode,
                "uri": uri,
                "active_thumbnail_uri": active_thumbnail_uri,
            }
    
    thumbnails: MetaOapg.properties.thumbnails
    title: MetaOapg.properties.title
    uri: MetaOapg.properties.uri
    timecode: MetaOapg.properties.timecode
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thumbnails"]) -> MetaOapg.properties.thumbnails: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timecode"]) -> MetaOapg.properties.timecode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active_thumbnail_uri"]) -> MetaOapg.properties.active_thumbnail_uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "thumbnails", "timecode", "uri", "active_thumbnail_uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thumbnails"]) -> MetaOapg.properties.thumbnails: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timecode"]) -> MetaOapg.properties.timecode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active_thumbnail_uri"]) -> typing.Union[MetaOapg.properties.active_thumbnail_uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "thumbnails", "timecode", "uri", "active_thumbnail_uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        thumbnails: typing.Union[MetaOapg.properties.thumbnails, list, tuple, ],
        title: typing.Union[MetaOapg.properties.title, None, str, ],
        uri: typing.Union[MetaOapg.properties.uri, str, ],
        timecode: typing.Union[MetaOapg.properties.timecode, None, decimal.Decimal, int, float, ],
        active_thumbnail_uri: typing.Union[MetaOapg.properties.active_thumbnail_uri, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Chapter':
        return super().__new__(
            cls,
            *args,
            thumbnails=thumbnails,
            title=title,
            uri=uri,
            timecode=timecode,
            active_thumbnail_uri=active_thumbnail_uri,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.picture import Picture

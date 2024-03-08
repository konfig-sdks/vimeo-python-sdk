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


class VideosTextTracksAddTextTrackRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
            "language",
            "type",
        }
        
        class properties:
            language = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CAPTIONS(cls):
                    return cls("captions")
                
                @schemas.classproperty
                def CHAPTERS(cls):
                    return cls("chapters")
                
                @schemas.classproperty
                def DESCRIPTIONS(cls):
                    return cls("descriptions")
                
                @schemas.classproperty
                def METADATA(cls):
                    return cls("metadata")
                
                @schemas.classproperty
                def SUBTITLES(cls):
                    return cls("subtitles")
            active = schemas.BoolSchema
            is_auto_generated = schemas.BoolSchema
            is_edited = schemas.BoolSchema
            __annotations__ = {
                "language": language,
                "name": name,
                "type": type,
                "active": active,
                "is_auto_generated": is_auto_generated,
                "is_edited": is_edited,
            }
    
    name: MetaOapg.properties.name
    language: MetaOapg.properties.language
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_auto_generated"]) -> MetaOapg.properties.is_auto_generated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_edited"]) -> MetaOapg.properties.is_edited: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["language", "name", "type", "active", "is_auto_generated", "is_edited", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_auto_generated"]) -> typing.Union[MetaOapg.properties.is_auto_generated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_edited"]) -> typing.Union[MetaOapg.properties.is_edited, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["language", "name", "type", "active", "is_auto_generated", "is_edited", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        language: typing.Union[MetaOapg.properties.language, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        is_auto_generated: typing.Union[MetaOapg.properties.is_auto_generated, bool, schemas.Unset] = schemas.unset,
        is_edited: typing.Union[MetaOapg.properties.is_edited, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VideosTextTracksAddTextTrackRequest':
        return super().__new__(
            cls,
            *args,
            name=name,
            language=language,
            type=type,
            active=active,
            is_auto_generated=is_auto_generated,
            is_edited=is_edited,
            _configuration=_configuration,
            **kwargs,
        )

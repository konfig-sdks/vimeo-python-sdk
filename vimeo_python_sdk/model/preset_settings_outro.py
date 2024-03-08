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


class PresetSettingsOutro(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "type",
        }
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "link": "LINK",
                        "no idea": "NO_IDEA",
                        "text": "TEXT",
                        "uploaded_clips": "UPLOADED_CLIPS",
                        "uploaded_videos": "UPLOADED_VIDEOS",
                    }
                
                @schemas.classproperty
                def LINK(cls):
                    return cls("link")
                
                @schemas.classproperty
                def NO_IDEA(cls):
                    return cls("no idea")
                
                @schemas.classproperty
                def TEXT(cls):
                    return cls("text")
                
                @schemas.classproperty
                def UPLOADED_CLIPS(cls):
                    return cls("uploaded_clips")
                
                @schemas.classproperty
                def UPLOADED_VIDEOS(cls):
                    return cls("uploaded_videos")
            
            
            class clips(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'clips':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def link() -> typing.Type['PresetSettingsOutroLink']:
                return PresetSettingsOutroLink
            
            
            class text(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'text':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class videos(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'videos':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "type": type,
                "clips": clips,
                "link": link,
                "text": text,
                "videos": videos,
            }
    
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clips"]) -> MetaOapg.properties.clips: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> 'PresetSettingsOutroLink': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["videos"]) -> MetaOapg.properties.videos: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "clips", "link", "text", "videos", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clips"]) -> typing.Union[MetaOapg.properties.clips, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> typing.Union['PresetSettingsOutroLink', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> typing.Union[MetaOapg.properties.text, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["videos"]) -> typing.Union[MetaOapg.properties.videos, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "clips", "link", "text", "videos", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        clips: typing.Union[MetaOapg.properties.clips, None, str, schemas.Unset] = schemas.unset,
        link: typing.Union['PresetSettingsOutroLink', schemas.Unset] = schemas.unset,
        text: typing.Union[MetaOapg.properties.text, None, str, schemas.Unset] = schemas.unset,
        videos: typing.Union[MetaOapg.properties.videos, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PresetSettingsOutro':
        return super().__new__(
            cls,
            *args,
            type=type,
            clips=clips,
            link=link,
            text=text,
            videos=videos,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.preset_settings_outro_link import PresetSettingsOutroLink

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


class LiveEventDestinationsCreateOneTimeLiveEventDestinationRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "service_name",
            "display_name",
            "type",
        }
        
        class properties:
            display_name = schemas.StrSchema
            
            
            class service_name(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "custom_rtmp": "CUSTOM_RTMP",
                        "facebook": "FACEBOOK",
                        "linkedin": "LINKEDIN",
                        "youtube": "YOUTUBE",
                    }
                
                @schemas.classproperty
                def CUSTOM_RTMP(cls):
                    return cls("custom_rtmp")
                
                @schemas.classproperty
                def FACEBOOK(cls):
                    return cls("facebook")
                
                @schemas.classproperty
                def LINKEDIN(cls):
                    return cls("linkedin")
                
                @schemas.classproperty
                def YOUTUBE(cls):
                    return cls("youtube")
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "channel": "CHANNEL",
                        "custom": "CUSTOM",
                        "organization": "ORGANIZATION",
                        "page": "PAGE",
                        "profile": "PROFILE",
                    }
                
                @schemas.classproperty
                def CHANNEL(cls):
                    return cls("channel")
                
                @schemas.classproperty
                def CUSTOM(cls):
                    return cls("custom")
                
                @schemas.classproperty
                def ORGANIZATION(cls):
                    return cls("organization")
                
                @schemas.classproperty
                def PAGE(cls):
                    return cls("page")
                
                @schemas.classproperty
                def PROFILE(cls):
                    return cls("profile")
            is_enabled = schemas.BoolSchema
            
            
            class privacy(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "CONNECTIONS": "CONNECTIONS",
                        "PUBLIC": "PUBLIC",
                        "all_friends": "ALL_FRIENDS",
                        "everyone": "EVERYONE",
                        "private": "PRIVATE",
                        "public": "PUBLIC",
                        "self": "SELF",
                        "unlisted": "UNLISTED",
                    }
                
                @schemas.classproperty
                def CONNECTIONS(cls):
                    return cls("CONNECTIONS")
                
                @schemas.classproperty
                def PUBLIC(cls):
                    return cls("PUBLIC")
                
                @schemas.classproperty
                def ALL_FRIENDS(cls):
                    return cls("all_friends")
                
                @schemas.classproperty
                def EVERYONE(cls):
                    return cls("everyone")
                
                @schemas.classproperty
                def PRIVATE(cls):
                    return cls("private")
                
                @schemas.classproperty
                def PUBLIC(cls):
                    return cls("public")
                
                @schemas.classproperty
                def SELF(cls):
                    return cls("self")
                
                @schemas.classproperty
                def UNLISTED(cls):
                    return cls("unlisted")
            provider_destination_id = schemas.StrSchema
            
            
            class provider_video_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'provider_video_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            scheduled_at = schemas.NumberSchema
            stream_key = schemas.StrSchema
            stream_url = schemas.StrSchema
            __annotations__ = {
                "display_name": display_name,
                "service_name": service_name,
                "type": type,
                "is_enabled": is_enabled,
                "privacy": privacy,
                "provider_destination_id": provider_destination_id,
                "provider_video_id": provider_video_id,
                "scheduled_at": scheduled_at,
                "stream_key": stream_key,
                "stream_url": stream_url,
            }
    
    service_name: MetaOapg.properties.service_name
    display_name: MetaOapg.properties.display_name
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["service_name"]) -> MetaOapg.properties.service_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_enabled"]) -> MetaOapg.properties.is_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privacy"]) -> MetaOapg.properties.privacy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider_destination_id"]) -> MetaOapg.properties.provider_destination_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider_video_id"]) -> MetaOapg.properties.provider_video_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheduled_at"]) -> MetaOapg.properties.scheduled_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stream_key"]) -> MetaOapg.properties.stream_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stream_url"]) -> MetaOapg.properties.stream_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["display_name", "service_name", "type", "is_enabled", "privacy", "provider_destination_id", "provider_video_id", "scheduled_at", "stream_key", "stream_url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["service_name"]) -> MetaOapg.properties.service_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_enabled"]) -> typing.Union[MetaOapg.properties.is_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privacy"]) -> typing.Union[MetaOapg.properties.privacy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider_destination_id"]) -> typing.Union[MetaOapg.properties.provider_destination_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider_video_id"]) -> typing.Union[MetaOapg.properties.provider_video_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheduled_at"]) -> typing.Union[MetaOapg.properties.scheduled_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stream_key"]) -> typing.Union[MetaOapg.properties.stream_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stream_url"]) -> typing.Union[MetaOapg.properties.stream_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["display_name", "service_name", "type", "is_enabled", "privacy", "provider_destination_id", "provider_video_id", "scheduled_at", "stream_key", "stream_url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        service_name: typing.Union[MetaOapg.properties.service_name, str, ],
        display_name: typing.Union[MetaOapg.properties.display_name, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        is_enabled: typing.Union[MetaOapg.properties.is_enabled, bool, schemas.Unset] = schemas.unset,
        privacy: typing.Union[MetaOapg.properties.privacy, str, schemas.Unset] = schemas.unset,
        provider_destination_id: typing.Union[MetaOapg.properties.provider_destination_id, str, schemas.Unset] = schemas.unset,
        provider_video_id: typing.Union[MetaOapg.properties.provider_video_id, None, str, schemas.Unset] = schemas.unset,
        scheduled_at: typing.Union[MetaOapg.properties.scheduled_at, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        stream_key: typing.Union[MetaOapg.properties.stream_key, str, schemas.Unset] = schemas.unset,
        stream_url: typing.Union[MetaOapg.properties.stream_url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LiveEventDestinationsCreateOneTimeLiveEventDestinationRequest':
        return super().__new__(
            cls,
            *args,
            service_name=service_name,
            display_name=display_name,
            type=type,
            is_enabled=is_enabled,
            privacy=privacy,
            provider_destination_id=provider_destination_id,
            provider_video_id=provider_video_id,
            scheduled_at=scheduled_at,
            stream_key=stream_key,
            stream_url=stream_url,
            _configuration=_configuration,
            **kwargs,
        )

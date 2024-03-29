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


class GroupPrivacy(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The group's privacy settings.
    """


    class MetaOapg:
        required = {
            "view",
            "comment",
            "videos",
            "invite",
            "join",
        }
        
        class properties:
            
            
            class comment(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ALL(cls):
                    return cls("all")
                
                @schemas.classproperty
                def MEMBERS(cls):
                    return cls("members")
            
            
            class invite(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ALL(cls):
                    return cls("all")
                
                @schemas.classproperty
                def MEMBERS(cls):
                    return cls("members")
            
            
            class join(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ANYBODY(cls):
                    return cls("anybody")
                
                @schemas.classproperty
                def MEMBERS(cls):
                    return cls("members")
            
            
            class videos(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ALL(cls):
                    return cls("all")
                
                @schemas.classproperty
                def MEMBERS(cls):
                    return cls("members")
            
            
            class view(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ANYBODY(cls):
                    return cls("anybody")
                
                @schemas.classproperty
                def MEMBERS(cls):
                    return cls("members")
            __annotations__ = {
                "comment": comment,
                "invite": invite,
                "join": join,
                "videos": videos,
                "view": view,
            }
    
    view: MetaOapg.properties.view
    comment: MetaOapg.properties.comment
    videos: MetaOapg.properties.videos
    invite: MetaOapg.properties.invite
    join: MetaOapg.properties.join
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invite"]) -> MetaOapg.properties.invite: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["join"]) -> MetaOapg.properties.join: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["videos"]) -> MetaOapg.properties.videos: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["view"]) -> MetaOapg.properties.view: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["comment", "invite", "join", "videos", "view", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invite"]) -> MetaOapg.properties.invite: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["join"]) -> MetaOapg.properties.join: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["videos"]) -> MetaOapg.properties.videos: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["view"]) -> MetaOapg.properties.view: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["comment", "invite", "join", "videos", "view", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        view: typing.Union[MetaOapg.properties.view, str, ],
        comment: typing.Union[MetaOapg.properties.comment, str, ],
        videos: typing.Union[MetaOapg.properties.videos, str, ],
        invite: typing.Union[MetaOapg.properties.invite, str, ],
        join: typing.Union[MetaOapg.properties.join, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GroupPrivacy':
        return super().__new__(
            cls,
            *args,
            view=view,
            comment=comment,
            videos=videos,
            invite=invite,
            join=join,
            _configuration=_configuration,
            **kwargs,
        )

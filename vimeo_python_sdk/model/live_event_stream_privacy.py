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


class LiveEventStreamPrivacy(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The initial privacy settings of videos generated by streaming to the event as well as the embed privacy of the entire collection.
    """


    class MetaOapg:
        required = {
            "view",
            "unlisted_hash",
            "embed",
        }
        
        class properties:
            
            
            class embed(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "private": "PRIVATE",
                        "public": "PUBLIC",
                        "whitelist": "WHITELIST",
                    }
                
                @schemas.classproperty
                def PRIVATE(cls):
                    return cls("private")
                
                @schemas.classproperty
                def PUBLIC(cls):
                    return cls("public")
                
                @schemas.classproperty
                def WHITELIST(cls):
                    return cls("whitelist")
            
            
            class unlisted_hash(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'unlisted_hash':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class view(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "anybody": "ANYBODY",
                        "embed_only": "EMBED_ONLY",
                        "nobody": "NOBODY",
                        "password": "PASSWORD",
                        "unlisted": "UNLISTED",
                    }
                
                @schemas.classproperty
                def ANYBODY(cls):
                    return cls("anybody")
                
                @schemas.classproperty
                def EMBED_ONLY(cls):
                    return cls("embed_only")
                
                @schemas.classproperty
                def NOBODY(cls):
                    return cls("nobody")
                
                @schemas.classproperty
                def PASSWORD(cls):
                    return cls("password")
                
                @schemas.classproperty
                def UNLISTED(cls):
                    return cls("unlisted")
            __annotations__ = {
                "embed": embed,
                "unlisted_hash": unlisted_hash,
                "view": view,
            }
    
    view: MetaOapg.properties.view
    unlisted_hash: MetaOapg.properties.unlisted_hash
    embed: MetaOapg.properties.embed
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embed"]) -> MetaOapg.properties.embed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unlisted_hash"]) -> MetaOapg.properties.unlisted_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["view"]) -> MetaOapg.properties.view: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["embed", "unlisted_hash", "view", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embed"]) -> MetaOapg.properties.embed: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unlisted_hash"]) -> MetaOapg.properties.unlisted_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["view"]) -> MetaOapg.properties.view: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["embed", "unlisted_hash", "view", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        view: typing.Union[MetaOapg.properties.view, str, ],
        unlisted_hash: typing.Union[MetaOapg.properties.unlisted_hash, None, str, ],
        embed: typing.Union[MetaOapg.properties.embed, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LiveEventStreamPrivacy':
        return super().__new__(
            cls,
            *args,
            view=view,
            unlisted_hash=unlisted_hash,
            embed=embed,
            _configuration=_configuration,
            **kwargs,
        )

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


class EditVideoRequestPrivacy(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            add = schemas.BoolSchema
            
            
            class comments(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "anybody": "ANYBODY",
                        "contacts": "CONTACTS",
                        "nobody": "NOBODY",
                    }
                
                @schemas.classproperty
                def ANYBODY(cls):
                    return cls("anybody")
                
                @schemas.classproperty
                def CONTACTS(cls):
                    return cls("contacts")
                
                @schemas.classproperty
                def NOBODY(cls):
                    return cls("nobody")
            download = schemas.BoolSchema
            
            
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
            
            
            class view(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "anybody": "ANYBODY",
                        "contacts": "CONTACTS",
                        "disable": "DISABLE",
                        "nobody": "NOBODY",
                        "password": "PASSWORD",
                        "unlisted": "UNLISTED",
                        "users": "USERS",
                    }
                
                @schemas.classproperty
                def ANYBODY(cls):
                    return cls("anybody")
                
                @schemas.classproperty
                def CONTACTS(cls):
                    return cls("contacts")
                
                @schemas.classproperty
                def DISABLE(cls):
                    return cls("disable")
                
                @schemas.classproperty
                def NOBODY(cls):
                    return cls("nobody")
                
                @schemas.classproperty
                def PASSWORD(cls):
                    return cls("password")
                
                @schemas.classproperty
                def UNLISTED(cls):
                    return cls("unlisted")
                
                @schemas.classproperty
                def USERS(cls):
                    return cls("users")
            __annotations__ = {
                "add": add,
                "comments": comments,
                "download": download,
                "embed": embed,
                "view": view,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["add"]) -> MetaOapg.properties.add: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comments"]) -> MetaOapg.properties.comments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["download"]) -> MetaOapg.properties.download: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embed"]) -> MetaOapg.properties.embed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["view"]) -> MetaOapg.properties.view: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["add", "comments", "download", "embed", "view", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["add"]) -> typing.Union[MetaOapg.properties.add, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comments"]) -> typing.Union[MetaOapg.properties.comments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["download"]) -> typing.Union[MetaOapg.properties.download, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embed"]) -> typing.Union[MetaOapg.properties.embed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["view"]) -> typing.Union[MetaOapg.properties.view, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["add", "comments", "download", "embed", "view", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        add: typing.Union[MetaOapg.properties.add, bool, schemas.Unset] = schemas.unset,
        comments: typing.Union[MetaOapg.properties.comments, str, schemas.Unset] = schemas.unset,
        download: typing.Union[MetaOapg.properties.download, bool, schemas.Unset] = schemas.unset,
        embed: typing.Union[MetaOapg.properties.embed, str, schemas.Unset] = schemas.unset,
        view: typing.Union[MetaOapg.properties.view, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EditVideoRequestPrivacy':
        return super().__new__(
            cls,
            *args,
            add=add,
            comments=comments,
            download=download,
            embed=embed,
            view=view,
            _configuration=_configuration,
            **kwargs,
        )

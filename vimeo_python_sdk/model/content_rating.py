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


class ContentRating(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "code",
            "name",
            "uri",
        }
        
        class properties:
            
            
            class code(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "advertisement": "ADVERTISEMENT",
                        "drugs": "DRUGS",
                        "language": "LANGUAGE",
                        "nudity": "NUDITY",
                        "safe": "SAFE",
                        "unrated": "UNRATED",
                        "violence": "VIOLENCE",
                    }
                
                @schemas.classproperty
                def ADVERTISEMENT(cls):
                    return cls("advertisement")
                
                @schemas.classproperty
                def DRUGS(cls):
                    return cls("drugs")
                
                @schemas.classproperty
                def LANGUAGE(cls):
                    return cls("language")
                
                @schemas.classproperty
                def NUDITY(cls):
                    return cls("nudity")
                
                @schemas.classproperty
                def SAFE(cls):
                    return cls("safe")
                
                @schemas.classproperty
                def UNRATED(cls):
                    return cls("unrated")
                
                @schemas.classproperty
                def VIOLENCE(cls):
                    return cls("violence")
            name = schemas.StrSchema
            
            
            class uri(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'uri':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "code": code,
                "name": name,
                "uri": uri,
            }
    
    code: MetaOapg.properties.code
    name: MetaOapg.properties.name
    uri: MetaOapg.properties.uri
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["code", "name", "uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["code", "name", "uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        code: typing.Union[MetaOapg.properties.code, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        uri: typing.Union[MetaOapg.properties.uri, None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContentRating':
        return super().__new__(
            cls,
            *args,
            code=code,
            name=name,
            uri=uri,
            _configuration=_configuration,
            **kwargs,
        )

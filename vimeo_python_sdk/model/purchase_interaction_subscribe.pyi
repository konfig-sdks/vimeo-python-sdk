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


class PurchaseInteractionSubscribe(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Information on subscribing to the On Demand video.
    """


    class MetaOapg:
        
        class properties:
            drm = schemas.BoolSchema
            
            
            class expires_time(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'expires_time':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class link(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'link':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class purchase_time(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'purchase_time':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class stream(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AVAILABLE(cls):
                    return cls("available")
                
                @schemas.classproperty
                def PURCHASED(cls):
                    return cls("purchased")
                
                @schemas.classproperty
                def RESTRICTED(cls):
                    return cls("restricted")
                
                @schemas.classproperty
                def UNAVAILABLE(cls):
                    return cls("unavailable")
            
            
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
                "drm": drm,
                "expires_time": expires_time,
                "link": link,
                "purchase_time": purchase_time,
                "stream": stream,
                "uri": uri,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["drm"]) -> MetaOapg.properties.drm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires_time"]) -> MetaOapg.properties.expires_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["purchase_time"]) -> MetaOapg.properties.purchase_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stream"]) -> MetaOapg.properties.stream: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["drm", "expires_time", "link", "purchase_time", "stream", "uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["drm"]) -> typing.Union[MetaOapg.properties.drm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires_time"]) -> typing.Union[MetaOapg.properties.expires_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> typing.Union[MetaOapg.properties.link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["purchase_time"]) -> typing.Union[MetaOapg.properties.purchase_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stream"]) -> typing.Union[MetaOapg.properties.stream, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> typing.Union[MetaOapg.properties.uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["drm", "expires_time", "link", "purchase_time", "stream", "uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        drm: typing.Union[MetaOapg.properties.drm, bool, schemas.Unset] = schemas.unset,
        expires_time: typing.Union[MetaOapg.properties.expires_time, None, str, schemas.Unset] = schemas.unset,
        link: typing.Union[MetaOapg.properties.link, None, str, schemas.Unset] = schemas.unset,
        purchase_time: typing.Union[MetaOapg.properties.purchase_time, None, str, schemas.Unset] = schemas.unset,
        stream: typing.Union[MetaOapg.properties.stream, str, schemas.Unset] = schemas.unset,
        uri: typing.Union[MetaOapg.properties.uri, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PurchaseInteractionSubscribe':
        return super().__new__(
            cls,
            *args,
            drm=drm,
            expires_time=expires_time,
            link=link,
            purchase_time=purchase_time,
            stream=stream,
            uri=uri,
            _configuration=_configuration,
            **kwargs,
        )

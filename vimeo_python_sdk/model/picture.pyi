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


class Picture(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "sizes",
            "resource_key",
            "active",
            "type",
            "uri",
            "default_picture",
            "base_link",
        }
        
        class properties:
            active = schemas.BoolSchema
            base_link = schemas.StrSchema
            default_picture = schemas.BoolSchema
            resource_key = schemas.StrSchema
        
            @staticmethod
            def sizes() -> typing.Type['PictureSizes']:
                return PictureSizes
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CAUTION(cls):
                    return cls("caution")
                
                @schemas.classproperty
                def CUSTOM(cls):
                    return cls("custom")
                
                @schemas.classproperty
                def DEFAULT(cls):
                    return cls("default")
            uri = schemas.StrSchema
            link = schemas.StrSchema
            __annotations__ = {
                "active": active,
                "base_link": base_link,
                "default_picture": default_picture,
                "resource_key": resource_key,
                "sizes": sizes,
                "type": type,
                "uri": uri,
                "link": link,
            }
    
    sizes: 'PictureSizes'
    resource_key: MetaOapg.properties.resource_key
    active: MetaOapg.properties.active
    type: MetaOapg.properties.type
    uri: MetaOapg.properties.uri
    default_picture: MetaOapg.properties.default_picture
    base_link: MetaOapg.properties.base_link
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["base_link"]) -> MetaOapg.properties.base_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_picture"]) -> MetaOapg.properties.default_picture: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resource_key"]) -> MetaOapg.properties.resource_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sizes"]) -> 'PictureSizes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["active", "base_link", "default_picture", "resource_key", "sizes", "type", "uri", "link", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["base_link"]) -> MetaOapg.properties.base_link: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_picture"]) -> MetaOapg.properties.default_picture: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resource_key"]) -> MetaOapg.properties.resource_key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sizes"]) -> 'PictureSizes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> typing.Union[MetaOapg.properties.link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["active", "base_link", "default_picture", "resource_key", "sizes", "type", "uri", "link", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sizes: 'PictureSizes',
        resource_key: typing.Union[MetaOapg.properties.resource_key, str, ],
        active: typing.Union[MetaOapg.properties.active, bool, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        uri: typing.Union[MetaOapg.properties.uri, str, ],
        default_picture: typing.Union[MetaOapg.properties.default_picture, bool, ],
        base_link: typing.Union[MetaOapg.properties.base_link, str, ],
        link: typing.Union[MetaOapg.properties.link, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Picture':
        return super().__new__(
            cls,
            *args,
            sizes=sizes,
            resource_key=resource_key,
            active=active,
            type=type,
            uri=uri,
            default_picture=default_picture,
            base_link=base_link,
            link=link,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.picture_sizes import PictureSizes

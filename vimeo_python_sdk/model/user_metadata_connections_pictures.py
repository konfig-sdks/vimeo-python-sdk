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


class UserMetadataConnectionsPictures(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Information about the authenticated user's portraits.
    """


    class MetaOapg:
        required = {
            "total",
            "options",
            "uri",
        }
        
        class properties:
        
            @staticmethod
            def options() -> typing.Type['UserMetadataConnectionsPicturesOptions']:
                return UserMetadataConnectionsPicturesOptions
            total = schemas.NumberSchema
            uri = schemas.StrSchema
            __annotations__ = {
                "options": options,
                "total": total,
                "uri": uri,
            }
    
    total: MetaOapg.properties.total
    options: 'UserMetadataConnectionsPicturesOptions'
    uri: MetaOapg.properties.uri
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> 'UserMetadataConnectionsPicturesOptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["options", "total", "uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> 'UserMetadataConnectionsPicturesOptions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["options", "total", "uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, float, ],
        options: 'UserMetadataConnectionsPicturesOptions',
        uri: typing.Union[MetaOapg.properties.uri, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserMetadataConnectionsPictures':
        return super().__new__(
            cls,
            *args,
            total=total,
            options=options,
            uri=uri,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.user_metadata_connections_pictures_options import UserMetadataConnectionsPicturesOptions

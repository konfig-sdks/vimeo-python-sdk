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


class CategoryMetadataInteractionsFollow(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An action indicating if the authenticated user has followed the category.
    """


    class MetaOapg:
        required = {
            "added_time",
            "added",
            "uri",
        }
        
        class properties:
            added = schemas.BoolSchema
            
            
            class added_time(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'added_time':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            uri = schemas.StrSchema
            __annotations__ = {
                "added": added,
                "added_time": added_time,
                "uri": uri,
            }
    
    added_time: MetaOapg.properties.added_time
    added: MetaOapg.properties.added
    uri: MetaOapg.properties.uri
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["added"]) -> MetaOapg.properties.added: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["added_time"]) -> MetaOapg.properties.added_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["added", "added_time", "uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["added"]) -> MetaOapg.properties.added: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["added_time"]) -> MetaOapg.properties.added_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["added", "added_time", "uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        added_time: typing.Union[MetaOapg.properties.added_time, None, str, ],
        added: typing.Union[MetaOapg.properties.added, bool, ],
        uri: typing.Union[MetaOapg.properties.uri, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CategoryMetadataInteractionsFollow':
        return super().__new__(
            cls,
            *args,
            added_time=added_time,
            added=added,
            uri=uri,
            _configuration=_configuration,
            **kwargs,
        )

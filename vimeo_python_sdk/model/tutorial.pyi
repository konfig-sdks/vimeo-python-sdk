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


class Tutorial(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "token_is_authenticated",
            "next_steps_link",
            "message",
        }
        
        class properties:
            message = schemas.StrSchema
            next_steps_link = schemas.StrSchema
            token_is_authenticated = schemas.BoolSchema
            __annotations__ = {
                "message": message,
                "next_steps_link": next_steps_link,
                "token_is_authenticated": token_is_authenticated,
            }
    
    token_is_authenticated: MetaOapg.properties.token_is_authenticated
    next_steps_link: MetaOapg.properties.next_steps_link
    message: MetaOapg.properties.message
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_steps_link"]) -> MetaOapg.properties.next_steps_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_is_authenticated"]) -> MetaOapg.properties.token_is_authenticated: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", "next_steps_link", "token_is_authenticated", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_steps_link"]) -> MetaOapg.properties.next_steps_link: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_is_authenticated"]) -> MetaOapg.properties.token_is_authenticated: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", "next_steps_link", "token_is_authenticated", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        token_is_authenticated: typing.Union[MetaOapg.properties.token_is_authenticated, bool, ],
        next_steps_link: typing.Union[MetaOapg.properties.next_steps_link, str, ],
        message: typing.Union[MetaOapg.properties.message, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Tutorial':
        return super().__new__(
            cls,
            *args,
            token_is_authenticated=token_is_authenticated,
            next_steps_link=next_steps_link,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )

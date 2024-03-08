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


class LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacy(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The privacy settings of the event.
    """


    class MetaOapg:
        
        class properties:
            
            
            class view(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
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
                "view": view,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["view"]) -> MetaOapg.properties.view: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["view", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["view"]) -> typing.Union[MetaOapg.properties.view, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["view", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        view: typing.Union[MetaOapg.properties.view, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacy':
        return super().__new__(
            cls,
            *args,
            view=view,
            _configuration=_configuration,
            **kwargs,
        )

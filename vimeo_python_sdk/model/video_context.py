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


class VideoContext(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The context of the video's subscription, if the video is part of a subscription.
    """


    class MetaOapg:
        required = {
            "resource",
            "resource_type",
            "action",
        }
        
        class properties:
            
            
            class action(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Added to": "ADDED_TO",
                        "Appearance by": "APPEARANCE_BY",
                        "Liked by": "LIKED_BY",
                        "Uploaded by": "UPLOADED_BY",
                    }
                
                @schemas.classproperty
                def ADDED_TO(cls):
                    return cls("Added to")
                
                @schemas.classproperty
                def APPEARANCE_BY(cls):
                    return cls("Appearance by")
                
                @schemas.classproperty
                def LIKED_BY(cls):
                    return cls("Liked by")
                
                @schemas.classproperty
                def UPLOADED_BY(cls):
                    return cls("Uploaded by")
            
            
            class resource(
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'resource':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            resource_type = schemas.StrSchema
            __annotations__ = {
                "action": action,
                "resource": resource,
                "resource_type": resource_type,
            }
    
    resource: MetaOapg.properties.resource
    resource_type: MetaOapg.properties.resource_type
    action: MetaOapg.properties.action
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resource"]) -> MetaOapg.properties.resource: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["action", "resource", "resource_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resource"]) -> MetaOapg.properties.resource: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["action", "resource", "resource_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        resource: typing.Union[MetaOapg.properties.resource, dict, frozendict.frozendict, None, ],
        resource_type: typing.Union[MetaOapg.properties.resource_type, str, ],
        action: typing.Union[MetaOapg.properties.action, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VideoContext':
        return super().__new__(
            cls,
            *args,
            resource=resource,
            resource_type=resource_type,
            action=action,
            _configuration=_configuration,
            **kwargs,
        )

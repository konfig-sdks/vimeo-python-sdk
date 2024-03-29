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


class OnDemandPagePreorder(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "cancel_time",
            "publish_time",
            "active",
            "time",
        }
        
        class properties:
            active = schemas.BoolSchema
            cancel_time = schemas.StrSchema
            publish_time = schemas.StrSchema
            time = schemas.StrSchema
            __annotations__ = {
                "active": active,
                "cancel_time": cancel_time,
                "publish_time": publish_time,
                "time": time,
            }
    
    cancel_time: MetaOapg.properties.cancel_time
    publish_time: MetaOapg.properties.publish_time
    active: MetaOapg.properties.active
    time: MetaOapg.properties.time
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cancel_time"]) -> MetaOapg.properties.cancel_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publish_time"]) -> MetaOapg.properties.publish_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time"]) -> MetaOapg.properties.time: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["active", "cancel_time", "publish_time", "time", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cancel_time"]) -> MetaOapg.properties.cancel_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publish_time"]) -> MetaOapg.properties.publish_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time"]) -> MetaOapg.properties.time: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["active", "cancel_time", "publish_time", "time", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cancel_time: typing.Union[MetaOapg.properties.cancel_time, str, ],
        publish_time: typing.Union[MetaOapg.properties.publish_time, str, ],
        active: typing.Union[MetaOapg.properties.active, bool, ],
        time: typing.Union[MetaOapg.properties.time, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OnDemandPagePreorder':
        return super().__new__(
            cls,
            *args,
            cancel_time=cancel_time,
            publish_time=publish_time,
            active=active,
            time=time,
            _configuration=_configuration,
            **kwargs,
        )

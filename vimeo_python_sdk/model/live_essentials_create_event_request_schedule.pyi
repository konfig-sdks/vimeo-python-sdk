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


class LiveEssentialsCreateEventRequestSchedule(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Information about the time or times that the event is expected to be live.
    """


    class MetaOapg:
        
        class properties:
            daily_time = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SINGLE(cls):
                    return cls("single")
                
                @schemas.classproperty
                def WEEKLY(cls):
                    return cls("weekly")
        
            @staticmethod
            def weekdays() -> typing.Type['LiveEssentialsCreateEventRequestScheduleWeekdays']:
                return LiveEssentialsCreateEventRequestScheduleWeekdays
            __annotations__ = {
                "daily_time": daily_time,
                "type": type,
                "weekdays": weekdays,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["daily_time"]) -> MetaOapg.properties.daily_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weekdays"]) -> 'LiveEssentialsCreateEventRequestScheduleWeekdays': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["daily_time", "type", "weekdays", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["daily_time"]) -> typing.Union[MetaOapg.properties.daily_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weekdays"]) -> typing.Union['LiveEssentialsCreateEventRequestScheduleWeekdays', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["daily_time", "type", "weekdays", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        daily_time: typing.Union[MetaOapg.properties.daily_time, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        weekdays: typing.Union['LiveEssentialsCreateEventRequestScheduleWeekdays', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LiveEssentialsCreateEventRequestSchedule':
        return super().__new__(
            cls,
            *args,
            daily_time=daily_time,
            type=type,
            weekdays=weekdays,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.live_essentials_create_event_request_schedule_weekdays import LiveEssentialsCreateEventRequestScheduleWeekdays

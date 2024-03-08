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


class UpdateWebinarRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            description = schemas.StrSchema
        
            @staticmethod
            def email_settings() -> typing.Type['UpdateWebinarRequestEmailSettings']:
                return UpdateWebinarRequestEmailSettings
            password = schemas.StrSchema
        
            @staticmethod
            def privacy() -> typing.Type['UpdateWebinarRequestPrivacy']:
                return UpdateWebinarRequestPrivacy
        
            @staticmethod
            def schedule() -> typing.Type['UpdateWebinarRequestSchedule']:
                return UpdateWebinarRequestSchedule
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ENDED(cls):
                    return cls("ended")
                
                @schemas.classproperty
                def STARTED(cls):
                    return cls("started")
            time_zone = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "description": description,
                "email_settings": email_settings,
                "password": password,
                "privacy": privacy,
                "schedule": schedule,
                "status": status,
                "time_zone": time_zone,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_settings"]) -> 'UpdateWebinarRequestEmailSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privacy"]) -> 'UpdateWebinarRequestPrivacy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedule"]) -> 'UpdateWebinarRequestSchedule': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_zone"]) -> MetaOapg.properties.time_zone: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "description", "email_settings", "password", "privacy", "schedule", "status", "time_zone", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_settings"]) -> typing.Union['UpdateWebinarRequestEmailSettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privacy"]) -> typing.Union['UpdateWebinarRequestPrivacy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedule"]) -> typing.Union['UpdateWebinarRequestSchedule', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_zone"]) -> typing.Union[MetaOapg.properties.time_zone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "description", "email_settings", "password", "privacy", "schedule", "status", "time_zone", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        email_settings: typing.Union['UpdateWebinarRequestEmailSettings', schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        privacy: typing.Union['UpdateWebinarRequestPrivacy', schemas.Unset] = schemas.unset,
        schedule: typing.Union['UpdateWebinarRequestSchedule', schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        time_zone: typing.Union[MetaOapg.properties.time_zone, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateWebinarRequest':
        return super().__new__(
            cls,
            *args,
            title=title,
            description=description,
            email_settings=email_settings,
            password=password,
            privacy=privacy,
            schedule=schedule,
            status=status,
            time_zone=time_zone,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.update_webinar_request_email_settings import UpdateWebinarRequestEmailSettings
from vimeo_python_sdk.model.update_webinar_request_privacy import UpdateWebinarRequestPrivacy
from vimeo_python_sdk.model.update_webinar_request_schedule import UpdateWebinarRequestSchedule

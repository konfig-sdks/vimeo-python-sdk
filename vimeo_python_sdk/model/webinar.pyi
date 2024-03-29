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


class Webinar(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "email_quota",
            "modified_on",
            "created_time",
            "metadata",
            "registration_form",
            "email_provider_list",
            "completed_on",
            "edit",
            "description",
            "has_polls",
            "privacy",
            "email_settings",
            "next_occurrence_time",
            "time_zone",
            "title",
            "uri",
            "schedule",
            "password",
            "registration_data",
            "user",
            "events",
            "status",
        }
        
        class properties:
            
            
            class title(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'title':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'description':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            completed_on = schemas.StrSchema
            created_time = schemas.StrSchema
        
            @staticmethod
            def edit() -> typing.Type['WebinarEdit']:
                return WebinarEdit
        
            @staticmethod
            def email_provider_list() -> typing.Type['WebinarEmailProviderList']:
                return WebinarEmailProviderList
        
            @staticmethod
            def email_quota() -> typing.Type['WebinarEmailQuota']:
                return WebinarEmailQuota
        
            @staticmethod
            def email_settings() -> typing.Type['WebinarEmailSettings']:
                return WebinarEmailSettings
        
            @staticmethod
            def events() -> typing.Type['WebinarEvents']:
                return WebinarEvents
            has_polls = schemas.BoolSchema
        
            @staticmethod
            def metadata() -> typing.Type['WebinarMetadata']:
                return WebinarMetadata
            modified_on = schemas.StrSchema
            
            
            class next_occurrence_time(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'next_occurrence_time':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class password(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'password':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def privacy() -> typing.Type['WebinarPrivacy']:
                return WebinarPrivacy
        
            @staticmethod
            def registration_data() -> typing.Type['WebinarRegistrationData']:
                return WebinarRegistrationData
        
            @staticmethod
            def registration_form() -> typing.Type['EmailCaptureForm']:
                return EmailCaptureForm
        
            @staticmethod
            def schedule() -> typing.Type['WebinarSchedule']:
                return WebinarSchedule
            
            
            class status(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ended": "ENDED",
                        "started": "STARTED",
                    }
                
                @schemas.classproperty
                def ENDED(cls):
                    return cls("ended")
                
                @schemas.classproperty
                def STARTED(cls):
                    return cls("started")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'status':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            time_zone = schemas.StrSchema
            uri = schemas.StrSchema
        
            @staticmethod
            def user() -> typing.Type['User']:
                return User
            __annotations__ = {
                "title": title,
                "description": description,
                "completed_on": completed_on,
                "created_time": created_time,
                "edit": edit,
                "email_provider_list": email_provider_list,
                "email_quota": email_quota,
                "email_settings": email_settings,
                "events": events,
                "has_polls": has_polls,
                "metadata": metadata,
                "modified_on": modified_on,
                "next_occurrence_time": next_occurrence_time,
                "password": password,
                "privacy": privacy,
                "registration_data": registration_data,
                "registration_form": registration_form,
                "schedule": schedule,
                "status": status,
                "time_zone": time_zone,
                "uri": uri,
                "user": user,
            }
    
    email_quota: 'WebinarEmailQuota'
    modified_on: MetaOapg.properties.modified_on
    created_time: MetaOapg.properties.created_time
    metadata: 'WebinarMetadata'
    registration_form: 'EmailCaptureForm'
    email_provider_list: 'WebinarEmailProviderList'
    completed_on: MetaOapg.properties.completed_on
    edit: 'WebinarEdit'
    description: MetaOapg.properties.description
    has_polls: MetaOapg.properties.has_polls
    privacy: 'WebinarPrivacy'
    email_settings: 'WebinarEmailSettings'
    next_occurrence_time: MetaOapg.properties.next_occurrence_time
    time_zone: MetaOapg.properties.time_zone
    title: MetaOapg.properties.title
    uri: MetaOapg.properties.uri
    schedule: 'WebinarSchedule'
    password: MetaOapg.properties.password
    registration_data: 'WebinarRegistrationData'
    user: 'User'
    events: 'WebinarEvents'
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["completed_on"]) -> MetaOapg.properties.completed_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_time"]) -> MetaOapg.properties.created_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edit"]) -> 'WebinarEdit': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_provider_list"]) -> 'WebinarEmailProviderList': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_quota"]) -> 'WebinarEmailQuota': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_settings"]) -> 'WebinarEmailSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> 'WebinarEvents': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_polls"]) -> MetaOapg.properties.has_polls: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'WebinarMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modified_on"]) -> MetaOapg.properties.modified_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_occurrence_time"]) -> MetaOapg.properties.next_occurrence_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privacy"]) -> 'WebinarPrivacy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registration_data"]) -> 'WebinarRegistrationData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registration_form"]) -> 'EmailCaptureForm': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedule"]) -> 'WebinarSchedule': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_zone"]) -> MetaOapg.properties.time_zone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'User': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "description", "completed_on", "created_time", "edit", "email_provider_list", "email_quota", "email_settings", "events", "has_polls", "metadata", "modified_on", "next_occurrence_time", "password", "privacy", "registration_data", "registration_form", "schedule", "status", "time_zone", "uri", "user", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["completed_on"]) -> MetaOapg.properties.completed_on: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_time"]) -> MetaOapg.properties.created_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edit"]) -> 'WebinarEdit': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_provider_list"]) -> 'WebinarEmailProviderList': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_quota"]) -> 'WebinarEmailQuota': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_settings"]) -> 'WebinarEmailSettings': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> 'WebinarEvents': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_polls"]) -> MetaOapg.properties.has_polls: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> 'WebinarMetadata': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modified_on"]) -> MetaOapg.properties.modified_on: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_occurrence_time"]) -> MetaOapg.properties.next_occurrence_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privacy"]) -> 'WebinarPrivacy': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registration_data"]) -> 'WebinarRegistrationData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registration_form"]) -> 'EmailCaptureForm': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedule"]) -> 'WebinarSchedule': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_zone"]) -> MetaOapg.properties.time_zone: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> 'User': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "description", "completed_on", "created_time", "edit", "email_provider_list", "email_quota", "email_settings", "events", "has_polls", "metadata", "modified_on", "next_occurrence_time", "password", "privacy", "registration_data", "registration_form", "schedule", "status", "time_zone", "uri", "user", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        email_quota: 'WebinarEmailQuota',
        modified_on: typing.Union[MetaOapg.properties.modified_on, str, ],
        created_time: typing.Union[MetaOapg.properties.created_time, str, ],
        metadata: 'WebinarMetadata',
        registration_form: 'EmailCaptureForm',
        email_provider_list: 'WebinarEmailProviderList',
        completed_on: typing.Union[MetaOapg.properties.completed_on, str, ],
        edit: 'WebinarEdit',
        description: typing.Union[MetaOapg.properties.description, None, str, ],
        has_polls: typing.Union[MetaOapg.properties.has_polls, bool, ],
        privacy: 'WebinarPrivacy',
        email_settings: 'WebinarEmailSettings',
        next_occurrence_time: typing.Union[MetaOapg.properties.next_occurrence_time, None, str, ],
        time_zone: typing.Union[MetaOapg.properties.time_zone, str, ],
        title: typing.Union[MetaOapg.properties.title, None, str, ],
        uri: typing.Union[MetaOapg.properties.uri, str, ],
        schedule: 'WebinarSchedule',
        password: typing.Union[MetaOapg.properties.password, None, str, ],
        registration_data: 'WebinarRegistrationData',
        user: 'User',
        events: 'WebinarEvents',
        status: typing.Union[MetaOapg.properties.status, None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Webinar':
        return super().__new__(
            cls,
            *args,
            email_quota=email_quota,
            modified_on=modified_on,
            created_time=created_time,
            metadata=metadata,
            registration_form=registration_form,
            email_provider_list=email_provider_list,
            completed_on=completed_on,
            edit=edit,
            description=description,
            has_polls=has_polls,
            privacy=privacy,
            email_settings=email_settings,
            next_occurrence_time=next_occurrence_time,
            time_zone=time_zone,
            title=title,
            uri=uri,
            schedule=schedule,
            password=password,
            registration_data=registration_data,
            user=user,
            events=events,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.email_capture_form import EmailCaptureForm
from vimeo_python_sdk.model.user import User
from vimeo_python_sdk.model.webinar_edit import WebinarEdit
from vimeo_python_sdk.model.webinar_email_provider_list import WebinarEmailProviderList
from vimeo_python_sdk.model.webinar_email_quota import WebinarEmailQuota
from vimeo_python_sdk.model.webinar_email_settings import WebinarEmailSettings
from vimeo_python_sdk.model.webinar_events import WebinarEvents
from vimeo_python_sdk.model.webinar_metadata import WebinarMetadata
from vimeo_python_sdk.model.webinar_privacy import WebinarPrivacy
from vimeo_python_sdk.model.webinar_registration_data import WebinarRegistrationData
from vimeo_python_sdk.model.webinar_schedule import WebinarSchedule

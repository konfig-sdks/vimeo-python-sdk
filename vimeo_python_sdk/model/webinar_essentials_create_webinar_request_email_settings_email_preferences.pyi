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


class WebinarEssentialsCreateWebinarRequestEmailSettingsEmailPreferences(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The preferences for emails that are sent about the webinar. _This field is deprecated._
    """


    class MetaOapg:
        
        class properties:
            email_event_reminder_15_min = schemas.BoolSchema
            email_event_reminder_1_hrs = schemas.BoolSchema
            email_event_reminder_24_hrs = schemas.BoolSchema
            email_post_event_no_show_thank_you = schemas.BoolSchema
            email_post_event_thank_you = schemas.BoolSchema
            email_registration_confirmation = schemas.BoolSchema
            __annotations__ = {
                "email_event_reminder_15_min": email_event_reminder_15_min,
                "email_event_reminder_1_hrs": email_event_reminder_1_hrs,
                "email_event_reminder_24_hrs": email_event_reminder_24_hrs,
                "email_post_event_no_show_thank_you": email_post_event_no_show_thank_you,
                "email_post_event_thank_you": email_post_event_thank_you,
                "email_registration_confirmation": email_registration_confirmation,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_event_reminder_15_min"]) -> MetaOapg.properties.email_event_reminder_15_min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_event_reminder_1_hrs"]) -> MetaOapg.properties.email_event_reminder_1_hrs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_event_reminder_24_hrs"]) -> MetaOapg.properties.email_event_reminder_24_hrs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_post_event_no_show_thank_you"]) -> MetaOapg.properties.email_post_event_no_show_thank_you: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_post_event_thank_you"]) -> MetaOapg.properties.email_post_event_thank_you: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_registration_confirmation"]) -> MetaOapg.properties.email_registration_confirmation: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["email_event_reminder_15_min", "email_event_reminder_1_hrs", "email_event_reminder_24_hrs", "email_post_event_no_show_thank_you", "email_post_event_thank_you", "email_registration_confirmation", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_event_reminder_15_min"]) -> typing.Union[MetaOapg.properties.email_event_reminder_15_min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_event_reminder_1_hrs"]) -> typing.Union[MetaOapg.properties.email_event_reminder_1_hrs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_event_reminder_24_hrs"]) -> typing.Union[MetaOapg.properties.email_event_reminder_24_hrs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_post_event_no_show_thank_you"]) -> typing.Union[MetaOapg.properties.email_post_event_no_show_thank_you, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_post_event_thank_you"]) -> typing.Union[MetaOapg.properties.email_post_event_thank_you, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_registration_confirmation"]) -> typing.Union[MetaOapg.properties.email_registration_confirmation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email_event_reminder_15_min", "email_event_reminder_1_hrs", "email_event_reminder_24_hrs", "email_post_event_no_show_thank_you", "email_post_event_thank_you", "email_registration_confirmation", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        email_event_reminder_15_min: typing.Union[MetaOapg.properties.email_event_reminder_15_min, bool, schemas.Unset] = schemas.unset,
        email_event_reminder_1_hrs: typing.Union[MetaOapg.properties.email_event_reminder_1_hrs, bool, schemas.Unset] = schemas.unset,
        email_event_reminder_24_hrs: typing.Union[MetaOapg.properties.email_event_reminder_24_hrs, bool, schemas.Unset] = schemas.unset,
        email_post_event_no_show_thank_you: typing.Union[MetaOapg.properties.email_post_event_no_show_thank_you, bool, schemas.Unset] = schemas.unset,
        email_post_event_thank_you: typing.Union[MetaOapg.properties.email_post_event_thank_you, bool, schemas.Unset] = schemas.unset,
        email_registration_confirmation: typing.Union[MetaOapg.properties.email_registration_confirmation, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebinarEssentialsCreateWebinarRequestEmailSettingsEmailPreferences':
        return super().__new__(
            cls,
            *args,
            email_event_reminder_15_min=email_event_reminder_15_min,
            email_event_reminder_1_hrs=email_event_reminder_1_hrs,
            email_event_reminder_24_hrs=email_event_reminder_24_hrs,
            email_post_event_no_show_thank_you=email_post_event_no_show_thank_you,
            email_post_event_thank_you=email_post_event_thank_you,
            email_registration_confirmation=email_registration_confirmation,
            _configuration=_configuration,
            **kwargs,
        )

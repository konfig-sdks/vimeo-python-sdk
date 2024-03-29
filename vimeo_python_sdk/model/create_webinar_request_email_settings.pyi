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


class CreateWebinarRequestEmailSettings(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The settings for emails that are sent about the webinar. _This field is deprecated._
    """


    class MetaOapg:
        
        class properties:
            accent_color = schemas.StrSchema
            custom_link = schemas.StrSchema
        
            @staticmethod
            def email_preferences() -> typing.Type['CreateWebinarRequestEmailSettingsEmailPreferences']:
                return CreateWebinarRequestEmailSettingsEmailPreferences
            _from = schemas.StrSchema
            logo_uri = schemas.StrSchema
            reply_email = schemas.StrSchema
            sender_address = schemas.StrSchema
            sender_policy_url = schemas.StrSchema
            use_custom_link = schemas.BoolSchema
            use_reply_email = schemas.BoolSchema
            use_sender_address = schemas.BoolSchema
            use_sender_policy_url = schemas.BoolSchema
            __annotations__ = {
                "accent_color": accent_color,
                "custom_link": custom_link,
                "email_preferences": email_preferences,
                "from": _from,
                "logo_uri": logo_uri,
                "reply_email": reply_email,
                "sender_address": sender_address,
                "sender_policy_url": sender_policy_url,
                "use_custom_link": use_custom_link,
                "use_reply_email": use_reply_email,
                "use_sender_address": use_sender_address,
                "use_sender_policy_url": use_sender_policy_url,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accent_color"]) -> MetaOapg.properties.accent_color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_link"]) -> MetaOapg.properties.custom_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_preferences"]) -> 'CreateWebinarRequestEmailSettingsEmailPreferences': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo_uri"]) -> MetaOapg.properties.logo_uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reply_email"]) -> MetaOapg.properties.reply_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sender_address"]) -> MetaOapg.properties.sender_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sender_policy_url"]) -> MetaOapg.properties.sender_policy_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["use_custom_link"]) -> MetaOapg.properties.use_custom_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["use_reply_email"]) -> MetaOapg.properties.use_reply_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["use_sender_address"]) -> MetaOapg.properties.use_sender_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["use_sender_policy_url"]) -> MetaOapg.properties.use_sender_policy_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accent_color", "custom_link", "email_preferences", "from", "logo_uri", "reply_email", "sender_address", "sender_policy_url", "use_custom_link", "use_reply_email", "use_sender_address", "use_sender_policy_url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accent_color"]) -> typing.Union[MetaOapg.properties.accent_color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_link"]) -> typing.Union[MetaOapg.properties.custom_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_preferences"]) -> typing.Union['CreateWebinarRequestEmailSettingsEmailPreferences', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from"]) -> typing.Union[MetaOapg.properties._from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo_uri"]) -> typing.Union[MetaOapg.properties.logo_uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reply_email"]) -> typing.Union[MetaOapg.properties.reply_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sender_address"]) -> typing.Union[MetaOapg.properties.sender_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sender_policy_url"]) -> typing.Union[MetaOapg.properties.sender_policy_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["use_custom_link"]) -> typing.Union[MetaOapg.properties.use_custom_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["use_reply_email"]) -> typing.Union[MetaOapg.properties.use_reply_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["use_sender_address"]) -> typing.Union[MetaOapg.properties.use_sender_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["use_sender_policy_url"]) -> typing.Union[MetaOapg.properties.use_sender_policy_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accent_color", "custom_link", "email_preferences", "from", "logo_uri", "reply_email", "sender_address", "sender_policy_url", "use_custom_link", "use_reply_email", "use_sender_address", "use_sender_policy_url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        accent_color: typing.Union[MetaOapg.properties.accent_color, str, schemas.Unset] = schemas.unset,
        custom_link: typing.Union[MetaOapg.properties.custom_link, str, schemas.Unset] = schemas.unset,
        email_preferences: typing.Union['CreateWebinarRequestEmailSettingsEmailPreferences', schemas.Unset] = schemas.unset,
        logo_uri: typing.Union[MetaOapg.properties.logo_uri, str, schemas.Unset] = schemas.unset,
        reply_email: typing.Union[MetaOapg.properties.reply_email, str, schemas.Unset] = schemas.unset,
        sender_address: typing.Union[MetaOapg.properties.sender_address, str, schemas.Unset] = schemas.unset,
        sender_policy_url: typing.Union[MetaOapg.properties.sender_policy_url, str, schemas.Unset] = schemas.unset,
        use_custom_link: typing.Union[MetaOapg.properties.use_custom_link, bool, schemas.Unset] = schemas.unset,
        use_reply_email: typing.Union[MetaOapg.properties.use_reply_email, bool, schemas.Unset] = schemas.unset,
        use_sender_address: typing.Union[MetaOapg.properties.use_sender_address, bool, schemas.Unset] = schemas.unset,
        use_sender_policy_url: typing.Union[MetaOapg.properties.use_sender_policy_url, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateWebinarRequestEmailSettings':
        return super().__new__(
            cls,
            *args,
            accent_color=accent_color,
            custom_link=custom_link,
            email_preferences=email_preferences,
            logo_uri=logo_uri,
            reply_email=reply_email,
            sender_address=sender_address,
            sender_policy_url=sender_policy_url,
            use_custom_link=use_custom_link,
            use_reply_email=use_reply_email,
            use_sender_address=use_sender_address,
            use_sender_policy_url=use_sender_policy_url,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.create_webinar_request_email_settings_email_preferences import CreateWebinarRequestEmailSettingsEmailPreferences

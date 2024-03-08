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


class EmailCaptureFormCustomFieldsItemConnectedFieldsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "form_field_id",
            "email_service_provider_field_id",
            "provider_id",
        }
        
        class properties:
            email_service_provider_field_id = schemas.StrSchema
            form_field_id = schemas.NumberSchema
            
            
            class provider_id(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "1": "POSITIVE_1",
                        "2": "POSITIVE_2",
                        "3": "POSITIVE_3",
                        "4": "POSITIVE_4",
                        "5": "POSITIVE_5",
                        "6": "POSITIVE_6",
                        "7": "POSITIVE_7",
                    }
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls("1")
                
                @schemas.classproperty
                def POSITIVE_2(cls):
                    return cls("2")
                
                @schemas.classproperty
                def POSITIVE_3(cls):
                    return cls("3")
                
                @schemas.classproperty
                def POSITIVE_4(cls):
                    return cls("4")
                
                @schemas.classproperty
                def POSITIVE_5(cls):
                    return cls("5")
                
                @schemas.classproperty
                def POSITIVE_6(cls):
                    return cls("6")
                
                @schemas.classproperty
                def POSITIVE_7(cls):
                    return cls("7")
            __annotations__ = {
                "email_service_provider_field_id": email_service_provider_field_id,
                "form_field_id": form_field_id,
                "provider_id": provider_id,
            }
    
    form_field_id: MetaOapg.properties.form_field_id
    email_service_provider_field_id: MetaOapg.properties.email_service_provider_field_id
    provider_id: MetaOapg.properties.provider_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_service_provider_field_id"]) -> MetaOapg.properties.email_service_provider_field_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["form_field_id"]) -> MetaOapg.properties.form_field_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider_id"]) -> MetaOapg.properties.provider_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["email_service_provider_field_id", "form_field_id", "provider_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_service_provider_field_id"]) -> MetaOapg.properties.email_service_provider_field_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["form_field_id"]) -> MetaOapg.properties.form_field_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider_id"]) -> MetaOapg.properties.provider_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email_service_provider_field_id", "form_field_id", "provider_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        form_field_id: typing.Union[MetaOapg.properties.form_field_id, decimal.Decimal, int, float, ],
        email_service_provider_field_id: typing.Union[MetaOapg.properties.email_service_provider_field_id, str, ],
        provider_id: typing.Union[MetaOapg.properties.provider_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmailCaptureFormCustomFieldsItemConnectedFieldsItem':
        return super().__new__(
            cls,
            *args,
            form_field_id=form_field_id,
            email_service_provider_field_id=email_service_provider_field_id,
            provider_id=provider_id,
            _configuration=_configuration,
            **kwargs,
        )

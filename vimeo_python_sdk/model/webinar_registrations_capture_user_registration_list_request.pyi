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


class WebinarRegistrationsCaptureUserRegistrationListRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def registrants() -> typing.Type['WebinarRegistrationsCaptureUserRegistrationListRequestRegistrants']:
                return WebinarRegistrationsCaptureUserRegistrationListRequestRegistrants
            __annotations__ = {
                "registrants": registrants,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registrants"]) -> 'WebinarRegistrationsCaptureUserRegistrationListRequestRegistrants': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["registrants", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registrants"]) -> typing.Union['WebinarRegistrationsCaptureUserRegistrationListRequestRegistrants', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["registrants", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        registrants: typing.Union['WebinarRegistrationsCaptureUserRegistrationListRequestRegistrants', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebinarRegistrationsCaptureUserRegistrationListRequest':
        return super().__new__(
            cls,
            *args,
            registrants=registrants,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.webinar_registrations_capture_user_registration_list_request_registrants import WebinarRegistrationsCaptureUserRegistrationListRequestRegistrants

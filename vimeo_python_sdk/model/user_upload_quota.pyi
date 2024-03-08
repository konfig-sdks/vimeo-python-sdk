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


class UserUploadQuota(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The upload quota. This information appears only when the authenticated user has upload access and is looking at their own user record.
    """


    class MetaOapg:
        required = {
            "periodic",
            "lifetime",
            "space",
        }
        
        class properties:
        
            @staticmethod
            def lifetime() -> typing.Type['UserUploadQuotaLifetime']:
                return UserUploadQuotaLifetime
        
            @staticmethod
            def periodic() -> typing.Type['UserUploadQuotaPeriodic']:
                return UserUploadQuotaPeriodic
        
            @staticmethod
            def space() -> typing.Type['UserUploadQuotaSpace']:
                return UserUploadQuotaSpace
            __annotations__ = {
                "lifetime": lifetime,
                "periodic": periodic,
                "space": space,
            }
    
    periodic: 'UserUploadQuotaPeriodic'
    lifetime: 'UserUploadQuotaLifetime'
    space: 'UserUploadQuotaSpace'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lifetime"]) -> 'UserUploadQuotaLifetime': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["periodic"]) -> 'UserUploadQuotaPeriodic': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["space"]) -> 'UserUploadQuotaSpace': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["lifetime", "periodic", "space", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lifetime"]) -> 'UserUploadQuotaLifetime': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["periodic"]) -> 'UserUploadQuotaPeriodic': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["space"]) -> 'UserUploadQuotaSpace': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["lifetime", "periodic", "space", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        periodic: 'UserUploadQuotaPeriodic',
        lifetime: 'UserUploadQuotaLifetime',
        space: 'UserUploadQuotaSpace',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserUploadQuota':
        return super().__new__(
            cls,
            *args,
            periodic=periodic,
            lifetime=lifetime,
            space=space,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.user_upload_quota_lifetime import UserUploadQuotaLifetime
from vimeo_python_sdk.model.user_upload_quota_periodic import UserUploadQuotaPeriodic
from vimeo_python_sdk.model.user_upload_quota_space import UserUploadQuotaSpace

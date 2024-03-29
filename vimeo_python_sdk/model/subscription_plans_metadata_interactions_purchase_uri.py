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


class SubscriptionPlansMetadataInteractionsPurchaseUri(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The redirect URIs associated with the plan.
    """


    class MetaOapg:
        required = {
            "annual",
            "monthly",
            "free_trial",
        }
        
        class properties:
            
            
            class annual(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'annual':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class free_trial(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'free_trial':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class monthly(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'monthly':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "annual": annual,
                "free_trial": free_trial,
                "monthly": monthly,
            }
    
    annual: MetaOapg.properties.annual
    monthly: MetaOapg.properties.monthly
    free_trial: MetaOapg.properties.free_trial
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annual"]) -> MetaOapg.properties.annual: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["free_trial"]) -> MetaOapg.properties.free_trial: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthly"]) -> MetaOapg.properties.monthly: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["annual", "free_trial", "monthly", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annual"]) -> MetaOapg.properties.annual: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["free_trial"]) -> MetaOapg.properties.free_trial: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthly"]) -> MetaOapg.properties.monthly: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["annual", "free_trial", "monthly", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        annual: typing.Union[MetaOapg.properties.annual, None, str, ],
        monthly: typing.Union[MetaOapg.properties.monthly, None, str, ],
        free_trial: typing.Union[MetaOapg.properties.free_trial, None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SubscriptionPlansMetadataInteractionsPurchaseUri':
        return super().__new__(
            cls,
            *args,
            annual=annual,
            monthly=monthly,
            free_trial=free_trial,
            _configuration=_configuration,
            **kwargs,
        )

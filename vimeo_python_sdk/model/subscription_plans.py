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


class SubscriptionPlans(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "metadata",
            "tier",
            "price",
            "name",
            "discount",
            "currency",
            "id",
            "uri",
            "promotion",
        }
        
        class properties:
        
            @staticmethod
            def currency() -> typing.Type['SubscriptionPlansCurrency']:
                return SubscriptionPlansCurrency
        
            @staticmethod
            def discount() -> typing.Type['SubscriptionPlansDiscount']:
                return SubscriptionPlansDiscount
            id = schemas.NumberSchema
        
            @staticmethod
            def metadata() -> typing.Type['SubscriptionPlansMetadata']:
                return SubscriptionPlansMetadata
            name = schemas.StrSchema
        
            @staticmethod
            def price() -> typing.Type['SubscriptionPlansPrice']:
                return SubscriptionPlansPrice
        
            @staticmethod
            def promotion() -> typing.Type['SubscriptionPlansPromotion']:
                return SubscriptionPlansPromotion
            
            
            class tier(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "advanced": "ADVANCED",
                        "basic": "BASIC",
                        "business": "BUSINESS",
                        "enterprise": "ENTERPRISE",
                        "free": "FREE",
                        "livePremium": "LIVE_PREMIUM",
                        "ott": "OTT",
                        "plus": "PLUS",
                        "pro": "PRO",
                        "proUnlimited": "PRO_UNLIMITED",
                        "standard": "STANDARD",
                        "starter": "STARTER",
                    }
                
                @schemas.classproperty
                def ADVANCED(cls):
                    return cls("advanced")
                
                @schemas.classproperty
                def BASIC(cls):
                    return cls("basic")
                
                @schemas.classproperty
                def BUSINESS(cls):
                    return cls("business")
                
                @schemas.classproperty
                def ENTERPRISE(cls):
                    return cls("enterprise")
                
                @schemas.classproperty
                def FREE(cls):
                    return cls("free")
                
                @schemas.classproperty
                def LIVE_PREMIUM(cls):
                    return cls("livePremium")
                
                @schemas.classproperty
                def OTT(cls):
                    return cls("ott")
                
                @schemas.classproperty
                def PLUS(cls):
                    return cls("plus")
                
                @schemas.classproperty
                def PRO(cls):
                    return cls("pro")
                
                @schemas.classproperty
                def PRO_UNLIMITED(cls):
                    return cls("proUnlimited")
                
                @schemas.classproperty
                def STANDARD(cls):
                    return cls("standard")
                
                @schemas.classproperty
                def STARTER(cls):
                    return cls("starter")
            uri = schemas.StrSchema
            __annotations__ = {
                "currency": currency,
                "discount": discount,
                "id": id,
                "metadata": metadata,
                "name": name,
                "price": price,
                "promotion": promotion,
                "tier": tier,
                "uri": uri,
            }
    
    metadata: 'SubscriptionPlansMetadata'
    tier: MetaOapg.properties.tier
    price: 'SubscriptionPlansPrice'
    name: MetaOapg.properties.name
    discount: 'SubscriptionPlansDiscount'
    currency: 'SubscriptionPlansCurrency'
    id: MetaOapg.properties.id
    uri: MetaOapg.properties.uri
    promotion: 'SubscriptionPlansPromotion'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> 'SubscriptionPlansCurrency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discount"]) -> 'SubscriptionPlansDiscount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'SubscriptionPlansMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> 'SubscriptionPlansPrice': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["promotion"]) -> 'SubscriptionPlansPromotion': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tier"]) -> MetaOapg.properties.tier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["currency", "discount", "id", "metadata", "name", "price", "promotion", "tier", "uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> 'SubscriptionPlansCurrency': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discount"]) -> 'SubscriptionPlansDiscount': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> 'SubscriptionPlansMetadata': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> 'SubscriptionPlansPrice': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["promotion"]) -> 'SubscriptionPlansPromotion': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tier"]) -> MetaOapg.properties.tier: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["currency", "discount", "id", "metadata", "name", "price", "promotion", "tier", "uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        metadata: 'SubscriptionPlansMetadata',
        tier: typing.Union[MetaOapg.properties.tier, str, ],
        price: 'SubscriptionPlansPrice',
        name: typing.Union[MetaOapg.properties.name, str, ],
        discount: 'SubscriptionPlansDiscount',
        currency: 'SubscriptionPlansCurrency',
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, ],
        uri: typing.Union[MetaOapg.properties.uri, str, ],
        promotion: 'SubscriptionPlansPromotion',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SubscriptionPlans':
        return super().__new__(
            cls,
            *args,
            metadata=metadata,
            tier=tier,
            price=price,
            name=name,
            discount=discount,
            currency=currency,
            id=id,
            uri=uri,
            promotion=promotion,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.subscription_plans_currency import SubscriptionPlansCurrency
from vimeo_python_sdk.model.subscription_plans_discount import SubscriptionPlansDiscount
from vimeo_python_sdk.model.subscription_plans_metadata import SubscriptionPlansMetadata
from vimeo_python_sdk.model.subscription_plans_price import SubscriptionPlansPrice
from vimeo_python_sdk.model.subscription_plans_promotion import SubscriptionPlansPromotion

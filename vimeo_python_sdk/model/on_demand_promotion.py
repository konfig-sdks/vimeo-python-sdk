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


class OnDemandPromotion(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "access_type",
            "download",
            "metadata",
            "total",
            "product_type",
            "percent_off",
            "label",
            "discount_type",
            "type",
            "stream_period",
            "uri",
        }
        
        class properties:
            
            
            class access_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "default": "DEFAULT",
                        "vip": "VIP",
                    }
                
                @schemas.classproperty
                def DEFAULT(cls):
                    return cls("default")
                
                @schemas.classproperty
                def VIP(cls):
                    return cls("vip")
            
            
            class discount_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "dollars": "DOLLARS",
                        "free": "FREE",
                        "percent": "PERCENT",
                    }
                
                @schemas.classproperty
                def DOLLARS(cls):
                    return cls("dollars")
                
                @schemas.classproperty
                def FREE(cls):
                    return cls("free")
                
                @schemas.classproperty
                def PERCENT(cls):
                    return cls("percent")
            download = schemas.BoolSchema
            
            
            class label(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'label':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def metadata() -> typing.Type['OnDemandPromotionMetadata']:
                return OnDemandPromotionMetadata
            percent_off = schemas.NumberSchema
            
            
            class product_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "any": "ANY",
                        "buy": "BUY",
                        "buy_episode": "BUY_EPISODE",
                        "rent": "RENT",
                        "rent_episode": "RENT_EPISODE",
                        "subscribe": "SUBSCRIBE",
                    }
                
                @schemas.classproperty
                def ANY(cls):
                    return cls("any")
                
                @schemas.classproperty
                def BUY(cls):
                    return cls("buy")
                
                @schemas.classproperty
                def BUY_EPISODE(cls):
                    return cls("buy_episode")
                
                @schemas.classproperty
                def RENT(cls):
                    return cls("rent")
                
                @schemas.classproperty
                def RENT_EPISODE(cls):
                    return cls("rent_episode")
                
                @schemas.classproperty
                def SUBSCRIBE(cls):
                    return cls("subscribe")
            
            
            class stream_period(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "1_week": "_1_WEEK",
                        "1_year": "_1_YEAR",
                        "24_hour": "_24_HOUR",
                        "30_days": "_30_DAYS",
                        "3_month": "_3_MONTH",
                        "48_hour": "_48_HOUR",
                        "6_month": "_6_MONTH",
                        "72_hour": "_72_HOUR",
                    }
                
                @schemas.classproperty
                def _1_WEEK(cls):
                    return cls("1_week")
                
                @schemas.classproperty
                def _1_YEAR(cls):
                    return cls("1_year")
                
                @schemas.classproperty
                def _24_HOUR(cls):
                    return cls("24_hour")
                
                @schemas.classproperty
                def _30_DAYS(cls):
                    return cls("30_days")
                
                @schemas.classproperty
                def _3_MONTH(cls):
                    return cls("3_month")
                
                @schemas.classproperty
                def _48_HOUR(cls):
                    return cls("48_hour")
                
                @schemas.classproperty
                def _6_MONTH(cls):
                    return cls("6_month")
                
                @schemas.classproperty
                def _72_HOUR(cls):
                    return cls("72_hour")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'stream_period':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            total = schemas.NumberSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "batch": "BATCH",
                        "batch_prefix": "BATCH_PREFIX",
                        "single": "SINGLE",
                    }
                
                @schemas.classproperty
                def BATCH(cls):
                    return cls("batch")
                
                @schemas.classproperty
                def BATCH_PREFIX(cls):
                    return cls("batch_prefix")
                
                @schemas.classproperty
                def SINGLE(cls):
                    return cls("single")
            uri = schemas.StrSchema
            __annotations__ = {
                "access_type": access_type,
                "discount_type": discount_type,
                "download": download,
                "label": label,
                "metadata": metadata,
                "percent_off": percent_off,
                "product_type": product_type,
                "stream_period": stream_period,
                "total": total,
                "type": type,
                "uri": uri,
            }
    
    access_type: MetaOapg.properties.access_type
    download: MetaOapg.properties.download
    metadata: 'OnDemandPromotionMetadata'
    total: MetaOapg.properties.total
    product_type: MetaOapg.properties.product_type
    percent_off: MetaOapg.properties.percent_off
    label: MetaOapg.properties.label
    discount_type: MetaOapg.properties.discount_type
    type: MetaOapg.properties.type
    stream_period: MetaOapg.properties.stream_period
    uri: MetaOapg.properties.uri
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access_type"]) -> MetaOapg.properties.access_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discount_type"]) -> MetaOapg.properties.discount_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["download"]) -> MetaOapg.properties.download: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'OnDemandPromotionMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["percent_off"]) -> MetaOapg.properties.percent_off: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["product_type"]) -> MetaOapg.properties.product_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stream_period"]) -> MetaOapg.properties.stream_period: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["access_type", "discount_type", "download", "label", "metadata", "percent_off", "product_type", "stream_period", "total", "type", "uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access_type"]) -> MetaOapg.properties.access_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discount_type"]) -> MetaOapg.properties.discount_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["download"]) -> MetaOapg.properties.download: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> 'OnDemandPromotionMetadata': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["percent_off"]) -> MetaOapg.properties.percent_off: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["product_type"]) -> MetaOapg.properties.product_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stream_period"]) -> MetaOapg.properties.stream_period: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["access_type", "discount_type", "download", "label", "metadata", "percent_off", "product_type", "stream_period", "total", "type", "uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        access_type: typing.Union[MetaOapg.properties.access_type, str, ],
        download: typing.Union[MetaOapg.properties.download, bool, ],
        metadata: 'OnDemandPromotionMetadata',
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, float, ],
        product_type: typing.Union[MetaOapg.properties.product_type, str, ],
        percent_off: typing.Union[MetaOapg.properties.percent_off, decimal.Decimal, int, float, ],
        label: typing.Union[MetaOapg.properties.label, None, str, ],
        discount_type: typing.Union[MetaOapg.properties.discount_type, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        stream_period: typing.Union[MetaOapg.properties.stream_period, None, str, ],
        uri: typing.Union[MetaOapg.properties.uri, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OnDemandPromotion':
        return super().__new__(
            cls,
            *args,
            access_type=access_type,
            download=download,
            metadata=metadata,
            total=total,
            product_type=product_type,
            percent_off=percent_off,
            label=label,
            discount_type=discount_type,
            type=type,
            stream_period=stream_period,
            uri=uri,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.on_demand_promotion_metadata import OnDemandPromotionMetadata

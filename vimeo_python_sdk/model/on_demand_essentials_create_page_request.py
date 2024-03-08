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


class OnDemandEssentialsCreatePageRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
            "content_rating",
            "description",
            "type",
        }
        
        class properties:
            description = schemas.StrSchema
            
            
            class content_rating(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "drugs": "DRUGS",
                        "language": "LANGUAGE",
                        "nudity": "NUDITY",
                        "safe": "SAFE",
                        "unrated": "UNRATED",
                        "violence": "VIOLENCE",
                    }
                
                @schemas.classproperty
                def DRUGS(cls):
                    return cls("drugs")
                
                @schemas.classproperty
                def LANGUAGE(cls):
                    return cls("language")
                
                @schemas.classproperty
                def NUDITY(cls):
                    return cls("nudity")
                
                @schemas.classproperty
                def SAFE(cls):
                    return cls("safe")
                
                @schemas.classproperty
                def UNRATED(cls):
                    return cls("unrated")
                
                @schemas.classproperty
                def VIOLENCE(cls):
                    return cls("violence")
            name = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "film": "FILM",
                        "series": "SERIES",
                    }
                
                @schemas.classproperty
                def FILM(cls):
                    return cls("film")
                
                @schemas.classproperty
                def SERIES(cls):
                    return cls("series")
            
            
            class accepted_currencies(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "AUD": "AUD",
                        "CAD": "CAD",
                        "CHF": "CHF",
                        "DKK": "DKK",
                        "EUR": "EUR",
                        "GBP": "GBP",
                        "JPY": "JPY",
                        "KRW": "KRW",
                        "NOK": "NOK",
                        "PLN": "PLN",
                        "SEK": "SEK",
                        "USD": "USD",
                    }
                
                @schemas.classproperty
                def AUD(cls):
                    return cls("AUD")
                
                @schemas.classproperty
                def CAD(cls):
                    return cls("CAD")
                
                @schemas.classproperty
                def CHF(cls):
                    return cls("CHF")
                
                @schemas.classproperty
                def DKK(cls):
                    return cls("DKK")
                
                @schemas.classproperty
                def EUR(cls):
                    return cls("EUR")
                
                @schemas.classproperty
                def GBP(cls):
                    return cls("GBP")
                
                @schemas.classproperty
                def JPY(cls):
                    return cls("JPY")
                
                @schemas.classproperty
                def KRW(cls):
                    return cls("KRW")
                
                @schemas.classproperty
                def NOK(cls):
                    return cls("NOK")
                
                @schemas.classproperty
                def PLN(cls):
                    return cls("PLN")
                
                @schemas.classproperty
                def SEK(cls):
                    return cls("SEK")
                
                @schemas.classproperty
                def USD(cls):
                    return cls("USD")
        
            @staticmethod
            def buy() -> typing.Type['OnDemandEssentialsCreatePageRequestBuy']:
                return OnDemandEssentialsCreatePageRequestBuy
            domain_link = schemas.StrSchema
        
            @staticmethod
            def episodes() -> typing.Type['OnDemandEssentialsCreatePageRequestEpisodes']:
                return OnDemandEssentialsCreatePageRequestEpisodes
            link = schemas.StrSchema
        
            @staticmethod
            def rent() -> typing.Type['OnDemandEssentialsCreatePageRequestRent']:
                return OnDemandEssentialsCreatePageRequestRent
        
            @staticmethod
            def subscription() -> typing.Type['OnDemandEssentialsCreatePageRequestSubscription']:
                return OnDemandEssentialsCreatePageRequestSubscription
            __annotations__ = {
                "description": description,
                "content_rating": content_rating,
                "name": name,
                "type": type,
                "accepted_currencies": accepted_currencies,
                "buy": buy,
                "domain_link": domain_link,
                "episodes": episodes,
                "link": link,
                "rent": rent,
                "subscription": subscription,
            }
    
    name: MetaOapg.properties.name
    content_rating: MetaOapg.properties.content_rating
    description: MetaOapg.properties.description
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content_rating"]) -> MetaOapg.properties.content_rating: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accepted_currencies"]) -> MetaOapg.properties.accepted_currencies: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buy"]) -> 'OnDemandEssentialsCreatePageRequestBuy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domain_link"]) -> MetaOapg.properties.domain_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["episodes"]) -> 'OnDemandEssentialsCreatePageRequestEpisodes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rent"]) -> 'OnDemandEssentialsCreatePageRequestRent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscription"]) -> 'OnDemandEssentialsCreatePageRequestSubscription': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "content_rating", "name", "type", "accepted_currencies", "buy", "domain_link", "episodes", "link", "rent", "subscription", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content_rating"]) -> MetaOapg.properties.content_rating: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accepted_currencies"]) -> typing.Union[MetaOapg.properties.accepted_currencies, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buy"]) -> typing.Union['OnDemandEssentialsCreatePageRequestBuy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domain_link"]) -> typing.Union[MetaOapg.properties.domain_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["episodes"]) -> typing.Union['OnDemandEssentialsCreatePageRequestEpisodes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> typing.Union[MetaOapg.properties.link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rent"]) -> typing.Union['OnDemandEssentialsCreatePageRequestRent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscription"]) -> typing.Union['OnDemandEssentialsCreatePageRequestSubscription', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "content_rating", "name", "type", "accepted_currencies", "buy", "domain_link", "episodes", "link", "rent", "subscription", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        content_rating: typing.Union[MetaOapg.properties.content_rating, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        accepted_currencies: typing.Union[MetaOapg.properties.accepted_currencies, str, schemas.Unset] = schemas.unset,
        buy: typing.Union['OnDemandEssentialsCreatePageRequestBuy', schemas.Unset] = schemas.unset,
        domain_link: typing.Union[MetaOapg.properties.domain_link, str, schemas.Unset] = schemas.unset,
        episodes: typing.Union['OnDemandEssentialsCreatePageRequestEpisodes', schemas.Unset] = schemas.unset,
        link: typing.Union[MetaOapg.properties.link, str, schemas.Unset] = schemas.unset,
        rent: typing.Union['OnDemandEssentialsCreatePageRequestRent', schemas.Unset] = schemas.unset,
        subscription: typing.Union['OnDemandEssentialsCreatePageRequestSubscription', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OnDemandEssentialsCreatePageRequest':
        return super().__new__(
            cls,
            *args,
            name=name,
            content_rating=content_rating,
            description=description,
            type=type,
            accepted_currencies=accepted_currencies,
            buy=buy,
            domain_link=domain_link,
            episodes=episodes,
            link=link,
            rent=rent,
            subscription=subscription,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.on_demand_essentials_create_page_request_buy import OnDemandEssentialsCreatePageRequestBuy
from vimeo_python_sdk.model.on_demand_essentials_create_page_request_episodes import OnDemandEssentialsCreatePageRequestEpisodes
from vimeo_python_sdk.model.on_demand_essentials_create_page_request_rent import OnDemandEssentialsCreatePageRequestRent
from vimeo_python_sdk.model.on_demand_essentials_create_page_request_subscription import OnDemandEssentialsCreatePageRequestSubscription

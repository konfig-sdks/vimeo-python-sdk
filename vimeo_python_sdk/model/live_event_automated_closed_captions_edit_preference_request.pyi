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


class LiveEventAutomatedClosedCaptionsEditPreferenceRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "auto_cc_enabled",
        }
        
        class properties:
            auto_cc_enabled = schemas.BoolSchema
            auto_cc_keywords = schemas.StrSchema
            
            
            class auto_cc_lang(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DEDE(cls):
                    return cls("de-DE")
                
                @schemas.classproperty
                def ENUS(cls):
                    return cls("en-US")
                
                @schemas.classproperty
                def ESES(cls):
                    return cls("es-ES")
                
                @schemas.classproperty
                def FRFR(cls):
                    return cls("fr-FR")
                
                @schemas.classproperty
                def PTBR(cls):
                    return cls("pt-BR")
            __annotations__ = {
                "auto_cc_enabled": auto_cc_enabled,
                "auto_cc_keywords": auto_cc_keywords,
                "auto_cc_lang": auto_cc_lang,
            }
    
    auto_cc_enabled: MetaOapg.properties.auto_cc_enabled
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_cc_enabled"]) -> MetaOapg.properties.auto_cc_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_cc_keywords"]) -> MetaOapg.properties.auto_cc_keywords: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_cc_lang"]) -> MetaOapg.properties.auto_cc_lang: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["auto_cc_enabled", "auto_cc_keywords", "auto_cc_lang", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_cc_enabled"]) -> MetaOapg.properties.auto_cc_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_cc_keywords"]) -> typing.Union[MetaOapg.properties.auto_cc_keywords, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_cc_lang"]) -> typing.Union[MetaOapg.properties.auto_cc_lang, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["auto_cc_enabled", "auto_cc_keywords", "auto_cc_lang", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        auto_cc_enabled: typing.Union[MetaOapg.properties.auto_cc_enabled, bool, ],
        auto_cc_keywords: typing.Union[MetaOapg.properties.auto_cc_keywords, str, schemas.Unset] = schemas.unset,
        auto_cc_lang: typing.Union[MetaOapg.properties.auto_cc_lang, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LiveEventAutomatedClosedCaptionsEditPreferenceRequest':
        return super().__new__(
            cls,
            *args,
            auto_cc_enabled=auto_cc_enabled,
            auto_cc_keywords=auto_cc_keywords,
            auto_cc_lang=auto_cc_lang,
            _configuration=_configuration,
            **kwargs,
        )

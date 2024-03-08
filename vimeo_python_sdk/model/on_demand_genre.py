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


class OnDemandGenre(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "metadata",
            "link",
            "name",
            "canonical",
            "uri",
            "interactions",
        }
        
        class properties:
            canonical = schemas.StrSchema
        
            @staticmethod
            def interactions() -> typing.Type['OnDemandGenreInteractions']:
                return OnDemandGenreInteractions
            link = schemas.StrSchema
        
            @staticmethod
            def metadata() -> typing.Type['OnDemandGenreMetadata']:
                return OnDemandGenreMetadata
            name = schemas.StrSchema
            uri = schemas.StrSchema
            __annotations__ = {
                "canonical": canonical,
                "interactions": interactions,
                "link": link,
                "metadata": metadata,
                "name": name,
                "uri": uri,
            }
    
    metadata: 'OnDemandGenreMetadata'
    link: MetaOapg.properties.link
    name: MetaOapg.properties.name
    canonical: MetaOapg.properties.canonical
    uri: MetaOapg.properties.uri
    interactions: 'OnDemandGenreInteractions'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["canonical"]) -> MetaOapg.properties.canonical: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interactions"]) -> 'OnDemandGenreInteractions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'OnDemandGenreMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["canonical", "interactions", "link", "metadata", "name", "uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["canonical"]) -> MetaOapg.properties.canonical: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interactions"]) -> 'OnDemandGenreInteractions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> 'OnDemandGenreMetadata': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["canonical", "interactions", "link", "metadata", "name", "uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        metadata: 'OnDemandGenreMetadata',
        link: typing.Union[MetaOapg.properties.link, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        canonical: typing.Union[MetaOapg.properties.canonical, str, ],
        uri: typing.Union[MetaOapg.properties.uri, str, ],
        interactions: 'OnDemandGenreInteractions',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OnDemandGenre':
        return super().__new__(
            cls,
            *args,
            metadata=metadata,
            link=link,
            name=name,
            canonical=canonical,
            uri=uri,
            interactions=interactions,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.on_demand_genre_interactions import OnDemandGenreInteractions
from vimeo_python_sdk.model.on_demand_genre_metadata import OnDemandGenreMetadata

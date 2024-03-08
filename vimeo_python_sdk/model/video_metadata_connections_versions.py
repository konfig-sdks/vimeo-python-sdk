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


class VideoMetadataConnectionsVersions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Information about the video's versions.
    """


    class MetaOapg:
        required = {
            "has_interactive",
            "total",
            "origin_variable_frame_resolution",
            "options",
            "uri",
        }
        
        class properties:
            has_interactive = schemas.BoolSchema
        
            @staticmethod
            def options() -> typing.Type['VideoMetadataConnectionsVersionsOptions']:
                return VideoMetadataConnectionsVersionsOptions
            origin_variable_frame_resolution = schemas.BoolSchema
            total = schemas.NumberSchema
            uri = schemas.StrSchema
            current_uri = schemas.StrSchema
            resource_key = schemas.StrSchema
            __annotations__ = {
                "has_interactive": has_interactive,
                "options": options,
                "origin_variable_frame_resolution": origin_variable_frame_resolution,
                "total": total,
                "uri": uri,
                "current_uri": current_uri,
                "resource_key": resource_key,
            }
    
    has_interactive: MetaOapg.properties.has_interactive
    total: MetaOapg.properties.total
    origin_variable_frame_resolution: MetaOapg.properties.origin_variable_frame_resolution
    options: 'VideoMetadataConnectionsVersionsOptions'
    uri: MetaOapg.properties.uri
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_interactive"]) -> MetaOapg.properties.has_interactive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> 'VideoMetadataConnectionsVersionsOptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["origin_variable_frame_resolution"]) -> MetaOapg.properties.origin_variable_frame_resolution: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_uri"]) -> MetaOapg.properties.current_uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resource_key"]) -> MetaOapg.properties.resource_key: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["has_interactive", "options", "origin_variable_frame_resolution", "total", "uri", "current_uri", "resource_key", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_interactive"]) -> MetaOapg.properties.has_interactive: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> 'VideoMetadataConnectionsVersionsOptions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["origin_variable_frame_resolution"]) -> MetaOapg.properties.origin_variable_frame_resolution: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_uri"]) -> typing.Union[MetaOapg.properties.current_uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resource_key"]) -> typing.Union[MetaOapg.properties.resource_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["has_interactive", "options", "origin_variable_frame_resolution", "total", "uri", "current_uri", "resource_key", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        has_interactive: typing.Union[MetaOapg.properties.has_interactive, bool, ],
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, float, ],
        origin_variable_frame_resolution: typing.Union[MetaOapg.properties.origin_variable_frame_resolution, bool, ],
        options: 'VideoMetadataConnectionsVersionsOptions',
        uri: typing.Union[MetaOapg.properties.uri, str, ],
        current_uri: typing.Union[MetaOapg.properties.current_uri, str, schemas.Unset] = schemas.unset,
        resource_key: typing.Union[MetaOapg.properties.resource_key, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VideoMetadataConnectionsVersions':
        return super().__new__(
            cls,
            *args,
            has_interactive=has_interactive,
            total=total,
            origin_variable_frame_resolution=origin_variable_frame_resolution,
            options=options,
            uri=uri,
            current_uri=current_uri,
            resource_key=resource_key,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.video_metadata_connections_versions_options import VideoMetadataConnectionsVersionsOptions

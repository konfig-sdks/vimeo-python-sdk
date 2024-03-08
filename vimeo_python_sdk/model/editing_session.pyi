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


class EditingSession(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "has_watermark",
            "is_max_resolution",
            "is_music_licensed",
            "min_tier_for_movie",
            "is_rated",
            "result_video_hash",
            "is_edited_by_tve",
            "status",
            "vsid",
        }
        
        class properties:
            has_watermark = schemas.BoolSchema
            is_edited_by_tve = schemas.BoolSchema
            is_max_resolution = schemas.BoolSchema
            is_music_licensed = schemas.BoolSchema
            is_rated = schemas.BoolSchema
            min_tier_for_movie = schemas.StrSchema
            result_video_hash = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DONE(cls):
                    return cls("done")
                
                @schemas.classproperty
                def PROCESSING(cls):
                    return cls("processing")
            vsid = schemas.NumberSchema
            version_uri = schemas.StrSchema
            __annotations__ = {
                "has_watermark": has_watermark,
                "is_edited_by_tve": is_edited_by_tve,
                "is_max_resolution": is_max_resolution,
                "is_music_licensed": is_music_licensed,
                "is_rated": is_rated,
                "min_tier_for_movie": min_tier_for_movie,
                "result_video_hash": result_video_hash,
                "status": status,
                "vsid": vsid,
                "version_uri": version_uri,
            }
    
    has_watermark: MetaOapg.properties.has_watermark
    is_max_resolution: MetaOapg.properties.is_max_resolution
    is_music_licensed: MetaOapg.properties.is_music_licensed
    min_tier_for_movie: MetaOapg.properties.min_tier_for_movie
    is_rated: MetaOapg.properties.is_rated
    result_video_hash: MetaOapg.properties.result_video_hash
    is_edited_by_tve: MetaOapg.properties.is_edited_by_tve
    status: MetaOapg.properties.status
    vsid: MetaOapg.properties.vsid
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_watermark"]) -> MetaOapg.properties.has_watermark: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_edited_by_tve"]) -> MetaOapg.properties.is_edited_by_tve: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_max_resolution"]) -> MetaOapg.properties.is_max_resolution: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_music_licensed"]) -> MetaOapg.properties.is_music_licensed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_rated"]) -> MetaOapg.properties.is_rated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["min_tier_for_movie"]) -> MetaOapg.properties.min_tier_for_movie: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result_video_hash"]) -> MetaOapg.properties.result_video_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vsid"]) -> MetaOapg.properties.vsid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version_uri"]) -> MetaOapg.properties.version_uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["has_watermark", "is_edited_by_tve", "is_max_resolution", "is_music_licensed", "is_rated", "min_tier_for_movie", "result_video_hash", "status", "vsid", "version_uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_watermark"]) -> MetaOapg.properties.has_watermark: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_edited_by_tve"]) -> MetaOapg.properties.is_edited_by_tve: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_max_resolution"]) -> MetaOapg.properties.is_max_resolution: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_music_licensed"]) -> MetaOapg.properties.is_music_licensed: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_rated"]) -> MetaOapg.properties.is_rated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min_tier_for_movie"]) -> MetaOapg.properties.min_tier_for_movie: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result_video_hash"]) -> MetaOapg.properties.result_video_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vsid"]) -> MetaOapg.properties.vsid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version_uri"]) -> typing.Union[MetaOapg.properties.version_uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["has_watermark", "is_edited_by_tve", "is_max_resolution", "is_music_licensed", "is_rated", "min_tier_for_movie", "result_video_hash", "status", "vsid", "version_uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        has_watermark: typing.Union[MetaOapg.properties.has_watermark, bool, ],
        is_max_resolution: typing.Union[MetaOapg.properties.is_max_resolution, bool, ],
        is_music_licensed: typing.Union[MetaOapg.properties.is_music_licensed, bool, ],
        min_tier_for_movie: typing.Union[MetaOapg.properties.min_tier_for_movie, str, ],
        is_rated: typing.Union[MetaOapg.properties.is_rated, bool, ],
        result_video_hash: typing.Union[MetaOapg.properties.result_video_hash, str, ],
        is_edited_by_tve: typing.Union[MetaOapg.properties.is_edited_by_tve, bool, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        vsid: typing.Union[MetaOapg.properties.vsid, decimal.Decimal, int, float, ],
        version_uri: typing.Union[MetaOapg.properties.version_uri, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EditingSession':
        return super().__new__(
            cls,
            *args,
            has_watermark=has_watermark,
            is_max_resolution=is_max_resolution,
            is_music_licensed=is_music_licensed,
            min_tier_for_movie=min_tier_for_movie,
            is_rated=is_rated,
            result_video_hash=result_video_hash,
            is_edited_by_tve=is_edited_by_tve,
            status=status,
            vsid=vsid,
            version_uri=version_uri,
            _configuration=_configuration,
            **kwargs,
        )
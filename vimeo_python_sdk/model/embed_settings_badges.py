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


class EmbedSettingsBadges(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A collection of the video's badges.
    """


    class MetaOapg:
        required = {
            "weekend_challenge",
            "hdr",
            "vod",
            "staff_pick",
            "live",
        }
        
        class properties:
            hdr = schemas.BoolSchema
        
            @staticmethod
            def live() -> typing.Type['EmbedSettingsBadgesLive']:
                return EmbedSettingsBadgesLive
        
            @staticmethod
            def staff_pick() -> typing.Type['EmbedSettingsBadgesStaffPick']:
                return EmbedSettingsBadgesStaffPick
            vod = schemas.BoolSchema
            weekend_challenge = schemas.BoolSchema
            dolby_vision = schemas.BoolSchema
            hdr_10 = schemas.BoolSchema
            hdr_10_plus = schemas.BoolSchema
            __annotations__ = {
                "hdr": hdr,
                "live": live,
                "staff_pick": staff_pick,
                "vod": vod,
                "weekend_challenge": weekend_challenge,
                "dolby_vision": dolby_vision,
                "hdr_10": hdr_10,
                "hdr_10_plus": hdr_10_plus,
            }
    
    weekend_challenge: MetaOapg.properties.weekend_challenge
    hdr: MetaOapg.properties.hdr
    vod: MetaOapg.properties.vod
    staff_pick: 'EmbedSettingsBadgesStaffPick'
    live: 'EmbedSettingsBadgesLive'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hdr"]) -> MetaOapg.properties.hdr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["live"]) -> 'EmbedSettingsBadgesLive': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["staff_pick"]) -> 'EmbedSettingsBadgesStaffPick': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vod"]) -> MetaOapg.properties.vod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weekend_challenge"]) -> MetaOapg.properties.weekend_challenge: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dolby_vision"]) -> MetaOapg.properties.dolby_vision: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hdr_10"]) -> MetaOapg.properties.hdr_10: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hdr_10_plus"]) -> MetaOapg.properties.hdr_10_plus: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["hdr", "live", "staff_pick", "vod", "weekend_challenge", "dolby_vision", "hdr_10", "hdr_10_plus", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hdr"]) -> MetaOapg.properties.hdr: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["live"]) -> 'EmbedSettingsBadgesLive': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["staff_pick"]) -> 'EmbedSettingsBadgesStaffPick': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vod"]) -> MetaOapg.properties.vod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weekend_challenge"]) -> MetaOapg.properties.weekend_challenge: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dolby_vision"]) -> typing.Union[MetaOapg.properties.dolby_vision, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hdr_10"]) -> typing.Union[MetaOapg.properties.hdr_10, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hdr_10_plus"]) -> typing.Union[MetaOapg.properties.hdr_10_plus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hdr", "live", "staff_pick", "vod", "weekend_challenge", "dolby_vision", "hdr_10", "hdr_10_plus", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        weekend_challenge: typing.Union[MetaOapg.properties.weekend_challenge, bool, ],
        hdr: typing.Union[MetaOapg.properties.hdr, bool, ],
        vod: typing.Union[MetaOapg.properties.vod, bool, ],
        staff_pick: 'EmbedSettingsBadgesStaffPick',
        live: 'EmbedSettingsBadgesLive',
        dolby_vision: typing.Union[MetaOapg.properties.dolby_vision, bool, schemas.Unset] = schemas.unset,
        hdr_10: typing.Union[MetaOapg.properties.hdr_10, bool, schemas.Unset] = schemas.unset,
        hdr_10_plus: typing.Union[MetaOapg.properties.hdr_10_plus, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmbedSettingsBadges':
        return super().__new__(
            cls,
            *args,
            weekend_challenge=weekend_challenge,
            hdr=hdr,
            vod=vod,
            staff_pick=staff_pick,
            live=live,
            dolby_vision=dolby_vision,
            hdr_10=hdr_10,
            hdr_10_plus=hdr_10_plus,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.embed_settings_badges_live import EmbedSettingsBadgesLive
from vimeo_python_sdk.model.embed_settings_badges_staff_pick import EmbedSettingsBadgesStaffPick

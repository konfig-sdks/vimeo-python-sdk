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


class LiveEssentialsCreateEventRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "title",
        }
        
        class properties:
            title = schemas.StrSchema
            allow_share_link = schemas.BoolSchema
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
            automatically_title_stream = schemas.BoolSchema
            chat_enabled = schemas.BoolSchema
        
            @staticmethod
            def content_rating() -> typing.Type['LiveEssentialsCreateEventRequestContentRating']:
                return LiveEssentialsCreateEventRequestContentRating
            dvr = schemas.BoolSchema
        
            @staticmethod
            def embed() -> typing.Type['LiveEssentialsCreateEventRequestEmbed']:
                return LiveEssentialsCreateEventRequestEmbed
            folder_uri = schemas.StrSchema
        
            @staticmethod
            def interaction_tools_settings() -> typing.Type['LiveEssentialsCreateEventRequestInteractionToolsSettings']:
                return LiveEssentialsCreateEventRequestInteractionToolsSettings
            low_latency = schemas.BoolSchema
            
            
            class playlist_sort(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ADDED_FIRST(cls):
                    return cls("added_first")
                
                @schemas.classproperty
                def ADDED_LAST(cls):
                    return cls("added_last")
                
                @schemas.classproperty
                def ALPHABETICAL(cls):
                    return cls("alphabetical")
                
                @schemas.classproperty
                def ARRANGED(cls):
                    return cls("arranged")
                
                @schemas.classproperty
                def COMMENTS(cls):
                    return cls("comments")
                
                @schemas.classproperty
                def DURATION(cls):
                    return cls("duration")
                
                @schemas.classproperty
                def LIKES(cls):
                    return cls("likes")
                
                @schemas.classproperty
                def NEWEST(cls):
                    return cls("newest")
                
                @schemas.classproperty
                def OLDEST(cls):
                    return cls("oldest")
                
                @schemas.classproperty
                def PLAYS(cls):
                    return cls("plays")
            rtmp_preview = schemas.BoolSchema
        
            @staticmethod
            def schedule() -> typing.Type['LiveEssentialsCreateEventRequestSchedule']:
                return LiveEssentialsCreateEventRequestSchedule
            scheduled_playback = schemas.BoolSchema
            stream_description = schemas.StrSchema
        
            @staticmethod
            def stream_embed() -> typing.Type['LiveEssentialsCreateEventRequestStreamEmbed']:
                return LiveEssentialsCreateEventRequestStreamEmbed
            stream_password = schemas.StrSchema
        
            @staticmethod
            def stream_privacy() -> typing.Type['LiveEssentialsCreateEventRequestStreamPrivacy']:
                return LiveEssentialsCreateEventRequestStreamPrivacy
            stream_title = schemas.StrSchema
            time_zone = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "allow_share_link": allow_share_link,
                "auto_cc_enabled": auto_cc_enabled,
                "auto_cc_keywords": auto_cc_keywords,
                "auto_cc_lang": auto_cc_lang,
                "automatically_title_stream": automatically_title_stream,
                "chat_enabled": chat_enabled,
                "content_rating": content_rating,
                "dvr": dvr,
                "embed": embed,
                "folder_uri": folder_uri,
                "interaction_tools_settings": interaction_tools_settings,
                "low_latency": low_latency,
                "playlist_sort": playlist_sort,
                "rtmp_preview": rtmp_preview,
                "schedule": schedule,
                "scheduled_playback": scheduled_playback,
                "stream_description": stream_description,
                "stream_embed": stream_embed,
                "stream_password": stream_password,
                "stream_privacy": stream_privacy,
                "stream_title": stream_title,
                "time_zone": time_zone,
            }
    
    title: MetaOapg.properties.title
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_share_link"]) -> MetaOapg.properties.allow_share_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_cc_enabled"]) -> MetaOapg.properties.auto_cc_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_cc_keywords"]) -> MetaOapg.properties.auto_cc_keywords: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_cc_lang"]) -> MetaOapg.properties.auto_cc_lang: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["automatically_title_stream"]) -> MetaOapg.properties.automatically_title_stream: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chat_enabled"]) -> MetaOapg.properties.chat_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content_rating"]) -> 'LiveEssentialsCreateEventRequestContentRating': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dvr"]) -> MetaOapg.properties.dvr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embed"]) -> 'LiveEssentialsCreateEventRequestEmbed': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["folder_uri"]) -> MetaOapg.properties.folder_uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interaction_tools_settings"]) -> 'LiveEssentialsCreateEventRequestInteractionToolsSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["low_latency"]) -> MetaOapg.properties.low_latency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["playlist_sort"]) -> MetaOapg.properties.playlist_sort: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rtmp_preview"]) -> MetaOapg.properties.rtmp_preview: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedule"]) -> 'LiveEssentialsCreateEventRequestSchedule': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheduled_playback"]) -> MetaOapg.properties.scheduled_playback: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stream_description"]) -> MetaOapg.properties.stream_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stream_embed"]) -> 'LiveEssentialsCreateEventRequestStreamEmbed': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stream_password"]) -> MetaOapg.properties.stream_password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stream_privacy"]) -> 'LiveEssentialsCreateEventRequestStreamPrivacy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stream_title"]) -> MetaOapg.properties.stream_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_zone"]) -> MetaOapg.properties.time_zone: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "allow_share_link", "auto_cc_enabled", "auto_cc_keywords", "auto_cc_lang", "automatically_title_stream", "chat_enabled", "content_rating", "dvr", "embed", "folder_uri", "interaction_tools_settings", "low_latency", "playlist_sort", "rtmp_preview", "schedule", "scheduled_playback", "stream_description", "stream_embed", "stream_password", "stream_privacy", "stream_title", "time_zone", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_share_link"]) -> typing.Union[MetaOapg.properties.allow_share_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_cc_enabled"]) -> typing.Union[MetaOapg.properties.auto_cc_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_cc_keywords"]) -> typing.Union[MetaOapg.properties.auto_cc_keywords, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_cc_lang"]) -> typing.Union[MetaOapg.properties.auto_cc_lang, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["automatically_title_stream"]) -> typing.Union[MetaOapg.properties.automatically_title_stream, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chat_enabled"]) -> typing.Union[MetaOapg.properties.chat_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content_rating"]) -> typing.Union['LiveEssentialsCreateEventRequestContentRating', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dvr"]) -> typing.Union[MetaOapg.properties.dvr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embed"]) -> typing.Union['LiveEssentialsCreateEventRequestEmbed', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["folder_uri"]) -> typing.Union[MetaOapg.properties.folder_uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interaction_tools_settings"]) -> typing.Union['LiveEssentialsCreateEventRequestInteractionToolsSettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["low_latency"]) -> typing.Union[MetaOapg.properties.low_latency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["playlist_sort"]) -> typing.Union[MetaOapg.properties.playlist_sort, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rtmp_preview"]) -> typing.Union[MetaOapg.properties.rtmp_preview, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedule"]) -> typing.Union['LiveEssentialsCreateEventRequestSchedule', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheduled_playback"]) -> typing.Union[MetaOapg.properties.scheduled_playback, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stream_description"]) -> typing.Union[MetaOapg.properties.stream_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stream_embed"]) -> typing.Union['LiveEssentialsCreateEventRequestStreamEmbed', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stream_password"]) -> typing.Union[MetaOapg.properties.stream_password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stream_privacy"]) -> typing.Union['LiveEssentialsCreateEventRequestStreamPrivacy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stream_title"]) -> typing.Union[MetaOapg.properties.stream_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_zone"]) -> typing.Union[MetaOapg.properties.time_zone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "allow_share_link", "auto_cc_enabled", "auto_cc_keywords", "auto_cc_lang", "automatically_title_stream", "chat_enabled", "content_rating", "dvr", "embed", "folder_uri", "interaction_tools_settings", "low_latency", "playlist_sort", "rtmp_preview", "schedule", "scheduled_playback", "stream_description", "stream_embed", "stream_password", "stream_privacy", "stream_title", "time_zone", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        allow_share_link: typing.Union[MetaOapg.properties.allow_share_link, bool, schemas.Unset] = schemas.unset,
        auto_cc_enabled: typing.Union[MetaOapg.properties.auto_cc_enabled, bool, schemas.Unset] = schemas.unset,
        auto_cc_keywords: typing.Union[MetaOapg.properties.auto_cc_keywords, str, schemas.Unset] = schemas.unset,
        auto_cc_lang: typing.Union[MetaOapg.properties.auto_cc_lang, str, schemas.Unset] = schemas.unset,
        automatically_title_stream: typing.Union[MetaOapg.properties.automatically_title_stream, bool, schemas.Unset] = schemas.unset,
        chat_enabled: typing.Union[MetaOapg.properties.chat_enabled, bool, schemas.Unset] = schemas.unset,
        content_rating: typing.Union['LiveEssentialsCreateEventRequestContentRating', schemas.Unset] = schemas.unset,
        dvr: typing.Union[MetaOapg.properties.dvr, bool, schemas.Unset] = schemas.unset,
        embed: typing.Union['LiveEssentialsCreateEventRequestEmbed', schemas.Unset] = schemas.unset,
        folder_uri: typing.Union[MetaOapg.properties.folder_uri, str, schemas.Unset] = schemas.unset,
        interaction_tools_settings: typing.Union['LiveEssentialsCreateEventRequestInteractionToolsSettings', schemas.Unset] = schemas.unset,
        low_latency: typing.Union[MetaOapg.properties.low_latency, bool, schemas.Unset] = schemas.unset,
        playlist_sort: typing.Union[MetaOapg.properties.playlist_sort, str, schemas.Unset] = schemas.unset,
        rtmp_preview: typing.Union[MetaOapg.properties.rtmp_preview, bool, schemas.Unset] = schemas.unset,
        schedule: typing.Union['LiveEssentialsCreateEventRequestSchedule', schemas.Unset] = schemas.unset,
        scheduled_playback: typing.Union[MetaOapg.properties.scheduled_playback, bool, schemas.Unset] = schemas.unset,
        stream_description: typing.Union[MetaOapg.properties.stream_description, str, schemas.Unset] = schemas.unset,
        stream_embed: typing.Union['LiveEssentialsCreateEventRequestStreamEmbed', schemas.Unset] = schemas.unset,
        stream_password: typing.Union[MetaOapg.properties.stream_password, str, schemas.Unset] = schemas.unset,
        stream_privacy: typing.Union['LiveEssentialsCreateEventRequestStreamPrivacy', schemas.Unset] = schemas.unset,
        stream_title: typing.Union[MetaOapg.properties.stream_title, str, schemas.Unset] = schemas.unset,
        time_zone: typing.Union[MetaOapg.properties.time_zone, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LiveEssentialsCreateEventRequest':
        return super().__new__(
            cls,
            *args,
            title=title,
            allow_share_link=allow_share_link,
            auto_cc_enabled=auto_cc_enabled,
            auto_cc_keywords=auto_cc_keywords,
            auto_cc_lang=auto_cc_lang,
            automatically_title_stream=automatically_title_stream,
            chat_enabled=chat_enabled,
            content_rating=content_rating,
            dvr=dvr,
            embed=embed,
            folder_uri=folder_uri,
            interaction_tools_settings=interaction_tools_settings,
            low_latency=low_latency,
            playlist_sort=playlist_sort,
            rtmp_preview=rtmp_preview,
            schedule=schedule,
            scheduled_playback=scheduled_playback,
            stream_description=stream_description,
            stream_embed=stream_embed,
            stream_password=stream_password,
            stream_privacy=stream_privacy,
            stream_title=stream_title,
            time_zone=time_zone,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.live_essentials_create_event_request_content_rating import LiveEssentialsCreateEventRequestContentRating
from vimeo_python_sdk.model.live_essentials_create_event_request_embed import LiveEssentialsCreateEventRequestEmbed
from vimeo_python_sdk.model.live_essentials_create_event_request_interaction_tools_settings import LiveEssentialsCreateEventRequestInteractionToolsSettings
from vimeo_python_sdk.model.live_essentials_create_event_request_schedule import LiveEssentialsCreateEventRequestSchedule
from vimeo_python_sdk.model.live_essentials_create_event_request_stream_embed import LiveEssentialsCreateEventRequestStreamEmbed
from vimeo_python_sdk.model.live_essentials_create_event_request_stream_privacy import LiveEssentialsCreateEventRequestStreamPrivacy

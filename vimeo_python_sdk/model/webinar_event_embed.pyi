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


class WebinarEventEmbed(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The event's embed data.
    """


    class MetaOapg:
        required = {
            "play_button_position",
            "show_timezone",
            "color",
            "like_button",
            "playbar",
            "title",
            "embed_chat",
            "logos",
            "colors",
            "event_schedule",
            "available_player_logos",
            "playlist",
            "loop",
            "pip",
            "responsive_html",
            "fullscreen_button",
            "hide_live_label",
            "airplay",
            "html",
            "closed_captions",
            "byline",
            "show_latest_archived_clip",
            "portrait",
            "use_color",
            "autoplay",
            "volume",
            "schedule",
            "chromecast",
            "chat_embed_source",
            "hide_viewer_count",
            "embed_properties",
        }
        
        class properties:
            title = schemas.BoolSchema
            airplay = schemas.BoolSchema
            autoplay = schemas.BoolSchema
        
            @staticmethod
            def available_player_logos() -> typing.Type['WebinarEventEmbedAvailablePlayerLogos']:
                return WebinarEventEmbedAvailablePlayerLogos
            byline = schemas.BoolSchema
            
            
            class chat_embed_source(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'chat_embed_source':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            chromecast = schemas.BoolSchema
            closed_captions = schemas.BoolSchema
            color = schemas.StrSchema
        
            @staticmethod
            def colors() -> typing.Type['WebinarEventEmbedColors']:
                return WebinarEventEmbedColors
            
            
            class embed_chat(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'embed_chat':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def embed_properties() -> typing.Type['WebinarEventEmbedEmbedProperties']:
                return WebinarEventEmbedEmbedProperties
            event_schedule = schemas.BoolSchema
            fullscreen_button = schemas.BoolSchema
            hide_live_label = schemas.BoolSchema
            hide_viewer_count = schemas.BoolSchema
            
            
            class html(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'html':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            like_button = schemas.BoolSchema
        
            @staticmethod
            def logos() -> typing.Type['WebinarEventEmbedLogos']:
                return WebinarEventEmbedLogos
            loop = schemas.BoolSchema
            pip = schemas.BoolSchema
            
            
            class play_button_position(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls("0")
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls("1")
                
                @schemas.classproperty
                def POSITIVE_2(cls):
                    return cls("2")
            playbar = schemas.BoolSchema
            playlist = schemas.BoolSchema
            portrait = schemas.BoolSchema
            
            
            class responsive_html(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'responsive_html':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            schedule = schemas.BoolSchema
            show_latest_archived_clip = schemas.BoolSchema
            show_timezone = schemas.BoolSchema
            use_color = schemas.StrSchema
            volume = schemas.BoolSchema
            __annotations__ = {
                "title": title,
                "airplay": airplay,
                "autoplay": autoplay,
                "available_player_logos": available_player_logos,
                "byline": byline,
                "chat_embed_source": chat_embed_source,
                "chromecast": chromecast,
                "closed_captions": closed_captions,
                "color": color,
                "colors": colors,
                "embed_chat": embed_chat,
                "embed_properties": embed_properties,
                "event_schedule": event_schedule,
                "fullscreen_button": fullscreen_button,
                "hide_live_label": hide_live_label,
                "hide_viewer_count": hide_viewer_count,
                "html": html,
                "like_button": like_button,
                "logos": logos,
                "loop": loop,
                "pip": pip,
                "play_button_position": play_button_position,
                "playbar": playbar,
                "playlist": playlist,
                "portrait": portrait,
                "responsive_html": responsive_html,
                "schedule": schedule,
                "show_latest_archived_clip": show_latest_archived_clip,
                "show_timezone": show_timezone,
                "use_color": use_color,
                "volume": volume,
            }
    
    play_button_position: MetaOapg.properties.play_button_position
    show_timezone: MetaOapg.properties.show_timezone
    color: MetaOapg.properties.color
    like_button: MetaOapg.properties.like_button
    playbar: MetaOapg.properties.playbar
    title: MetaOapg.properties.title
    embed_chat: MetaOapg.properties.embed_chat
    logos: 'WebinarEventEmbedLogos'
    colors: 'WebinarEventEmbedColors'
    event_schedule: MetaOapg.properties.event_schedule
    available_player_logos: 'WebinarEventEmbedAvailablePlayerLogos'
    playlist: MetaOapg.properties.playlist
    loop: MetaOapg.properties.loop
    pip: MetaOapg.properties.pip
    responsive_html: MetaOapg.properties.responsive_html
    fullscreen_button: MetaOapg.properties.fullscreen_button
    hide_live_label: MetaOapg.properties.hide_live_label
    airplay: MetaOapg.properties.airplay
    html: MetaOapg.properties.html
    closed_captions: MetaOapg.properties.closed_captions
    byline: MetaOapg.properties.byline
    show_latest_archived_clip: MetaOapg.properties.show_latest_archived_clip
    portrait: MetaOapg.properties.portrait
    use_color: MetaOapg.properties.use_color
    autoplay: MetaOapg.properties.autoplay
    volume: MetaOapg.properties.volume
    schedule: MetaOapg.properties.schedule
    chromecast: MetaOapg.properties.chromecast
    chat_embed_source: MetaOapg.properties.chat_embed_source
    hide_viewer_count: MetaOapg.properties.hide_viewer_count
    embed_properties: 'WebinarEventEmbedEmbedProperties'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["airplay"]) -> MetaOapg.properties.airplay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoplay"]) -> MetaOapg.properties.autoplay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["available_player_logos"]) -> 'WebinarEventEmbedAvailablePlayerLogos': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["byline"]) -> MetaOapg.properties.byline: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chat_embed_source"]) -> MetaOapg.properties.chat_embed_source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chromecast"]) -> MetaOapg.properties.chromecast: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["closed_captions"]) -> MetaOapg.properties.closed_captions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["colors"]) -> 'WebinarEventEmbedColors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embed_chat"]) -> MetaOapg.properties.embed_chat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embed_properties"]) -> 'WebinarEventEmbedEmbedProperties': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_schedule"]) -> MetaOapg.properties.event_schedule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fullscreen_button"]) -> MetaOapg.properties.fullscreen_button: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hide_live_label"]) -> MetaOapg.properties.hide_live_label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hide_viewer_count"]) -> MetaOapg.properties.hide_viewer_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["html"]) -> MetaOapg.properties.html: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["like_button"]) -> MetaOapg.properties.like_button: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logos"]) -> 'WebinarEventEmbedLogos': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loop"]) -> MetaOapg.properties.loop: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pip"]) -> MetaOapg.properties.pip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["play_button_position"]) -> MetaOapg.properties.play_button_position: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["playbar"]) -> MetaOapg.properties.playbar: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["playlist"]) -> MetaOapg.properties.playlist: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["portrait"]) -> MetaOapg.properties.portrait: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["responsive_html"]) -> MetaOapg.properties.responsive_html: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedule"]) -> MetaOapg.properties.schedule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["show_latest_archived_clip"]) -> MetaOapg.properties.show_latest_archived_clip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["show_timezone"]) -> MetaOapg.properties.show_timezone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["use_color"]) -> MetaOapg.properties.use_color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["volume"]) -> MetaOapg.properties.volume: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "airplay", "autoplay", "available_player_logos", "byline", "chat_embed_source", "chromecast", "closed_captions", "color", "colors", "embed_chat", "embed_properties", "event_schedule", "fullscreen_button", "hide_live_label", "hide_viewer_count", "html", "like_button", "logos", "loop", "pip", "play_button_position", "playbar", "playlist", "portrait", "responsive_html", "schedule", "show_latest_archived_clip", "show_timezone", "use_color", "volume", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["airplay"]) -> MetaOapg.properties.airplay: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoplay"]) -> MetaOapg.properties.autoplay: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["available_player_logos"]) -> 'WebinarEventEmbedAvailablePlayerLogos': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["byline"]) -> MetaOapg.properties.byline: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chat_embed_source"]) -> MetaOapg.properties.chat_embed_source: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chromecast"]) -> MetaOapg.properties.chromecast: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["closed_captions"]) -> MetaOapg.properties.closed_captions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["colors"]) -> 'WebinarEventEmbedColors': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embed_chat"]) -> MetaOapg.properties.embed_chat: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embed_properties"]) -> 'WebinarEventEmbedEmbedProperties': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_schedule"]) -> MetaOapg.properties.event_schedule: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fullscreen_button"]) -> MetaOapg.properties.fullscreen_button: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hide_live_label"]) -> MetaOapg.properties.hide_live_label: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hide_viewer_count"]) -> MetaOapg.properties.hide_viewer_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["html"]) -> MetaOapg.properties.html: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["like_button"]) -> MetaOapg.properties.like_button: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logos"]) -> 'WebinarEventEmbedLogos': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loop"]) -> MetaOapg.properties.loop: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pip"]) -> MetaOapg.properties.pip: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["play_button_position"]) -> MetaOapg.properties.play_button_position: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["playbar"]) -> MetaOapg.properties.playbar: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["playlist"]) -> MetaOapg.properties.playlist: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["portrait"]) -> MetaOapg.properties.portrait: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["responsive_html"]) -> MetaOapg.properties.responsive_html: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedule"]) -> MetaOapg.properties.schedule: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["show_latest_archived_clip"]) -> MetaOapg.properties.show_latest_archived_clip: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["show_timezone"]) -> MetaOapg.properties.show_timezone: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["use_color"]) -> MetaOapg.properties.use_color: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["volume"]) -> MetaOapg.properties.volume: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "airplay", "autoplay", "available_player_logos", "byline", "chat_embed_source", "chromecast", "closed_captions", "color", "colors", "embed_chat", "embed_properties", "event_schedule", "fullscreen_button", "hide_live_label", "hide_viewer_count", "html", "like_button", "logos", "loop", "pip", "play_button_position", "playbar", "playlist", "portrait", "responsive_html", "schedule", "show_latest_archived_clip", "show_timezone", "use_color", "volume", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        play_button_position: typing.Union[MetaOapg.properties.play_button_position, str, ],
        show_timezone: typing.Union[MetaOapg.properties.show_timezone, bool, ],
        color: typing.Union[MetaOapg.properties.color, str, ],
        like_button: typing.Union[MetaOapg.properties.like_button, bool, ],
        playbar: typing.Union[MetaOapg.properties.playbar, bool, ],
        title: typing.Union[MetaOapg.properties.title, bool, ],
        embed_chat: typing.Union[MetaOapg.properties.embed_chat, None, str, ],
        logos: 'WebinarEventEmbedLogos',
        colors: 'WebinarEventEmbedColors',
        event_schedule: typing.Union[MetaOapg.properties.event_schedule, bool, ],
        available_player_logos: 'WebinarEventEmbedAvailablePlayerLogos',
        playlist: typing.Union[MetaOapg.properties.playlist, bool, ],
        loop: typing.Union[MetaOapg.properties.loop, bool, ],
        pip: typing.Union[MetaOapg.properties.pip, bool, ],
        responsive_html: typing.Union[MetaOapg.properties.responsive_html, None, str, ],
        fullscreen_button: typing.Union[MetaOapg.properties.fullscreen_button, bool, ],
        hide_live_label: typing.Union[MetaOapg.properties.hide_live_label, bool, ],
        airplay: typing.Union[MetaOapg.properties.airplay, bool, ],
        html: typing.Union[MetaOapg.properties.html, None, str, ],
        closed_captions: typing.Union[MetaOapg.properties.closed_captions, bool, ],
        byline: typing.Union[MetaOapg.properties.byline, bool, ],
        show_latest_archived_clip: typing.Union[MetaOapg.properties.show_latest_archived_clip, bool, ],
        portrait: typing.Union[MetaOapg.properties.portrait, bool, ],
        use_color: typing.Union[MetaOapg.properties.use_color, str, ],
        autoplay: typing.Union[MetaOapg.properties.autoplay, bool, ],
        volume: typing.Union[MetaOapg.properties.volume, bool, ],
        schedule: typing.Union[MetaOapg.properties.schedule, bool, ],
        chromecast: typing.Union[MetaOapg.properties.chromecast, bool, ],
        chat_embed_source: typing.Union[MetaOapg.properties.chat_embed_source, None, str, ],
        hide_viewer_count: typing.Union[MetaOapg.properties.hide_viewer_count, bool, ],
        embed_properties: 'WebinarEventEmbedEmbedProperties',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebinarEventEmbed':
        return super().__new__(
            cls,
            *args,
            play_button_position=play_button_position,
            show_timezone=show_timezone,
            color=color,
            like_button=like_button,
            playbar=playbar,
            title=title,
            embed_chat=embed_chat,
            logos=logos,
            colors=colors,
            event_schedule=event_schedule,
            available_player_logos=available_player_logos,
            playlist=playlist,
            loop=loop,
            pip=pip,
            responsive_html=responsive_html,
            fullscreen_button=fullscreen_button,
            hide_live_label=hide_live_label,
            airplay=airplay,
            html=html,
            closed_captions=closed_captions,
            byline=byline,
            show_latest_archived_clip=show_latest_archived_clip,
            portrait=portrait,
            use_color=use_color,
            autoplay=autoplay,
            volume=volume,
            schedule=schedule,
            chromecast=chromecast,
            chat_embed_source=chat_embed_source,
            hide_viewer_count=hide_viewer_count,
            embed_properties=embed_properties,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.webinar_event_embed_available_player_logos import WebinarEventEmbedAvailablePlayerLogos
from vimeo_python_sdk.model.webinar_event_embed_colors import WebinarEventEmbedColors
from vimeo_python_sdk.model.webinar_event_embed_embed_properties import WebinarEventEmbedEmbedProperties
from vimeo_python_sdk.model.webinar_event_embed_logos import WebinarEventEmbedLogos

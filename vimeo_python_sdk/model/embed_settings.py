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


class EmbedSettings(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "cards",
            "show_timezone",
            "color",
            "chapters",
            "quality_selector",
            "interactive",
            "playbar",
            "title",
            "logos",
            "colors",
            "speed",
            "event_schedule",
            "transcript",
            "pip",
            "airplay",
            "closed_captions",
            "audio_tracks",
            "buttons",
            "play_button",
            "outro_type",
            "email_capture_form",
            "badges",
            "volume",
            "autopip",
            "chromecast",
            "has_cards",
            "end_screen",
        }
        
        class properties:
        
            @staticmethod
            def title() -> typing.Type['EmbedSettingsTitle']:
                return EmbedSettingsTitle
            airplay = schemas.BoolSchema
            audio_tracks = schemas.BoolSchema
            autopip = schemas.BoolSchema
        
            @staticmethod
            def badges() -> typing.Type['EmbedSettingsBadges']:
                return EmbedSettingsBadges
        
            @staticmethod
            def buttons() -> typing.Type['EmbedSettingsButtons']:
                return EmbedSettingsButtons
        
            @staticmethod
            def cards() -> typing.Type['EmbedSettingsCards']:
                return EmbedSettingsCards
            chapters = schemas.BoolSchema
            chromecast = schemas.BoolSchema
            closed_captions = schemas.BoolSchema
            color = schemas.StrSchema
        
            @staticmethod
            def colors() -> typing.Type['EmbedSettingsColors']:
                return EmbedSettingsColors
        
            @staticmethod
            def email_capture_form() -> typing.Type['EmailCaptureForm']:
                return EmailCaptureForm
        
            @staticmethod
            def end_screen() -> typing.Type['EmbedSettingsEndScreen']:
                return EmbedSettingsEndScreen
            event_schedule = schemas.BoolSchema
            has_cards = schemas.BoolSchema
            interactive = schemas.BoolSchema
        
            @staticmethod
            def logos() -> typing.Type['EmbedSettingsLogos']:
                return EmbedSettingsLogos
            
            
            class outro_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "beginning": "BEGINNING",
                        "custom": "CUSTOM",
                        "email": "EMAIL",
                        "image": "IMAGE",
                        "link": "LINK",
                        "loop": "LOOP",
                        "nothing": "NOTHING",
                        "share": "SHARE",
                        "text": "TEXT",
                        "threevideos": "THREEVIDEOS",
                        "videos": "VIDEOS",
                    }
                
                @schemas.classproperty
                def BEGINNING(cls):
                    return cls("beginning")
                
                @schemas.classproperty
                def CUSTOM(cls):
                    return cls("custom")
                
                @schemas.classproperty
                def EMAIL(cls):
                    return cls("email")
                
                @schemas.classproperty
                def IMAGE(cls):
                    return cls("image")
                
                @schemas.classproperty
                def LINK(cls):
                    return cls("link")
                
                @schemas.classproperty
                def LOOP(cls):
                    return cls("loop")
                
                @schemas.classproperty
                def NOTHING(cls):
                    return cls("nothing")
                
                @schemas.classproperty
                def SHARE(cls):
                    return cls("share")
                
                @schemas.classproperty
                def TEXT(cls):
                    return cls("text")
                
                @schemas.classproperty
                def THREEVIDEOS(cls):
                    return cls("threevideos")
                
                @schemas.classproperty
                def VIDEOS(cls):
                    return cls("videos")
            pip = schemas.BoolSchema
        
            @staticmethod
            def play_button() -> typing.Type['EmbedSettingsPlayButton']:
                return EmbedSettingsPlayButton
            playbar = schemas.BoolSchema
            quality_selector = schemas.BoolSchema
            show_timezone = schemas.BoolSchema
            speed = schemas.BoolSchema
            transcript = schemas.BoolSchema
            volume = schemas.BoolSchema
            html = schemas.StrSchema
            uri = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "airplay": airplay,
                "audio_tracks": audio_tracks,
                "autopip": autopip,
                "badges": badges,
                "buttons": buttons,
                "cards": cards,
                "chapters": chapters,
                "chromecast": chromecast,
                "closed_captions": closed_captions,
                "color": color,
                "colors": colors,
                "email_capture_form": email_capture_form,
                "end_screen": end_screen,
                "event_schedule": event_schedule,
                "has_cards": has_cards,
                "interactive": interactive,
                "logos": logos,
                "outro_type": outro_type,
                "pip": pip,
                "play_button": play_button,
                "playbar": playbar,
                "quality_selector": quality_selector,
                "show_timezone": show_timezone,
                "speed": speed,
                "transcript": transcript,
                "volume": volume,
                "html": html,
                "uri": uri,
            }
    
    cards: 'EmbedSettingsCards'
    show_timezone: MetaOapg.properties.show_timezone
    color: MetaOapg.properties.color
    chapters: MetaOapg.properties.chapters
    quality_selector: MetaOapg.properties.quality_selector
    interactive: MetaOapg.properties.interactive
    playbar: MetaOapg.properties.playbar
    title: 'EmbedSettingsTitle'
    logos: 'EmbedSettingsLogos'
    colors: 'EmbedSettingsColors'
    speed: MetaOapg.properties.speed
    event_schedule: MetaOapg.properties.event_schedule
    transcript: MetaOapg.properties.transcript
    pip: MetaOapg.properties.pip
    airplay: MetaOapg.properties.airplay
    closed_captions: MetaOapg.properties.closed_captions
    audio_tracks: MetaOapg.properties.audio_tracks
    buttons: 'EmbedSettingsButtons'
    play_button: 'EmbedSettingsPlayButton'
    outro_type: MetaOapg.properties.outro_type
    email_capture_form: 'EmailCaptureForm'
    badges: 'EmbedSettingsBadges'
    volume: MetaOapg.properties.volume
    autopip: MetaOapg.properties.autopip
    chromecast: MetaOapg.properties.chromecast
    has_cards: MetaOapg.properties.has_cards
    end_screen: 'EmbedSettingsEndScreen'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> 'EmbedSettingsTitle': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["airplay"]) -> MetaOapg.properties.airplay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audio_tracks"]) -> MetaOapg.properties.audio_tracks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autopip"]) -> MetaOapg.properties.autopip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["badges"]) -> 'EmbedSettingsBadges': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buttons"]) -> 'EmbedSettingsButtons': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cards"]) -> 'EmbedSettingsCards': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chapters"]) -> MetaOapg.properties.chapters: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chromecast"]) -> MetaOapg.properties.chromecast: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["closed_captions"]) -> MetaOapg.properties.closed_captions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["colors"]) -> 'EmbedSettingsColors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_capture_form"]) -> 'EmailCaptureForm': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_screen"]) -> 'EmbedSettingsEndScreen': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_schedule"]) -> MetaOapg.properties.event_schedule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_cards"]) -> MetaOapg.properties.has_cards: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interactive"]) -> MetaOapg.properties.interactive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logos"]) -> 'EmbedSettingsLogos': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outro_type"]) -> MetaOapg.properties.outro_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pip"]) -> MetaOapg.properties.pip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["play_button"]) -> 'EmbedSettingsPlayButton': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["playbar"]) -> MetaOapg.properties.playbar: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quality_selector"]) -> MetaOapg.properties.quality_selector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["show_timezone"]) -> MetaOapg.properties.show_timezone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["speed"]) -> MetaOapg.properties.speed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transcript"]) -> MetaOapg.properties.transcript: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["volume"]) -> MetaOapg.properties.volume: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["html"]) -> MetaOapg.properties.html: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "airplay", "audio_tracks", "autopip", "badges", "buttons", "cards", "chapters", "chromecast", "closed_captions", "color", "colors", "email_capture_form", "end_screen", "event_schedule", "has_cards", "interactive", "logos", "outro_type", "pip", "play_button", "playbar", "quality_selector", "show_timezone", "speed", "transcript", "volume", "html", "uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> 'EmbedSettingsTitle': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["airplay"]) -> MetaOapg.properties.airplay: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audio_tracks"]) -> MetaOapg.properties.audio_tracks: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autopip"]) -> MetaOapg.properties.autopip: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["badges"]) -> 'EmbedSettingsBadges': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buttons"]) -> 'EmbedSettingsButtons': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cards"]) -> 'EmbedSettingsCards': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chapters"]) -> MetaOapg.properties.chapters: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chromecast"]) -> MetaOapg.properties.chromecast: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["closed_captions"]) -> MetaOapg.properties.closed_captions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["colors"]) -> 'EmbedSettingsColors': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_capture_form"]) -> 'EmailCaptureForm': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_screen"]) -> 'EmbedSettingsEndScreen': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_schedule"]) -> MetaOapg.properties.event_schedule: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_cards"]) -> MetaOapg.properties.has_cards: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interactive"]) -> MetaOapg.properties.interactive: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logos"]) -> 'EmbedSettingsLogos': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outro_type"]) -> MetaOapg.properties.outro_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pip"]) -> MetaOapg.properties.pip: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["play_button"]) -> 'EmbedSettingsPlayButton': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["playbar"]) -> MetaOapg.properties.playbar: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quality_selector"]) -> MetaOapg.properties.quality_selector: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["show_timezone"]) -> MetaOapg.properties.show_timezone: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["speed"]) -> MetaOapg.properties.speed: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transcript"]) -> MetaOapg.properties.transcript: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["volume"]) -> MetaOapg.properties.volume: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["html"]) -> typing.Union[MetaOapg.properties.html, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> typing.Union[MetaOapg.properties.uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "airplay", "audio_tracks", "autopip", "badges", "buttons", "cards", "chapters", "chromecast", "closed_captions", "color", "colors", "email_capture_form", "end_screen", "event_schedule", "has_cards", "interactive", "logos", "outro_type", "pip", "play_button", "playbar", "quality_selector", "show_timezone", "speed", "transcript", "volume", "html", "uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cards: 'EmbedSettingsCards',
        show_timezone: typing.Union[MetaOapg.properties.show_timezone, bool, ],
        color: typing.Union[MetaOapg.properties.color, str, ],
        chapters: typing.Union[MetaOapg.properties.chapters, bool, ],
        quality_selector: typing.Union[MetaOapg.properties.quality_selector, bool, ],
        interactive: typing.Union[MetaOapg.properties.interactive, bool, ],
        playbar: typing.Union[MetaOapg.properties.playbar, bool, ],
        title: 'EmbedSettingsTitle',
        logos: 'EmbedSettingsLogos',
        colors: 'EmbedSettingsColors',
        speed: typing.Union[MetaOapg.properties.speed, bool, ],
        event_schedule: typing.Union[MetaOapg.properties.event_schedule, bool, ],
        transcript: typing.Union[MetaOapg.properties.transcript, bool, ],
        pip: typing.Union[MetaOapg.properties.pip, bool, ],
        airplay: typing.Union[MetaOapg.properties.airplay, bool, ],
        closed_captions: typing.Union[MetaOapg.properties.closed_captions, bool, ],
        audio_tracks: typing.Union[MetaOapg.properties.audio_tracks, bool, ],
        buttons: 'EmbedSettingsButtons',
        play_button: 'EmbedSettingsPlayButton',
        outro_type: typing.Union[MetaOapg.properties.outro_type, str, ],
        email_capture_form: 'EmailCaptureForm',
        badges: 'EmbedSettingsBadges',
        volume: typing.Union[MetaOapg.properties.volume, bool, ],
        autopip: typing.Union[MetaOapg.properties.autopip, bool, ],
        chromecast: typing.Union[MetaOapg.properties.chromecast, bool, ],
        has_cards: typing.Union[MetaOapg.properties.has_cards, bool, ],
        end_screen: 'EmbedSettingsEndScreen',
        html: typing.Union[MetaOapg.properties.html, str, schemas.Unset] = schemas.unset,
        uri: typing.Union[MetaOapg.properties.uri, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmbedSettings':
        return super().__new__(
            cls,
            *args,
            cards=cards,
            show_timezone=show_timezone,
            color=color,
            chapters=chapters,
            quality_selector=quality_selector,
            interactive=interactive,
            playbar=playbar,
            title=title,
            logos=logos,
            colors=colors,
            speed=speed,
            event_schedule=event_schedule,
            transcript=transcript,
            pip=pip,
            airplay=airplay,
            closed_captions=closed_captions,
            audio_tracks=audio_tracks,
            buttons=buttons,
            play_button=play_button,
            outro_type=outro_type,
            email_capture_form=email_capture_form,
            badges=badges,
            volume=volume,
            autopip=autopip,
            chromecast=chromecast,
            has_cards=has_cards,
            end_screen=end_screen,
            html=html,
            uri=uri,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.email_capture_form import EmailCaptureForm
from vimeo_python_sdk.model.embed_settings_badges import EmbedSettingsBadges
from vimeo_python_sdk.model.embed_settings_buttons import EmbedSettingsButtons
from vimeo_python_sdk.model.embed_settings_cards import EmbedSettingsCards
from vimeo_python_sdk.model.embed_settings_colors import EmbedSettingsColors
from vimeo_python_sdk.model.embed_settings_end_screen import EmbedSettingsEndScreen
from vimeo_python_sdk.model.embed_settings_logos import EmbedSettingsLogos
from vimeo_python_sdk.model.embed_settings_play_button import EmbedSettingsPlayButton
from vimeo_python_sdk.model.embed_settings_title import EmbedSettingsTitle
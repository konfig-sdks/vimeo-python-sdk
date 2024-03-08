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


class EditVideoRequestEmbed(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def title() -> typing.Type['EditVideoRequestEmbedTitle']:
                return EditVideoRequestEmbedTitle
            airplay = schemas.BoolSchema
            audio_tracks = schemas.BoolSchema
        
            @staticmethod
            def buttons() -> typing.Type['EditVideoRequestEmbedButtons']:
                return EditVideoRequestEmbedButtons
        
            @staticmethod
            def cards() -> typing.Type['EditVideoRequestEmbedCards']:
                return EditVideoRequestEmbedCards
            chapters = schemas.BoolSchema
            chromecast = schemas.BoolSchema
            closed_captions = schemas.BoolSchema
            color = schemas.StrSchema
        
            @staticmethod
            def end_screen() -> typing.Type['EditVideoRequestEmbedEndScreen']:
                return EditVideoRequestEmbedEndScreen
        
            @staticmethod
            def logos() -> typing.Type['EditVideoRequestEmbedLogos']:
                return EditVideoRequestEmbedLogos
        
            @staticmethod
            def play_button() -> typing.Type['EditVideoRequestEmbedPlayButton']:
                return EditVideoRequestEmbedPlayButton
            playbar = schemas.BoolSchema
            quality_selector = schemas.BoolSchema
            transcript = schemas.BoolSchema
            volume = schemas.BoolSchema
            __annotations__ = {
                "title": title,
                "airplay": airplay,
                "audio_tracks": audio_tracks,
                "buttons": buttons,
                "cards": cards,
                "chapters": chapters,
                "chromecast": chromecast,
                "closed_captions": closed_captions,
                "color": color,
                "end_screen": end_screen,
                "logos": logos,
                "play_button": play_button,
                "playbar": playbar,
                "quality_selector": quality_selector,
                "transcript": transcript,
                "volume": volume,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> 'EditVideoRequestEmbedTitle': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["airplay"]) -> MetaOapg.properties.airplay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audio_tracks"]) -> MetaOapg.properties.audio_tracks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buttons"]) -> 'EditVideoRequestEmbedButtons': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cards"]) -> 'EditVideoRequestEmbedCards': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chapters"]) -> MetaOapg.properties.chapters: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chromecast"]) -> MetaOapg.properties.chromecast: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["closed_captions"]) -> MetaOapg.properties.closed_captions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_screen"]) -> 'EditVideoRequestEmbedEndScreen': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logos"]) -> 'EditVideoRequestEmbedLogos': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["play_button"]) -> 'EditVideoRequestEmbedPlayButton': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["playbar"]) -> MetaOapg.properties.playbar: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quality_selector"]) -> MetaOapg.properties.quality_selector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transcript"]) -> MetaOapg.properties.transcript: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["volume"]) -> MetaOapg.properties.volume: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "airplay", "audio_tracks", "buttons", "cards", "chapters", "chromecast", "closed_captions", "color", "end_screen", "logos", "play_button", "playbar", "quality_selector", "transcript", "volume", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union['EditVideoRequestEmbedTitle', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["airplay"]) -> typing.Union[MetaOapg.properties.airplay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audio_tracks"]) -> typing.Union[MetaOapg.properties.audio_tracks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buttons"]) -> typing.Union['EditVideoRequestEmbedButtons', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cards"]) -> typing.Union['EditVideoRequestEmbedCards', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chapters"]) -> typing.Union[MetaOapg.properties.chapters, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chromecast"]) -> typing.Union[MetaOapg.properties.chromecast, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["closed_captions"]) -> typing.Union[MetaOapg.properties.closed_captions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_screen"]) -> typing.Union['EditVideoRequestEmbedEndScreen', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logos"]) -> typing.Union['EditVideoRequestEmbedLogos', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["play_button"]) -> typing.Union['EditVideoRequestEmbedPlayButton', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["playbar"]) -> typing.Union[MetaOapg.properties.playbar, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quality_selector"]) -> typing.Union[MetaOapg.properties.quality_selector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transcript"]) -> typing.Union[MetaOapg.properties.transcript, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["volume"]) -> typing.Union[MetaOapg.properties.volume, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "airplay", "audio_tracks", "buttons", "cards", "chapters", "chromecast", "closed_captions", "color", "end_screen", "logos", "play_button", "playbar", "quality_selector", "transcript", "volume", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union['EditVideoRequestEmbedTitle', schemas.Unset] = schemas.unset,
        airplay: typing.Union[MetaOapg.properties.airplay, bool, schemas.Unset] = schemas.unset,
        audio_tracks: typing.Union[MetaOapg.properties.audio_tracks, bool, schemas.Unset] = schemas.unset,
        buttons: typing.Union['EditVideoRequestEmbedButtons', schemas.Unset] = schemas.unset,
        cards: typing.Union['EditVideoRequestEmbedCards', schemas.Unset] = schemas.unset,
        chapters: typing.Union[MetaOapg.properties.chapters, bool, schemas.Unset] = schemas.unset,
        chromecast: typing.Union[MetaOapg.properties.chromecast, bool, schemas.Unset] = schemas.unset,
        closed_captions: typing.Union[MetaOapg.properties.closed_captions, bool, schemas.Unset] = schemas.unset,
        color: typing.Union[MetaOapg.properties.color, str, schemas.Unset] = schemas.unset,
        end_screen: typing.Union['EditVideoRequestEmbedEndScreen', schemas.Unset] = schemas.unset,
        logos: typing.Union['EditVideoRequestEmbedLogos', schemas.Unset] = schemas.unset,
        play_button: typing.Union['EditVideoRequestEmbedPlayButton', schemas.Unset] = schemas.unset,
        playbar: typing.Union[MetaOapg.properties.playbar, bool, schemas.Unset] = schemas.unset,
        quality_selector: typing.Union[MetaOapg.properties.quality_selector, bool, schemas.Unset] = schemas.unset,
        transcript: typing.Union[MetaOapg.properties.transcript, bool, schemas.Unset] = schemas.unset,
        volume: typing.Union[MetaOapg.properties.volume, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EditVideoRequestEmbed':
        return super().__new__(
            cls,
            *args,
            title=title,
            airplay=airplay,
            audio_tracks=audio_tracks,
            buttons=buttons,
            cards=cards,
            chapters=chapters,
            chromecast=chromecast,
            closed_captions=closed_captions,
            color=color,
            end_screen=end_screen,
            logos=logos,
            play_button=play_button,
            playbar=playbar,
            quality_selector=quality_selector,
            transcript=transcript,
            volume=volume,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.edit_video_request_embed_buttons import EditVideoRequestEmbedButtons
from vimeo_python_sdk.model.edit_video_request_embed_cards import EditVideoRequestEmbedCards
from vimeo_python_sdk.model.edit_video_request_embed_end_screen import EditVideoRequestEmbedEndScreen
from vimeo_python_sdk.model.edit_video_request_embed_logos import EditVideoRequestEmbedLogos
from vimeo_python_sdk.model.edit_video_request_embed_play_button import EditVideoRequestEmbedPlayButton
from vimeo_python_sdk.model.edit_video_request_embed_title import EditVideoRequestEmbedTitle

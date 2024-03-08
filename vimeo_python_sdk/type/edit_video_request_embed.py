# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from vimeo_python_sdk.type.edit_video_request_embed_buttons import EditVideoRequestEmbedButtons
from vimeo_python_sdk.type.edit_video_request_embed_cards import EditVideoRequestEmbedCards
from vimeo_python_sdk.type.edit_video_request_embed_end_screen import EditVideoRequestEmbedEndScreen
from vimeo_python_sdk.type.edit_video_request_embed_logos import EditVideoRequestEmbedLogos
from vimeo_python_sdk.type.edit_video_request_embed_play_button import EditVideoRequestEmbedPlayButton
from vimeo_python_sdk.type.edit_video_request_embed_title import EditVideoRequestEmbedTitle

class RequiredEditVideoRequestEmbed(TypedDict):
    pass

class OptionalEditVideoRequestEmbed(TypedDict, total=False):
    title: EditVideoRequestEmbedTitle

    # Whether AirPlay is enabled in the embeddable player.
    airplay: bool

    # Whether multiple audio tracks can appear in the embeddable player.
    audio_tracks: bool

    buttons: EditVideoRequestEmbedButtons

    cards: EditVideoRequestEmbedCards

    # Whether chapters are enabled in the embeddable player.
    chapters: bool

    # Whether the Chromecast button appears in the embeddable player.
    chromecast: bool

    # Whether closed captions are enabled in the embeddable player.
    closed_captions: bool

    # The main color of the embeddable player.
    color: str

    end_screen: EditVideoRequestEmbedEndScreen

    logos: EditVideoRequestEmbedLogos

    play_button: EditVideoRequestEmbedPlayButton

    # Whether to show the playbar on the embeddable player.
    playbar: bool

    # Whether to show the quality selector in the embeddable player.
    quality_selector: bool

    # Whether the transcript controls appear in the embeddable player.
    transcript: bool

    # Whether to show the volume selector on the embeddable player.
    volume: bool

class EditVideoRequestEmbed(RequiredEditVideoRequestEmbed, OptionalEditVideoRequestEmbed):
    pass

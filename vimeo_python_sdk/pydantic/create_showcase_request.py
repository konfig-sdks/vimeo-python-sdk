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
from pydantic import BaseModel, Field, RootModel


class CreateShowcaseRequest(BaseModel):
    # The name of the showcase.
    name: str = Field(alias='name')

    # The description of the showcase.
    description: typing.Optional[str] = Field(None, alias='description')

    # The hexadecimal code for the color of the player buttons and showcase controls.
    brand_color: typing.Optional[str] = Field(None, alias='brand_color')

    # Whether the showcase should be hidden from Vimeo when unlisted.
    hide_from_vimeo: typing.Optional[bool] = Field(None, alias='hide_from_vimeo')

    # Whether to hide Vimeo navigation when displaying the showcase.
    hide_nav: typing.Optional[bool] = Field(None, alias='hide_nav')

    # Whether to include the upcoming event in the showcase.
    hide_upcoming: typing.Optional[bool] = Field(None, alias='hide_upcoming')

    # The type of layout for presenting the showcase.  Option descriptions:  * `grid` - The videos appear in a grid.  * `player` - The videos appear in the player. 
    layout: typing.Optional[Literal["grid", "player"]] = Field(None, alias='layout')

    # The showcase's password. This field is required only when **privacy** is `password`.
    password: typing.Optional[str] = Field(None, alias='password')

    # The privacy level of the showcase.  Option descriptions:  * `anybody` - Anyone can access the showcase, either on Vimeo or through an embed.  * `embed_only` - The showcase doesn't appear on Vimeo, but it can be embedded on other sites.  * `nobody` - No one can access the showcase, including the authenticated user.  * `password` - Only those with the password can access the showcase.  * `team` - Only members of the authenticated user's team can access the showcase.  * `unlisted` - The showcase can't be accessed if the URL omits its unlisted hash. 
    privacy: typing.Optional[Literal["anybody", "embed_only", "nobody", "password", "team", "unlisted"]] = Field(None, alias='privacy')

    # Whether showcase videos use the review mode URL.
    review_mode: typing.Optional[bool] = Field(None, alias='review_mode')

    # The default sort order of the videos as they appear in the showcase.  Option descriptions:  * `added_first` - The videos appear according to when they were added to the showcase, with the most recently added first.  * `added_last` - The videos appear according to when they were added to the showcase, with the most recently added last.  * `alphabetical` - The videos appear alphabetically by their title.  * `arranged` - The videos appear as arranged by the owner of the showcase.  * `comments` - The videos appear according to their number of comments.  * `likes` - The videos appear according to their number of likes.  * `newest` - The videos appear in chronological order with the newest first.  * `oldest` - The videos appear in chronological order with the oldest first.  * `plays` - The videos appear according to their number of plays. 
    sort: typing.Optional[Literal["added_first", "added_last", "alphabetical", "arranged", "comments", "likes", "newest", "oldest", "plays"]] = Field(None, alias='sort')

    # The color theme of the showcase.  Option descriptions:  * `dark` - The showcase uses the dark theme.  * `standard` - The showcase uses the standard theme. 
    theme: typing.Optional[Literal["dark", "standard"]] = Field(None, alias='theme')
    class Config:
        arbitrary_types_allowed = True

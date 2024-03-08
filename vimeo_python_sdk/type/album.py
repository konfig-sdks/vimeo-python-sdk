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

from vimeo_python_sdk.type.album_embed import AlbumEmbed
from vimeo_python_sdk.type.album_metadata import AlbumMetadata
from vimeo_python_sdk.type.album_privacy import AlbumPrivacy
from vimeo_python_sdk.type.album_seo_keywords import AlbumSeoKeywords
from vimeo_python_sdk.type.picture import Picture
from vimeo_python_sdk.type.user import User

class RequiredAlbum(TypedDict):
    # A brief description of the showcase's content.
    description: typing.Optional[str]

    # Whether the showcase permits continuous play.
    allow_continuous_play: bool

    # Whether the showcase permits downloads.
    allow_downloads: bool

    # Whether the showcase permits sharing.
    allow_share: bool

    # Whether to start playback of the next video in the showcase's embedded playlist immediately after the previous video finishes.
    autoplay: bool

    # The hexadecimal code for the color of the player buttons and showcase controls.
    brand_color: typing.Optional[str]

    # The time in ISO 8601 format when the showcase was created.
    created_time: str

    # The custom logo of the showcase.
    custom_logo: Picture

    # The custom domain of the showcase.
    domain: typing.Optional[str]

    # The state of the SSL certificate that is associated with the showcase's domain.  Option descriptions:  * `null` - There is no associated HTTPS domain with this showcase.  * `0` - The new certificate has yet to be processed.  * `1` - The new certificate is being processed in the queue.  * `2` - The certificate is being processed for renewal in the queue.  * `3` - The new certificate has failed to be issued in the queue.  * `4` - The certificate has failed to be renewed in the queue.  * `5` - The certificate has been successfully issued.  * `6` - The certificate has been successfully renewed.  * `7` - The certificate has failed in the polling flow.  * `8` - The certificate has failed to be renewed in the polling flow. 
    domain_certificate_state: str

    # The total duration in seconds of all the videos in the showcase.
    duration: typing.Union[int, float]

    embed: AlbumEmbed

    # Whether to show the showcase's custom brand color in the player of the showcase's embedded playlist.
    embed_brand_color: typing.Optional[bool]

    # Whether to show the showcase's custom logo in the player of the showcase's embedded playlist.
    embed_custom_logo: typing.Optional[bool]

    # Whether the showcase has a thumbnail.
    has_chosen_thumbnail: bool

    # Whether the showcase should be hidden from Vimeo when unlisted.
    hide_from_vimeo: bool

    # Whether to hide Vimeo navigation when displaying the showcase.
    hide_nav: bool

    # Whether to include the upcoming event in the showcase.
    hide_upcoming: bool

    # Whether to hide the Vimeo logo in the player of the showcase's embedded playlist.
    hide_vimeo_logo: typing.Optional[bool]

    # The type of layout for presenting the showcase.  Option descriptions:  * `grid` - The showcase videos appear in a grid.  * `player` - The showcase videos appear in the player. 
    layout: str

    # The URL of the showcase.
    link: str

    # Whether automatic playback restarts at the top of the showcase's embedded playlist after reaching the end of the last video in the playlist.
    loop: bool

    metadata: AlbumMetadata

    # The time in ISO 8601 format when the showcase was last modified.
    modified_time: str

    # The display name of the showcase.
    name: str

    # The active image of the showcase.
    pictures: Picture

    privacy: AlbumPrivacy

    # The resource key of the showcase.
    resource_key: str

    # Whether showcase videos use the review mode URL.
    review_mode: bool

    # Whether search engines can index the showcase.
    seo_allow_indexed: bool

    # The SEO description of the showcase.
    seo_description: typing.Optional[str]

    seo_keywords: AlbumSeoKeywords

    # The SEO title of the showcase.
    seo_title: typing.Optional[str]

    # The URL for sharing the showcase.
    share_link: str

    # The sort order of the showcase.  Option descriptions:  * `added_first` - Sort the showcase videos in order of those most recently added.  * `added_last` - Sort the showcase videos in order of those least recently added.  * `alphabetical` - Sort the showcase videos alphabetically.  * `arranged` - Sort the showcase videos according to their custom arrangement.  * `comments` - Sort the showcase videos by number of comments.  * `likes` - Sort the showcase videos by number of likes.  * `newest` - Sort the showcase videos in order of creation date with the newest first.  * `oldest` - Sort the showcase videos in order of creation date with the oldest first.  * `plays` - Sort the showcase videos by number of plays. 
    sort: str

    # The color theme of the showcase.  Option descriptions:  * `dark` - The showcase uses the dark theme.  * `standard` - The showcase uses the standard theme. 
    theme: str

    # The unlisted hash of the showcase. Omit this hash from the showcase URL to prevent access to the showcase on Vimeo.
    unlisted_hash: str

    # The URI of the showcase.
    uri: str

    # The custom Vimeo URL of the showcase.
    url: typing.Optional[str]

    # Whether the showcase uses a custom domain.
    use_custom_domain: bool

    # The owner of the showcase.
    user: User

    # Whether to use the showcase's brand color in the web layout.
    web_brand_color: bool

    # Whether to use the showcase's custom logo in the web layout.
    web_custom_logo: bool

class OptionalAlbum(TypedDict, total=False):
    pass

class Album(RequiredAlbum, OptionalAlbum):
    pass

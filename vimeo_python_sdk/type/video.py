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

from vimeo_python_sdk.type.api_app import ApiApp
from vimeo_python_sdk.type.category import Category
from vimeo_python_sdk.type.disabled_video_properties import DisabledVideoProperties
from vimeo_python_sdk.type.editing_session import EditingSession
from vimeo_python_sdk.type.embed_settings import EmbedSettings
from vimeo_python_sdk.type.picture import Picture
from vimeo_python_sdk.type.play import Play
from vimeo_python_sdk.type.project import Project
from vimeo_python_sdk.type.tag import Tag
from vimeo_python_sdk.type.user import User
from vimeo_python_sdk.type.version_transcode_status import VersionTranscodeStatus
from vimeo_python_sdk.type.video_allowed_privacies import VideoAllowedPrivacies
from vimeo_python_sdk.type.video_content_rating import VideoContentRating
from vimeo_python_sdk.type.video_context import VideoContext
from vimeo_python_sdk.type.video_file import VideoFile
from vimeo_python_sdk.type.video_metadata import VideoMetadata
from vimeo_python_sdk.type.video_privacy import VideoPrivacy
from vimeo_python_sdk.type.video_spatial import VideoSpatial
from vimeo_python_sdk.type.video_stats import VideoStats
from vimeo_python_sdk.type.video_transcode import VideoTranscode
from vimeo_python_sdk.type.video_transcript import VideoTranscript
from vimeo_python_sdk.type.video_upload import VideoUpload
from vimeo_python_sdk.type.video_uploader import VideoUploader
from vimeo_python_sdk.type.video_vod import VideoVod

class RequiredVideo(TypedDict):
    # An array of all tags assigned to the video.
    tags: typing.List[Tag]

    # A brief explanation of the video's content.
    description: typing.Optional[str]

    allowed_privacies: VideoAllowedPrivacies

    # The API application associated with the video owner's token.
    app: ApiApp

    # Whether the video can be moved to a folder. This data requires a bearer token with the `private` scope.
    can_move_to_project: typing.Optional[bool]

    # The categories that the video belongs to.
    categories: typing.List[Category]

    content_rating: VideoContentRating

    # The video's high-level content rating class.  Option descriptions:  * `explicit` - The video contains one or more explicit content rating types.  * `safe` - The video contains no explicit content rating types.  * `unrated` - The video doesn't belong to a content rating class. 
    content_rating_class: str

    context: VideoContext

    # The time in ISO 8601 format when the video was created.
    created_time: str

    # The custom URL of the video.
    custom_url: typing.Optional[str]

    # A brief explanation of the video's content, formatted with HTML entities.
    description_html: typing.Optional[str]

    # The list of downloadable files for the video. This data requires a bearer token with the `private` scope.
    download: typing.List[VideoFile]

    # The video's duration in seconds. A value of `0` indicates the duration hasn't been calculated yet.
    duration: typing.Union[int, float]

    # Information about embedding the video.
    embed: EmbedSettings

    # The list of files for the video. This data requires a bearer token with the `private` scope.
    files: typing.List[VideoFile]

    # Whether the video has audio.
    has_audio: bool

    # Whether the video has alternate audio tracks.
    has_audio_tracks: bool

    # Whether the video has chapters.
    has_chapters: bool

    # Whether the video has interactive capability.
    has_interactive: bool

    # Whether the video has text tracks.
    has_text_tracks: bool

    # The video's height in pixels.
    height: typing.Union[int, float]

    # Whether the video is privacy restricted due to a copyright infringement. This data requires a bearer token with the `private` scope.
    is_copyright_restricted: bool

    # Whether the video is playable.
    is_playable: bool

    # The video's primary language.
    language: typing.Optional[str]

    # The [Creative Commons](http://creativecommons.org/licenses/) license that the video is given under.  Option descriptions:  * `by` - The video is given under the Attribution license.  * `by-nc` - The video is given under the Attribution Non-Commercial license.  * `by-nc-nd` - The video is given under the Attribution Non-Commercial No Derivatives license.  * `by-nc-sa` - The video is given under the Attribution Non-Commercial Share Alike license.  * `by-nd` - The video is given under the Attribution No Derivatives license.  * `by-sa` - The video is given under the Attribution Share Alike license.  * `cc0` - The video is given under the Public Domain Dedication license. 
    license: str

    # The link to the video.
    link: str

    metadata: VideoMetadata

    # The time in ISO 8601 format when the video metadata was last modified.
    modified_time: str

    # The video's title.
    name: str

    # Whether the video has unified resolution. If the value of this field is `false`, the video requires transcoding.
    origin_variable_frame_resolution: bool

    # The video's active picture.
    pictures: Picture

    # The video's player embed URL.
    player_embed_url: str

    privacy: VideoPrivacy

    # Whether the video's content rating is locked by a mod.
    rating_mod_locked: bool

    # The time in ISO 8601 format when the video was released.
    release_time: str

    # The resource key string of the video.
    resource_key: str

    # Whether to show the `Review` button on single video view recipient pages. This data requires a bearer token with the `private` scope.
    show_review_page: typing.Optional[bool]

    # Whether to show the single video view footer banner on recipient pages. This data requires a bearer token with the `private` scope.
    show_svv_footer_banner: typing.Optional[bool]

    # Whether to enable timecoded comments on the single video view recipient page. This data requires a bearer token with the `private` scope.
    show_svv_timecoded_comments: typing.Optional[bool]

    spatial: VideoSpatial

    stats: VideoStats

    # The status code for the availability of the video.  Option descriptions:  * `available` - The video is available.  * `quota_exceeded` - The user's weekly upload quota is exceeded with this video.  * `total_cap_exceeded` - The user's total storage limit is exceeded with this video.  * `transcode_starting` - Transcoding is starting for the video.  * `transcoding` - Transcoding has started and is currently underway for the video.  * `transcoding_error` - There was an error in transcoding the video.  * `unavailable` - The video is unavailable.  * `uploading` - The video is being uploaded.  * `uploading_error` - There was an error in uploading the video. 
    status: typing.Optional[str]

    transcode: VideoTranscode

    transcript: VideoTranscript

    # The type of the video.  Option descriptions:  * `live` - The video is or was an event.  * `stock` - The video is a Vimeo Stock video.  * `video` - The video is a standard Vimeo video. 
    type: str

    upload: VideoUpload

    uploader: VideoUploader

    # The video's canonical relative URI.
    uri: str

    # The video's owner.
    user: User

    # Detailed transcode status information for the current version of the video upload.
    version_transcode_status: VersionTranscodeStatus

    vod: VideoVod

    # The video's width in pixels.
    width: typing.Union[int, float]

class OptionalVideo(TypedDict, total=False):
    # A JSON representation of the description.
    description_rich: str

    # Information about what features may be disabled on the video.
    disabled_properties: DisabledVideoProperties

    # Information about the video's Vimeo Create editing session. This data requires a bearer token with the `private` scope.
    edit_session: EditingSession

    # Whether the video is a free Vimeo Stock video.
    is_free: bool

    # The time in ISO 8601 format when the user last modified the video.
    last_user_action_event_date: typing.Optional[str]

    # The link to the video management page. This data requires a bearer token with the `private` scope.
    manage_link: str

    # Information about the folder that contains the video.
    parent_folder: Project

    # The privacy-enabled password to watch the video. Only the video's owner and team members with permission can access the video's password. This data requires a bearer token with the `private` scope.
    password: str

    # The `Play` representation.
    play: Play

class Video(RequiredVideo, OptionalVideo):
    pass

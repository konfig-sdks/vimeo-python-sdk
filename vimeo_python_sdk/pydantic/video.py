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

from vimeo_python_sdk.pydantic.api_app import ApiApp
from vimeo_python_sdk.pydantic.category import Category
from vimeo_python_sdk.pydantic.disabled_video_properties import DisabledVideoProperties
from vimeo_python_sdk.pydantic.editing_session import EditingSession
from vimeo_python_sdk.pydantic.embed_settings import EmbedSettings
from vimeo_python_sdk.pydantic.picture import Picture
from vimeo_python_sdk.pydantic.play import Play
from vimeo_python_sdk.pydantic.project import Project
from vimeo_python_sdk.pydantic.tag import Tag
from vimeo_python_sdk.pydantic.user import User
from vimeo_python_sdk.pydantic.version_transcode_status import VersionTranscodeStatus
from vimeo_python_sdk.pydantic.video_allowed_privacies import VideoAllowedPrivacies
from vimeo_python_sdk.pydantic.video_content_rating import VideoContentRating
from vimeo_python_sdk.pydantic.video_context import VideoContext
from vimeo_python_sdk.pydantic.video_file import VideoFile
from vimeo_python_sdk.pydantic.video_metadata import VideoMetadata
from vimeo_python_sdk.pydantic.video_privacy import VideoPrivacy
from vimeo_python_sdk.pydantic.video_spatial import VideoSpatial
from vimeo_python_sdk.pydantic.video_stats import VideoStats
from vimeo_python_sdk.pydantic.video_transcode import VideoTranscode
from vimeo_python_sdk.pydantic.video_transcript import VideoTranscript
from vimeo_python_sdk.pydantic.video_upload import VideoUpload
from vimeo_python_sdk.pydantic.video_uploader import VideoUploader
from vimeo_python_sdk.pydantic.video_vod import VideoVod

class Video(BaseModel):
    # An array of all tags assigned to the video.
    tags: typing.List[Tag] = Field(alias='tags')

    # A brief explanation of the video's content.
    description: typing.Optional[str] = Field(alias='description')

    allowed_privacies: VideoAllowedPrivacies = Field(alias='allowed_privacies')

    # The API application associated with the video owner's token.
    app: ApiApp = Field(alias='app')

    # Whether the video can be moved to a folder. This data requires a bearer token with the `private` scope.
    can_move_to_project: typing.Optional[bool] = Field(alias='can_move_to_project')

    # The categories that the video belongs to.
    categories: typing.List[Category] = Field(alias='categories')

    content_rating: VideoContentRating = Field(alias='content_rating')

    # The video's high-level content rating class.  Option descriptions:  * `explicit` - The video contains one or more explicit content rating types.  * `safe` - The video contains no explicit content rating types.  * `unrated` - The video doesn't belong to a content rating class. 
    content_rating_class: Literal["explicit", "safe", "unrated"] = Field(alias='content_rating_class')

    context: VideoContext = Field(alias='context')

    # The time in ISO 8601 format when the video was created.
    created_time: str = Field(alias='created_time')

    # The custom URL of the video.
    custom_url: typing.Optional[str] = Field(alias='custom_url')

    # A brief explanation of the video's content, formatted with HTML entities.
    description_html: typing.Optional[str] = Field(alias='description_html')

    # The list of downloadable files for the video. This data requires a bearer token with the `private` scope.
    download: typing.List[VideoFile] = Field(alias='download')

    # The video's duration in seconds. A value of `0` indicates the duration hasn't been calculated yet.
    duration: typing.Union[int, float] = Field(alias='duration')

    # Information about embedding the video.
    embed: EmbedSettings = Field(alias='embed')

    # The list of files for the video. This data requires a bearer token with the `private` scope.
    files: typing.List[VideoFile] = Field(alias='files')

    # Whether the video has audio.
    has_audio: bool = Field(alias='has_audio')

    # Whether the video has alternate audio tracks.
    has_audio_tracks: bool = Field(alias='has_audio_tracks')

    # Whether the video has chapters.
    has_chapters: bool = Field(alias='has_chapters')

    # Whether the video has interactive capability.
    has_interactive: bool = Field(alias='has_interactive')

    # Whether the video has text tracks.
    has_text_tracks: bool = Field(alias='has_text_tracks')

    # The video's height in pixels.
    height: typing.Union[int, float] = Field(alias='height')

    # Whether the video is privacy restricted due to a copyright infringement. This data requires a bearer token with the `private` scope.
    is_copyright_restricted: bool = Field(alias='is_copyright_restricted')

    # Whether the video is playable.
    is_playable: bool = Field(alias='is_playable')

    # The video's primary language.
    language: typing.Optional[str] = Field(alias='language')

    # The [Creative Commons](http://creativecommons.org/licenses/) license that the video is given under.  Option descriptions:  * `by` - The video is given under the Attribution license.  * `by-nc` - The video is given under the Attribution Non-Commercial license.  * `by-nc-nd` - The video is given under the Attribution Non-Commercial No Derivatives license.  * `by-nc-sa` - The video is given under the Attribution Non-Commercial Share Alike license.  * `by-nd` - The video is given under the Attribution No Derivatives license.  * `by-sa` - The video is given under the Attribution Share Alike license.  * `cc0` - The video is given under the Public Domain Dedication license. 
    license: Literal["by", "by-nc", "by-nc-nd", "by-nc-sa", "by-nd", "by-sa", "cc0"] = Field(alias='license')

    # The link to the video.
    link: str = Field(alias='link')

    metadata: VideoMetadata = Field(alias='metadata')

    # The time in ISO 8601 format when the video metadata was last modified.
    modified_time: str = Field(alias='modified_time')

    # The video's title.
    name: str = Field(alias='name')

    # Whether the video has unified resolution. If the value of this field is `false`, the video requires transcoding.
    origin_variable_frame_resolution: bool = Field(alias='origin_variable_frame_resolution')

    # The video's active picture.
    pictures: Picture = Field(alias='pictures')

    # The video's player embed URL.
    player_embed_url: str = Field(alias='player_embed_url')

    privacy: VideoPrivacy = Field(alias='privacy')

    # Whether the video's content rating is locked by a mod.
    rating_mod_locked: bool = Field(alias='rating_mod_locked')

    # The time in ISO 8601 format when the video was released.
    release_time: str = Field(alias='release_time')

    # The resource key string of the video.
    resource_key: str = Field(alias='resource_key')

    # Whether to show the `Review` button on single video view recipient pages. This data requires a bearer token with the `private` scope.
    show_review_page: typing.Optional[bool] = Field(alias='show_review_page')

    # Whether to show the single video view footer banner on recipient pages. This data requires a bearer token with the `private` scope.
    show_svv_footer_banner: typing.Optional[bool] = Field(alias='show_svv_footer_banner')

    # Whether to enable timecoded comments on the single video view recipient page. This data requires a bearer token with the `private` scope.
    show_svv_timecoded_comments: typing.Optional[bool] = Field(alias='show_svv_timecoded_comments')

    spatial: VideoSpatial = Field(alias='spatial')

    stats: VideoStats = Field(alias='stats')

    # The status code for the availability of the video.  Option descriptions:  * `available` - The video is available.  * `quota_exceeded` - The user's weekly upload quota is exceeded with this video.  * `total_cap_exceeded` - The user's total storage limit is exceeded with this video.  * `transcode_starting` - Transcoding is starting for the video.  * `transcoding` - Transcoding has started and is currently underway for the video.  * `transcoding_error` - There was an error in transcoding the video.  * `unavailable` - The video is unavailable.  * `uploading` - The video is being uploaded.  * `uploading_error` - There was an error in uploading the video. 
    status: Literal["available", "quota_exceeded", "total_cap_exceeded", "transcode_starting", "transcoding", "transcoding_error", "unavailable", "uploading", "uploading_error"] = Field(alias='status')

    transcode: VideoTranscode = Field(alias='transcode')

    transcript: VideoTranscript = Field(alias='transcript')

    # The type of the video.  Option descriptions:  * `live` - The video is or was an event.  * `stock` - The video is a Vimeo Stock video.  * `video` - The video is a standard Vimeo video. 
    type: Literal["live", "stock", "video"] = Field(alias='type')

    upload: VideoUpload = Field(alias='upload')

    uploader: VideoUploader = Field(alias='uploader')

    # The video's canonical relative URI.
    uri: str = Field(alias='uri')

    # The video's owner.
    user: User = Field(alias='user')

    # Detailed transcode status information for the current version of the video upload.
    version_transcode_status: VersionTranscodeStatus = Field(alias='version_transcode_status')

    vod: VideoVod = Field(alias='vod')

    # The video's width in pixels.
    width: typing.Union[int, float] = Field(alias='width')

    # A JSON representation of the description.
    description_rich: typing.Optional[str] = Field(None, alias='description_rich')

    # Information about what features may be disabled on the video.
    disabled_properties: typing.Optional[DisabledVideoProperties] = Field(None, alias='disabled_properties')

    # Information about the video's Vimeo Create editing session. This data requires a bearer token with the `private` scope.
    edit_session: typing.Optional[EditingSession] = Field(None, alias='edit_session')

    # Whether the video is a free Vimeo Stock video.
    is_free: typing.Optional[bool] = Field(None, alias='is_free')

    # The time in ISO 8601 format when the user last modified the video.
    last_user_action_event_date: typing.Optional[typing.Optional[str]] = Field(None, alias='last_user_action_event_date')

    # The link to the video management page. This data requires a bearer token with the `private` scope.
    manage_link: typing.Optional[str] = Field(None, alias='manage_link')

    # Information about the folder that contains the video.
    parent_folder: typing.Optional[Project] = Field(None, alias='parent_folder')

    # The privacy-enabled password to watch the video. Only the video's owner and team members with permission can access the video's password. This data requires a bearer token with the `private` scope.
    password: typing.Optional[str] = Field(None, alias='password')

    # The `Play` representation.
    play: typing.Optional[Play] = Field(None, alias='play')
    class Config:
        arbitrary_types_allowed = True

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

from vimeo_python_sdk.pydantic.video_metadata_interactions_album import VideoMetadataInteractionsAlbum
from vimeo_python_sdk.pydantic.video_metadata_interactions_ask_ai import VideoMetadataInteractionsAskAi
from vimeo_python_sdk.pydantic.video_metadata_interactions_ask_ai_viewer import VideoMetadataInteractionsAskAiViewer
from vimeo_python_sdk.pydantic.video_metadata_interactions_buy import VideoMetadataInteractionsBuy
from vimeo_python_sdk.pydantic.video_metadata_interactions_can_request_team_role_upgrade import VideoMetadataInteractionsCanRequestTeamRoleUpgrade
from vimeo_python_sdk.pydantic.video_metadata_interactions_can_update_privacy_to_public import VideoMetadataInteractionsCanUpdatePrivacyToPublic
from vimeo_python_sdk.pydantic.video_metadata_interactions_channel import VideoMetadataInteractionsChannel
from vimeo_python_sdk.pydantic.video_metadata_interactions_create_editor import VideoMetadataInteractionsCreateEditor
from vimeo_python_sdk.pydantic.video_metadata_interactions_delete import VideoMetadataInteractionsDelete
from vimeo_python_sdk.pydantic.video_metadata_interactions_edit import VideoMetadataInteractionsEdit
from vimeo_python_sdk.pydantic.video_metadata_interactions_edit_privacy import VideoMetadataInteractionsEditPrivacy
from vimeo_python_sdk.pydantic.video_metadata_interactions_has_restricted_privacy_options import VideoMetadataInteractionsHasRestrictedPrivacyOptions
from vimeo_python_sdk.pydantic.video_metadata_interactions_highlights import VideoMetadataInteractionsHighlights
from vimeo_python_sdk.pydantic.video_metadata_interactions_invite import VideoMetadataInteractionsInvite
from vimeo_python_sdk.pydantic.video_metadata_interactions_legal_hold import VideoMetadataInteractionsLegalHold
from vimeo_python_sdk.pydantic.video_metadata_interactions_like import VideoMetadataInteractionsLike
from vimeo_python_sdk.pydantic.video_metadata_interactions_rent import VideoMetadataInteractionsRent
from vimeo_python_sdk.pydantic.video_metadata_interactions_report import VideoMetadataInteractionsReport
from vimeo_python_sdk.pydantic.video_metadata_interactions_set_content_rating import VideoMetadataInteractionsSetContentRating
from vimeo_python_sdk.pydantic.video_metadata_interactions_subscribe import VideoMetadataInteractionsSubscribe
from vimeo_python_sdk.pydantic.video_metadata_interactions_summary import VideoMetadataInteractionsSummary
from vimeo_python_sdk.pydantic.video_metadata_interactions_team_mentions import VideoMetadataInteractionsTeamMentions
from vimeo_python_sdk.pydantic.video_metadata_interactions_transcript_video_editor import VideoMetadataInteractionsTranscriptVideoEditor
from vimeo_python_sdk.pydantic.video_metadata_interactions_trim import VideoMetadataInteractionsTrim
from vimeo_python_sdk.pydantic.video_metadata_interactions_validate import VideoMetadataInteractionsValidate
from vimeo_python_sdk.pydantic.video_metadata_interactions_view_privacy import VideoMetadataInteractionsViewPrivacy
from vimeo_python_sdk.pydantic.video_metadata_interactions_view_team_members import VideoMetadataInteractionsViewTeamMembers
from vimeo_python_sdk.pydantic.video_metadata_interactions_watched import VideoMetadataInteractionsWatched
from vimeo_python_sdk.pydantic.video_metadata_interactions_watchlater import VideoMetadataInteractionsWatchlater

class VideoMetadataInteractions(BaseModel):
    summary: VideoMetadataInteractionsSummary = Field(alias='summary')

    album: VideoMetadataInteractionsAlbum = Field(alias='album')

    ask_ai: VideoMetadataInteractionsAskAi = Field(alias='ask_ai')

    ask_ai_viewer: VideoMetadataInteractionsAskAiViewer = Field(alias='ask_ai_viewer')

    buy: VideoMetadataInteractionsBuy = Field(alias='buy')

    can_request_team_role_upgrade: VideoMetadataInteractionsCanRequestTeamRoleUpgrade = Field(alias='can_request_team_role_upgrade')

    can_update_privacy_to_public: VideoMetadataInteractionsCanUpdatePrivacyToPublic = Field(alias='can_update_privacy_to_public')

    channel: VideoMetadataInteractionsChannel = Field(alias='channel')

    create_editor: VideoMetadataInteractionsCreateEditor = Field(alias='create_editor')

    delete: VideoMetadataInteractionsDelete = Field(alias='delete')

    edit: VideoMetadataInteractionsEdit = Field(alias='edit')

    edit_privacy: VideoMetadataInteractionsEditPrivacy = Field(alias='edit_privacy')

    has_restricted_privacy_options: VideoMetadataInteractionsHasRestrictedPrivacyOptions = Field(alias='has_restricted_privacy_options')

    highlights: VideoMetadataInteractionsHighlights = Field(alias='highlights')

    invite: VideoMetadataInteractionsInvite = Field(alias='invite')

    legal_hold: VideoMetadataInteractionsLegalHold = Field(alias='legal_hold')

    like: VideoMetadataInteractionsLike = Field(alias='like')

    rent: VideoMetadataInteractionsRent = Field(alias='rent')

    report: VideoMetadataInteractionsReport = Field(alias='report')

    set_content_rating: VideoMetadataInteractionsSetContentRating = Field(alias='set_content_rating')

    team_mentions: VideoMetadataInteractionsTeamMentions = Field(alias='team_mentions')

    transcript_video_editor: VideoMetadataInteractionsTranscriptVideoEditor = Field(alias='transcript_video_editor')

    trim: VideoMetadataInteractionsTrim = Field(alias='trim')

    validate: VideoMetadataInteractionsValidate = Field(alias='validate')

    view_privacy: VideoMetadataInteractionsViewPrivacy = Field(alias='view_privacy')

    view_team_members: VideoMetadataInteractionsViewTeamMembers = Field(alias='view_team_members')

    watched: VideoMetadataInteractionsWatched = Field(alias='watched')

    watchlater: VideoMetadataInteractionsWatchlater = Field(alias='watchlater')

    subscribe: typing.Optional[VideoMetadataInteractionsSubscribe] = Field(None, alias='subscribe')
    class Config:
        arbitrary_types_allowed = True

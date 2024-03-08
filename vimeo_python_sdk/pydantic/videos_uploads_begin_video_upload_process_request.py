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

from vimeo_python_sdk.pydantic.videos_uploads_begin_video_upload_process_request_content_rating import VideosUploadsBeginVideoUploadProcessRequestContentRating
from vimeo_python_sdk.pydantic.videos_uploads_begin_video_upload_process_request_embed import VideosUploadsBeginVideoUploadProcessRequestEmbed
from vimeo_python_sdk.pydantic.videos_uploads_begin_video_upload_process_request_embed_domains import VideosUploadsBeginVideoUploadProcessRequestEmbedDomains
from vimeo_python_sdk.pydantic.videos_uploads_begin_video_upload_process_request_privacy import VideosUploadsBeginVideoUploadProcessRequestPrivacy
from vimeo_python_sdk.pydantic.videos_uploads_begin_video_upload_process_request_review_page import VideosUploadsBeginVideoUploadProcessRequestReviewPage
from vimeo_python_sdk.pydantic.videos_uploads_begin_video_upload_process_request_spatial import VideosUploadsBeginVideoUploadProcessRequestSpatial
from vimeo_python_sdk.pydantic.videos_uploads_begin_video_upload_process_request_upload import VideosUploadsBeginVideoUploadProcessRequestUpload

class VideosUploadsBeginVideoUploadProcessRequest(BaseModel):
    upload: VideosUploadsBeginVideoUploadProcessRequestUpload = Field(alias='upload')

    # The description of the video.
    description: typing.Optional[str] = Field(None, alias='description')

    content_rating: typing.Optional[VideosUploadsBeginVideoUploadProcessRequestContentRating] = Field(None, alias='content_rating')

    embed: typing.Optional[VideosUploadsBeginVideoUploadProcessRequestEmbed] = Field(None, alias='embed')

    embed_domains: typing.Optional[VideosUploadsBeginVideoUploadProcessRequestEmbedDomains] = Field(None, alias='embed_domains')

    # The URI of the folder to which the video is uploaded.
    folder_uri: typing.Optional[str] = Field(None, alias='folder_uri')

    # Whether to hide the video from everyone except the video's owner. When the value is `true`, unlisted video links work only for the video's owner.
    hide_from_vimeo: typing.Optional[bool] = Field(None, alias='hide_from_vimeo')

    # The Creative Commons license under which the video is offered.  Option descriptions:  * `by` - The video is offered under CC BY, or the attibution-only license.  * `by-nc` - The video is offered under CC BY-NC, or the Attribution-NonCommercial license.  * `by-nc-nd` - The video is offered under CC BY-NC-ND, or the Attribution-NonCommercian-NoDerivs license.  * `by-nc-sa` - The video is offered under CC BY-NC-SA, or the Attribution-NonCommercial-ShareAlike licence.  * `by-nd` - The video is offered under CC BY-ND, or the Attribution-NoDerivs license.  * `by-sa` - The video is offered under CC BY-SA, or the Attribution-ShareAlike license.  * `cc0` - The video is offered under CC0, or the public domain license. 
    license: typing.Optional[Literal["by", "by-nc", "by-nc-nd", "by-nc-sa", "by-nd", "by-sa", "cc0"]] = Field(None, alias='license')

    # The video's default language. For a full list of supported languages, use the [`/languages?filter=texttracks`](https://developer.vimeo.com/api/reference/videos#get_languages) endpoint.
    locale: typing.Optional[str] = Field(None, alias='locale')

    # The title of the video.
    name: typing.Optional[str] = Field(None, alias='name')

    # The password. This field is required when **privacy.view** is `password`.
    password: typing.Optional[str] = Field(None, alias='password')

    privacy: typing.Optional[VideosUploadsBeginVideoUploadProcessRequestPrivacy] = Field(None, alias='privacy')

    review_page: typing.Optional[VideosUploadsBeginVideoUploadProcessRequestReviewPage] = Field(None, alias='review_page')

    spatial: typing.Optional[VideosUploadsBeginVideoUploadProcessRequestSpatial] = Field(None, alias='spatial')
    class Config:
        arbitrary_types_allowed = True

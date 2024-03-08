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

from vimeo_python_sdk.type.videos_uploads_begin_video_upload_process_request_content_rating import VideosUploadsBeginVideoUploadProcessRequestContentRating
from vimeo_python_sdk.type.videos_uploads_begin_video_upload_process_request_embed import VideosUploadsBeginVideoUploadProcessRequestEmbed
from vimeo_python_sdk.type.videos_uploads_begin_video_upload_process_request_embed_domains import VideosUploadsBeginVideoUploadProcessRequestEmbedDomains
from vimeo_python_sdk.type.videos_uploads_begin_video_upload_process_request_privacy import VideosUploadsBeginVideoUploadProcessRequestPrivacy
from vimeo_python_sdk.type.videos_uploads_begin_video_upload_process_request_review_page import VideosUploadsBeginVideoUploadProcessRequestReviewPage
from vimeo_python_sdk.type.videos_uploads_begin_video_upload_process_request_spatial import VideosUploadsBeginVideoUploadProcessRequestSpatial
from vimeo_python_sdk.type.videos_uploads_begin_video_upload_process_request_upload import VideosUploadsBeginVideoUploadProcessRequestUpload

class RequiredVideosUploadsBeginVideoUploadProcessRequest(TypedDict):
    upload: VideosUploadsBeginVideoUploadProcessRequestUpload

class OptionalVideosUploadsBeginVideoUploadProcessRequest(TypedDict, total=False):
    # The description of the video.
    description: str

    content_rating: VideosUploadsBeginVideoUploadProcessRequestContentRating

    embed: VideosUploadsBeginVideoUploadProcessRequestEmbed

    embed_domains: VideosUploadsBeginVideoUploadProcessRequestEmbedDomains

    # The URI of the folder to which the video is uploaded.
    folder_uri: str

    # Whether to hide the video from everyone except the video's owner. When the value is `true`, unlisted video links work only for the video's owner.
    hide_from_vimeo: bool

    # The Creative Commons license under which the video is offered.  Option descriptions:  * `by` - The video is offered under CC BY, or the attibution-only license.  * `by-nc` - The video is offered under CC BY-NC, or the Attribution-NonCommercial license.  * `by-nc-nd` - The video is offered under CC BY-NC-ND, or the Attribution-NonCommercian-NoDerivs license.  * `by-nc-sa` - The video is offered under CC BY-NC-SA, or the Attribution-NonCommercial-ShareAlike licence.  * `by-nd` - The video is offered under CC BY-ND, or the Attribution-NoDerivs license.  * `by-sa` - The video is offered under CC BY-SA, or the Attribution-ShareAlike license.  * `cc0` - The video is offered under CC0, or the public domain license. 
    license: str

    # The video's default language. For a full list of supported languages, use the [`/languages?filter=texttracks`](https://developer.vimeo.com/api/reference/videos#get_languages) endpoint.
    locale: str

    # The title of the video.
    name: str

    # The password. This field is required when **privacy.view** is `password`.
    password: str

    privacy: VideosUploadsBeginVideoUploadProcessRequestPrivacy

    review_page: VideosUploadsBeginVideoUploadProcessRequestReviewPage

    spatial: VideosUploadsBeginVideoUploadProcessRequestSpatial

class VideosUploadsBeginVideoUploadProcessRequest(RequiredVideosUploadsBeginVideoUploadProcessRequest, OptionalVideosUploadsBeginVideoUploadProcessRequest):
    pass

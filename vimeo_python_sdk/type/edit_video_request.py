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

from vimeo_python_sdk.type.edit_video_request_content_rating import EditVideoRequestContentRating
from vimeo_python_sdk.type.edit_video_request_embed import EditVideoRequestEmbed
from vimeo_python_sdk.type.edit_video_request_embed_domains import EditVideoRequestEmbedDomains
from vimeo_python_sdk.type.edit_video_request_embed_domains_add import EditVideoRequestEmbedDomainsAdd
from vimeo_python_sdk.type.edit_video_request_embed_domains_delete import EditVideoRequestEmbedDomainsDelete
from vimeo_python_sdk.type.edit_video_request_privacy import EditVideoRequestPrivacy
from vimeo_python_sdk.type.edit_video_request_review_page import EditVideoRequestReviewPage
from vimeo_python_sdk.type.edit_video_request_spatial import EditVideoRequestSpatial

class RequiredEditVideoRequest(TypedDict):
    pass

class OptionalEditVideoRequest(TypedDict, total=False):
    # The description of the video. This field can hold a maximum of 5000 characters.
    description: str

    content_rating: EditVideoRequestContentRating

    # The custom link of the video. This link doesn't include the base URL and the username or user ID of the video's owner.
    custom_url: str

    embed: EditVideoRequestEmbed

    embed_domains: EditVideoRequestEmbedDomains

    embed_domains_add: EditVideoRequestEmbedDomainsAdd

    embed_domains_delete: EditVideoRequestEmbedDomainsDelete

    # Whether to hide the video from everyone except the video's owner. When the value is `true`, unlisted video links work only for the video's owner.
    hide_from_vimeo: bool

    # The Creative Commons license under which the video is offered.  Option descriptions:  * `by` - The video is offered under CC BY, or the attibution-only license.  * `by-nc` - The video is offered under CC BY-NC, or the Attribution-NonCommercial license.  * `by-nc-nd` - The video is offered under CC BY-NC-ND, or the Attribution-NonCommercian-NoDerivs license.  * `by-nc-sa` - The video is offered under CC BY-NC-SA, or the Attribution-NonCommercial-ShareAlike licence.  * `by-nd` - The video is offered under CC BY-ND, or the Attribution-NoDerivs license.  * `by-sa` - The video is offered under CC BY-SA, or the Attribution-ShareAlike license.  * `cc0` - The video is offered under CC0, or public domain, videos. 
    license: str

    # The video's default language. For a full list of supported languages, use the [`/languages?filter=texttracks`](https://developer.vimeo.com/api/reference/videos#get_languages) endpoint.
    locale: str

    # The title of the video. This field can hold a maximum of 128 characters.
    name: str

    # The password. When you set **privacy.view** to `password`, you must provide the password as an additional parameter. This field can hold a maximum of 32 characters.
    password: str

    privacy: EditVideoRequestPrivacy

    review_page: EditVideoRequestReviewPage

    spatial: EditVideoRequestSpatial

class EditVideoRequest(RequiredEditVideoRequest, OptionalEditVideoRequest):
    pass

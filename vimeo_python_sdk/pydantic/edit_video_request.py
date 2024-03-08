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

from vimeo_python_sdk.pydantic.edit_video_request_content_rating import EditVideoRequestContentRating
from vimeo_python_sdk.pydantic.edit_video_request_embed import EditVideoRequestEmbed
from vimeo_python_sdk.pydantic.edit_video_request_embed_domains import EditVideoRequestEmbedDomains
from vimeo_python_sdk.pydantic.edit_video_request_embed_domains_add import EditVideoRequestEmbedDomainsAdd
from vimeo_python_sdk.pydantic.edit_video_request_embed_domains_delete import EditVideoRequestEmbedDomainsDelete
from vimeo_python_sdk.pydantic.edit_video_request_privacy import EditVideoRequestPrivacy
from vimeo_python_sdk.pydantic.edit_video_request_review_page import EditVideoRequestReviewPage
from vimeo_python_sdk.pydantic.edit_video_request_spatial import EditVideoRequestSpatial

class EditVideoRequest(BaseModel):
    # The description of the video. This field can hold a maximum of 5000 characters.
    description: typing.Optional[str] = Field(None, alias='description')

    content_rating: typing.Optional[EditVideoRequestContentRating] = Field(None, alias='content_rating')

    # The custom link of the video. This link doesn't include the base URL and the username or user ID of the video's owner.
    custom_url: typing.Optional[str] = Field(None, alias='custom_url')

    embed: typing.Optional[EditVideoRequestEmbed] = Field(None, alias='embed')

    embed_domains: typing.Optional[EditVideoRequestEmbedDomains] = Field(None, alias='embed_domains')

    embed_domains_add: typing.Optional[EditVideoRequestEmbedDomainsAdd] = Field(None, alias='embed_domains_add')

    embed_domains_delete: typing.Optional[EditVideoRequestEmbedDomainsDelete] = Field(None, alias='embed_domains_delete')

    # Whether to hide the video from everyone except the video's owner. When the value is `true`, unlisted video links work only for the video's owner.
    hide_from_vimeo: typing.Optional[bool] = Field(None, alias='hide_from_vimeo')

    # The Creative Commons license under which the video is offered.  Option descriptions:  * `by` - The video is offered under CC BY, or the attibution-only license.  * `by-nc` - The video is offered under CC BY-NC, or the Attribution-NonCommercial license.  * `by-nc-nd` - The video is offered under CC BY-NC-ND, or the Attribution-NonCommercian-NoDerivs license.  * `by-nc-sa` - The video is offered under CC BY-NC-SA, or the Attribution-NonCommercial-ShareAlike licence.  * `by-nd` - The video is offered under CC BY-ND, or the Attribution-NoDerivs license.  * `by-sa` - The video is offered under CC BY-SA, or the Attribution-ShareAlike license.  * `cc0` - The video is offered under CC0, or public domain, videos. 
    license: typing.Optional[Literal["by", "by-nc", "by-nc-nd", "by-nc-sa", "by-nd", "by-sa", "cc0"]] = Field(None, alias='license')

    # The video's default language. For a full list of supported languages, use the [`/languages?filter=texttracks`](https://developer.vimeo.com/api/reference/videos#get_languages) endpoint.
    locale: typing.Optional[str] = Field(None, alias='locale')

    # The title of the video. This field can hold a maximum of 128 characters.
    name: typing.Optional[str] = Field(None, alias='name')

    # The password. When you set **privacy.view** to `password`, you must provide the password as an additional parameter. This field can hold a maximum of 32 characters.
    password: typing.Optional[str] = Field(None, alias='password')

    privacy: typing.Optional[EditVideoRequestPrivacy] = Field(None, alias='privacy')

    review_page: typing.Optional[EditVideoRequestReviewPage] = Field(None, alias='review_page')

    spatial: typing.Optional[EditVideoRequestSpatial] = Field(None, alias='spatial')
    class Config:
        arbitrary_types_allowed = True

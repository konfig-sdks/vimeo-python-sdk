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


class RequiredVideoPrivacy(TypedDict):
    # Whether the video can be added to collections.
    add: bool

    # Whether the share link is usable.
    allow_share_link: bool

    # The video's comment permission setting.  Option descriptions:  * `anybody` - Anyone can comment on the video.  * `contacts` - Only contacts can comment on the video.  * `nobody` - No one can comment on the video. 
    comments: str

    # Whether the video can be downloaded.
    download: bool

    # The video's embed permission setting.  Option descriptions:  * `private` - The video is private.  * `public` - Anyone can embed the video.  * `whitelist` - The video can be embedded on specific domains. 
    embed: str

    # The general privacy setting of the video.  Option descriptions:  * `anybody` - Anyone can access the video. This privacy setting appears as `Public` on the Vimeo front end.  * `contacts` - Only contacts can access the video. _This field is deprecated._  * `disable` - The video is hidden from Vimeo. This privacy setting appears as `Hide from Vimeo` on the Vimeo front end.  * `nobody` - No one besides the owner can access the video. This privacy setting appears as `Private` on the Vimeo front end.  * `password` - Anyone with the video's password can access the video.  * `ptv` - The Vimeo On Demand video is accessible and searchable from Vimeo. _This field is deprecated._  * `ptvhide` - The Vimeo On Demand video is hidden from Vimeo. _This field is deprecated._  * `stock` - The stock footage is accessible and searchable from Vimeo. _This field is deprecated._  * `stock_purchased` - The purchased stock footage is accessible and searchable from Vimeo. _This field is deprecated._  * `unlisted` - The video is accessible but not searchable from Vimeo.  * `users` - Only Vimeo members can access the video. _This field is deprecated._ 
    view: str

class OptionalVideoPrivacy(TypedDict, total=False):
    pass

class VideoPrivacy(RequiredVideoPrivacy, OptionalVideoPrivacy):
    pass
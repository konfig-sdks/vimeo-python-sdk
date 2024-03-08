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


class RequiredLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1StreamPrivacy(TypedDict):
    pass

class OptionalLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1StreamPrivacy(TypedDict, total=False):
    # The initial privacy of the videos generated by streaming to the event as well as the embed privacy of the entire collection.  Option descriptions:  * `anybody` - Anyone can access the event. This privacy setting appears as `Public` on the Vimeo front end.  * `embed_only` - The event doesn't appear on Vimeo, but it can be embedded on other sites.  * `nobody` - No one except the owner can access the event. This privacy setting appears as `Private` on the Vimeo front end.  * `password` - Only those with the password can access the event.  * `unlisted` - Only those with the private link can access the event. 
    view: str

class LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1StreamPrivacy(RequiredLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1StreamPrivacy, OptionalLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1StreamPrivacy):
    pass

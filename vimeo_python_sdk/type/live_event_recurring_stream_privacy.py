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


class RequiredLiveEventRecurringStreamPrivacy(TypedDict):
    # The event's embed permission setting.  Option descriptions:  * `private` - The event can't be embedded on any domain.  * `public` - The event can be embedded on any domain.  * `whitelist` - The event can be embedded on whitelisted domains only. 
    embed: str

    # The hash for unlisted events.
    unlisted_hash: typing.Optional[str]

    # The general privacy setting for generated videos and the embed privacy of the entire collection.  Option descriptions:  * `anybody` - Anyone can access the videos. This privacy setting appears as `Public` on the Vimeo front end.  * `embed_only` - The videos don't appear on Vimeo, but they can be embedded elsewhere.  * `nobody` - Only the event owner can access the videos. This privacy setting appears as `Private` on the Vimeo front end.  * `password` - Only those with the password can access the videos.  * `unlisted` - Only those with the private link can access the videos. 
    view: str

class OptionalLiveEventRecurringStreamPrivacy(TypedDict, total=False):
    pass

class LiveEventRecurringStreamPrivacy(RequiredLiveEventRecurringStreamPrivacy, OptionalLiveEventRecurringStreamPrivacy):
    pass

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


class RequiredCreateWebinarRequestPrivacy(TypedDict):
    pass

class OptionalCreateWebinarRequestPrivacy(TypedDict, total=False):
    # The initial embed privacy of the webinar.  Option descriptions:  * `private` - The webinar can't be embedded on any domain.  * `public` - The webinar can be embedded on any domain.  * `whitelist` - The webinar can be embedded on whitelisted domains only. 
    embed: str

    # The initial privacy of the webinar.  Option descriptions:  * `anybody` - Anyone can access the webinar. This privacy setting appears as `Public` on the Vimeo front end.  * `nobody` - No one except the owner can access the webinar. This privacy setting appears as `Private` on the Vimeo front end.  * `password` - Only those with the password can access the event.  * `team` - Only members of the authenticated user's team can access the webinar. 
    view: str

class CreateWebinarRequestPrivacy(RequiredCreateWebinarRequestPrivacy, OptionalCreateWebinarRequestPrivacy):
    pass

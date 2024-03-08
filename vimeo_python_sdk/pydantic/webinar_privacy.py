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


class WebinarPrivacy(BaseModel):
    # The webinar's embed permission setting.  Option descriptions:  * `private` - The webinar can't be embedded on any domain.  * `public` - The webinar can be embedded on any domain.  * `whitelist` - The webinar can be embedded on whitelisted domains only. 
    embed: Literal["private", "public", "whitelist"] = Field(alias='embed')

    # The general privacy setting for the webinar.  Option descriptions:  * `anybody` - Anyone can access the webinar. This privacy setting appears as `Public` on the Vimeo front end.  * `nobody` - Only the event owner can access the webinar. This privacy setting appears as `Private` on the Vimeo front end.  * `password` - Only those with the password can access the live event.  * `team` - Only members of the authenticated user's team can access the webinar. 
    view: Literal["anybody", "nobody", "password", "team"] = Field(alias='view')
    class Config:
        arbitrary_types_allowed = True

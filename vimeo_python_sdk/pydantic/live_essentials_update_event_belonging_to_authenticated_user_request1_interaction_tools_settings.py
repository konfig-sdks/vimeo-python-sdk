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


class LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1InteractionToolsSettings(BaseModel):
    # Whether anonymous questions are disabled for the interaction tools settings.
    is_anonymous_questions_disabled: typing.Optional[bool] = Field(None, alias='is_anonymous_questions_disabled')

    # Whether the Q&A is moderated for the interaction tools settings.
    is_qna_moderated: typing.Optional[bool] = Field(None, alias='is_qna_moderated')
    class Config:
        arbitrary_types_allowed = True

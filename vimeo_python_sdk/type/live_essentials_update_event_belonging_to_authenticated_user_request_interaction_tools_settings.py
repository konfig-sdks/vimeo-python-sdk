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


class RequiredLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings(TypedDict):
    pass

class OptionalLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings(TypedDict, total=False):
    # Whether anonymous questions are disabled for the interaction tools settings.
    is_anonymous_questions_disabled: bool

    # Whether the Q&A is moderated for the interaction tools settings.
    is_qna_moderated: bool

class LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings(RequiredLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings, OptionalLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings):
    pass

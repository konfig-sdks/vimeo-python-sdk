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

from vimeo_python_sdk.type.user_metadata_interactions_add_privacy_user import UserMetadataInteractionsAddPrivacyUser
from vimeo_python_sdk.type.user_metadata_interactions_block import UserMetadataInteractionsBlock
from vimeo_python_sdk.type.user_metadata_interactions_connected_apps import UserMetadataInteractionsConnectedApps
from vimeo_python_sdk.type.user_metadata_interactions_follow import UserMetadataInteractionsFollow
from vimeo_python_sdk.type.user_metadata_interactions_report import UserMetadataInteractionsReport

class RequiredUserMetadataInteractions(TypedDict):
    block: UserMetadataInteractionsBlock

    connected_apps: UserMetadataInteractionsConnectedApps

    follow: UserMetadataInteractionsFollow

    report: UserMetadataInteractionsReport

class OptionalUserMetadataInteractions(TypedDict, total=False):
    add_privacy_user: UserMetadataInteractionsAddPrivacyUser

class UserMetadataInteractions(RequiredUserMetadataInteractions, OptionalUserMetadataInteractions):
    pass

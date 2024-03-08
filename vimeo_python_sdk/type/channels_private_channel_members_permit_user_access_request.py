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

from vimeo_python_sdk.type.channels_private_channel_members_permit_user_access_request_users import ChannelsPrivateChannelMembersPermitUserAccessRequestUsers

class RequiredChannelsPrivateChannelMembersPermitUserAccessRequest(TypedDict):
    users: ChannelsPrivateChannelMembersPermitUserAccessRequestUsers

class OptionalChannelsPrivateChannelMembersPermitUserAccessRequest(TypedDict, total=False):
    pass

class ChannelsPrivateChannelMembersPermitUserAccessRequest(RequiredChannelsPrivateChannelMembersPermitUserAccessRequest, OptionalChannelsPrivateChannelMembersPermitUserAccessRequest):
    pass

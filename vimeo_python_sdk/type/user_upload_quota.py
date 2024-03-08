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

from vimeo_python_sdk.type.user_upload_quota_lifetime import UserUploadQuotaLifetime
from vimeo_python_sdk.type.user_upload_quota_periodic import UserUploadQuotaPeriodic
from vimeo_python_sdk.type.user_upload_quota_space import UserUploadQuotaSpace

class RequiredUserUploadQuota(TypedDict):
    lifetime: UserUploadQuotaLifetime

    periodic: UserUploadQuotaPeriodic

    space: UserUploadQuotaSpace

class OptionalUserUploadQuota(TypedDict, total=False):
    pass

class UserUploadQuota(RequiredUserUploadQuota, OptionalUserUploadQuota):
    pass

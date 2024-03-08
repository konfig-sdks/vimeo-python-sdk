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

from vimeo_python_sdk.type.webinar_email_provider_list_item_list import WebinarEmailProviderListItemList
from vimeo_python_sdk.type.webinar_email_provider_list_item_provider import WebinarEmailProviderListItemProvider

RequiredWebinarEmailProviderListItem = TypedDict("RequiredWebinarEmailProviderListItem", {
    # Whether the connection is active.
    "is_active": bool,

    # The most recent sync date of the provider list.
    "last_import_time": typing.Optional[str],

    "list": WebinarEmailProviderListItemList,

    "provider": WebinarEmailProviderListItemProvider,
    })

OptionalWebinarEmailProviderListItem = TypedDict("OptionalWebinarEmailProviderListItem", {
    }, total=False)

class WebinarEmailProviderListItem(RequiredWebinarEmailProviderListItem, OptionalWebinarEmailProviderListItem):
    pass

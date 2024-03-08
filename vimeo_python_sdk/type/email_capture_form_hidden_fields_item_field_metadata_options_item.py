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


class RequiredEmailCaptureFormHiddenFieldsItemFieldMetadataOptionsItem(TypedDict):
    # The label for the field option.
    option_label: str

    # The position of the option in the dropdown relative to the others.
    option_position: typing.Union[int, float]

class OptionalEmailCaptureFormHiddenFieldsItemFieldMetadataOptionsItem(TypedDict, total=False):
    pass

class EmailCaptureFormHiddenFieldsItemFieldMetadataOptionsItem(RequiredEmailCaptureFormHiddenFieldsItemFieldMetadataOptionsItem, OptionalEmailCaptureFormHiddenFieldsItemFieldMetadataOptionsItem):
    pass

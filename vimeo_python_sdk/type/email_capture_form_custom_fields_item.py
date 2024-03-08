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

from vimeo_python_sdk.type.email_capture_form_custom_fields_item_connected_fields import EmailCaptureFormCustomFieldsItemConnectedFields
from vimeo_python_sdk.type.email_capture_form_custom_fields_item_field_metadata import EmailCaptureFormCustomFieldsItemFieldMetadata

class RequiredEmailCaptureFormCustomFieldsItem(TypedDict):
    connected_fields: EmailCaptureFormCustomFieldsItemConnectedFields

    field_metadata: EmailCaptureFormCustomFieldsItemFieldMetadata

    # The name of a field in the form.
    field_name: str

    # The type of custom field.  Option descriptions:  * `dropdown` - The custom field used for dropdown item selection.  * `text` - The custom field used for text input. 
    field_type: str

    # Whether the field's **required** property is editable but **field_name** isn't. If the value is `true`, the field can't be deleted.
    locked: bool

    # Whether the field is required.
    required: bool

    # Whether the field's **required** and **field_name** properties are both uneditable. If the value is `true`, the field can't be deleted.
    static_field: bool

class OptionalEmailCaptureFormCustomFieldsItem(TypedDict, total=False):
    pass

class EmailCaptureFormCustomFieldsItem(RequiredEmailCaptureFormCustomFieldsItem, OptionalEmailCaptureFormCustomFieldsItem):
    pass

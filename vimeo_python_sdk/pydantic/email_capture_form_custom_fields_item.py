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

from vimeo_python_sdk.pydantic.email_capture_form_custom_fields_item_connected_fields import EmailCaptureFormCustomFieldsItemConnectedFields
from vimeo_python_sdk.pydantic.email_capture_form_custom_fields_item_field_metadata import EmailCaptureFormCustomFieldsItemFieldMetadata

class EmailCaptureFormCustomFieldsItem(BaseModel):
    connected_fields: EmailCaptureFormCustomFieldsItemConnectedFields = Field(alias='connected_fields')

    field_metadata: EmailCaptureFormCustomFieldsItemFieldMetadata = Field(alias='field_metadata')

    # The name of a field in the form.
    field_name: str = Field(alias='field_name')

    # The type of custom field.  Option descriptions:  * `dropdown` - The custom field used for dropdown item selection.  * `text` - The custom field used for text input. 
    field_type: Literal["dropdown", "text"] = Field(alias='field_type')

    # Whether the field's **required** property is editable but **field_name** isn't. If the value is `true`, the field can't be deleted.
    locked: bool = Field(alias='locked')

    # Whether the field is required.
    required: bool = Field(alias='required')

    # Whether the field's **required** and **field_name** properties are both uneditable. If the value is `true`, the field can't be deleted.
    static_field: bool = Field(alias='static_field')
    class Config:
        arbitrary_types_allowed = True

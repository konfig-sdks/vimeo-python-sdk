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


class RequiredEmailCaptureFormHiddenFieldsItemConnectedFieldsItem(TypedDict):
    # The ID of the provider field.
    email_service_provider_field_id: str

    # The ID of the field in the form associated with the connected field.
    form_field_id: typing.Union[int, float]

    # A third-party email service provider.  Option descriptions:  * `1` - The provider is Mailchimp.  * `2` - The provider is Campaign Monitor.  * `3` - The provider is Constant Contact.  * `4` - The provider is Infusionsoft.  * `5` - The provider is HubSpot.  * `6` - The provider is Constant Contact V3.  * `7` - The provider is Marketo. 
    provider_id: str

class OptionalEmailCaptureFormHiddenFieldsItemConnectedFieldsItem(TypedDict, total=False):
    pass

class EmailCaptureFormHiddenFieldsItemConnectedFieldsItem(RequiredEmailCaptureFormHiddenFieldsItemConnectedFieldsItem, OptionalEmailCaptureFormHiddenFieldsItemConnectedFieldsItem):
    pass

# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from vimeo_python_sdk import schemas  # noqa: F401


class EmailCaptureFormHiddenFieldsItemConnectedFields(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    The email provider fields associated with the field in the form.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['EmailCaptureFormHiddenFieldsItemConnectedFieldsItem']:
            return EmailCaptureFormHiddenFieldsItemConnectedFieldsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['EmailCaptureFormHiddenFieldsItemConnectedFieldsItem'], typing.List['EmailCaptureFormHiddenFieldsItemConnectedFieldsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EmailCaptureFormHiddenFieldsItemConnectedFields':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'EmailCaptureFormHiddenFieldsItemConnectedFieldsItem':
        return super().__getitem__(i)

from vimeo_python_sdk.model.email_capture_form_hidden_fields_item_connected_fields_item import EmailCaptureFormHiddenFieldsItemConnectedFieldsItem
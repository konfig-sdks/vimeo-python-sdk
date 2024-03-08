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

from vimeo_python_sdk.type.email_capture_form_custom_fields import EmailCaptureFormCustomFields
from vimeo_python_sdk.type.email_capture_form_email_lists import EmailCaptureFormEmailLists
from vimeo_python_sdk.type.email_capture_form_hidden_fields import EmailCaptureFormHiddenFields

class RequiredEmailCaptureForm(TypedDict):
    # The ID of the video associated with the form. If there is no associated video, the value of this field is `-1`.
    clip_id: typing.Union[int, float]

    # The time in ISO 8601 format when the form was created.
    created_time: str

    custom_fields: EmailCaptureFormCustomFields

    # The ID of the logo image to display on the form.
    custom_logo: typing.Union[int, float]

    # The message to display on the form.
    custom_message: str

    email_lists: EmailCaptureFormEmailLists

    hidden_fields: EmailCaptureFormHiddenFields

    # The ID of the email capture form.
    id: typing.Union[int, float]

    # When the form appears relative to the video playback.  Option descriptions:  * `after-video` - The form appears immediately after the video ends.  * `before-video` - The form appears before the video begins.  * `during-video` - The form appears during the video at the time specified by the **timecode** field. 
    position: str

    # The URL of the privacy policy related to the form.
    privacy_policy: str

    # Whether the user can skip the form.
    skippable: bool

    # The timecode for when the form appears. This field is used when the value of **position** is `during-video`.
    timecode: str

    # The canonical relative URI of the video's email capture form.
    uri: str

class OptionalEmailCaptureForm(TypedDict, total=False):
    pass

class EmailCaptureForm(RequiredEmailCaptureForm, OptionalEmailCaptureForm):
    pass

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


class RequiredVideoUpload(TypedDict):
    # The status code for the availability of the uploaded video.  Option descriptions:  * `complete` - The upload is complete.  * `error` - The upload ended with an error.  * `in_progress` - The upload is underway. 
    status: str

class OptionalVideoUpload(TypedDict, total=False):
    # The approach for uploading the video.  Option descriptions:  * `post` - The video upload uses the POST approach.  * `pull` - The video upload uses the pull approach.  * `tus` - The video upload uses the tus approach. 
    approach: str

    # The HTML form for uploading a video through the POST approach.
    form: str

    # The ID of the Google Cloud Storage upload.
    gcs_uid: str

    # The link of the video to capture through the pull approach.
    link: str

    # The redirect URL for the upload app.
    redirect_url: str

    # The file size in bytes of the uploaded video.
    size: typing.Union[int, float]

    # The link for sending video file data.
    upload_link: str

class VideoUpload(RequiredVideoUpload, OptionalVideoUpload):
    pass

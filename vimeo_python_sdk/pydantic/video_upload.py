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


class VideoUpload(BaseModel):
    # The status code for the availability of the uploaded video.  Option descriptions:  * `complete` - The upload is complete.  * `error` - The upload ended with an error.  * `in_progress` - The upload is underway. 
    status: Literal["complete", "error", "in_progress"] = Field(alias='status')

    # The approach for uploading the video.  Option descriptions:  * `post` - The video upload uses the POST approach.  * `pull` - The video upload uses the pull approach.  * `tus` - The video upload uses the tus approach. 
    approach: typing.Optional[Literal["post", "pull", "tus"]] = Field(None, alias='approach')

    # The HTML form for uploading a video through the POST approach.
    form: typing.Optional[str] = Field(None, alias='form')

    # The ID of the Google Cloud Storage upload.
    gcs_uid: typing.Optional[str] = Field(None, alias='gcs_uid')

    # The link of the video to capture through the pull approach.
    link: typing.Optional[str] = Field(None, alias='link')

    # The redirect URL for the upload app.
    redirect_url: typing.Optional[str] = Field(None, alias='redirect_url')

    # The file size in bytes of the uploaded video.
    size: typing.Optional[typing.Union[int, float]] = Field(None, alias='size')

    # The link for sending video file data.
    upload_link: typing.Optional[str] = Field(None, alias='upload_link')
    class Config:
        arbitrary_types_allowed = True

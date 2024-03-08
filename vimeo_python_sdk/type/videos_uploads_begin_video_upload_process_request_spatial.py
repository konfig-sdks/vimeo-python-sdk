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

from vimeo_python_sdk.type.videos_uploads_begin_video_upload_process_request_spatial_director_timeline import VideosUploadsBeginVideoUploadProcessRequestSpatialDirectorTimeline

class RequiredVideosUploadsBeginVideoUploadProcessRequestSpatial(TypedDict):
    pass

class OptionalVideosUploadsBeginVideoUploadProcessRequestSpatial(TypedDict, total=False):
    director_timeline: VideosUploadsBeginVideoUploadProcessRequestSpatialDirectorTimeline

    # The 360 field of view. This value must be between `30` and `90`; the default value is `50`.
    field_of_view: typing.Union[int, float]

    # The 360 spatial projection.  Option descriptions:  * `cubical` - Use cubical projection.  * `cylindrical` - Use cylindrical projection.  * `dome` - Use dome projection.  * `equirectangular` - Use equirectangular projection.  * `pyramid` - Use pyramid projection. 
    projection: str

    # The 360 spatial stereo format.  Option descriptions:  * `left-right` - Use left-right stereo.  * `mono` - Use monaural audio.  * `top-bottom` - Use top-bottom stereo. 
    stereo_format: str

class VideosUploadsBeginVideoUploadProcessRequestSpatial(RequiredVideosUploadsBeginVideoUploadProcessRequestSpatial, OptionalVideosUploadsBeginVideoUploadProcessRequestSpatial):
    pass

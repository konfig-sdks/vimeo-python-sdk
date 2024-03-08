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

from vimeo_python_sdk.pydantic.video_spatial_director_timeline import VideoSpatialDirectorTimeline

class VideoSpatial(BaseModel):
    director_timeline: VideoSpatialDirectorTimeline = Field(alias='director_timeline')

    # The video's 360 field of view value, ranging from a mininum of `30` to a maximum of `90`. The default value is `50`.
    field_of_view: typing.Optional[typing.Union[int, float]] = Field(alias='field_of_view')

    # The video's 360 spatial projection.  Option descriptions:  * `cubical` - The spatial projection is cubical.  * `cylindrical` - The spatial projection is cylindrical.  * `dome` - The spatial projection is dome-shaped.  * `equirectangular` - The spatial projection is equirectangular.  * `pyramid` - The spatial projection is pyramid-shaped. 
    projection: Literal["cubical", "cylindrical", "dome", "equirectangular", "pyramid"] = Field(alias='projection')

    # The video's 360 stereo format.  Option descriptions:  * `left-right` - The stereo format is left-right.  * `mono` - The audio is monaural.  * `top-bottom` - The stereo format is top-bottom. 
    stereo_format: Literal["left-right", "mono", "top-bottom"] = Field(alias='stereo_format')
    class Config:
        arbitrary_types_allowed = True

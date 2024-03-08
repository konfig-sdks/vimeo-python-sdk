# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.videos_video_id_tags.put import AddMultipleRaw
from vimeo_python_sdk.paths.videos_video_id_tags_word.put import AddTagToVideoRaw
from vimeo_python_sdk.paths.videos_video_id_tags_word.get import CheckTagVideoRaw
from vimeo_python_sdk.paths.tags_word_videos.get import GetAllByTagRaw
from vimeo_python_sdk.paths.videos_video_id_tags.get import GetVideoTagsRaw
from vimeo_python_sdk.paths.videos_video_id_tags_word.delete import RemoveTagRaw


class VideosTagsApiRaw(
    AddMultipleRaw,
    AddTagToVideoRaw,
    CheckTagVideoRaw,
    GetAllByTagRaw,
    GetVideoTagsRaw,
    RemoveTagRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.videos_video_id_presets_preset_id.put import AddPresetToVideoRaw
from vimeo_python_sdk.paths.videos_video_id_presets_preset_id.get import CheckIfPresetAddedToVideoRaw
from vimeo_python_sdk.paths.users_user_id_presets_preset_id_videos.get import GetPresetVideosRaw
from vimeo_python_sdk.paths.me_presets_preset_id_videos.get import GetSpecificPresetVideosRaw
from vimeo_python_sdk.paths.videos_video_id_presets_preset_id.delete import RemovePresetFromVideoRaw


class EmbedPresetsVideosApiRaw(
    AddPresetToVideoRaw,
    CheckIfPresetAddedToVideoRaw,
    GetPresetVideosRaw,
    GetSpecificPresetVideosRaw,
    RemovePresetFromVideoRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

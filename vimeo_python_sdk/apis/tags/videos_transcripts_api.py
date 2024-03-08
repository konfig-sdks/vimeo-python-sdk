# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.videos_video_id_transcripts_texttrack_id.get import Transcript
from vimeo_python_sdk.apis.tags.videos_transcripts_api_raw import VideosTranscriptsApiRaw


class VideosTranscriptsApi(
    Transcript,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: VideosTranscriptsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = VideosTranscriptsApiRaw(api_client)
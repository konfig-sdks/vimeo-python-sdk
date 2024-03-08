# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.me_videos.post import BeginVideoUploadProcess
from vimeo_python_sdk.paths.users_user_id_uploads_upload_id.delete import CompleteStreamingUpload
from vimeo_python_sdk.paths.users_user_id_uploads_upload_id.get import GetUploadAttempt
from vimeo_python_sdk.paths.users_user_id_videos.post import Video
from vimeo_python_sdk.apis.tags.videos_uploads_api_raw import VideosUploadsApiRaw


class VideosUploadsApi(
    BeginVideoUploadProcess,
    CompleteStreamingUpload,
    GetUploadAttempt,
    Video,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: VideosUploadsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = VideosUploadsApiRaw(api_client)

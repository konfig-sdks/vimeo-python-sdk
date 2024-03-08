# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.me_projects_project_id_videos.put import AddMultipleToFolderRaw
from vimeo_python_sdk.paths.users_user_id_projects_project_id_videos_video_id.put import AddSingleFolderVideoRaw
from vimeo_python_sdk.paths.me_projects_project_id_videos_video_id.put import AddToFolderRaw
from vimeo_python_sdk.paths.users_user_id_projects_project_id_videos.put import AddToFolderVideosRaw
from vimeo_python_sdk.paths.users_user_id_projects_project_id_videos.get import GetAllFolderVideosRaw
from vimeo_python_sdk.paths.me_projects_project_id_videos.get import GetVideosInFolderRaw
from vimeo_python_sdk.paths.users_user_id_projects_project_id_videos_video_id.delete import RemoveFromFolderVideoRaw
from vimeo_python_sdk.paths.me_projects_project_id_videos.delete import RemoveMultipleFromFolderRaw
from vimeo_python_sdk.paths.users_user_id_projects_project_id_videos.delete import RemoveMultipleVideosFromFolderRaw
from vimeo_python_sdk.paths.me_projects_project_id_videos_video_id.delete import RemoveSingleVideoRaw


class FoldersVideosApiRaw(
    AddMultipleToFolderRaw,
    AddSingleFolderVideoRaw,
    AddToFolderRaw,
    AddToFolderVideosRaw,
    GetAllFolderVideosRaw,
    GetVideosInFolderRaw,
    RemoveFromFolderVideoRaw,
    RemoveMultipleFromFolderRaw,
    RemoveMultipleVideosFromFolderRaw,
    RemoveSingleVideoRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
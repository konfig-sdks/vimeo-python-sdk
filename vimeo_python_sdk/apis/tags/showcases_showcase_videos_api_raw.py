# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.me_albums_album_id_videos_video_id.put import AddToShowcaseRaw
from vimeo_python_sdk.paths.users_user_id_albums_album_id_videos_video_id.put import AddToShowcase0Raw
from vimeo_python_sdk.paths.me_albums_album_id_videos_video_id_set_album_thumbnail.post import CreateShowcaseThumbnailRaw
from vimeo_python_sdk.paths.users_user_id_albums_album_id_videos_video_id_set_album_thumbnail.post import CreateShowcaseThumbnail0Raw
from vimeo_python_sdk.paths.users_user_id_albums_album_id_videos.get import GetShowcaseVideosRaw
from vimeo_python_sdk.paths.me_albums_album_id_videos_video_id.get import GetSpecificVideoInShowcaseRaw
from vimeo_python_sdk.paths.users_user_id_albums_album_id_videos_video_id.get import GetSpecificVideoInShowcase0Raw
from vimeo_python_sdk.paths.videos_video_id_available_albums.get import ListAvailableShowcasesRaw
from vimeo_python_sdk.paths.albums_album_id_available_videos.get import ListInShowcaseRaw
from vimeo_python_sdk.paths.me_albums_album_id_videos.get import ListInShowcase0Raw
from vimeo_python_sdk.paths.me_albums_album_id_videos_video_id.delete import RemoveFromShowcaseRaw
from vimeo_python_sdk.paths.users_user_id_albums_album_id_videos_video_id.delete import RemoveVideoFromShowcaseRaw
from vimeo_python_sdk.paths.users_user_id_albums_album_id_videos.put import ReplaceShowcaseVideosRaw
from vimeo_python_sdk.paths.me_albums_album_id_videos.put import ReplaceVideosRaw
from vimeo_python_sdk.paths.me_albums_album_id_videos_video_id_set_featured_video.patch import SetFeaturedVideoRaw
from vimeo_python_sdk.paths.users_user_id_albums_album_id_videos_video_id_set_featured_video.patch import SetFeaturedVideo0Raw


class ShowcasesShowcaseVideosApiRaw(
    AddToShowcaseRaw,
    AddToShowcase0Raw,
    CreateShowcaseThumbnailRaw,
    CreateShowcaseThumbnail0Raw,
    GetShowcaseVideosRaw,
    GetSpecificVideoInShowcaseRaw,
    GetSpecificVideoInShowcase0Raw,
    ListAvailableShowcasesRaw,
    ListInShowcaseRaw,
    ListInShowcase0Raw,
    RemoveFromShowcaseRaw,
    RemoveVideoFromShowcaseRaw,
    ReplaceShowcaseVideosRaw,
    ReplaceVideosRaw,
    SetFeaturedVideoRaw,
    SetFeaturedVideo0Raw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
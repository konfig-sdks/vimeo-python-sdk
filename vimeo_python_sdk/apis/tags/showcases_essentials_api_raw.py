# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.me_albums.post import CreateUserShowcaseRaw
from vimeo_python_sdk.paths.me_albums_album_id.delete import DeleteShowcaseRaw
from vimeo_python_sdk.paths.me_albums_album_id.patch import EditShowcaseRaw
from vimeo_python_sdk.paths.me_albums.get import GetAllUserShowcasesRaw
from vimeo_python_sdk.paths.me_albums_album_id.get import GetSpecificShowcaseRaw
from vimeo_python_sdk.paths.users_user_id_albums.post import ShowcaseRaw
from vimeo_python_sdk.paths.users_user_id_albums_album_id.get import Showcase0Raw
from vimeo_python_sdk.paths.users_user_id_albums_album_id.delete import Showcase1Raw
from vimeo_python_sdk.paths.users_user_id_albums_album_id.patch import Showcase2Raw
from vimeo_python_sdk.paths.users_user_id_albums.get import ShowcasesRaw
from vimeo_python_sdk.paths.users_user_id_albums.patch import Showcases0Raw


class ShowcasesEssentialsApiRaw(
    CreateUserShowcaseRaw,
    DeleteShowcaseRaw,
    EditShowcaseRaw,
    GetAllUserShowcasesRaw,
    GetSpecificShowcaseRaw,
    ShowcaseRaw,
    Showcase0Raw,
    Showcase1Raw,
    Showcase2Raw,
    ShowcasesRaw,
    Showcases0Raw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

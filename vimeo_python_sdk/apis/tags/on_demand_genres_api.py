# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_genres_genre_id.put import AddGenreToPage
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_genres_genre_id.get import CheckGenreAssociation
from vimeo_python_sdk.paths.ondemand_genres.get import GetAllGenres
from vimeo_python_sdk.paths.ondemand_genres_genre_id_pages.get import GetAllPagesInGenre
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_genres.get import GetGenres
from vimeo_python_sdk.paths.ondemand_genres_genre_id_pages_ondemand_id.get import GetSpecificPageInGenre
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_genres_genre_id.delete import RemoveGenreFromPage
from vimeo_python_sdk.paths.ondemand_genres_genre_id.get import SpecificGenreGet
from vimeo_python_sdk.apis.tags.on_demand_genres_api_raw import OnDemandGenresApiRaw


class OnDemandGenresApi(
    AddGenreToPage,
    CheckGenreAssociation,
    GetAllGenres,
    GetAllPagesInGenre,
    GetGenres,
    GetSpecificPageInGenre,
    RemoveGenreFromPage,
    SpecificGenreGet,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: OnDemandGenresApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = OnDemandGenresApiRaw(api_client)

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


class OnDemandVideosAddVideoToPageRequestRentPrice(BaseModel):
    # The rental price of the video in Australian dollars.
    a_u_d: typing.Optional[typing.Union[int, float]] = Field(None, alias='AUD')

    # The rental price of the video in Canadian dollars.
    c_a_d: typing.Optional[typing.Union[int, float]] = Field(None, alias='CAD')

    # The rental price of the video in Swiss francs.
    c_h_f: typing.Optional[typing.Union[int, float]] = Field(None, alias='CHF')

    # The rental price of the video in Danish krone.
    d_k_k: typing.Optional[typing.Union[int, float]] = Field(None, alias='DKK')

    # The rental price of the video in euros.
    e_u_r: typing.Optional[typing.Union[int, float]] = Field(None, alias='EUR')

    # The rental price of the video in British pounds.
    g_b_p: typing.Optional[typing.Union[int, float]] = Field(None, alias='GBP')

    # The rental price of the video in Japanese yen.
    j_p_y: typing.Optional[typing.Union[int, float]] = Field(None, alias='JPY')

    # The rental price of the video in South Korean won.
    k_r_w: typing.Optional[typing.Union[int, float]] = Field(None, alias='KRW')

    # The rental price of the video in Norwegian krone.
    n_o_k: typing.Optional[typing.Union[int, float]] = Field(None, alias='NOK')

    # The rental price of the video in Polish zloty.
    p_l_n: typing.Optional[typing.Union[int, float]] = Field(None, alias='PLN')

    # The rental price of the video in Swedish krona.
    s_e_k: typing.Optional[typing.Union[int, float]] = Field(None, alias='SEK')

    # The rental price of the video in United States dollars. This parameter is required when **rent.active** is `true`.
    u_s_d: typing.Optional[typing.Union[int, float]] = Field(None, alias='USD')
    class Config:
        arbitrary_types_allowed = True

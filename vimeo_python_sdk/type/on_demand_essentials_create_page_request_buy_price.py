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


class RequiredOnDemandEssentialsCreatePageRequestBuyPrice(TypedDict):
    pass

class OptionalOnDemandEssentialsCreatePageRequestBuyPrice(TypedDict, total=False):
    # The purchase price of the video in Australian dollars.
    AUD: typing.Union[int, float]

    # The purchase price of the video in Canadian dollars.
    CAD: typing.Union[int, float]

    # The purchase price of the video in Swiss francs.
    CHF: typing.Union[int, float]

    # The purchase price of the video in Danish krone.
    DKK: typing.Union[int, float]

    # The purchase price of the video in euros.
    EUR: typing.Union[int, float]

    # The purchase price of the video in British pounds.
    GBP: typing.Union[int, float]

    # The purchase price of the video in Japanese yen.
    JPY: typing.Union[int, float]

    # The purchase price of the video in South Korean won.
    KRW: typing.Union[int, float]

    # The purchase price of the video in Norwegian krone.
    NOK: typing.Union[int, float]

    # The purchase price of the video in Polish zloty.
    PLN: typing.Union[int, float]

    # The purchase price of the video in Swedish krona.
    SEK: typing.Union[int, float]

    # When **type** is `film`, the purchase price of the video in United States dollars. When **type** is `series`, the purchase price of the entire collection in United States dollars.
    USD: typing.Union[int, float]

class OnDemandEssentialsCreatePageRequestBuyPrice(RequiredOnDemandEssentialsCreatePageRequestBuyPrice, OptionalOnDemandEssentialsCreatePageRequestBuyPrice):
    pass

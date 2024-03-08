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

from vimeo_python_sdk.type.portfolio_metadata import PortfolioMetadata

class RequiredPortfolio(TypedDict):
    # The description of the portfolio.
    description: typing.Optional[str]

    # The time in ISO 8601 format when the portfolio was created.
    created_time: str

    # The link to the portfolio.
    link: str

    metadata: PortfolioMetadata

    # The time in ISO 8601 format when the portfolio's data was last modified.
    modified_time: str

    # The display name of the portfolio.
    name: str

    # The default video sort order of the portfolio.  Option descriptions:  * `alphabetical` - The default sort order is alphabetical by name.  * `clips` - The default sort order is video creation date.  * `modified` - The default sort order is the order in which the videos were modified.  * `recent` - The default sort order is the order in which the videos were added. 
    sort: str

    # The canonical relative URI of the portfolio.
    uri: str

class OptionalPortfolio(TypedDict, total=False):
    pass

class Portfolio(RequiredPortfolio, OptionalPortfolio):
    pass

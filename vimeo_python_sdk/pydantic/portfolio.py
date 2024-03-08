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

from vimeo_python_sdk.pydantic.portfolio_metadata import PortfolioMetadata

class Portfolio(BaseModel):
    # The description of the portfolio.
    description: typing.Optional[str] = Field(alias='description')

    # The time in ISO 8601 format when the portfolio was created.
    created_time: str = Field(alias='created_time')

    # The link to the portfolio.
    link: str = Field(alias='link')

    metadata: PortfolioMetadata = Field(alias='metadata')

    # The time in ISO 8601 format when the portfolio's data was last modified.
    modified_time: str = Field(alias='modified_time')

    # The display name of the portfolio.
    name: str = Field(alias='name')

    # The default video sort order of the portfolio.  Option descriptions:  * `alphabetical` - The default sort order is alphabetical by name.  * `clips` - The default sort order is video creation date.  * `modified` - The default sort order is the order in which the videos were modified.  * `recent` - The default sort order is the order in which the videos were added. 
    sort: Literal["alphabetical", "clips", "modified", "recent"] = Field(alias='sort')

    # The canonical relative URI of the portfolio.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

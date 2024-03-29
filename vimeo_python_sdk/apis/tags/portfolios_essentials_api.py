# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.me_portfolios.get import GetAllUserPortfolios
from vimeo_python_sdk.paths.me_portfolios_portfolio_id.get import GetUserPortfolio
from vimeo_python_sdk.paths.users_user_id_portfolios_portfolio_id.get import Portfolio
from vimeo_python_sdk.paths.users_user_id_portfolios.get import Portfolios
from vimeo_python_sdk.apis.tags.portfolios_essentials_api_raw import PortfoliosEssentialsApiRaw


class PortfoliosEssentialsApi(
    GetAllUserPortfolios,
    GetUserPortfolio,
    Portfolio,
    Portfolios,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PortfoliosEssentialsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PortfoliosEssentialsApiRaw(api_client)

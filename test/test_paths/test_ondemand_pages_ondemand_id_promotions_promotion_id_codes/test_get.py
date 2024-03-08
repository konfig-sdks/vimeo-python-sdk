# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

import unittest
from unittest.mock import patch

import urllib3

import vimeo_python_sdk
from vimeo_python_sdk.paths.ondemand_pages_ondemand_id_promotions_promotion_id_codes import get
from vimeo_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestOndemandPagesOndemandIdPromotionsPromotionIdCodes(ApiTestMixin, unittest.TestCase):
    """
    OndemandPagesOndemandIdPromotionsPromotionIdCodes unit test stubs
        Get all the codes of a promotion on an On Demand page
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()

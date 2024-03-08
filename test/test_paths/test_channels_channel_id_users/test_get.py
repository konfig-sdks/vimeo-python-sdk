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
from vimeo_python_sdk.paths.channels_channel_id_users import get
from vimeo_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestChannelsChannelIdUsers(ApiTestMixin, unittest.TestCase):
    """
    ChannelsChannelIdUsers unit test stubs
        Get all the followers of a channel
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()

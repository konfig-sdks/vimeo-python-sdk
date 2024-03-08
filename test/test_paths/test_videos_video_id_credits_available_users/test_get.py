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
from vimeo_python_sdk.paths.videos_video_id_credits_available_users import get
from vimeo_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestVideosVideoIdCreditsAvailableUsers(ApiTestMixin, unittest.TestCase):
    """
    VideosVideoIdCreditsAvailableUsers unit test stubs
        Get users who can be credited on a video
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()

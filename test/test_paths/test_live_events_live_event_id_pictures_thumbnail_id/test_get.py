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
from vimeo_python_sdk.paths.live_events_live_event_id_pictures_thumbnail_id import get
from vimeo_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestLiveEventsLiveEventIdPicturesThumbnailId(ApiTestMixin, unittest.TestCase):
    """
    LiveEventsLiveEventIdPicturesThumbnailId unit test stubs
        Get a specific live event thumbnail
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()

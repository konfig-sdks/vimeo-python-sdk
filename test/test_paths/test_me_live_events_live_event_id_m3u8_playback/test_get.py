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
from vimeo_python_sdk.paths.me_live_events_live_event_id_m3u8_playback import get
from vimeo_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestMeLiveEventsLiveEventIdM3u8Playback(ApiTestMixin, unittest.TestCase):
    """
    MeLiveEventsLiveEventIdM3u8Playback unit test stubs
        Get an M3U8 playback URL for a live event
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()

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
from vimeo_python_sdk.paths.users_user_id_live_events_live_event_id_ott_destination_destination_id import delete
from vimeo_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestUsersUserIdLiveEventsLiveEventIdOttDestinationDestinationId(ApiTestMixin, unittest.TestCase):
    """
    UsersUserIdLiveEventsLiveEventIdOttDestinationDestinationId unit test stubs
        Delete a live event OTT destination
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()

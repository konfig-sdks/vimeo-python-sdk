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
from vimeo_python_sdk.paths.me_projects_project_id_videos import put
from vimeo_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestMeProjectsProjectIdVideos(ApiTestMixin, unittest.TestCase):
    """
    MeProjectsProjectIdVideos unit test stubs
        Add a list of videos to a folder
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
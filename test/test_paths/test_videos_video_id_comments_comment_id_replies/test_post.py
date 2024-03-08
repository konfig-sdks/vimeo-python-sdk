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
from vimeo_python_sdk.paths.videos_video_id_comments_comment_id_replies import post
from vimeo_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestVideosVideoIdCommentsCommentIdReplies(ApiTestMixin, unittest.TestCase):
    """
    VideosVideoIdCommentsCommentIdReplies unit test stubs
        Add a reply to a video comment
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 201






if __name__ == '__main__':
    unittest.main()

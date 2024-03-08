# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

import unittest

import os
from pprint import pprint
from vimeo_python_sdk import Vimeo

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        vimeo = Vimeo(
        
            access_token = 'YOUR_BEARER_TOKEN',
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',,
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(vimeo)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

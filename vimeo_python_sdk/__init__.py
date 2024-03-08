# coding: utf-8

# flake8: noqa

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

__version__ = "3.4"

# import ApiClient
from vimeo_python_sdk.api_client import ApiClient

# import Configuration
from vimeo_python_sdk.configuration import Configuration

# import exceptions
from vimeo_python_sdk.exceptions import OpenApiException
from vimeo_python_sdk.exceptions import ApiAttributeError
from vimeo_python_sdk.exceptions import ApiTypeError
from vimeo_python_sdk.exceptions import ApiValueError
from vimeo_python_sdk.exceptions import ApiKeyError
from vimeo_python_sdk.exceptions import ApiException

from vimeo_python_sdk.client import Vimeo

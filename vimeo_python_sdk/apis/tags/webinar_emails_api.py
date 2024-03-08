# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.me_webinars_webinar_id_email_settings.patch import CustomizePreferences
from vimeo_python_sdk.paths.users_user_id_webinars_webinar_id_email_settings.patch import CustomizePreferences0
from vimeo_python_sdk.paths.me_webinars_webinar_id_email_settings.get import GetCustomizationData
from vimeo_python_sdk.paths.users_user_id_webinars_webinar_id_email_settings.get import GetCustomizationData0
from vimeo_python_sdk.apis.tags.webinar_emails_api_raw import WebinarEmailsApiRaw


class WebinarEmailsApi(
    CustomizePreferences,
    CustomizePreferences0,
    GetCustomizationData,
    GetCustomizationData0,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: WebinarEmailsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = WebinarEmailsApiRaw(api_client)
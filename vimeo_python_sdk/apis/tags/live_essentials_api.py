# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.live_events.post import CreateEvent
from vimeo_python_sdk.paths.users_user_id_live_events.post import CreateEventForUser
from vimeo_python_sdk.paths.me_live_events.post import CreateLiveEvent
from vimeo_python_sdk.paths.live_events.delete import DeleteMultipleEvents
from vimeo_python_sdk.paths.me_live_events.delete import DeleteMultipleEvents0
from vimeo_python_sdk.paths.users_user_id_live_events.delete import DeleteMultipleEvents1
from vimeo_python_sdk.paths.me_live_events_live_event_id.delete import DeleteSingleEvent
from vimeo_python_sdk.paths.users_user_id_live_events_live_event_id.delete import DeleteSpecificEvent
from vimeo_python_sdk.paths.live_events_live_event_id.delete import DeleteSpecificLiveEvent
from vimeo_python_sdk.paths.me_live_events.get import GetAllUserLiveEvents
from vimeo_python_sdk.paths.live_events_live_event_id.get import GetEventById
from vimeo_python_sdk.paths.users_user_id_live_events_live_event_id.get import GetEventById0
from vimeo_python_sdk.paths.me_live_events_live_event_id.get import GetSpecificLiveEvent
from vimeo_python_sdk.paths.live_events.get import GetUserLiveEvents
from vimeo_python_sdk.paths.users_user_id_live_events.get import GetUserLiveEvents0
from vimeo_python_sdk.paths.live_events_live_event_id.patch import UpdateEventBelongingToAuthenticatedUser
from vimeo_python_sdk.paths.me_live_events_live_event_id.patch import UpdateEventBelongingToAuthenticatedUser0
from vimeo_python_sdk.paths.users_user_id_live_events_live_event_id.patch import UpdateEventBelongingToAuthenticatedUser1
from vimeo_python_sdk.apis.tags.live_essentials_api_raw import LiveEssentialsApiRaw


class LiveEssentialsApi(
    CreateEvent,
    CreateEventForUser,
    CreateLiveEvent,
    DeleteMultipleEvents,
    DeleteMultipleEvents0,
    DeleteMultipleEvents1,
    DeleteSingleEvent,
    DeleteSpecificEvent,
    DeleteSpecificLiveEvent,
    GetAllUserLiveEvents,
    GetEventById,
    GetEventById0,
    GetSpecificLiveEvent,
    GetUserLiveEvents,
    GetUserLiveEvents0,
    UpdateEventBelongingToAuthenticatedUser,
    UpdateEventBelongingToAuthenticatedUser0,
    UpdateEventBelongingToAuthenticatedUser1,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: LiveEssentialsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = LiveEssentialsApiRaw(api_client)

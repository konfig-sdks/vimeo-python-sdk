# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.me_live_events_live_event_id_destinations.post import CreateDestination
from vimeo_python_sdk.paths.users_user_id_live_events_live_event_id_destinations.post import CreateEventDestination
from vimeo_python_sdk.paths.me_videos_video_id_destinations.post import CreateOneTimeLiveEventDestination
from vimeo_python_sdk.paths.users_user_id_videos_video_id_destinations.post import CreateOneTimeLiveEventDestination0
from vimeo_python_sdk.paths.users_user_id_live_events_live_event_id_ott_destinations.post import CreateOttDestination
from vimeo_python_sdk.paths.destination_destination_id.delete import DeleteDestination
from vimeo_python_sdk.paths.users_user_id_live_events_live_event_id_ott_destination_destination_id.delete import DeleteOttDestination
from vimeo_python_sdk.paths.me_destinations.get import GetAllAvailableDestinations
from vimeo_python_sdk.paths.users_user_id_live_events_live_event_id_destinations.get import GetAllAvailableDestinations0
from vimeo_python_sdk.paths.users_user_id_videos_video_id_destinations.get import GetAllAvailableDestinations1
from vimeo_python_sdk.paths.me_videos_video_id_destinations.get import GetAllDestinations
from vimeo_python_sdk.paths.users_user_id_live_events_live_event_id_ott_destinations.get import GetAllOttDestinations
from vimeo_python_sdk.paths.destination_destination_id.get import GetDestination
from vimeo_python_sdk.paths.me_live_events_live_event_id_destinations.get import ListAllAvailableDestinations
from vimeo_python_sdk.paths.users_user_id_destinations.get import ListAvailableDestinations
from vimeo_python_sdk.paths.destination_destination_id.patch import UpdateDestination
from vimeo_python_sdk.apis.tags.live_event_destinations_api_raw import LiveEventDestinationsApiRaw


class LiveEventDestinationsApi(
    CreateDestination,
    CreateEventDestination,
    CreateOneTimeLiveEventDestination,
    CreateOneTimeLiveEventDestination0,
    CreateOttDestination,
    DeleteDestination,
    DeleteOttDestination,
    GetAllAvailableDestinations,
    GetAllAvailableDestinations0,
    GetAllAvailableDestinations1,
    GetAllDestinations,
    GetAllOttDestinations,
    GetDestination,
    ListAllAvailableDestinations,
    ListAvailableDestinations,
    UpdateDestination,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: LiveEventDestinationsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = LiveEventDestinationsApiRaw(api_client)

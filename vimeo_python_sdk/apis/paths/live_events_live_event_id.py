from vimeo_python_sdk.paths.live_events_live_event_id.get import ApiForget
from vimeo_python_sdk.paths.live_events_live_event_id.delete import ApiFordelete
from vimeo_python_sdk.paths.live_events_live_event_id.patch import ApiForpatch


class LiveEventsLiveEventId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass

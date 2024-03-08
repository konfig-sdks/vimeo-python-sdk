from vimeo_python_sdk.paths.live_events.get import ApiForget
from vimeo_python_sdk.paths.live_events.post import ApiForpost
from vimeo_python_sdk.paths.live_events.delete import ApiFordelete


class LiveEvents(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass

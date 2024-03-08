from vimeo_python_sdk.paths.me_live_events.get import ApiForget
from vimeo_python_sdk.paths.me_live_events.post import ApiForpost
from vimeo_python_sdk.paths.me_live_events.delete import ApiFordelete


class MeLiveEvents(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass

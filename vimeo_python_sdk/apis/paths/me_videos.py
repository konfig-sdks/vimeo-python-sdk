from vimeo_python_sdk.paths.me_videos.get import ApiForget
from vimeo_python_sdk.paths.me_videos.post import ApiForpost
from vimeo_python_sdk.paths.me_videos.delete import ApiFordelete


class MeVideos(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass

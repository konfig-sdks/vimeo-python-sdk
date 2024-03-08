from vimeo_python_sdk.paths.videos_video_id.get import ApiForget
from vimeo_python_sdk.paths.videos_video_id.delete import ApiFordelete
from vimeo_python_sdk.paths.videos_video_id.patch import ApiForpatch


class VideosVideoId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass

from vimeo_python_sdk.paths.users_user_id_videos.get import ApiForget
from vimeo_python_sdk.paths.users_user_id_videos.post import ApiForpost
from vimeo_python_sdk.paths.users_user_id_videos.delete import ApiFordelete


class UsersUserIdVideos(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass

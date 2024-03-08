from vimeo_python_sdk.paths.channels_channel_id.get import ApiForget
from vimeo_python_sdk.paths.channels_channel_id.delete import ApiFordelete
from vimeo_python_sdk.paths.channels_channel_id.patch import ApiForpatch


class ChannelsChannelId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass

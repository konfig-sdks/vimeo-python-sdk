from vimeo_python_sdk.paths.me_albums_album_id.get import ApiForget
from vimeo_python_sdk.paths.me_albums_album_id.delete import ApiFordelete
from vimeo_python_sdk.paths.me_albums_album_id.patch import ApiForpatch


class MeAlbumsAlbumId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass

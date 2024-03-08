from vimeo_python_sdk.paths.me_projects_project_id.get import ApiForget
from vimeo_python_sdk.paths.me_projects_project_id.delete import ApiFordelete
from vimeo_python_sdk.paths.me_projects_project_id.patch import ApiForpatch


class MeProjectsProjectId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass

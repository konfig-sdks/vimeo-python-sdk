# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from vimeo_python_sdk.paths.oauth_access_token import Api

from vimeo_python_sdk.paths import PathValues

path = PathValues.OAUTH_ACCESS_TOKEN
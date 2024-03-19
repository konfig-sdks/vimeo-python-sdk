operation_parameter_map = {
    '/-GET': {
        'parameters': [
            {
                'name': 'openapi'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/oauth/authorize/client-POST': {
        'parameters': [
            {
                'name': 'grant_type'
            },
            {
                'name': 'scope'
            },
        ]
    },
    '/oauth/authorize/vimeo_oauth1-POST': {
        'parameters': [
            {
                'name': 'grant_type'
            },
            {
                'name': 'token'
            },
            {
                'name': 'token_secret'
            },
        ]
    },
    '/oauth/verify-GET': {
        'parameters': [
        ]
    },
    '/tokens-DELETE': {
        'parameters': [
        ]
    },
    '/oauth/access_token-POST': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'grant_type'
            },
            {
                'name': 'redirect_uri'
            },
        ]
    },
    '/categories/{category}/channels-GET': {
        'parameters': [
            {
                'name': 'category'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/categories-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/categories/{category}-GET': {
        'parameters': [
            {
                'name': 'category'
            },
        ]
    },
    '/categories/{category}/groups-GET': {
        'parameters': [
            {
                'name': 'category'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/categories/{category}-GET': {
        'parameters': [
            {
                'name': 'category'
            },
        ]
    },
    '/users/{user_id}/categories/{category}-GET': {
        'parameters': [
            {
                'name': 'category'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/categories/{category}-PUT': {
        'parameters': [
            {
                'name': 'category'
            },
        ]
    },
    '/users/{user_id}/categories/{category}-PUT': {
        'parameters': [
            {
                'name': 'category'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/categories-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/users/{user_id}/categories-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/categories/{category}-DELETE': {
        'parameters': [
            {
                'name': 'category'
            },
        ]
    },
    '/users/{user_id}/categories/{category}-DELETE': {
        'parameters': [
            {
                'name': 'category'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/videos/{video_id}/categories-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/categories/{category}/videos/{video_id}-GET': {
        'parameters': [
            {
                'name': 'category'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/categories/{category}/videos-GET': {
        'parameters': [
            {
                'name': 'category'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/videos/{video_id}/categories-PUT': {
        'parameters': [
            {
                'name': 'category'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/channels/{channel_id}/categories-PUT': {
        'parameters': [
            {
                'name': 'channels'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/channels/{channel_id}/categories/{category}-PUT': {
        'parameters': [
            {
                'name': 'category'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/channels/{channel_id}/categories-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
        ]
    },
    '/channels/{channel_id}/categories/{category}-DELETE': {
        'parameters': [
            {
                'name': 'category'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/channels-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'description'
            },
            {
                'name': 'link'
            },
        ]
    },
    '/channels/{channel_id}-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
        ]
    },
    '/channels/{channel_id}-DELETE': {
        'parameters': [
            {
                'name': 'channel_id'
            },
        ]
    },
    '/channels/{channel_id}-PATCH': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'link'
            },
            {
                'name': 'name'
            },
            {
                'name': 'privacy'
            },
        ]
    },
    '/channels-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/channels-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/users/{user_id}/channels-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/channels/{channel_id}/moderators/{user_id}-PUT': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/channels/{channel_id}/moderators-PUT': {
        'parameters': [
            {
                'name': 'channel_id'
            },
        ]
    },
    '/channels/{channel_id}/moderators/{user_id}-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/channels/{channel_id}/moderators-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/channels/{channel_id}/moderators/{user_id}-DELETE': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/channels/{channel_id}/moderators-DELETE': {
        'parameters': [
            {
                'name': 'user_uri'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/channels/{channel_id}/moderators-PATCH': {
        'parameters': [
            {
                'name': 'user_uri'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/channels/{channel_id}/privacy/users-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/channels/{channel_id}/privacy/users-PUT': {
        'parameters': [
            {
                'name': 'users'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/channels/{channel_id}/privacy/users/{user_id}-PUT': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/channels/{channel_id}/privacy/users/{user_id}-DELETE': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/channels/{channel_id}-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
        ]
    },
    '/users/{user_id}/channels/{channel_id}-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/channels/{channel_id}/users-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/users/{user_id}/channels/{channel_id}-PUT': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/channels/{channel_id}-PUT': {
        'parameters': [
            {
                'name': 'channel_id'
            },
        ]
    },
    '/me/channels/{channel_id}-DELETE': {
        'parameters': [
            {
                'name': 'channel_id'
            },
        ]
    },
    '/users/{user_id}/channels/{channel_id}-DELETE': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/channels/{channel_id}/tags-PUT': {
        'parameters': [
            {
                'name': 'tag'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/channels/{channel_id}/tags/{word}-PUT': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'word'
            },
        ]
    },
    '/channels/{channel_id}/tags/{word}-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'word'
            },
        ]
    },
    '/channels/{channel_id}/tags-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
        ]
    },
    '/channels/{channel_id}/tags/{word}-DELETE': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'word'
            },
        ]
    },
    '/channels/{channel_id}/videos-PUT': {
        'parameters': [
            {
                'name': 'video_uri'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/channels/{channel_id}/videos/{video_id}-PUT': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/available_channels-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/channels/{channel_id}/videos/{video_id}-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/channels/{channel_id}/videos-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'containing_uri'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/channels/{channel_id}/videos-DELETE': {
        'parameters': [
            {
                'name': 'video_uri'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/channels/{channel_id}/videos/{video_id}-DELETE': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/customlogos-POST': {
        'parameters': [
        ]
    },
    '/users/{user_id}/customlogos-POST': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/customlogos/{logo_id}-DELETE': {
        'parameters': [
            {
                'name': 'logo_id'
            },
        ]
    },
    '/users/{user_id}/customlogos/{logo_id}-DELETE': {
        'parameters': [
            {
                'name': 'logo_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/customlogos/{logo_id}-GET': {
        'parameters': [
            {
                'name': 'logo_id'
            },
        ]
    },
    '/users/{user_id}/customlogos/{logo_id}-GET': {
        'parameters': [
            {
                'name': 'logo_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/customlogos-GET': {
        'parameters': [
        ]
    },
    '/users/{user_id}/customlogos-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/presets-POST': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'embed'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/me/presets-POST': {
        'parameters': [
            {
                'name': 'embed'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/me/presets/{preset_id}-PATCH': {
        'parameters': [
            {
                'name': 'preset_id'
            },
            {
                'name': 'outro'
            },
        ]
    },
    '/users/{user_id}/presets/{preset_id}-PATCH': {
        'parameters': [
            {
                'name': 'preset_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'outro'
            },
        ]
    },
    '/me/presets-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/users/{user_id}/presets/{preset_id}-GET': {
        'parameters': [
            {
                'name': 'preset_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/presets/{preset_id}-GET': {
        'parameters': [
            {
                'name': 'preset_id'
            },
        ]
    },
    '/users/{user_id}/presets-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/timelinethumbnails-POST': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/timelinethumbnails/{thumbnail_id}-GET': {
        'parameters': [
            {
                'name': 'thumbnail_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/presets/{preset_id}-PUT': {
        'parameters': [
            {
                'name': 'preset_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/presets/{preset_id}-GET': {
        'parameters': [
            {
                'name': 'preset_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/presets/{preset_id}/videos-GET': {
        'parameters': [
            {
                'name': 'preset_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/me/presets/{preset_id}/videos-GET': {
        'parameters': [
            {
                'name': 'preset_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/presets/{preset_id}-DELETE': {
        'parameters': [
            {
                'name': 'preset_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/projects-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'parent_folder_uri'
            },
        ]
    },
    '/me/projects/{project_id}-DELETE': {
        'parameters': [
            {
                'name': 'project_id'
            },
            {
                'name': 'should_delete_clips'
            },
        ]
    },
    '/me/projects/{project_id}-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'project_id'
            },
        ]
    },
    '/me/projects-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/projects/{project_id}-GET': {
        'parameters': [
            {
                'name': 'project_id'
            },
        ]
    },
    '/users/{owner_id}/folders/private_to_me-GET': {
        'parameters': [
            {
                'name': 'owner_id'
            },
        ]
    },
    '/users/{user_id}/projects-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'parent_folder_uri'
            },
        ]
    },
    '/users/{user_id}/projects/{project_id}-GET': {
        'parameters': [
            {
                'name': 'project_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/projects/{project_id}-DELETE': {
        'parameters': [
            {
                'name': 'project_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'should_delete_clips'
            },
        ]
    },
    '/users/{user_id}/projects/{project_id}-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'project_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/projects-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/users/{user_id}/projects/{project_id}/items-GET': {
        'parameters': [
            {
                'name': 'project_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/projects/{project_id}/items-GET': {
        'parameters': [
            {
                'name': 'project_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/projects/{project_id}/items-DELETE': {
        'parameters': [
            {
                'name': 'project_id'
            },
            {
                'name': 'uris'
            },
            {
                'name': 'should_delete_items'
            },
        ]
    },
    '/me/projects/{project_id}/videos-PUT': {
        'parameters': [
            {
                'name': 'project_id'
            },
            {
                'name': 'uris'
            },
        ]
    },
    '/users/{user_id}/projects/{project_id}/videos/{video_id}-PUT': {
        'parameters': [
            {
                'name': 'project_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/projects/{project_id}/videos/{video_id}-PUT': {
        'parameters': [
            {
                'name': 'project_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/projects/{project_id}/videos-PUT': {
        'parameters': [
            {
                'name': 'project_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'uris'
            },
        ]
    },
    '/users/{user_id}/projects/{project_id}/videos-GET': {
        'parameters': [
            {
                'name': 'project_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter_tag'
            },
            {
                'name': 'filter_tag_all_of'
            },
            {
                'name': 'filter_tag_exclude'
            },
            {
                'name': 'include_subfolders'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'query_fields'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/projects/{project_id}/videos-GET': {
        'parameters': [
            {
                'name': 'project_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter_tag'
            },
            {
                'name': 'filter_tag_all_of'
            },
            {
                'name': 'filter_tag_exclude'
            },
            {
                'name': 'include_subfolders'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'query_fields'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/users/{user_id}/projects/{project_id}/videos/{video_id}-DELETE': {
        'parameters': [
            {
                'name': 'project_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/projects/{project_id}/videos-DELETE': {
        'parameters': [
            {
                'name': 'project_id'
            },
            {
                'name': 'uris'
            },
            {
                'name': 'should_delete_clips'
            },
        ]
    },
    '/users/{user_id}/projects/{project_id}/videos-DELETE': {
        'parameters': [
            {
                'name': 'project_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'uris'
            },
            {
                'name': 'should_delete_clips'
            },
        ]
    },
    '/me/projects/{project_id}/videos/{video_id}-DELETE': {
        'parameters': [
            {
                'name': 'project_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/groups-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/groups/{group_id}-GET': {
        'parameters': [
            {
                'name': 'group_id'
            },
        ]
    },
    '/groups/{group_id}-DELETE': {
        'parameters': [
            {
                'name': 'group_id'
            },
        ]
    },
    '/groups-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/groups/{group_id}-PUT': {
        'parameters': [
            {
                'name': 'group_id'
            },
        ]
    },
    '/users/{user_id}/groups/{group_id}-PUT': {
        'parameters': [
            {
                'name': 'group_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/groups/{group_id}-DELETE': {
        'parameters': [
            {
                'name': 'group_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/groups/{group_id}-DELETE': {
        'parameters': [
            {
                'name': 'group_id'
            },
        ]
    },
    '/users/{user_id}/groups/{group_id}-GET': {
        'parameters': [
            {
                'name': 'group_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/groups/{group_id}-GET': {
        'parameters': [
            {
                'name': 'group_id'
            },
        ]
    },
    '/groups/{group_id}/users-GET': {
        'parameters': [
            {
                'name': 'group_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/groups-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/users/{user_id}/groups-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/groups/{group_id}/videos/{video_id}-PUT': {
        'parameters': [
            {
                'name': 'group_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/groups/{group_id}/videos-GET': {
        'parameters': [
            {
                'name': 'group_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/groups/{group_id}/videos/{video_id}-GET': {
        'parameters': [
            {
                'name': 'group_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/groups/{group_id}/videos/{video_id}-DELETE': {
        'parameters': [
            {
                'name': 'group_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/likes/{video_id}-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/likes/{video_id}-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/likes-GET': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/likes-GET': {
        'parameters': [
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/videos/{video_id}/likes-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/channels/{channel_id}/videos/{video_id}/likes-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/likes/{video_id}-PUT': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/likes-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/likes/{video_id}-DELETE': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/likes/{video_id}-PUT': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/likes/{video_id}-DELETE': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/live_events/{live_event_id}/privacy/domains-PUT': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'allowed_domains'
            },
        ]
    },
    '/me/live_events/{live_event_id}/privacy/domains-PUT': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'allowed_domains'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/privacy/domains-PUT': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'allowed_domains'
            },
        ]
    },
    '/live_events/{live_event_id}/privacy/domains-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
        ]
    },
    '/me/live_events/{live_event_id}/privacy/domains-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/privacy/domains-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/live_events-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'allow_share_link'
            },
            {
                'name': 'auto_cc_enabled'
            },
            {
                'name': 'auto_cc_keywords'
            },
            {
                'name': 'auto_cc_lang'
            },
            {
                'name': 'automatically_title_stream'
            },
            {
                'name': 'chat_enabled'
            },
            {
                'name': 'content_rating'
            },
            {
                'name': 'dvr'
            },
            {
                'name': 'embed'
            },
            {
                'name': 'folder_uri'
            },
            {
                'name': 'interaction_tools_settings'
            },
            {
                'name': 'low_latency'
            },
            {
                'name': 'playlist_sort'
            },
            {
                'name': 'rtmp_preview'
            },
            {
                'name': 'schedule'
            },
            {
                'name': 'scheduled_playback'
            },
            {
                'name': 'stream_description'
            },
            {
                'name': 'stream_embed'
            },
            {
                'name': 'stream_password'
            },
            {
                'name': 'stream_privacy'
            },
            {
                'name': 'stream_title'
            },
            {
                'name': 'time_zone'
            },
        ]
    },
    '/users/{user_id}/live_events-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'allow_share_link'
            },
            {
                'name': 'auto_cc_enabled'
            },
            {
                'name': 'auto_cc_keywords'
            },
            {
                'name': 'auto_cc_lang'
            },
            {
                'name': 'automatically_title_stream'
            },
            {
                'name': 'chat_enabled'
            },
            {
                'name': 'content_rating'
            },
            {
                'name': 'dvr'
            },
            {
                'name': 'embed'
            },
            {
                'name': 'folder_uri'
            },
            {
                'name': 'interaction_tools_settings'
            },
            {
                'name': 'low_latency'
            },
            {
                'name': 'playlist_sort'
            },
            {
                'name': 'rtmp_preview'
            },
            {
                'name': 'schedule'
            },
            {
                'name': 'scheduled_playback'
            },
            {
                'name': 'stream_description'
            },
            {
                'name': 'stream_embed'
            },
            {
                'name': 'stream_password'
            },
            {
                'name': 'stream_privacy'
            },
            {
                'name': 'stream_title'
            },
            {
                'name': 'time_zone'
            },
        ]
    },
    '/me/live_events-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'allow_share_link'
            },
            {
                'name': 'auto_cc_enabled'
            },
            {
                'name': 'auto_cc_keywords'
            },
            {
                'name': 'auto_cc_lang'
            },
            {
                'name': 'automatically_title_stream'
            },
            {
                'name': 'chat_enabled'
            },
            {
                'name': 'content_rating'
            },
            {
                'name': 'dvr'
            },
            {
                'name': 'embed'
            },
            {
                'name': 'folder_uri'
            },
            {
                'name': 'interaction_tools_settings'
            },
            {
                'name': 'low_latency'
            },
            {
                'name': 'playlist_sort'
            },
            {
                'name': 'rtmp_preview'
            },
            {
                'name': 'schedule'
            },
            {
                'name': 'scheduled_playback'
            },
            {
                'name': 'stream_description'
            },
            {
                'name': 'stream_embed'
            },
            {
                'name': 'stream_password'
            },
            {
                'name': 'stream_privacy'
            },
            {
                'name': 'stream_title'
            },
            {
                'name': 'time_zone'
            },
        ]
    },
    '/live_events-DELETE': {
        'parameters': [
            {
                'name': 'password'
            },
        ]
    },
    '/me/live_events-DELETE': {
        'parameters': [
            {
                'name': 'password'
            },
        ]
    },
    '/users/{user_id}/live_events-DELETE': {
        'parameters': [
            {
                'name': 'password'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/live_events/{live_event_id}-DELETE': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}-DELETE': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/live_events/{live_event_id}-DELETE': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
        ]
    },
    '/me/live_events-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/live_events/{live_event_id}-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/me/live_events/{live_event_id}-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/live_events-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/users/{user_id}/live_events-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/live_events/{live_event_id}-PATCH': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'auto_cc_enabled'
            },
            {
                'name': 'auto_cc_keywords'
            },
            {
                'name': 'auto_cc_language'
            },
            {
                'name': 'automatically_title_stream'
            },
            {
                'name': 'chat_enabled'
            },
            {
                'name': 'content_rating'
            },
            {
                'name': 'dvr'
            },
            {
                'name': 'embed'
            },
            {
                'name': 'interaction_tools_settings'
            },
            {
                'name': 'playlist_sort'
            },
            {
                'name': 'schedule'
            },
            {
                'name': 'scheduled_playback'
            },
            {
                'name': 'stream_description'
            },
            {
                'name': 'stream_embed'
            },
            {
                'name': 'stream_mode'
            },
            {
                'name': 'stream_password'
            },
            {
                'name': 'stream_privacy'
            },
            {
                'name': 'stream_title'
            },
            {
                'name': 'time_zone'
            },
        ]
    },
    '/me/live_events/{live_event_id}-PATCH': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'auto_cc_enabled'
            },
            {
                'name': 'auto_cc_keywords'
            },
            {
                'name': 'auto_cc_language'
            },
            {
                'name': 'automatically_title_stream'
            },
            {
                'name': 'chat_enabled'
            },
            {
                'name': 'content_rating'
            },
            {
                'name': 'dvr'
            },
            {
                'name': 'embed'
            },
            {
                'name': 'interaction_tools_settings'
            },
            {
                'name': 'playlist_sort'
            },
            {
                'name': 'schedule'
            },
            {
                'name': 'scheduled_playback'
            },
            {
                'name': 'stream_description'
            },
            {
                'name': 'stream_embed'
            },
            {
                'name': 'stream_mode'
            },
            {
                'name': 'stream_password'
            },
            {
                'name': 'stream_privacy'
            },
            {
                'name': 'stream_title'
            },
            {
                'name': 'time_zone'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}-PATCH': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'auto_cc_enabled'
            },
            {
                'name': 'auto_cc_keywords'
            },
            {
                'name': 'auto_cc_language'
            },
            {
                'name': 'automatically_title_stream'
            },
            {
                'name': 'chat_enabled'
            },
            {
                'name': 'content_rating'
            },
            {
                'name': 'dvr'
            },
            {
                'name': 'embed'
            },
            {
                'name': 'interaction_tools_settings'
            },
            {
                'name': 'playlist_sort'
            },
            {
                'name': 'schedule'
            },
            {
                'name': 'scheduled_playback'
            },
            {
                'name': 'stream_description'
            },
            {
                'name': 'stream_embed'
            },
            {
                'name': 'stream_mode'
            },
            {
                'name': 'stream_password'
            },
            {
                'name': 'stream_privacy'
            },
            {
                'name': 'stream_title'
            },
            {
                'name': 'time_zone'
            },
        ]
    },
    '/me/live_events/{live_event_id}/m3u8_playback-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'max_fps_fhd'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/m3u8_playback-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'max_fps_fhd'
            },
        ]
    },
    '/live_events/{live_event_id}/activate-POST': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'cloud_composing_streaming'
            },
            {
                'name': 'streaming_start_requested'
            },
        ]
    },
    '/me/live_events/{live_event_id}/activate-POST': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'cloud_composing_streaming'
            },
            {
                'name': 'streaming_start_requested'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/activate-POST': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'cloud_composing_streaming'
            },
            {
                'name': 'streaming_start_requested'
            },
        ]
    },
    '/live_events/{live_event_id}/auto_cc-PATCH': {
        'parameters': [
            {
                'name': 'auto_cc_enabled'
            },
            {
                'name': 'live_event_id'
            },
            {
                'name': 'auto_cc_keywords'
            },
            {
                'name': 'auto_cc_lang'
            },
        ]
    },
    '/me/live_events/{live_event_id}/auto_cc-PATCH': {
        'parameters': [
            {
                'name': 'auto_cc_enabled'
            },
            {
                'name': 'live_event_id'
            },
            {
                'name': 'auto_cc_keywords'
            },
            {
                'name': 'auto_cc_lang'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/auto_cc-PATCH': {
        'parameters': [
            {
                'name': 'auto_cc_enabled'
            },
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'auto_cc_keywords'
            },
            {
                'name': 'auto_cc_lang'
            },
        ]
    },
    '/me/live_events/{live_event_id}/destinations-POST': {
        'parameters': [
            {
                'name': 'display_name'
            },
            {
                'name': 'service_name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'live_event_id'
            },
            {
                'name': 'is_enabled'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'provider_destination_id'
            },
            {
                'name': 'provider_video_id'
            },
            {
                'name': 'scheduled_at'
            },
            {
                'name': 'stream_key'
            },
            {
                'name': 'stream_url'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/destinations-POST': {
        'parameters': [
            {
                'name': 'display_name'
            },
            {
                'name': 'service_name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'is_enabled'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'provider_destination_id'
            },
            {
                'name': 'provider_video_id'
            },
            {
                'name': 'scheduled_at'
            },
            {
                'name': 'stream_key'
            },
            {
                'name': 'stream_url'
            },
        ]
    },
    '/me/videos/{video_id}/destinations-POST': {
        'parameters': [
            {
                'name': 'display_name'
            },
            {
                'name': 'service_name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'is_enabled'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'provider_destination_id'
            },
            {
                'name': 'provider_video_id'
            },
            {
                'name': 'scheduled_at'
            },
            {
                'name': 'stream_key'
            },
            {
                'name': 'stream_url'
            },
        ]
    },
    '/users/{user_id}/videos/{video_id}/destinations-POST': {
        'parameters': [
            {
                'name': 'display_name'
            },
            {
                'name': 'service_name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'is_enabled'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'provider_destination_id'
            },
            {
                'name': 'provider_video_id'
            },
            {
                'name': 'scheduled_at'
            },
            {
                'name': 'stream_key'
            },
            {
                'name': 'stream_url'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/ott_destinations-POST': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/destination/{destination_id}-DELETE': {
        'parameters': [
            {
                'name': 'destination_id'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/ott_destination/{destination_id}-DELETE': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/destinations-GET': {
        'parameters': [
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/destinations-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/videos/{video_id}/destinations-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/videos/{video_id}/destinations-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/ott_destinations-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/destination/{destination_id}-GET': {
        'parameters': [
            {
                'name': 'destination_id'
            },
        ]
    },
    '/me/live_events/{live_event_id}/destinations-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
        ]
    },
    '/users/{user_id}/destinations-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/destination/{destination_id}-PATCH': {
        'parameters': [
            {
                'name': 'destination_id'
            },
            {
                'name': 'display_name'
            },
            {
                'name': 'is_enabled'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'provider_destination_id'
            },
            {
                'name': 'service_name'
            },
            {
                'name': 'stream_key'
            },
            {
                'name': 'stream_url'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/live_events/{live_event_id}/end-POST': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'clip_id'
            },
        ]
    },
    '/me/live_events/{live_event_id}/end-POST': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'clip_id'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/end-POST': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'clip_id'
            },
        ]
    },
    '/live_events/{live_event_id}/low_latency-PATCH': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'low_latency'
            },
        ]
    },
    '/me/live_events/{live_event_id}/low_latency-PATCH': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'low_latency'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/low_latency-PATCH': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'low_latency'
            },
        ]
    },
    '/videos/{video_id}/sessions/status-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/live_events/{live_event_id}/pictures-POST': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'active'
            },
        ]
    },
    '/live_events/{live_event_id}/pictures-POST': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'active'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/pictures-POST': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'active'
            },
        ]
    },
    '/me/live_events/{live_event_id}/pictures/{thumbnail_id}-DELETE': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'thumbnail_id'
            },
        ]
    },
    '/live_events/{live_event_id}/pictures/{thumbnail_id}-DELETE': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'thumbnail_id'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/pictures/{thumbnail_id}-DELETE': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'thumbnail_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/pictures/{thumbnail_id}-PATCH': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'thumbnail_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'active'
            },
        ]
    },
    '/live_events/{live_event_id}/pictures/{thumbnail_id}-PATCH': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'thumbnail_id'
            },
            {
                'name': 'active'
            },
        ]
    },
    '/me/live_events/{live_event_id}/pictures-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
        ]
    },
    '/live_events/{live_event_id}/pictures-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/pictures-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/live_events/{live_event_id}/pictures/{thumbnail_id}-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'thumbnail_id'
            },
        ]
    },
    '/me/live_events/{live_event_id}/pictures/{thumbnail_id}-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'thumbnail_id'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/pictures/{thumbnail_id}-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'thumbnail_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/live_events/{live_event_id}/pictures/{thumbnail_id}-PATCH': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'thumbnail_id'
            },
            {
                'name': 'active'
            },
        ]
    },
    '/live_events/{live_event_id}/videos-POST': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'videos'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/videos-POST': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'videos'
            },
        ]
    },
    '/me/live_events/{live_event_id}/videos-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'containing_uri'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/videos/{video_id}-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/videos-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'containing_uri'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/live_events/{live_event_id}/videos-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'containing_uri'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/live_events/{live_event_id}/videos-DELETE': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'videos'
            },
        ]
    },
    '/users/{user_id}/live_events/{live_event_id}/videos-DELETE': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'videos'
            },
        ]
    },
    '/live_events/{live_event_id}/videos-DELETE': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'videos'
            },
        ]
    },
    '/live_events/{live_event_id}/videos/{video_id}-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/live_events/{live_event_id}/videos/{video_id}-GET': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/live_events/{live_event_id}/videos-POST': {
        'parameters': [
            {
                'name': 'live_event_id'
            },
            {
                'name': 'videos'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/backgrounds-POST': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/backgrounds/{background_id}-DELETE': {
        'parameters': [
            {
                'name': 'background_id'
            },
            {
                'name': 'ondemand_id'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/backgrounds/{background_id}-PATCH': {
        'parameters': [
            {
                'name': 'background_id'
            },
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'active'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/backgrounds-GET': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/backgrounds/{background_id}-GET': {
        'parameters': [
            {
                'name': 'background_id'
            },
            {
                'name': 'ondemand_id'
            },
        ]
    },
    '/me/ondemand/pages-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'content_rating'
            },
            {
                'name': 'name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'accepted_currencies'
            },
            {
                'name': 'buy'
            },
            {
                'name': 'domain_link'
            },
            {
                'name': 'episodes'
            },
            {
                'name': 'link'
            },
            {
                'name': 'rent'
            },
            {
                'name': 'subscription'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}-DELETE': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
        ]
    },
    '/me/ondemand/pages-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/users/{user_id}/ondemand/pages-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}-GET': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}-PATCH': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'link'
            },
            {
                'name': 'preorder'
            },
            {
                'name': 'publish'
            },
            {
                'name': 'publish_when_ready'
            },
        ]
    },
    '/users/{user_id}/ondemand/pages-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'content_rating'
            },
            {
                'name': 'name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'accepted_currencies'
            },
            {
                'name': 'buy'
            },
            {
                'name': 'domain_link'
            },
            {
                'name': 'episodes'
            },
            {
                'name': 'link'
            },
            {
                'name': 'rent'
            },
            {
                'name': 'subscription'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/genres/{genre_id}-PUT': {
        'parameters': [
            {
                'name': 'genre_id'
            },
            {
                'name': 'ondemand_id'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/genres/{genre_id}-GET': {
        'parameters': [
            {
                'name': 'genre_id'
            },
            {
                'name': 'ondemand_id'
            },
        ]
    },
    '/ondemand/genres-GET': {
        'parameters': [
        ]
    },
    '/ondemand/genres/{genre_id}/pages-GET': {
        'parameters': [
            {
                'name': 'genre_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/genres-GET': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
        ]
    },
    '/ondemand/genres/{genre_id}/pages/{ondemand_id}-GET': {
        'parameters': [
            {
                'name': 'genre_id'
            },
            {
                'name': 'ondemand_id'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/genres/{genre_id}-DELETE': {
        'parameters': [
            {
                'name': 'genre_id'
            },
            {
                'name': 'ondemand_id'
            },
        ]
    },
    '/ondemand/genres/{genre_id}-GET': {
        'parameters': [
            {
                'name': 'genre_id'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/pictures-POST': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/pictures-GET': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/pictures/{poster_id}-GET': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'poster_id'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/pictures/{poster_id}-PATCH': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'poster_id'
            },
            {
                'name': 'active'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/promotions-POST': {
        'parameters': [
            {
                'name': 'download'
            },
            {
                'name': 'stream_period'
            },
            {
                'name': 'total'
            },
            {
                'name': 'type'
            },
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'access_type'
            },
            {
                'name': 'code'
            },
            {
                'name': 'discount_type'
            },
            {
                'name': 'end_time'
            },
            {
                'name': 'label'
            },
            {
                'name': 'percent_off'
            },
            {
                'name': 'product_type'
            },
            {
                'name': 'start_time'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/promotions/{promotion_id}-DELETE': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'promotion_id'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/promotions-GET': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/promotions/{promotion_id}/codes-GET': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'promotion_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/promotions/{promotion_id}-GET': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'promotion_id'
            },
        ]
    },
    '/me/ondemand/purchases/{ondemand_id}-GET': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
        ]
    },
    '/me/ondemand/purchases-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/users/{user_id}/ondemand/purchases-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/regions-PUT': {
        'parameters': [
            {
                'name': 'countries'
            },
            {
                'name': 'ondemand_id'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/regions/{country}-PUT': {
        'parameters': [
            {
                'name': 'country'
            },
            {
                'name': 'ondemand_id'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/regions-GET': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/regions/{country}-GET': {
        'parameters': [
            {
                'name': 'country'
            },
            {
                'name': 'ondemand_id'
            },
        ]
    },
    '/ondemand/regions/{country}-GET': {
        'parameters': [
            {
                'name': 'country'
            },
        ]
    },
    '/ondemand/regions-GET': {
        'parameters': [
        ]
    },
    '/ondemand/pages/{ondemand_id}/regions-DELETE': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'countries'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/regions/{country}-DELETE': {
        'parameters': [
            {
                'name': 'country'
            },
            {
                'name': 'ondemand_id'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/seasons/{season_id}/videos-GET': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'season_id'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/seasons-GET': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/seasons/{season_id}-GET': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'season_id'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/videos/{video_id}-PUT': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'buy'
            },
            {
                'name': 'position'
            },
            {
                'name': 'release_year'
            },
            {
                'name': 'rent'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/videos-GET': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/videos/{video_id}-DELETE': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/ondemand/pages/{ondemand_id}/videos/{video_id}-GET': {
        'parameters': [
            {
                'name': 'ondemand_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/payment_methods/{payment_method_id}-GET': {
        'parameters': [
            {
                'name': 'payment_method_id'
            },
        ]
    },
    '/users/{user_id}/{subscription_id}-GET': {
        'parameters': [
            {
                'name': 'subscription_id'
            },
        ]
    },
    '/me/payment_methods-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'cardmember_name'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'show_disabled'
            },
        ]
    },
    '/me/portfolios-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/portfolios/{portfolio_id}-GET': {
        'parameters': [
            {
                'name': 'portfolio_id'
            },
        ]
    },
    '/users/{user_id}/portfolios/{portfolio_id}-GET': {
        'parameters': [
            {
                'name': 'portfolio_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/portfolios-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}-PUT': {
        'parameters': [
            {
                'name': 'portfolio_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/portfolios/{portfolio_id}/videos-GET': {
        'parameters': [
            {
                'name': 'portfolio_id'
            },
            {
                'name': 'containing_uri'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/users/{user_id}/portfolios/{portfolio_id}/videos-GET': {
        'parameters': [
            {
                'name': 'portfolio_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'containing_uri'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/portfolios/{portfolio_id}/videos/{video_id}-GET': {
        'parameters': [
            {
                'name': 'portfolio_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}-GET': {
        'parameters': [
            {
                'name': 'portfolio_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/portfolios/{portfolio_id}/videos/{video_id}-PUT': {
        'parameters': [
            {
                'name': 'portfolio_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/portfolios/{portfolio_id}/videos/{video_id}-DELETE': {
        'parameters': [
            {
                'name': 'portfolio_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}-DELETE': {
        'parameters': [
            {
                'name': 'portfolio_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}/logos-POST': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}/logos/{logo_id}-DELETE': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'logo_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}/logos/{logo_id}-GET': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'logo_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}/logos-GET': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}/logos/{logo_id}-PATCH': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'logo_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'active'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}/custom_thumbnails-POST': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}-DELETE': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'thumbnail_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}-GET': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'thumbnail_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}/custom_thumbnails-GET': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}-PATCH': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'thumbnail_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'active'
            },
        ]
    },
    '/me/albums-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'brand_color'
            },
            {
                'name': 'hide_from_vimeo'
            },
            {
                'name': 'hide_nav'
            },
            {
                'name': 'hide_upcoming'
            },
            {
                'name': 'layout'
            },
            {
                'name': 'password'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'review_mode'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'theme'
            },
        ]
    },
    '/me/albums/{album_id}-DELETE': {
        'parameters': [
            {
                'name': 'album_id'
            },
        ]
    },
    '/me/albums/{album_id}-PATCH': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'brand_color'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'hide_nav'
            },
            {
                'name': 'hide_upcoming'
            },
            {
                'name': 'layout'
            },
            {
                'name': 'name'
            },
            {
                'name': 'password'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'review_mode'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'theme'
            },
            {
                'name': 'url'
            },
            {
                'name': 'use_custom_domain'
            },
        ]
    },
    '/me/albums-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/albums/{album_id}-GET': {
        'parameters': [
            {
                'name': 'album_id'
            },
        ]
    },
    '/users/{user_id}/albums-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'brand_color'
            },
            {
                'name': 'hide_from_vimeo'
            },
            {
                'name': 'hide_nav'
            },
            {
                'name': 'hide_upcoming'
            },
            {
                'name': 'layout'
            },
            {
                'name': 'password'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'review_mode'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'theme'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}-GET': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}-DELETE': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}-PATCH': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'brand_color'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'hide_nav'
            },
            {
                'name': 'hide_upcoming'
            },
            {
                'name': 'layout'
            },
            {
                'name': 'name'
            },
            {
                'name': 'password'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'review_mode'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'theme'
            },
            {
                'name': 'url'
            },
            {
                'name': 'use_custom_domain'
            },
        ]
    },
    '/users/{user_id}/albums-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/users/{user_id}/albums-PATCH': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'album_item_uris'
            },
            {
                'name': 'album_uris'
            },
        ]
    },
    '/me/albums/{album_id}/videos/{video_id}-PUT': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}/videos/{video_id}-PUT': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/albums/{album_id}/videos/{video_id}/set_album_thumbnail-POST': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'time_code'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}/videos/{video_id}/set_album_thumbnail-POST': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'time_code'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}/videos-GET': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'containing_uri'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'page'
            },
            {
                'name': 'password'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'weak_search'
            },
        ]
    },
    '/me/albums/{album_id}/videos/{video_id}-GET': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}/videos/{video_id}-GET': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/videos/{video_id}/available_albums-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/albums/{album_id}/available_videos-GET': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/albums/{album_id}/videos-GET': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'containing_uri'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'page'
            },
            {
                'name': 'password'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'weak_search'
            },
        ]
    },
    '/me/albums/{album_id}/videos/{video_id}-DELETE': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}/videos/{video_id}-DELETE': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}/videos-PUT': {
        'parameters': [
            {
                'name': 'videos'
            },
            {
                'name': 'album_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/albums/{album_id}/videos-PUT': {
        'parameters': [
            {
                'name': 'videos'
            },
            {
                'name': 'album_id'
            },
        ]
    },
    '/me/albums/{album_id}/videos/{video_id}/set_featured_video-PATCH': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/albums/{album_id}/videos/{video_id}/set_featured_video-PATCH': {
        'parameters': [
            {
                'name': 'album_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/subscription_plans/{tier}-GET': {
        'parameters': [
            {
                'name': 'tier'
            },
        ]
    },
    '/tags/{word}-GET': {
        'parameters': [
            {
                'name': 'word'
            },
        ]
    },
    '/teammembers/{code}-GET': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/users/{user_id}/team_users/{team_user_id}-GET': {
        'parameters': [
            {
                'name': 'team_user_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/team/role-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/tutorial-GET': {
        'parameters': [
        ]
    },
    '/users/{user_id}/analytics-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'dimension'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter_content'
            },
            {
                'name': 'filter_countries'
            },
            {
                'name': 'filter_device_types'
            },
            {
                'name': 'filter_embed_domains'
            },
            {
                'name': 'filter_streaming_types'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'time_interval'
            },
        ]
    },
    '/me/analytics-GET': {
        'parameters': [
            {
                'name': 'dimension'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter_content'
            },
            {
                'name': 'filter_countries'
            },
            {
                'name': 'filter_device_types'
            },
            {
                'name': 'filter_embed_domains'
            },
            {
                'name': 'filter_streaming_types'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'time_interval'
            },
        ]
    },
    '/me-PATCH': {
        'parameters': [
            {
                'name': 'bio'
            },
            {
                'name': 'content_filter'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'link'
            },
            {
                'name': 'location'
            },
            {
                'name': 'name'
            },
            {
                'name': 'password'
            },
            {
                'name': 'videos'
            },
        ]
    },
    '/me-GET': {
        'parameters': [
        ]
    },
    '/users/{user_id}-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}-PATCH': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'bio'
            },
            {
                'name': 'content_filter'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'link'
            },
            {
                'name': 'location'
            },
            {
                'name': 'name'
            },
            {
                'name': 'password'
            },
            {
                'name': 'videos'
            },
        ]
    },
    '/users/{user_id}/feed-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/me/feed-GET': {
        'parameters': [
            {
                'name': 'offset'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/users/{user_id}/following/{follow_user_id}-GET': {
        'parameters': [
            {
                'name': 'follow_user_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/following/{follow_user_id}-GET': {
        'parameters': [
            {
                'name': 'follow_user_id'
            },
        ]
    },
    '/me/following-POST': {
        'parameters': [
            {
                'name': 'users'
            },
        ]
    },
    '/me/following/{follow_user_id}-PUT': {
        'parameters': [
            {
                'name': 'follow_user_id'
            },
        ]
    },
    '/users/{user_id}/followers-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/followers-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/users/{user_id}/following-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/following-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/following/{follow_user_id}-DELETE': {
        'parameters': [
            {
                'name': 'follow_user_id'
            },
        ]
    },
    '/users/{user_id}/following/{follow_user_id}-PUT': {
        'parameters': [
            {
                'name': 'follow_user_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/following/{follow_user_id}-DELETE': {
        'parameters': [
            {
                'name': 'follow_user_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/following-POST': {
        'parameters': [
            {
                'name': 'users'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/me/pictures-POST': {
        'parameters': [
        ]
    },
    '/me/pictures/{portraitset_id}-PATCH': {
        'parameters': [
            {
                'name': 'portraitset_id'
            },
            {
                'name': 'active'
            },
        ]
    },
    '/me/pictures/{portraitset_id}-GET': {
        'parameters': [
            {
                'name': 'portraitset_id'
            },
        ]
    },
    '/me/pictures-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/users/{user_id}/pictures-POST': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/pictures/{portraitset_id}-GET': {
        'parameters': [
            {
                'name': 'portraitset_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/pictures/{portraitset_id}-DELETE': {
        'parameters': [
            {
                'name': 'portraitset_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/pictures/{portraitset_id}-PATCH': {
        'parameters': [
            {
                'name': 'portraitset_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'active'
            },
        ]
    },
    '/users/{user_id}/pictures-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/me/pictures/{portraitset_id}-DELETE': {
        'parameters': [
            {
                'name': 'portraitset_id'
            },
        ]
    },
    '/users-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/watched/videos-DELETE': {
        'parameters': [
        ]
    },
    '/me/watched/videos/{video_id}-DELETE': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/watched/videos-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/animated_thumbsets-POST': {
        'parameters': [
            {
                'name': 'duration'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'start_time'
            },
        ]
    },
    '/videos/{video_id}/animated_thumbsets/{picture_id}-DELETE': {
        'parameters': [
            {
                'name': 'picture_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/animated_thumbsets-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/animated_thumbsets/{picture_id}/status-GET': {
        'parameters': [
            {
                'name': 'picture_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/animated_thumbsets/{picture_id}-GET': {
        'parameters': [
            {
                'name': 'picture_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/chapters-POST': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'active_thumbnail_uri'
            },
            {
                'name': 'thumbnail_uris'
            },
            {
                'name': 'timecode'
            },
        ]
    },
    '/videos/{video_id}/chapters/{chapter_id}-GET': {
        'parameters': [
            {
                'name': 'chapter_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/chapters/{chapter_id}-DELETE': {
        'parameters': [
            {
                'name': 'chapter_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/chapters/{chapter_id}-PATCH': {
        'parameters': [
            {
                'name': 'chapter_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'active_thumbnail_uri'
            },
            {
                'name': 'timecode'
            },
        ]
    },
    '/videos/{video_id}/chapters-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/chapters/{chapter_id}/pictures/{uid}-DELETE': {
        'parameters': [
            {
                'name': 'chapter_id'
            },
            {
                'name': 'uid'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/chapters/temporary/pictures-POST': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'timecode'
            },
        ]
    },
    '/videos/{video_id}/chapters/{chapter_id}/pictures-POST': {
        'parameters': [
            {
                'name': 'chapter_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'timecode'
            },
        ]
    },
    '/videos/{video_id}/chapters/{chapter_id}/pictures-GET': {
        'parameters': [
            {
                'name': 'chapter_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/chapters/temporary/pictures/{uid}-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/chapters/{chapter_id}/pictures/{uid}-GET': {
        'parameters': [
            {
                'name': 'chapter_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/chapters/{chapter_id}/pictures/{uid}-PATCH': {
        'parameters': [
            {
                'name': 'chapter_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'active'
            },
        ]
    },
    '/contentratings-GET': {
        'parameters': [
        ]
    },
    '/creativecommons-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/credits-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'name'
            },
            {
                'name': 'role'
            },
            {
                'name': 'user_uri'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/channels/{channel_id}/videos/{video_id}/credits-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'name'
            },
            {
                'name': 'role'
            },
            {
                'name': 'user_uri'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/credits/{credit_id}-DELETE': {
        'parameters': [
            {
                'name': 'credit_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/credits/{credit_id}-PATCH': {
        'parameters': [
            {
                'name': 'credit_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'role'
            },
        ]
    },
    '/channels/{channel_id}/videos/{video_id}/credits-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/videos/{video_id}/credits-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/videos/{video_id}/credits/{credit_id}-GET': {
        'parameters': [
            {
                'name': 'credit_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/credits/available_users-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/videos/{video_id}/privacy/domains/{domain}-PUT': {
        'parameters': [
            {
                'name': 'domain'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/privacy/domains-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/privacy/domains/{domain}-DELETE': {
        'parameters': [
            {
                'name': 'domain'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/appearances-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/users/{user_id}/videos/{video_id}-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/videos/{video_id}-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/videos-DELETE': {
        'parameters': [
            {
                'name': 'uris'
            },
        ]
    },
    '/me/videos-GET': {
        'parameters': [
            {
                'name': 'containing_uri'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'filter_playable'
            },
            {
                'name': 'filter_screen_recorded'
            },
            {
                'name': 'filter_tag'
            },
            {
                'name': 'filter_tag_all_of'
            },
            {
                'name': 'filter_tag_exclude'
            },
            {
                'name': 'include_team_content'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'query_fields'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/appearances-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/videos/{video_id}-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}-DELETE': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}-PATCH': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'content_rating'
            },
            {
                'name': 'custom_url'
            },
            {
                'name': 'embed'
            },
            {
                'name': 'embed_domains'
            },
            {
                'name': 'embed_domains_add'
            },
            {
                'name': 'embed_domains_delete'
            },
            {
                'name': 'hide_from_vimeo'
            },
            {
                'name': 'license'
            },
            {
                'name': 'locale'
            },
            {
                'name': 'name'
            },
            {
                'name': 'password'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'review_page'
            },
            {
                'name': 'spatial'
            },
        ]
    },
    '/users/{user_id}/videos-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'containing_uri'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'filter_playable'
            },
            {
                'name': 'filter_screen_recorded'
            },
            {
                'name': 'filter_tag'
            },
            {
                'name': 'filter_tag_all_of'
            },
            {
                'name': 'filter_tag_exclude'
            },
            {
                'name': 'include_team_content'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'query_fields'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/users/{user_id}/videos-DELETE': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'uris'
            },
        ]
    },
    '/videos-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'links'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'uris'
            },
        ]
    },
    '/videos/{video_id}/fragments-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/fragments-PUT': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/fragments-DELETE': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/languages-GET': {
        'parameters': [
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/me/videos/{video_id}/m3u8_playback-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/videos/{video_id}/m3u8_playback-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/trim-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/trim-POST': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'trim_end'
            },
            {
                'name': 'trim_start'
            },
        ]
    },
    '/videos/{video_id}/videos-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/albums-PATCH': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'add'
            },
            {
                'name': 'remove'
            },
        ]
    },
    '/videos/{video_id}/albums-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/tags-PUT': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/tags/{word}-PUT': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'word'
            },
        ]
    },
    '/videos/{video_id}/tags/{word}-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'word'
            },
        ]
    },
    '/tags/{word}/videos-GET': {
        'parameters': [
            {
                'name': 'word'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/videos/{video_id}/tags-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/tags/{word}-DELETE': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'word'
            },
        ]
    },
    '/videos/{video_id}/texttracks-POST': {
        'parameters': [
            {
                'name': 'language'
            },
            {
                'name': 'name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'active'
            },
            {
                'name': 'is_auto_generated'
            },
            {
                'name': 'is_edited'
            },
        ]
    },
    '/channels/{channel_id}/videos/{video_id}/texttracks-POST': {
        'parameters': [
            {
                'name': 'language'
            },
            {
                'name': 'name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'active'
            },
            {
                'name': 'is_auto_generated'
            },
            {
                'name': 'is_edited'
            },
        ]
    },
    '/videos/{video_id}/texttracks/{texttrack_id}-DELETE': {
        'parameters': [
            {
                'name': 'texttrack_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/texttracks/{texttrack_id}-PATCH': {
        'parameters': [
            {
                'name': 'texttrack_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'active'
            },
            {
                'name': 'language'
            },
            {
                'name': 'name'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/channels/{channel_id}/videos/{video_id}/texttracks-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/texttracks-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/texttracks/{texttrack_id}-GET': {
        'parameters': [
            {
                'name': 'texttrack_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/channels/{channel_id}/videos/{video_id}/pictures-POST': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'active'
            },
            {
                'name': 'time'
            },
        ]
    },
    '/videos/{video_id}/pictures-POST': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'active'
            },
            {
                'name': 'time'
            },
        ]
    },
    '/videos/{video_id}/pictures/{picture_id}-DELETE': {
        'parameters': [
            {
                'name': 'picture_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/pictures/{picture_id}-PATCH': {
        'parameters': [
            {
                'name': 'picture_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'active'
            },
        ]
    },
    '/channels/{channel_id}/videos/{video_id}/pictures-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/pictures-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/pictures/{picture_id}-GET': {
        'parameters': [
            {
                'name': 'picture_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/transcripts/{texttrack_id}-GET': {
        'parameters': [
            {
                'name': 'texttrack_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/channels/{channel_id}/videos/{video_id}/privacy/users-PUT': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/privacy/users-PUT': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/privacy/users/{user_id}-PUT': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/channels/{channel_id}/videos/{video_id}/privacy/users-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/privacy/users-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/privacy/users/{user_id}-DELETE': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/videos-POST': {
        'parameters': [
            {
                'name': 'upload'
            },
            {
                'name': 'description'
            },
            {
                'name': 'content_rating'
            },
            {
                'name': 'embed'
            },
            {
                'name': 'embed_domains'
            },
            {
                'name': 'folder_uri'
            },
            {
                'name': 'hide_from_vimeo'
            },
            {
                'name': 'license'
            },
            {
                'name': 'locale'
            },
            {
                'name': 'name'
            },
            {
                'name': 'password'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'review_page'
            },
            {
                'name': 'spatial'
            },
        ]
    },
    '/users/{user_id}/uploads/{upload_id}-DELETE': {
        'parameters': [
            {
                'name': 'upload_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'signature'
            },
            {
                'name': 'video_file_id'
            },
        ]
    },
    '/users/{user_id}/uploads/{upload_id}-GET': {
        'parameters': [
            {
                'name': 'upload_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/videos-POST': {
        'parameters': [
            {
                'name': 'upload'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'content_rating'
            },
            {
                'name': 'embed'
            },
            {
                'name': 'embed_domains'
            },
            {
                'name': 'folder_uri'
            },
            {
                'name': 'hide_from_vimeo'
            },
            {
                'name': 'license'
            },
            {
                'name': 'locale'
            },
            {
                'name': 'name'
            },
            {
                'name': 'password'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'review_page'
            },
            {
                'name': 'spatial'
            },
        ]
    },
    '/videos/{video_id}/versions-POST': {
        'parameters': [
            {
                'name': 'file_name'
            },
            {
                'name': 'upload'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/versions/{version_id}-DELETE': {
        'parameters': [
            {
                'name': 'version_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/versions/{version_id}-PATCH': {
        'parameters': [
            {
                'name': 'version_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'is_current'
            },
        ]
    },
    '/channels/{channel_id}/videos/{video_id}/versions-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/versions-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/versions/{version_id}-GET': {
        'parameters': [
            {
                'name': 'version_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/channels/{channel_id}/videos/{video_id}/comments-POST': {
        'parameters': [
            {
                'name': 'text'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/comments-POST': {
        'parameters': [
            {
                'name': 'text'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/comments/{comment_id}-GET': {
        'parameters': [
            {
                'name': 'comment_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/comments/{comment_id}-DELETE': {
        'parameters': [
            {
                'name': 'comment_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/comments/{comment_id}-PATCH': {
        'parameters': [
            {
                'name': 'text'
            },
            {
                'name': 'comment_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/videos/{video_id}/comments-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/comments/{comment_id}/replies-POST': {
        'parameters': [
            {
                'name': 'text'
            },
            {
                'name': 'comment_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/channels/{channel_id}/videos/{video_id}/comments-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/videos/{video_id}/comments/{comment_id}/replies-GET': {
        'parameters': [
            {
                'name': 'comment_id'
            },
            {
                'name': 'video_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/me/watchlater/{video_id}-PUT': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/watchlater/{video_id}-PUT': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/watchlater/{video_id}-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/watchlater/{video_id}-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/watchlater-GET': {
        'parameters': [
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/users/{user_id}/watchlater-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'filter_embeddable'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'query'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/watchlater/{video_id}-DELETE': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/users/{user_id}/watchlater/{video_id}-DELETE': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'video_id'
            },
        ]
    },
    '/me/webinars/{webinar_id}/email_settings-PATCH': {
        'parameters': [
            {
                'name': 'webinar_id'
            },
            {
                'name': 'accent_color'
            },
            {
                'name': 'custom_link'
            },
            {
                'name': 'email_event_reminder_24_hrs'
            },
            {
                'name': 'email_post_event_thank_you'
            },
            {
                'name': 'email_preferences'
            },
            {
                'name': 'email_registration_confirmation'
            },
            {
                'name': 'from'
            },
            {
                'name': 'logo_uri'
            },
            {
                'name': 'reply_email'
            },
            {
                'name': 'sender_address'
            },
            {
                'name': 'sender_policy_url'
            },
            {
                'name': 'use_custom_link'
            },
            {
                'name': 'use_reply_email'
            },
            {
                'name': 'use_sender_address'
            },
            {
                'name': 'use_sender_policy_url'
            },
        ]
    },
    '/users/{user_id}/webinars/{webinar_id}/email_settings-PATCH': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'webinar_id'
            },
            {
                'name': 'accent_color'
            },
            {
                'name': 'custom_link'
            },
            {
                'name': 'email_event_reminder_24_hrs'
            },
            {
                'name': 'email_post_event_thank_you'
            },
            {
                'name': 'email_preferences'
            },
            {
                'name': 'email_registration_confirmation'
            },
            {
                'name': 'from'
            },
            {
                'name': 'logo_uri'
            },
            {
                'name': 'reply_email'
            },
            {
                'name': 'sender_address'
            },
            {
                'name': 'sender_policy_url'
            },
            {
                'name': 'use_custom_link'
            },
            {
                'name': 'use_reply_email'
            },
            {
                'name': 'use_sender_address'
            },
            {
                'name': 'use_sender_policy_url'
            },
        ]
    },
    '/me/webinars/{webinar_id}/email_settings-GET': {
        'parameters': [
            {
                'name': 'webinar_id'
            },
        ]
    },
    '/users/{user_id}/webinars/{webinar_id}/email_settings-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'webinar_id'
            },
        ]
    },
    '/me/webinars-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'email_settings'
            },
            {
                'name': 'folder_uri'
            },
            {
                'name': 'password'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'schedule'
            },
            {
                'name': 'time_zone'
            },
        ]
    },
    '/me/webinars/{webinar_id}-GET': {
        'parameters': [
            {
                'name': 'webinar_id'
            },
        ]
    },
    '/webinars/{webinar_id}-GET': {
        'parameters': [
            {
                'name': 'webinar_id'
            },
        ]
    },
    '/me/webinars/{webinar_id}-PATCH': {
        'parameters': [
            {
                'name': 'webinar_id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'email_settings'
            },
            {
                'name': 'password'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'schedule'
            },
            {
                'name': 'status'
            },
            {
                'name': 'time_zone'
            },
        ]
    },
    '/users/{user_id}/webinars-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'email_settings'
            },
            {
                'name': 'folder_uri'
            },
            {
                'name': 'password'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'schedule'
            },
            {
                'name': 'time_zone'
            },
        ]
    },
    '/users/{user_id}/webinars/{webinar_id}-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'webinar_id'
            },
        ]
    },
    '/users/{user_id}/webinars/{webinar_id}-PATCH': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'webinar_id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'email_settings'
            },
            {
                'name': 'password'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'schedule'
            },
            {
                'name': 'status'
            },
            {
                'name': 'time_zone'
            },
        ]
    },
    '/me/webinars/{webinar_id}/registrants-PUT': {
        'parameters': [
            {
                'name': 'webinar_id'
            },
            {
                'name': 'registrants'
            },
        ]
    },
    '/users/{user_id}/webinars/{webinar_id}/registrants-PUT': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'webinar_id'
            },
            {
                'name': 'registrants'
            },
        ]
    },
    '/me/webinars/{webinar_id}/registrants/{registrant_id}-DELETE': {
        'parameters': [
            {
                'name': 'registrant_id'
            },
            {
                'name': 'webinar_id'
            },
        ]
    },
    '/users/{user_id}/webinars/{webinar_id}/registrants/{registrant_id}-DELETE': {
        'parameters': [
            {
                'name': 'registrant_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'webinar_id'
            },
        ]
    },
    '/me/webinars/{webinar_id}/registrants-GET': {
        'parameters': [
            {
                'name': 'webinar_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/users/{user_id}/webinars/{webinar_id}/registrants-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'webinar_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/me/webinars/{webinar_id}/registrants/{registrant_id}-PATCH': {
        'parameters': [
            {
                'name': 'registrant_id'
            },
            {
                'name': 'webinar_id'
            },
            {
                'name': 'is_blocked'
            },
        ]
    },
    '/users/{user_id}/webinars/{webinar_id}/registrants/{registrant_id}-PATCH': {
        'parameters': [
            {
                'name': 'registrant_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'webinar_id'
            },
            {
                'name': 'is_blocked'
            },
        ]
    },
};
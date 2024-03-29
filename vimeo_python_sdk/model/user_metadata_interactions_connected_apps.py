# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from vimeo_python_sdk import schemas  # noqa: F401


class UserMetadataInteractionsConnectedApps(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "is_connected",
            "options",
            "all_scopes",
            "uri",
            "needed_scopes",
        }
        
        class properties:
            all_scopes = schemas.DictSchema
            is_connected = schemas.BoolSchema
            needed_scopes = schemas.DictSchema
        
            @staticmethod
            def options() -> typing.Type['UserMetadataInteractionsConnectedAppsOptions']:
                return UserMetadataInteractionsConnectedAppsOptions
            uri = schemas.StrSchema
            __annotations__ = {
                "all_scopes": all_scopes,
                "is_connected": is_connected,
                "needed_scopes": needed_scopes,
                "options": options,
                "uri": uri,
            }
    
    is_connected: MetaOapg.properties.is_connected
    options: 'UserMetadataInteractionsConnectedAppsOptions'
    all_scopes: MetaOapg.properties.all_scopes
    uri: MetaOapg.properties.uri
    needed_scopes: MetaOapg.properties.needed_scopes
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["all_scopes"]) -> MetaOapg.properties.all_scopes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_connected"]) -> MetaOapg.properties.is_connected: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["needed_scopes"]) -> MetaOapg.properties.needed_scopes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> 'UserMetadataInteractionsConnectedAppsOptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["all_scopes", "is_connected", "needed_scopes", "options", "uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["all_scopes"]) -> MetaOapg.properties.all_scopes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_connected"]) -> MetaOapg.properties.is_connected: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["needed_scopes"]) -> MetaOapg.properties.needed_scopes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> 'UserMetadataInteractionsConnectedAppsOptions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["all_scopes", "is_connected", "needed_scopes", "options", "uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        is_connected: typing.Union[MetaOapg.properties.is_connected, bool, ],
        options: 'UserMetadataInteractionsConnectedAppsOptions',
        all_scopes: typing.Union[MetaOapg.properties.all_scopes, dict, frozendict.frozendict, ],
        uri: typing.Union[MetaOapg.properties.uri, str, ],
        needed_scopes: typing.Union[MetaOapg.properties.needed_scopes, dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserMetadataInteractionsConnectedApps':
        return super().__new__(
            cls,
            *args,
            is_connected=is_connected,
            options=options,
            all_scopes=all_scopes,
            uri=uri,
            needed_scopes=needed_scopes,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.user_metadata_interactions_connected_apps_options import UserMetadataInteractionsConnectedAppsOptions

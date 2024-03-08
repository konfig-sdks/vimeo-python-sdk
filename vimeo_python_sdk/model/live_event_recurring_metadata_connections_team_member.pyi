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


class LiveEventRecurringMetadataConnectionsTeamMember(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Information about the team member who owns the event.
    """


    class MetaOapg:
        required = {
            "options",
            "uri",
        }
        
        class properties:
        
            @staticmethod
            def options() -> typing.Type['LiveEventRecurringMetadataConnectionsTeamMemberOptions']:
                return LiveEventRecurringMetadataConnectionsTeamMemberOptions
            uri = schemas.StrSchema
            __annotations__ = {
                "options": options,
                "uri": uri,
            }

    
    options: 'LiveEventRecurringMetadataConnectionsTeamMemberOptions'
    uri: MetaOapg.properties.uri
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> 'LiveEventRecurringMetadataConnectionsTeamMemberOptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["options", "uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> 'LiveEventRecurringMetadataConnectionsTeamMemberOptions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["options", "uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LiveEventRecurringMetadataConnectionsTeamMember':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.live_event_recurring_metadata_connections_team_member_options import LiveEventRecurringMetadataConnectionsTeamMemberOptions

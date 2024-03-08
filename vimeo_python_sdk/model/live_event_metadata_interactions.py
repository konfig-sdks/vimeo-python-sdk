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


class LiveEventMetadataInteractions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A list of resource URIs related to the event.
    """


    class MetaOapg:
        required = {
            "edit",
            "activate",
            "delete",
        }
        
        class properties:
        
            @staticmethod
            def activate() -> typing.Type['LiveEventMetadataInteractionsActivate']:
                return LiveEventMetadataInteractionsActivate
        
            @staticmethod
            def delete() -> typing.Type['LiveEventMetadataInteractionsDelete']:
                return LiveEventMetadataInteractionsDelete
        
            @staticmethod
            def edit() -> typing.Type['LiveEventMetadataInteractionsEdit']:
                return LiveEventMetadataInteractionsEdit
            __annotations__ = {
                "activate": activate,
                "delete": delete,
                "edit": edit,
            }
    
    edit: 'LiveEventMetadataInteractionsEdit'
    activate: 'LiveEventMetadataInteractionsActivate'
    delete: 'LiveEventMetadataInteractionsDelete'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activate"]) -> 'LiveEventMetadataInteractionsActivate': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delete"]) -> 'LiveEventMetadataInteractionsDelete': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edit"]) -> 'LiveEventMetadataInteractionsEdit': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["activate", "delete", "edit", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activate"]) -> 'LiveEventMetadataInteractionsActivate': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delete"]) -> 'LiveEventMetadataInteractionsDelete': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edit"]) -> 'LiveEventMetadataInteractionsEdit': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["activate", "delete", "edit", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        edit: 'LiveEventMetadataInteractionsEdit',
        activate: 'LiveEventMetadataInteractionsActivate',
        delete: 'LiveEventMetadataInteractionsDelete',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LiveEventMetadataInteractions':
        return super().__new__(
            cls,
            *args,
            edit=edit,
            activate=activate,
            delete=delete,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.live_event_metadata_interactions_activate import LiveEventMetadataInteractionsActivate
from vimeo_python_sdk.model.live_event_metadata_interactions_delete import LiveEventMetadataInteractionsDelete
from vimeo_python_sdk.model.live_event_metadata_interactions_edit import LiveEventMetadataInteractionsEdit
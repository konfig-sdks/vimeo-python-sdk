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


class ProjectMetadataInteractions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A list of permitted interactions related to the folder.
    """


    class MetaOapg:
        required = {
            "move_video",
            "view",
            "delete_video",
            "edit",
            "add_subfolder",
            "upload_video",
            "edit_settings",
            "invite",
            "delete",
        }
        
        class properties:
        
            @staticmethod
            def add_subfolder() -> typing.Type['ProjectMetadataInteractionsAddSubfolder']:
                return ProjectMetadataInteractionsAddSubfolder
        
            @staticmethod
            def delete() -> typing.Type['ProjectMetadataInteractionsDelete']:
                return ProjectMetadataInteractionsDelete
        
            @staticmethod
            def delete_video() -> typing.Type['ProjectMetadataInteractionsDeleteVideo']:
                return ProjectMetadataInteractionsDeleteVideo
        
            @staticmethod
            def edit() -> typing.Type['ProjectMetadataInteractionsEdit']:
                return ProjectMetadataInteractionsEdit
        
            @staticmethod
            def edit_settings() -> typing.Type['ProjectMetadataInteractionsEditSettings']:
                return ProjectMetadataInteractionsEditSettings
        
            @staticmethod
            def invite() -> typing.Type['ProjectMetadataInteractionsInvite']:
                return ProjectMetadataInteractionsInvite
        
            @staticmethod
            def move_video() -> typing.Type['ProjectMetadataInteractionsMoveVideo']:
                return ProjectMetadataInteractionsMoveVideo
        
            @staticmethod
            def upload_video() -> typing.Type['ProjectMetadataInteractionsUploadVideo']:
                return ProjectMetadataInteractionsUploadVideo
        
            @staticmethod
            def view() -> typing.Type['ProjectMetadataInteractionsView']:
                return ProjectMetadataInteractionsView
            __annotations__ = {
                "add_subfolder": add_subfolder,
                "delete": delete,
                "delete_video": delete_video,
                "edit": edit,
                "edit_settings": edit_settings,
                "invite": invite,
                "move_video": move_video,
                "upload_video": upload_video,
                "view": view,
            }
    
    move_video: 'ProjectMetadataInteractionsMoveVideo'
    view: 'ProjectMetadataInteractionsView'
    delete_video: 'ProjectMetadataInteractionsDeleteVideo'
    edit: 'ProjectMetadataInteractionsEdit'
    add_subfolder: 'ProjectMetadataInteractionsAddSubfolder'
    upload_video: 'ProjectMetadataInteractionsUploadVideo'
    edit_settings: 'ProjectMetadataInteractionsEditSettings'
    invite: 'ProjectMetadataInteractionsInvite'
    delete: 'ProjectMetadataInteractionsDelete'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["add_subfolder"]) -> 'ProjectMetadataInteractionsAddSubfolder': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delete"]) -> 'ProjectMetadataInteractionsDelete': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delete_video"]) -> 'ProjectMetadataInteractionsDeleteVideo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edit"]) -> 'ProjectMetadataInteractionsEdit': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edit_settings"]) -> 'ProjectMetadataInteractionsEditSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invite"]) -> 'ProjectMetadataInteractionsInvite': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["move_video"]) -> 'ProjectMetadataInteractionsMoveVideo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upload_video"]) -> 'ProjectMetadataInteractionsUploadVideo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["view"]) -> 'ProjectMetadataInteractionsView': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["add_subfolder", "delete", "delete_video", "edit", "edit_settings", "invite", "move_video", "upload_video", "view", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["add_subfolder"]) -> 'ProjectMetadataInteractionsAddSubfolder': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delete"]) -> 'ProjectMetadataInteractionsDelete': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delete_video"]) -> 'ProjectMetadataInteractionsDeleteVideo': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edit"]) -> 'ProjectMetadataInteractionsEdit': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edit_settings"]) -> 'ProjectMetadataInteractionsEditSettings': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invite"]) -> 'ProjectMetadataInteractionsInvite': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["move_video"]) -> 'ProjectMetadataInteractionsMoveVideo': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upload_video"]) -> 'ProjectMetadataInteractionsUploadVideo': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["view"]) -> 'ProjectMetadataInteractionsView': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["add_subfolder", "delete", "delete_video", "edit", "edit_settings", "invite", "move_video", "upload_video", "view", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        move_video: 'ProjectMetadataInteractionsMoveVideo',
        view: 'ProjectMetadataInteractionsView',
        delete_video: 'ProjectMetadataInteractionsDeleteVideo',
        edit: 'ProjectMetadataInteractionsEdit',
        add_subfolder: 'ProjectMetadataInteractionsAddSubfolder',
        upload_video: 'ProjectMetadataInteractionsUploadVideo',
        edit_settings: 'ProjectMetadataInteractionsEditSettings',
        invite: 'ProjectMetadataInteractionsInvite',
        delete: 'ProjectMetadataInteractionsDelete',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectMetadataInteractions':
        return super().__new__(
            cls,
            *args,
            move_video=move_video,
            view=view,
            delete_video=delete_video,
            edit=edit,
            add_subfolder=add_subfolder,
            upload_video=upload_video,
            edit_settings=edit_settings,
            invite=invite,
            delete=delete,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.project_metadata_interactions_add_subfolder import ProjectMetadataInteractionsAddSubfolder
from vimeo_python_sdk.model.project_metadata_interactions_delete import ProjectMetadataInteractionsDelete
from vimeo_python_sdk.model.project_metadata_interactions_delete_video import ProjectMetadataInteractionsDeleteVideo
from vimeo_python_sdk.model.project_metadata_interactions_edit import ProjectMetadataInteractionsEdit
from vimeo_python_sdk.model.project_metadata_interactions_edit_settings import ProjectMetadataInteractionsEditSettings
from vimeo_python_sdk.model.project_metadata_interactions_invite import ProjectMetadataInteractionsInvite
from vimeo_python_sdk.model.project_metadata_interactions_move_video import ProjectMetadataInteractionsMoveVideo
from vimeo_python_sdk.model.project_metadata_interactions_upload_video import ProjectMetadataInteractionsUploadVideo
from vimeo_python_sdk.model.project_metadata_interactions_view import ProjectMetadataInteractionsView

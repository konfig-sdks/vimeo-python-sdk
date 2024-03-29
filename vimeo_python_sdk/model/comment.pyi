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


class Comment(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "metadata",
            "replies",
            "created_on",
            "resource_key",
            "link",
            "text",
            "type",
            "uri",
            "user",
        }
        
        class properties:
            created_on = schemas.StrSchema
            link = schemas.StrSchema
        
            @staticmethod
            def metadata() -> typing.Type['CommentMetadata']:
                return CommentMetadata
            
            
            class replies(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Reply']:
                        return Reply
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Reply'], typing.List['Reply']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'replies':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Reply':
                    return super().__getitem__(i)
            resource_key = schemas.StrSchema
            text = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def VIDEO(cls):
                    return cls("video")
            uri = schemas.StrSchema
        
            @staticmethod
            def user() -> typing.Type['User']:
                return User
            __annotations__ = {
                "created_on": created_on,
                "link": link,
                "metadata": metadata,
                "replies": replies,
                "resource_key": resource_key,
                "text": text,
                "type": type,
                "uri": uri,
                "user": user,
            }
    
    metadata: 'CommentMetadata'
    replies: MetaOapg.properties.replies
    created_on: MetaOapg.properties.created_on
    resource_key: MetaOapg.properties.resource_key
    link: MetaOapg.properties.link
    text: MetaOapg.properties.text
    type: MetaOapg.properties.type
    uri: MetaOapg.properties.uri
    user: 'User'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_on"]) -> MetaOapg.properties.created_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'CommentMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["replies"]) -> MetaOapg.properties.replies: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resource_key"]) -> MetaOapg.properties.resource_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'User': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["created_on", "link", "metadata", "replies", "resource_key", "text", "type", "uri", "user", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_on"]) -> MetaOapg.properties.created_on: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> 'CommentMetadata': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["replies"]) -> MetaOapg.properties.replies: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resource_key"]) -> MetaOapg.properties.resource_key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> 'User': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["created_on", "link", "metadata", "replies", "resource_key", "text", "type", "uri", "user", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        metadata: 'CommentMetadata',
        replies: typing.Union[MetaOapg.properties.replies, list, tuple, ],
        created_on: typing.Union[MetaOapg.properties.created_on, str, ],
        resource_key: typing.Union[MetaOapg.properties.resource_key, str, ],
        link: typing.Union[MetaOapg.properties.link, str, ],
        text: typing.Union[MetaOapg.properties.text, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        uri: typing.Union[MetaOapg.properties.uri, str, ],
        user: 'User',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Comment':
        return super().__new__(
            cls,
            *args,
            metadata=metadata,
            replies=replies,
            created_on=created_on,
            resource_key=resource_key,
            link=link,
            text=text,
            type=type,
            uri=uri,
            user=user,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.comment_metadata import CommentMetadata
from vimeo_python_sdk.model.reply import Reply
from vimeo_python_sdk.model.user import User

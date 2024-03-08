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


class UploadVideoRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "upload",
        }
        
        class properties:
        
            @staticmethod
            def upload() -> typing.Type['UploadVideoRequestUpload']:
                return UploadVideoRequestUpload
            description = schemas.StrSchema
        
            @staticmethod
            def content_rating() -> typing.Type['UploadVideoRequestContentRating']:
                return UploadVideoRequestContentRating
        
            @staticmethod
            def embed() -> typing.Type['UploadVideoRequestEmbed']:
                return UploadVideoRequestEmbed
        
            @staticmethod
            def embed_domains() -> typing.Type['UploadVideoRequestEmbedDomains']:
                return UploadVideoRequestEmbedDomains
            folder_uri = schemas.StrSchema
            hide_from_vimeo = schemas.BoolSchema
            
            
            class license(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BY(cls):
                    return cls("by")
                
                @schemas.classproperty
                def BYNC(cls):
                    return cls("by-nc")
                
                @schemas.classproperty
                def BYNCND(cls):
                    return cls("by-nc-nd")
                
                @schemas.classproperty
                def BYNCSA(cls):
                    return cls("by-nc-sa")
                
                @schemas.classproperty
                def BYND(cls):
                    return cls("by-nd")
                
                @schemas.classproperty
                def BYSA(cls):
                    return cls("by-sa")
                
                @schemas.classproperty
                def CC0(cls):
                    return cls("cc0")
            locale = schemas.StrSchema
            name = schemas.StrSchema
            password = schemas.StrSchema
        
            @staticmethod
            def privacy() -> typing.Type['UploadVideoRequestPrivacy']:
                return UploadVideoRequestPrivacy
        
            @staticmethod
            def review_page() -> typing.Type['UploadVideoRequestReviewPage']:
                return UploadVideoRequestReviewPage
        
            @staticmethod
            def spatial() -> typing.Type['UploadVideoRequestSpatial']:
                return UploadVideoRequestSpatial
            __annotations__ = {
                "upload": upload,
                "description": description,
                "content_rating": content_rating,
                "embed": embed,
                "embed_domains": embed_domains,
                "folder_uri": folder_uri,
                "hide_from_vimeo": hide_from_vimeo,
                "license": license,
                "locale": locale,
                "name": name,
                "password": password,
                "privacy": privacy,
                "review_page": review_page,
                "spatial": spatial,
            }
    
    upload: 'UploadVideoRequestUpload'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upload"]) -> 'UploadVideoRequestUpload': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content_rating"]) -> 'UploadVideoRequestContentRating': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embed"]) -> 'UploadVideoRequestEmbed': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embed_domains"]) -> 'UploadVideoRequestEmbedDomains': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["folder_uri"]) -> MetaOapg.properties.folder_uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hide_from_vimeo"]) -> MetaOapg.properties.hide_from_vimeo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["license"]) -> MetaOapg.properties.license: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locale"]) -> MetaOapg.properties.locale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privacy"]) -> 'UploadVideoRequestPrivacy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["review_page"]) -> 'UploadVideoRequestReviewPage': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spatial"]) -> 'UploadVideoRequestSpatial': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["upload", "description", "content_rating", "embed", "embed_domains", "folder_uri", "hide_from_vimeo", "license", "locale", "name", "password", "privacy", "review_page", "spatial", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upload"]) -> 'UploadVideoRequestUpload': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content_rating"]) -> typing.Union['UploadVideoRequestContentRating', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embed"]) -> typing.Union['UploadVideoRequestEmbed', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embed_domains"]) -> typing.Union['UploadVideoRequestEmbedDomains', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["folder_uri"]) -> typing.Union[MetaOapg.properties.folder_uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hide_from_vimeo"]) -> typing.Union[MetaOapg.properties.hide_from_vimeo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["license"]) -> typing.Union[MetaOapg.properties.license, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locale"]) -> typing.Union[MetaOapg.properties.locale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privacy"]) -> typing.Union['UploadVideoRequestPrivacy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["review_page"]) -> typing.Union['UploadVideoRequestReviewPage', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spatial"]) -> typing.Union['UploadVideoRequestSpatial', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["upload", "description", "content_rating", "embed", "embed_domains", "folder_uri", "hide_from_vimeo", "license", "locale", "name", "password", "privacy", "review_page", "spatial", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        upload: 'UploadVideoRequestUpload',
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        content_rating: typing.Union['UploadVideoRequestContentRating', schemas.Unset] = schemas.unset,
        embed: typing.Union['UploadVideoRequestEmbed', schemas.Unset] = schemas.unset,
        embed_domains: typing.Union['UploadVideoRequestEmbedDomains', schemas.Unset] = schemas.unset,
        folder_uri: typing.Union[MetaOapg.properties.folder_uri, str, schemas.Unset] = schemas.unset,
        hide_from_vimeo: typing.Union[MetaOapg.properties.hide_from_vimeo, bool, schemas.Unset] = schemas.unset,
        license: typing.Union[MetaOapg.properties.license, str, schemas.Unset] = schemas.unset,
        locale: typing.Union[MetaOapg.properties.locale, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        privacy: typing.Union['UploadVideoRequestPrivacy', schemas.Unset] = schemas.unset,
        review_page: typing.Union['UploadVideoRequestReviewPage', schemas.Unset] = schemas.unset,
        spatial: typing.Union['UploadVideoRequestSpatial', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UploadVideoRequest':
        return super().__new__(
            cls,
            *args,
            upload=upload,
            description=description,
            content_rating=content_rating,
            embed=embed,
            embed_domains=embed_domains,
            folder_uri=folder_uri,
            hide_from_vimeo=hide_from_vimeo,
            license=license,
            locale=locale,
            name=name,
            password=password,
            privacy=privacy,
            review_page=review_page,
            spatial=spatial,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.upload_video_request_content_rating import UploadVideoRequestContentRating
from vimeo_python_sdk.model.upload_video_request_embed import UploadVideoRequestEmbed
from vimeo_python_sdk.model.upload_video_request_embed_domains import UploadVideoRequestEmbedDomains
from vimeo_python_sdk.model.upload_video_request_privacy import UploadVideoRequestPrivacy
from vimeo_python_sdk.model.upload_video_request_review_page import UploadVideoRequestReviewPage
from vimeo_python_sdk.model.upload_video_request_spatial import UploadVideoRequestSpatial
from vimeo_python_sdk.model.upload_video_request_upload import UploadVideoRequestUpload
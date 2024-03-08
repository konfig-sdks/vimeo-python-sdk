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


class VideoVersionUpload(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The version's upload information.
    """


    class MetaOapg:
        required = {
            "status",
        }
        
        class properties:
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "complete": "COMPLETE",
                        "error": "ERROR",
                        "in_progress": "IN_PROGRESS",
                    }
                
                @schemas.classproperty
                def COMPLETE(cls):
                    return cls("complete")
                
                @schemas.classproperty
                def ERROR(cls):
                    return cls("error")
                
                @schemas.classproperty
                def IN_PROGRESS(cls):
                    return cls("in_progress")
            
            
            class approach(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "post": "POST",
                        "pull": "PULL",
                        "tus": "TUS",
                    }
                
                @schemas.classproperty
                def POST(cls):
                    return cls("post")
                
                @schemas.classproperty
                def PULL(cls):
                    return cls("pull")
                
                @schemas.classproperty
                def TUS(cls):
                    return cls("tus")
            form = schemas.StrSchema
            gcs_uid = schemas.StrSchema
            link = schemas.StrSchema
            redirect_url = schemas.StrSchema
            size = schemas.NumberSchema
            upload_link = schemas.StrSchema
            __annotations__ = {
                "status": status,
                "approach": approach,
                "form": form,
                "gcs_uid": gcs_uid,
                "link": link,
                "redirect_url": redirect_url,
                "size": size,
                "upload_link": upload_link,
            }

    
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approach"]) -> MetaOapg.properties.approach: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["form"]) -> MetaOapg.properties.form: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gcs_uid"]) -> MetaOapg.properties.gcs_uid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirect_url"]) -> MetaOapg.properties.redirect_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upload_link"]) -> MetaOapg.properties.upload_link: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "approach", "form", "gcs_uid", "link", "redirect_url", "size", "upload_link", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approach"]) -> typing.Union[MetaOapg.properties.approach, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["form"]) -> typing.Union[MetaOapg.properties.form, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gcs_uid"]) -> typing.Union[MetaOapg.properties.gcs_uid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> typing.Union[MetaOapg.properties.link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirect_url"]) -> typing.Union[MetaOapg.properties.redirect_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upload_link"]) -> typing.Union[MetaOapg.properties.upload_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "approach", "form", "gcs_uid", "link", "redirect_url", "size", "upload_link", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        approach: typing.Union[MetaOapg.properties.approach, str, schemas.Unset] = schemas.unset,
        form: typing.Union[MetaOapg.properties.form, str, schemas.Unset] = schemas.unset,
        gcs_uid: typing.Union[MetaOapg.properties.gcs_uid, str, schemas.Unset] = schemas.unset,
        link: typing.Union[MetaOapg.properties.link, str, schemas.Unset] = schemas.unset,
        redirect_url: typing.Union[MetaOapg.properties.redirect_url, str, schemas.Unset] = schemas.unset,
        size: typing.Union[MetaOapg.properties.size, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        upload_link: typing.Union[MetaOapg.properties.upload_link, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VideoVersionUpload':
        return super().__new__(
            cls,
            *args,
            approach=approach,
            form=form,
            gcs_uid=gcs_uid,
            link=link,
            redirect_url=redirect_url,
            size=size,
            upload_link=upload_link,
            _configuration=_configuration,
            **kwargs,
        )

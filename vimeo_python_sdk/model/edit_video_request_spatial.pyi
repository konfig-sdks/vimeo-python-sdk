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


class EditVideoRequestSpatial(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def director_timeline() -> typing.Type['EditVideoRequestSpatialDirectorTimeline']:
                return EditVideoRequestSpatialDirectorTimeline
            field_of_view = schemas.NumberSchema
            
            
            class projection(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CUBICAL(cls):
                    return cls("cubical")
                
                @schemas.classproperty
                def CYLINDRICAL(cls):
                    return cls("cylindrical")
                
                @schemas.classproperty
                def DOME(cls):
                    return cls("dome")
                
                @schemas.classproperty
                def EQUIRECTANGULAR(cls):
                    return cls("equirectangular")
                
                @schemas.classproperty
                def PYRAMID(cls):
                    return cls("pyramid")
            
            
            class stereo_format(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def LEFTRIGHT(cls):
                    return cls("left-right")
                
                @schemas.classproperty
                def MONO(cls):
                    return cls("mono")
                
                @schemas.classproperty
                def TOPBOTTOM(cls):
                    return cls("top-bottom")
            __annotations__ = {
                "director_timeline": director_timeline,
                "field_of_view": field_of_view,
                "projection": projection,
                "stereo_format": stereo_format,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["director_timeline"]) -> 'EditVideoRequestSpatialDirectorTimeline': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field_of_view"]) -> MetaOapg.properties.field_of_view: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projection"]) -> MetaOapg.properties.projection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stereo_format"]) -> MetaOapg.properties.stereo_format: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["director_timeline", "field_of_view", "projection", "stereo_format", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["director_timeline"]) -> typing.Union['EditVideoRequestSpatialDirectorTimeline', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field_of_view"]) -> typing.Union[MetaOapg.properties.field_of_view, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projection"]) -> typing.Union[MetaOapg.properties.projection, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stereo_format"]) -> typing.Union[MetaOapg.properties.stereo_format, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["director_timeline", "field_of_view", "projection", "stereo_format", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        director_timeline: typing.Union['EditVideoRequestSpatialDirectorTimeline', schemas.Unset] = schemas.unset,
        field_of_view: typing.Union[MetaOapg.properties.field_of_view, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        projection: typing.Union[MetaOapg.properties.projection, str, schemas.Unset] = schemas.unset,
        stereo_format: typing.Union[MetaOapg.properties.stereo_format, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EditVideoRequestSpatial':
        return super().__new__(
            cls,
            *args,
            director_timeline=director_timeline,
            field_of_view=field_of_view,
            projection=projection,
            stereo_format=stereo_format,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.edit_video_request_spatial_director_timeline import EditVideoRequestSpatialDirectorTimeline

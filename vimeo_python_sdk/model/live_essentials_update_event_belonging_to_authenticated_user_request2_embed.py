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


class LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2Embed(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The embed settings of the event and the videos generated by streaming to this event.
    """


    class MetaOapg:
        
        class properties:
            autoplay = schemas.BoolSchema
            color = schemas.StrSchema
        
            @staticmethod
            def logos() -> typing.Type['LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2EmbedLogos']:
                return LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2EmbedLogos
            loop = schemas.BoolSchema
            playlist = schemas.BoolSchema
            schedule = schemas.BoolSchema
            use_color = schemas.BoolSchema
            __annotations__ = {
                "autoplay": autoplay,
                "color": color,
                "logos": logos,
                "loop": loop,
                "playlist": playlist,
                "schedule": schedule,
                "use_color": use_color,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoplay"]) -> MetaOapg.properties.autoplay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logos"]) -> 'LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2EmbedLogos': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loop"]) -> MetaOapg.properties.loop: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["playlist"]) -> MetaOapg.properties.playlist: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedule"]) -> MetaOapg.properties.schedule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["use_color"]) -> MetaOapg.properties.use_color: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["autoplay", "color", "logos", "loop", "playlist", "schedule", "use_color", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoplay"]) -> typing.Union[MetaOapg.properties.autoplay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logos"]) -> typing.Union['LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2EmbedLogos', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loop"]) -> typing.Union[MetaOapg.properties.loop, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["playlist"]) -> typing.Union[MetaOapg.properties.playlist, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedule"]) -> typing.Union[MetaOapg.properties.schedule, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["use_color"]) -> typing.Union[MetaOapg.properties.use_color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["autoplay", "color", "logos", "loop", "playlist", "schedule", "use_color", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        autoplay: typing.Union[MetaOapg.properties.autoplay, bool, schemas.Unset] = schemas.unset,
        color: typing.Union[MetaOapg.properties.color, str, schemas.Unset] = schemas.unset,
        logos: typing.Union['LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2EmbedLogos', schemas.Unset] = schemas.unset,
        loop: typing.Union[MetaOapg.properties.loop, bool, schemas.Unset] = schemas.unset,
        playlist: typing.Union[MetaOapg.properties.playlist, bool, schemas.Unset] = schemas.unset,
        schedule: typing.Union[MetaOapg.properties.schedule, bool, schemas.Unset] = schemas.unset,
        use_color: typing.Union[MetaOapg.properties.use_color, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2Embed':
        return super().__new__(
            cls,
            *args,
            autoplay=autoplay,
            color=color,
            logos=logos,
            loop=loop,
            playlist=playlist,
            schedule=schedule,
            use_color=use_color,
            _configuration=_configuration,
            **kwargs,
        )

from vimeo_python_sdk.model.live_essentials_update_event_belonging_to_authenticated_user_request2_embed_logos import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2EmbedLogos

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


class LiveEventSessionStatusIngest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The ingest of the video.
    """


    class MetaOapg:
        required = {
            "rtmp_link",
            "is_rtmp_session",
            "end_time",
            "session_id",
            "stream_key",
            "encoder_type",
            "rtmps_link",
            "start_time",
            "stream_ended_reason",
            "width",
            "rtmp_expires_at",
            "is_scheduled_playback",
            "height",
            "scheduled_start_time",
            "status",
        }
        
        class properties:
            
            
            class encoder_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DASH(cls):
                    return cls("dash")
                
                @schemas.classproperty
                def RTMP(cls):
                    return cls("rtmp")
                
                @schemas.classproperty
                def SIMPLE_LIVE(cls):
                    return cls("simple_live")
                
                @schemas.classproperty
                def STUDIO_CLOUD(cls):
                    return cls("studio_cloud")
                
                @schemas.classproperty
                def UNKNOWN(cls):
                    return cls("unknown")
                
                @schemas.classproperty
                def WEBRTC(cls):
                    return cls("webrtc")
            
            
            class end_time(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'end_time':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class height(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'height':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            is_rtmp_session = schemas.BoolSchema
            
            
            class is_scheduled_playback(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'is_scheduled_playback':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class rtmp_expires_at(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'rtmp_expires_at':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class rtmp_link(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'rtmp_link':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class rtmps_link(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'rtmps_link':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class scheduled_start_time(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'scheduled_start_time':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class session_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'session_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class start_time(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'start_time':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class status(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "0": "POSITIVE_0",
                        "1": "POSITIVE_1",
                        "2": "POSITIVE_2",
                        "3": "POSITIVE_3",
                        "4": "POSITIVE_4",
                        "5": "POSITIVE_5",
                    }
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls("0")
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls("1")
                
                @schemas.classproperty
                def POSITIVE_2(cls):
                    return cls("2")
                
                @schemas.classproperty
                def POSITIVE_3(cls):
                    return cls("3")
                
                @schemas.classproperty
                def POSITIVE_4(cls):
                    return cls("4")
                
                @schemas.classproperty
                def POSITIVE_5(cls):
                    return cls("5")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'status':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class stream_ended_reason(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'stream_ended_reason':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class stream_key(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'stream_key':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class width(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'width':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "encoder_type": encoder_type,
                "end_time": end_time,
                "height": height,
                "is_rtmp_session": is_rtmp_session,
                "is_scheduled_playback": is_scheduled_playback,
                "rtmp_expires_at": rtmp_expires_at,
                "rtmp_link": rtmp_link,
                "rtmps_link": rtmps_link,
                "scheduled_start_time": scheduled_start_time,
                "session_id": session_id,
                "start_time": start_time,
                "status": status,
                "stream_ended_reason": stream_ended_reason,
                "stream_key": stream_key,
                "width": width,
            }
    
    rtmp_link: MetaOapg.properties.rtmp_link
    is_rtmp_session: MetaOapg.properties.is_rtmp_session
    end_time: MetaOapg.properties.end_time
    session_id: MetaOapg.properties.session_id
    stream_key: MetaOapg.properties.stream_key
    encoder_type: MetaOapg.properties.encoder_type
    rtmps_link: MetaOapg.properties.rtmps_link
    start_time: MetaOapg.properties.start_time
    stream_ended_reason: MetaOapg.properties.stream_ended_reason
    width: MetaOapg.properties.width
    rtmp_expires_at: MetaOapg.properties.rtmp_expires_at
    is_scheduled_playback: MetaOapg.properties.is_scheduled_playback
    height: MetaOapg.properties.height
    scheduled_start_time: MetaOapg.properties.scheduled_start_time
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["encoder_type"]) -> MetaOapg.properties.encoder_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_time"]) -> MetaOapg.properties.end_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["height"]) -> MetaOapg.properties.height: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_rtmp_session"]) -> MetaOapg.properties.is_rtmp_session: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_scheduled_playback"]) -> MetaOapg.properties.is_scheduled_playback: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rtmp_expires_at"]) -> MetaOapg.properties.rtmp_expires_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rtmp_link"]) -> MetaOapg.properties.rtmp_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rtmps_link"]) -> MetaOapg.properties.rtmps_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheduled_start_time"]) -> MetaOapg.properties.scheduled_start_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["session_id"]) -> MetaOapg.properties.session_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_time"]) -> MetaOapg.properties.start_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stream_ended_reason"]) -> MetaOapg.properties.stream_ended_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stream_key"]) -> MetaOapg.properties.stream_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["encoder_type", "end_time", "height", "is_rtmp_session", "is_scheduled_playback", "rtmp_expires_at", "rtmp_link", "rtmps_link", "scheduled_start_time", "session_id", "start_time", "status", "stream_ended_reason", "stream_key", "width", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["encoder_type"]) -> MetaOapg.properties.encoder_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_time"]) -> MetaOapg.properties.end_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["height"]) -> MetaOapg.properties.height: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_rtmp_session"]) -> MetaOapg.properties.is_rtmp_session: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_scheduled_playback"]) -> MetaOapg.properties.is_scheduled_playback: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rtmp_expires_at"]) -> MetaOapg.properties.rtmp_expires_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rtmp_link"]) -> MetaOapg.properties.rtmp_link: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rtmps_link"]) -> MetaOapg.properties.rtmps_link: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheduled_start_time"]) -> MetaOapg.properties.scheduled_start_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["session_id"]) -> MetaOapg.properties.session_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_time"]) -> MetaOapg.properties.start_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stream_ended_reason"]) -> MetaOapg.properties.stream_ended_reason: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stream_key"]) -> MetaOapg.properties.stream_key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["encoder_type", "end_time", "height", "is_rtmp_session", "is_scheduled_playback", "rtmp_expires_at", "rtmp_link", "rtmps_link", "scheduled_start_time", "session_id", "start_time", "status", "stream_ended_reason", "stream_key", "width", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        rtmp_link: typing.Union[MetaOapg.properties.rtmp_link, None, str, ],
        is_rtmp_session: typing.Union[MetaOapg.properties.is_rtmp_session, bool, ],
        end_time: typing.Union[MetaOapg.properties.end_time, None, decimal.Decimal, int, float, ],
        session_id: typing.Union[MetaOapg.properties.session_id, None, str, ],
        stream_key: typing.Union[MetaOapg.properties.stream_key, None, str, ],
        encoder_type: typing.Union[MetaOapg.properties.encoder_type, str, ],
        rtmps_link: typing.Union[MetaOapg.properties.rtmps_link, None, str, ],
        start_time: typing.Union[MetaOapg.properties.start_time, None, decimal.Decimal, int, float, ],
        stream_ended_reason: typing.Union[MetaOapg.properties.stream_ended_reason, None, decimal.Decimal, int, float, ],
        width: typing.Union[MetaOapg.properties.width, None, decimal.Decimal, int, float, ],
        rtmp_expires_at: typing.Union[MetaOapg.properties.rtmp_expires_at, None, str, ],
        is_scheduled_playback: typing.Union[MetaOapg.properties.is_scheduled_playback, None, bool, ],
        height: typing.Union[MetaOapg.properties.height, None, decimal.Decimal, int, float, ],
        scheduled_start_time: typing.Union[MetaOapg.properties.scheduled_start_time, None, str, ],
        status: typing.Union[MetaOapg.properties.status, None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LiveEventSessionStatusIngest':
        return super().__new__(
            cls,
            *args,
            rtmp_link=rtmp_link,
            is_rtmp_session=is_rtmp_session,
            end_time=end_time,
            session_id=session_id,
            stream_key=stream_key,
            encoder_type=encoder_type,
            rtmps_link=rtmps_link,
            start_time=start_time,
            stream_ended_reason=stream_ended_reason,
            width=width,
            rtmp_expires_at=rtmp_expires_at,
            is_scheduled_playback=is_scheduled_playback,
            height=height,
            scheduled_start_time=scheduled_start_time,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

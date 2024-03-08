# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from vimeo_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from vimeo_python_sdk.api_response import AsyncGeneratorResponse
from vimeo_python_sdk import api_client, exceptions
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

from vimeo_python_sdk.model.live_essentials_create_live_event_request_stream_privacy import LiveEssentialsCreateLiveEventRequestStreamPrivacy as LiveEssentialsCreateLiveEventRequestStreamPrivacySchema
from vimeo_python_sdk.model.live_essentials_create_live_event_request_schedule import LiveEssentialsCreateLiveEventRequestSchedule as LiveEssentialsCreateLiveEventRequestScheduleSchema
from vimeo_python_sdk.model.live_essentials_create_live_event_request_embed import LiveEssentialsCreateLiveEventRequestEmbed as LiveEssentialsCreateLiveEventRequestEmbedSchema
from vimeo_python_sdk.model.error import Error as ErrorSchema
from vimeo_python_sdk.model.live_event_recurring import LiveEventRecurring as LiveEventRecurringSchema
from vimeo_python_sdk.model.live_essentials_create_live_event_request_interaction_tools_settings import LiveEssentialsCreateLiveEventRequestInteractionToolsSettings as LiveEssentialsCreateLiveEventRequestInteractionToolsSettingsSchema
from vimeo_python_sdk.model.live_essentials_create_live_event_request_content_rating import LiveEssentialsCreateLiveEventRequestContentRating as LiveEssentialsCreateLiveEventRequestContentRatingSchema
from vimeo_python_sdk.model.live_essentials_create_live_event_request_stream_embed import LiveEssentialsCreateLiveEventRequestStreamEmbed as LiveEssentialsCreateLiveEventRequestStreamEmbedSchema
from vimeo_python_sdk.model.live_essentials_create_live_event_request import LiveEssentialsCreateLiveEventRequest as LiveEssentialsCreateLiveEventRequestSchema

from vimeo_python_sdk.type.live_essentials_create_live_event_request_stream_privacy import LiveEssentialsCreateLiveEventRequestStreamPrivacy
from vimeo_python_sdk.type.live_essentials_create_live_event_request_content_rating import LiveEssentialsCreateLiveEventRequestContentRating
from vimeo_python_sdk.type.live_essentials_create_live_event_request_stream_embed import LiveEssentialsCreateLiveEventRequestStreamEmbed
from vimeo_python_sdk.type.error import Error
from vimeo_python_sdk.type.live_essentials_create_live_event_request_schedule import LiveEssentialsCreateLiveEventRequestSchedule
from vimeo_python_sdk.type.live_essentials_create_live_event_request_embed import LiveEssentialsCreateLiveEventRequestEmbed
from vimeo_python_sdk.type.live_event_recurring import LiveEventRecurring
from vimeo_python_sdk.type.live_essentials_create_live_event_request import LiveEssentialsCreateLiveEventRequest
from vimeo_python_sdk.type.live_essentials_create_live_event_request_interaction_tools_settings import LiveEssentialsCreateLiveEventRequestInteractionToolsSettings

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.error import Error as ErrorPydantic
from vimeo_python_sdk.pydantic.live_essentials_create_live_event_request_stream_embed import LiveEssentialsCreateLiveEventRequestStreamEmbed as LiveEssentialsCreateLiveEventRequestStreamEmbedPydantic
from vimeo_python_sdk.pydantic.live_essentials_create_live_event_request import LiveEssentialsCreateLiveEventRequest as LiveEssentialsCreateLiveEventRequestPydantic
from vimeo_python_sdk.pydantic.live_essentials_create_live_event_request_interaction_tools_settings import LiveEssentialsCreateLiveEventRequestInteractionToolsSettings as LiveEssentialsCreateLiveEventRequestInteractionToolsSettingsPydantic
from vimeo_python_sdk.pydantic.live_essentials_create_live_event_request_stream_privacy import LiveEssentialsCreateLiveEventRequestStreamPrivacy as LiveEssentialsCreateLiveEventRequestStreamPrivacyPydantic
from vimeo_python_sdk.pydantic.live_essentials_create_live_event_request_schedule import LiveEssentialsCreateLiveEventRequestSchedule as LiveEssentialsCreateLiveEventRequestSchedulePydantic
from vimeo_python_sdk.pydantic.live_essentials_create_live_event_request_content_rating import LiveEssentialsCreateLiveEventRequestContentRating as LiveEssentialsCreateLiveEventRequestContentRatingPydantic
from vimeo_python_sdk.pydantic.live_essentials_create_live_event_request_embed import LiveEssentialsCreateLiveEventRequestEmbed as LiveEssentialsCreateLiveEventRequestEmbedPydantic
from vimeo_python_sdk.pydantic.live_event_recurring import LiveEventRecurring as LiveEventRecurringPydantic

from . import path

# body param
SchemaForRequestBodyApplicationVndVimeoLiveEventRecurringjson = LiveEssentialsCreateLiveEventRequestSchema


request_body_live_essentials_create_live_event_request = api_client.RequestBody(
    content={
        'application/vnd.vimeo.live.event.recurring+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndVimeoLiveEventRecurringjson),
    },
    required=True,
)
_auth = [
    'oauth2',
    'oauth2',
]
SchemaFor200ResponseBodyApplicationVndVimeoLiveEventRecurringjson = LiveEventRecurringSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: LiveEventRecurring


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: LiveEventRecurring


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.live.event.recurring+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoLiveEventRecurringjson),
    },
)
SchemaFor400ResponseBodyApplicationVndVimeoLiveEventRecurringjson = ErrorSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: Error


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/vnd.vimeo.live.event.recurring+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndVimeoLiveEventRecurringjson),
    },
)
SchemaFor401ResponseBodyApplicationVndVimeoLiveEventRecurringjson = ErrorSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: Error


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/vnd.vimeo.live.event.recurring+json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationVndVimeoLiveEventRecurringjson),
    },
)
SchemaFor403ResponseBodyApplicationVndVimeoLiveEventRecurringjson = ErrorSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: Error


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/vnd.vimeo.live.event.recurring+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationVndVimeoLiveEventRecurringjson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
}
_all_accept_content_types = (
    'application/vnd.vimeo.live.event.recurring+json',
)


class BaseApi(api_client.Api):

    def _create_live_event_mapped_args(
        self,
        title: str,
        allow_share_link: typing.Optional[bool] = None,
        auto_cc_enabled: typing.Optional[bool] = None,
        auto_cc_keywords: typing.Optional[str] = None,
        auto_cc_lang: typing.Optional[str] = None,
        automatically_title_stream: typing.Optional[bool] = None,
        chat_enabled: typing.Optional[bool] = None,
        content_rating: typing.Optional[LiveEssentialsCreateLiveEventRequestContentRating] = None,
        dvr: typing.Optional[bool] = None,
        embed: typing.Optional[LiveEssentialsCreateLiveEventRequestEmbed] = None,
        folder_uri: typing.Optional[str] = None,
        interaction_tools_settings: typing.Optional[LiveEssentialsCreateLiveEventRequestInteractionToolsSettings] = None,
        low_latency: typing.Optional[bool] = None,
        playlist_sort: typing.Optional[str] = None,
        rtmp_preview: typing.Optional[bool] = None,
        schedule: typing.Optional[LiveEssentialsCreateLiveEventRequestSchedule] = None,
        scheduled_playback: typing.Optional[bool] = None,
        stream_description: typing.Optional[str] = None,
        stream_embed: typing.Optional[LiveEssentialsCreateLiveEventRequestStreamEmbed] = None,
        stream_password: typing.Optional[str] = None,
        stream_privacy: typing.Optional[LiveEssentialsCreateLiveEventRequestStreamPrivacy] = None,
        stream_title: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if title is not None:
            _body["title"] = title
        if allow_share_link is not None:
            _body["allow_share_link"] = allow_share_link
        if auto_cc_enabled is not None:
            _body["auto_cc_enabled"] = auto_cc_enabled
        if auto_cc_keywords is not None:
            _body["auto_cc_keywords"] = auto_cc_keywords
        if auto_cc_lang is not None:
            _body["auto_cc_lang"] = auto_cc_lang
        if automatically_title_stream is not None:
            _body["automatically_title_stream"] = automatically_title_stream
        if chat_enabled is not None:
            _body["chat_enabled"] = chat_enabled
        if content_rating is not None:
            _body["content_rating"] = content_rating
        if dvr is not None:
            _body["dvr"] = dvr
        if embed is not None:
            _body["embed"] = embed
        if folder_uri is not None:
            _body["folder_uri"] = folder_uri
        if interaction_tools_settings is not None:
            _body["interaction_tools_settings"] = interaction_tools_settings
        if low_latency is not None:
            _body["low_latency"] = low_latency
        if playlist_sort is not None:
            _body["playlist_sort"] = playlist_sort
        if rtmp_preview is not None:
            _body["rtmp_preview"] = rtmp_preview
        if schedule is not None:
            _body["schedule"] = schedule
        if scheduled_playback is not None:
            _body["scheduled_playback"] = scheduled_playback
        if stream_description is not None:
            _body["stream_description"] = stream_description
        if stream_embed is not None:
            _body["stream_embed"] = stream_embed
        if stream_password is not None:
            _body["stream_password"] = stream_password
        if stream_privacy is not None:
            _body["stream_privacy"] = stream_privacy
        if stream_title is not None:
            _body["stream_title"] = stream_title
        if time_zone is not None:
            _body["time_zone"] = time_zone
        args.body = _body
        return args

    async def _acreate_live_event_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.live.event.recurring+json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a live event
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/me/live_events',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_live_essentials_create_live_event_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_live_event_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.live.event.recurring+json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a live event
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/me/live_events',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_live_essentials_create_live_event_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateLiveEventRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_live_event(
        self,
        title: str,
        allow_share_link: typing.Optional[bool] = None,
        auto_cc_enabled: typing.Optional[bool] = None,
        auto_cc_keywords: typing.Optional[str] = None,
        auto_cc_lang: typing.Optional[str] = None,
        automatically_title_stream: typing.Optional[bool] = None,
        chat_enabled: typing.Optional[bool] = None,
        content_rating: typing.Optional[LiveEssentialsCreateLiveEventRequestContentRating] = None,
        dvr: typing.Optional[bool] = None,
        embed: typing.Optional[LiveEssentialsCreateLiveEventRequestEmbed] = None,
        folder_uri: typing.Optional[str] = None,
        interaction_tools_settings: typing.Optional[LiveEssentialsCreateLiveEventRequestInteractionToolsSettings] = None,
        low_latency: typing.Optional[bool] = None,
        playlist_sort: typing.Optional[str] = None,
        rtmp_preview: typing.Optional[bool] = None,
        schedule: typing.Optional[LiveEssentialsCreateLiveEventRequestSchedule] = None,
        scheduled_playback: typing.Optional[bool] = None,
        stream_description: typing.Optional[str] = None,
        stream_embed: typing.Optional[LiveEssentialsCreateLiveEventRequestStreamEmbed] = None,
        stream_password: typing.Optional[str] = None,
        stream_privacy: typing.Optional[LiveEssentialsCreateLiveEventRequestStreamPrivacy] = None,
        stream_title: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_live_event_mapped_args(
            title=title,
            allow_share_link=allow_share_link,
            auto_cc_enabled=auto_cc_enabled,
            auto_cc_keywords=auto_cc_keywords,
            auto_cc_lang=auto_cc_lang,
            automatically_title_stream=automatically_title_stream,
            chat_enabled=chat_enabled,
            content_rating=content_rating,
            dvr=dvr,
            embed=embed,
            folder_uri=folder_uri,
            interaction_tools_settings=interaction_tools_settings,
            low_latency=low_latency,
            playlist_sort=playlist_sort,
            rtmp_preview=rtmp_preview,
            schedule=schedule,
            scheduled_playback=scheduled_playback,
            stream_description=stream_description,
            stream_embed=stream_embed,
            stream_password=stream_password,
            stream_privacy=stream_privacy,
            stream_title=stream_title,
            time_zone=time_zone,
        )
        return await self._acreate_live_event_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_live_event(
        self,
        title: str,
        allow_share_link: typing.Optional[bool] = None,
        auto_cc_enabled: typing.Optional[bool] = None,
        auto_cc_keywords: typing.Optional[str] = None,
        auto_cc_lang: typing.Optional[str] = None,
        automatically_title_stream: typing.Optional[bool] = None,
        chat_enabled: typing.Optional[bool] = None,
        content_rating: typing.Optional[LiveEssentialsCreateLiveEventRequestContentRating] = None,
        dvr: typing.Optional[bool] = None,
        embed: typing.Optional[LiveEssentialsCreateLiveEventRequestEmbed] = None,
        folder_uri: typing.Optional[str] = None,
        interaction_tools_settings: typing.Optional[LiveEssentialsCreateLiveEventRequestInteractionToolsSettings] = None,
        low_latency: typing.Optional[bool] = None,
        playlist_sort: typing.Optional[str] = None,
        rtmp_preview: typing.Optional[bool] = None,
        schedule: typing.Optional[LiveEssentialsCreateLiveEventRequestSchedule] = None,
        scheduled_playback: typing.Optional[bool] = None,
        stream_description: typing.Optional[str] = None,
        stream_embed: typing.Optional[LiveEssentialsCreateLiveEventRequestStreamEmbed] = None,
        stream_password: typing.Optional[str] = None,
        stream_privacy: typing.Optional[LiveEssentialsCreateLiveEventRequestStreamPrivacy] = None,
        stream_title: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_live_event_mapped_args(
            title=title,
            allow_share_link=allow_share_link,
            auto_cc_enabled=auto_cc_enabled,
            auto_cc_keywords=auto_cc_keywords,
            auto_cc_lang=auto_cc_lang,
            automatically_title_stream=automatically_title_stream,
            chat_enabled=chat_enabled,
            content_rating=content_rating,
            dvr=dvr,
            embed=embed,
            folder_uri=folder_uri,
            interaction_tools_settings=interaction_tools_settings,
            low_latency=low_latency,
            playlist_sort=playlist_sort,
            rtmp_preview=rtmp_preview,
            schedule=schedule,
            scheduled_playback=scheduled_playback,
            stream_description=stream_description,
            stream_embed=stream_embed,
            stream_password=stream_password,
            stream_privacy=stream_privacy,
            stream_title=stream_title,
            time_zone=time_zone,
        )
        return self._create_live_event_oapg(
            body=args.body,
        )

class CreateLiveEvent(BaseApi):

    async def acreate_live_event(
        self,
        title: str,
        allow_share_link: typing.Optional[bool] = None,
        auto_cc_enabled: typing.Optional[bool] = None,
        auto_cc_keywords: typing.Optional[str] = None,
        auto_cc_lang: typing.Optional[str] = None,
        automatically_title_stream: typing.Optional[bool] = None,
        chat_enabled: typing.Optional[bool] = None,
        content_rating: typing.Optional[LiveEssentialsCreateLiveEventRequestContentRating] = None,
        dvr: typing.Optional[bool] = None,
        embed: typing.Optional[LiveEssentialsCreateLiveEventRequestEmbed] = None,
        folder_uri: typing.Optional[str] = None,
        interaction_tools_settings: typing.Optional[LiveEssentialsCreateLiveEventRequestInteractionToolsSettings] = None,
        low_latency: typing.Optional[bool] = None,
        playlist_sort: typing.Optional[str] = None,
        rtmp_preview: typing.Optional[bool] = None,
        schedule: typing.Optional[LiveEssentialsCreateLiveEventRequestSchedule] = None,
        scheduled_playback: typing.Optional[bool] = None,
        stream_description: typing.Optional[str] = None,
        stream_embed: typing.Optional[LiveEssentialsCreateLiveEventRequestStreamEmbed] = None,
        stream_password: typing.Optional[str] = None,
        stream_privacy: typing.Optional[LiveEssentialsCreateLiveEventRequestStreamPrivacy] = None,
        stream_title: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> LiveEventRecurringPydantic:
        raw_response = await self.raw.acreate_live_event(
            title=title,
            allow_share_link=allow_share_link,
            auto_cc_enabled=auto_cc_enabled,
            auto_cc_keywords=auto_cc_keywords,
            auto_cc_lang=auto_cc_lang,
            automatically_title_stream=automatically_title_stream,
            chat_enabled=chat_enabled,
            content_rating=content_rating,
            dvr=dvr,
            embed=embed,
            folder_uri=folder_uri,
            interaction_tools_settings=interaction_tools_settings,
            low_latency=low_latency,
            playlist_sort=playlist_sort,
            rtmp_preview=rtmp_preview,
            schedule=schedule,
            scheduled_playback=scheduled_playback,
            stream_description=stream_description,
            stream_embed=stream_embed,
            stream_password=stream_password,
            stream_privacy=stream_privacy,
            stream_title=stream_title,
            time_zone=time_zone,
            **kwargs,
        )
        if validate:
            return LiveEventRecurringPydantic(**raw_response.body)
        return api_client.construct_model_instance(LiveEventRecurringPydantic, raw_response.body)
    
    
    def create_live_event(
        self,
        title: str,
        allow_share_link: typing.Optional[bool] = None,
        auto_cc_enabled: typing.Optional[bool] = None,
        auto_cc_keywords: typing.Optional[str] = None,
        auto_cc_lang: typing.Optional[str] = None,
        automatically_title_stream: typing.Optional[bool] = None,
        chat_enabled: typing.Optional[bool] = None,
        content_rating: typing.Optional[LiveEssentialsCreateLiveEventRequestContentRating] = None,
        dvr: typing.Optional[bool] = None,
        embed: typing.Optional[LiveEssentialsCreateLiveEventRequestEmbed] = None,
        folder_uri: typing.Optional[str] = None,
        interaction_tools_settings: typing.Optional[LiveEssentialsCreateLiveEventRequestInteractionToolsSettings] = None,
        low_latency: typing.Optional[bool] = None,
        playlist_sort: typing.Optional[str] = None,
        rtmp_preview: typing.Optional[bool] = None,
        schedule: typing.Optional[LiveEssentialsCreateLiveEventRequestSchedule] = None,
        scheduled_playback: typing.Optional[bool] = None,
        stream_description: typing.Optional[str] = None,
        stream_embed: typing.Optional[LiveEssentialsCreateLiveEventRequestStreamEmbed] = None,
        stream_password: typing.Optional[str] = None,
        stream_privacy: typing.Optional[LiveEssentialsCreateLiveEventRequestStreamPrivacy] = None,
        stream_title: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
        validate: bool = False,
    ) -> LiveEventRecurringPydantic:
        raw_response = self.raw.create_live_event(
            title=title,
            allow_share_link=allow_share_link,
            auto_cc_enabled=auto_cc_enabled,
            auto_cc_keywords=auto_cc_keywords,
            auto_cc_lang=auto_cc_lang,
            automatically_title_stream=automatically_title_stream,
            chat_enabled=chat_enabled,
            content_rating=content_rating,
            dvr=dvr,
            embed=embed,
            folder_uri=folder_uri,
            interaction_tools_settings=interaction_tools_settings,
            low_latency=low_latency,
            playlist_sort=playlist_sort,
            rtmp_preview=rtmp_preview,
            schedule=schedule,
            scheduled_playback=scheduled_playback,
            stream_description=stream_description,
            stream_embed=stream_embed,
            stream_password=stream_password,
            stream_privacy=stream_privacy,
            stream_title=stream_title,
            time_zone=time_zone,
        )
        if validate:
            return LiveEventRecurringPydantic(**raw_response.body)
        return api_client.construct_model_instance(LiveEventRecurringPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        title: str,
        allow_share_link: typing.Optional[bool] = None,
        auto_cc_enabled: typing.Optional[bool] = None,
        auto_cc_keywords: typing.Optional[str] = None,
        auto_cc_lang: typing.Optional[str] = None,
        automatically_title_stream: typing.Optional[bool] = None,
        chat_enabled: typing.Optional[bool] = None,
        content_rating: typing.Optional[LiveEssentialsCreateLiveEventRequestContentRating] = None,
        dvr: typing.Optional[bool] = None,
        embed: typing.Optional[LiveEssentialsCreateLiveEventRequestEmbed] = None,
        folder_uri: typing.Optional[str] = None,
        interaction_tools_settings: typing.Optional[LiveEssentialsCreateLiveEventRequestInteractionToolsSettings] = None,
        low_latency: typing.Optional[bool] = None,
        playlist_sort: typing.Optional[str] = None,
        rtmp_preview: typing.Optional[bool] = None,
        schedule: typing.Optional[LiveEssentialsCreateLiveEventRequestSchedule] = None,
        scheduled_playback: typing.Optional[bool] = None,
        stream_description: typing.Optional[str] = None,
        stream_embed: typing.Optional[LiveEssentialsCreateLiveEventRequestStreamEmbed] = None,
        stream_password: typing.Optional[str] = None,
        stream_privacy: typing.Optional[LiveEssentialsCreateLiveEventRequestStreamPrivacy] = None,
        stream_title: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_live_event_mapped_args(
            title=title,
            allow_share_link=allow_share_link,
            auto_cc_enabled=auto_cc_enabled,
            auto_cc_keywords=auto_cc_keywords,
            auto_cc_lang=auto_cc_lang,
            automatically_title_stream=automatically_title_stream,
            chat_enabled=chat_enabled,
            content_rating=content_rating,
            dvr=dvr,
            embed=embed,
            folder_uri=folder_uri,
            interaction_tools_settings=interaction_tools_settings,
            low_latency=low_latency,
            playlist_sort=playlist_sort,
            rtmp_preview=rtmp_preview,
            schedule=schedule,
            scheduled_playback=scheduled_playback,
            stream_description=stream_description,
            stream_embed=stream_embed,
            stream_password=stream_password,
            stream_privacy=stream_privacy,
            stream_title=stream_title,
            time_zone=time_zone,
        )
        return await self._acreate_live_event_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        title: str,
        allow_share_link: typing.Optional[bool] = None,
        auto_cc_enabled: typing.Optional[bool] = None,
        auto_cc_keywords: typing.Optional[str] = None,
        auto_cc_lang: typing.Optional[str] = None,
        automatically_title_stream: typing.Optional[bool] = None,
        chat_enabled: typing.Optional[bool] = None,
        content_rating: typing.Optional[LiveEssentialsCreateLiveEventRequestContentRating] = None,
        dvr: typing.Optional[bool] = None,
        embed: typing.Optional[LiveEssentialsCreateLiveEventRequestEmbed] = None,
        folder_uri: typing.Optional[str] = None,
        interaction_tools_settings: typing.Optional[LiveEssentialsCreateLiveEventRequestInteractionToolsSettings] = None,
        low_latency: typing.Optional[bool] = None,
        playlist_sort: typing.Optional[str] = None,
        rtmp_preview: typing.Optional[bool] = None,
        schedule: typing.Optional[LiveEssentialsCreateLiveEventRequestSchedule] = None,
        scheduled_playback: typing.Optional[bool] = None,
        stream_description: typing.Optional[str] = None,
        stream_embed: typing.Optional[LiveEssentialsCreateLiveEventRequestStreamEmbed] = None,
        stream_password: typing.Optional[str] = None,
        stream_privacy: typing.Optional[LiveEssentialsCreateLiveEventRequestStreamPrivacy] = None,
        stream_title: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_live_event_mapped_args(
            title=title,
            allow_share_link=allow_share_link,
            auto_cc_enabled=auto_cc_enabled,
            auto_cc_keywords=auto_cc_keywords,
            auto_cc_lang=auto_cc_lang,
            automatically_title_stream=automatically_title_stream,
            chat_enabled=chat_enabled,
            content_rating=content_rating,
            dvr=dvr,
            embed=embed,
            folder_uri=folder_uri,
            interaction_tools_settings=interaction_tools_settings,
            low_latency=low_latency,
            playlist_sort=playlist_sort,
            rtmp_preview=rtmp_preview,
            schedule=schedule,
            scheduled_playback=scheduled_playback,
            stream_description=stream_description,
            stream_embed=stream_embed,
            stream_password=stream_password,
            stream_privacy=stream_privacy,
            stream_title=stream_title,
            time_zone=time_zone,
        )
        return self._create_live_event_oapg(
            body=args.body,
        )


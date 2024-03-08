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

from vimeo_python_sdk.model.live_essentials_update_event_belonging_to_authenticated_user_request_stream_embed import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamEmbed as LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamEmbedSchema
from vimeo_python_sdk.model.live_essentials_update_event_belonging_to_authenticated_user_request_schedule import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestSchedule as LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestScheduleSchema
from vimeo_python_sdk.model.live_essentials_update_event_belonging_to_authenticated_user_request import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest as LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestSchema
from vimeo_python_sdk.model.live_essentials_update_event_belonging_to_authenticated_user_request_embed import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbed as LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbedSchema
from vimeo_python_sdk.model.live_essentials_update_event_belonging_to_authenticated_user_request_stream_privacy import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacy as LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacySchema
from vimeo_python_sdk.model.live_essentials_update_event_belonging_to_authenticated_user_request_content_rating import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestContentRating as LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestContentRatingSchema
from vimeo_python_sdk.model.error import Error as ErrorSchema
from vimeo_python_sdk.model.live_event_recurring import LiveEventRecurring as LiveEventRecurringSchema
from vimeo_python_sdk.model.live_essentials_update_event_belonging_to_authenticated_user_request_interaction_tools_settings import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings as LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettingsSchema

from vimeo_python_sdk.type.live_essentials_update_event_belonging_to_authenticated_user_request_stream_privacy import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacy
from vimeo_python_sdk.type.live_essentials_update_event_belonging_to_authenticated_user_request_embed import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbed
from vimeo_python_sdk.type.live_essentials_update_event_belonging_to_authenticated_user_request_stream_embed import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamEmbed
from vimeo_python_sdk.type.live_essentials_update_event_belonging_to_authenticated_user_request_interaction_tools_settings import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings
from vimeo_python_sdk.type.error import Error
from vimeo_python_sdk.type.live_event_recurring import LiveEventRecurring
from vimeo_python_sdk.type.live_essentials_update_event_belonging_to_authenticated_user_request_content_rating import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestContentRating
from vimeo_python_sdk.type.live_essentials_update_event_belonging_to_authenticated_user_request import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest
from vimeo_python_sdk.type.live_essentials_update_event_belonging_to_authenticated_user_request_schedule import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestSchedule

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.error import Error as ErrorPydantic
from vimeo_python_sdk.pydantic.live_essentials_update_event_belonging_to_authenticated_user_request_schedule import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestSchedule as LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestSchedulePydantic
from vimeo_python_sdk.pydantic.live_essentials_update_event_belonging_to_authenticated_user_request_content_rating import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestContentRating as LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestContentRatingPydantic
from vimeo_python_sdk.pydantic.live_essentials_update_event_belonging_to_authenticated_user_request_interaction_tools_settings import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings as LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettingsPydantic
from vimeo_python_sdk.pydantic.live_essentials_update_event_belonging_to_authenticated_user_request_stream_embed import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamEmbed as LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamEmbedPydantic
from vimeo_python_sdk.pydantic.live_essentials_update_event_belonging_to_authenticated_user_request import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest as LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestPydantic
from vimeo_python_sdk.pydantic.live_essentials_update_event_belonging_to_authenticated_user_request_stream_privacy import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacy as LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacyPydantic
from vimeo_python_sdk.pydantic.live_essentials_update_event_belonging_to_authenticated_user_request_embed import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbed as LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbedPydantic
from vimeo_python_sdk.pydantic.live_event_recurring import LiveEventRecurring as LiveEventRecurringPydantic

# Path params
LiveEventIdSchema = schemas.NumberSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'live_event_id': typing.Union[LiveEventIdSchema, decimal.Decimal, int, float, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_live_event_id = api_client.PathParameter(
    name="live_event_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=LiveEventIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationVndVimeoLiveEventRecurringjson = LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestSchema


request_body_live_essentials_update_event_belonging_to_authenticated_user_request = api_client.RequestBody(
    content={
        'application/vnd.vimeo.live.event.recurring+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndVimeoLiveEventRecurringjson),
    },
)
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
SchemaFor404ResponseBodyApplicationVndVimeoLiveEventRecurringjson = ErrorSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: Error


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/vnd.vimeo.live.event.recurring+json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationVndVimeoLiveEventRecurringjson),
    },
)
_all_accept_content_types = (
    'application/vnd.vimeo.live.event.recurring+json',
)


class BaseApi(api_client.Api):

    def _update_event_belonging_to_authenticated_user_mapped_args(
        self,
        live_event_id: typing.Union[int, float],
        title: typing.Optional[str] = None,
        auto_cc_enabled: typing.Optional[bool] = None,
        auto_cc_keywords: typing.Optional[str] = None,
        auto_cc_language: typing.Optional[str] = None,
        automatically_title_stream: typing.Optional[bool] = None,
        chat_enabled: typing.Optional[bool] = None,
        content_rating: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestContentRating] = None,
        dvr: typing.Optional[bool] = None,
        embed: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbed] = None,
        interaction_tools_settings: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings] = None,
        playlist_sort: typing.Optional[str] = None,
        schedule: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestSchedule] = None,
        scheduled_playback: typing.Optional[bool] = None,
        stream_description: typing.Optional[str] = None,
        stream_embed: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamEmbed] = None,
        stream_mode: typing.Optional[str] = None,
        stream_password: typing.Optional[str] = None,
        stream_privacy: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacy] = None,
        stream_title: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if title is not None:
            _body["title"] = title
        if auto_cc_enabled is not None:
            _body["auto_cc_enabled"] = auto_cc_enabled
        if auto_cc_keywords is not None:
            _body["auto_cc_keywords"] = auto_cc_keywords
        if auto_cc_language is not None:
            _body["auto_cc_language"] = auto_cc_language
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
        if interaction_tools_settings is not None:
            _body["interaction_tools_settings"] = interaction_tools_settings
        if playlist_sort is not None:
            _body["playlist_sort"] = playlist_sort
        if schedule is not None:
            _body["schedule"] = schedule
        if scheduled_playback is not None:
            _body["scheduled_playback"] = scheduled_playback
        if stream_description is not None:
            _body["stream_description"] = stream_description
        if stream_embed is not None:
            _body["stream_embed"] = stream_embed
        if stream_mode is not None:
            _body["stream_mode"] = stream_mode
        if stream_password is not None:
            _body["stream_password"] = stream_password
        if stream_privacy is not None:
            _body["stream_privacy"] = stream_privacy
        if stream_title is not None:
            _body["stream_title"] = stream_title
        if time_zone is not None:
            _body["time_zone"] = time_zone
        args.body = _body
        if live_event_id is not None:
            _path_params["live_event_id"] = live_event_id
        args.path = _path_params
        return args

    async def _aupdate_event_belonging_to_authenticated_user_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Update a live event
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_live_event_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/live_events/{live_event_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_live_essentials_update_event_belonging_to_authenticated_user_request.serialize(body, content_type)
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


    def _update_event_belonging_to_authenticated_user_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Update a live event
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_live_event_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/live_events/{live_event_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_live_essentials_update_event_belonging_to_authenticated_user_request.serialize(body, content_type)
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


class UpdateEventBelongingToAuthenticatedUserRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_event_belonging_to_authenticated_user(
        self,
        live_event_id: typing.Union[int, float],
        title: typing.Optional[str] = None,
        auto_cc_enabled: typing.Optional[bool] = None,
        auto_cc_keywords: typing.Optional[str] = None,
        auto_cc_language: typing.Optional[str] = None,
        automatically_title_stream: typing.Optional[bool] = None,
        chat_enabled: typing.Optional[bool] = None,
        content_rating: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestContentRating] = None,
        dvr: typing.Optional[bool] = None,
        embed: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbed] = None,
        interaction_tools_settings: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings] = None,
        playlist_sort: typing.Optional[str] = None,
        schedule: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestSchedule] = None,
        scheduled_playback: typing.Optional[bool] = None,
        stream_description: typing.Optional[str] = None,
        stream_embed: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamEmbed] = None,
        stream_mode: typing.Optional[str] = None,
        stream_password: typing.Optional[str] = None,
        stream_privacy: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacy] = None,
        stream_title: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_event_belonging_to_authenticated_user_mapped_args(
            live_event_id=live_event_id,
            title=title,
            auto_cc_enabled=auto_cc_enabled,
            auto_cc_keywords=auto_cc_keywords,
            auto_cc_language=auto_cc_language,
            automatically_title_stream=automatically_title_stream,
            chat_enabled=chat_enabled,
            content_rating=content_rating,
            dvr=dvr,
            embed=embed,
            interaction_tools_settings=interaction_tools_settings,
            playlist_sort=playlist_sort,
            schedule=schedule,
            scheduled_playback=scheduled_playback,
            stream_description=stream_description,
            stream_embed=stream_embed,
            stream_mode=stream_mode,
            stream_password=stream_password,
            stream_privacy=stream_privacy,
            stream_title=stream_title,
            time_zone=time_zone,
        )
        return await self._aupdate_event_belonging_to_authenticated_user_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_event_belonging_to_authenticated_user(
        self,
        live_event_id: typing.Union[int, float],
        title: typing.Optional[str] = None,
        auto_cc_enabled: typing.Optional[bool] = None,
        auto_cc_keywords: typing.Optional[str] = None,
        auto_cc_language: typing.Optional[str] = None,
        automatically_title_stream: typing.Optional[bool] = None,
        chat_enabled: typing.Optional[bool] = None,
        content_rating: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestContentRating] = None,
        dvr: typing.Optional[bool] = None,
        embed: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbed] = None,
        interaction_tools_settings: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings] = None,
        playlist_sort: typing.Optional[str] = None,
        schedule: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestSchedule] = None,
        scheduled_playback: typing.Optional[bool] = None,
        stream_description: typing.Optional[str] = None,
        stream_embed: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamEmbed] = None,
        stream_mode: typing.Optional[str] = None,
        stream_password: typing.Optional[str] = None,
        stream_privacy: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacy] = None,
        stream_title: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_event_belonging_to_authenticated_user_mapped_args(
            live_event_id=live_event_id,
            title=title,
            auto_cc_enabled=auto_cc_enabled,
            auto_cc_keywords=auto_cc_keywords,
            auto_cc_language=auto_cc_language,
            automatically_title_stream=automatically_title_stream,
            chat_enabled=chat_enabled,
            content_rating=content_rating,
            dvr=dvr,
            embed=embed,
            interaction_tools_settings=interaction_tools_settings,
            playlist_sort=playlist_sort,
            schedule=schedule,
            scheduled_playback=scheduled_playback,
            stream_description=stream_description,
            stream_embed=stream_embed,
            stream_mode=stream_mode,
            stream_password=stream_password,
            stream_privacy=stream_privacy,
            stream_title=stream_title,
            time_zone=time_zone,
        )
        return self._update_event_belonging_to_authenticated_user_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateEventBelongingToAuthenticatedUser(BaseApi):

    async def aupdate_event_belonging_to_authenticated_user(
        self,
        live_event_id: typing.Union[int, float],
        title: typing.Optional[str] = None,
        auto_cc_enabled: typing.Optional[bool] = None,
        auto_cc_keywords: typing.Optional[str] = None,
        auto_cc_language: typing.Optional[str] = None,
        automatically_title_stream: typing.Optional[bool] = None,
        chat_enabled: typing.Optional[bool] = None,
        content_rating: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestContentRating] = None,
        dvr: typing.Optional[bool] = None,
        embed: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbed] = None,
        interaction_tools_settings: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings] = None,
        playlist_sort: typing.Optional[str] = None,
        schedule: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestSchedule] = None,
        scheduled_playback: typing.Optional[bool] = None,
        stream_description: typing.Optional[str] = None,
        stream_embed: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamEmbed] = None,
        stream_mode: typing.Optional[str] = None,
        stream_password: typing.Optional[str] = None,
        stream_privacy: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacy] = None,
        stream_title: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> LiveEventRecurringPydantic:
        raw_response = await self.raw.aupdate_event_belonging_to_authenticated_user(
            live_event_id=live_event_id,
            title=title,
            auto_cc_enabled=auto_cc_enabled,
            auto_cc_keywords=auto_cc_keywords,
            auto_cc_language=auto_cc_language,
            automatically_title_stream=automatically_title_stream,
            chat_enabled=chat_enabled,
            content_rating=content_rating,
            dvr=dvr,
            embed=embed,
            interaction_tools_settings=interaction_tools_settings,
            playlist_sort=playlist_sort,
            schedule=schedule,
            scheduled_playback=scheduled_playback,
            stream_description=stream_description,
            stream_embed=stream_embed,
            stream_mode=stream_mode,
            stream_password=stream_password,
            stream_privacy=stream_privacy,
            stream_title=stream_title,
            time_zone=time_zone,
            **kwargs,
        )
        if validate:
            return LiveEventRecurringPydantic(**raw_response.body)
        return api_client.construct_model_instance(LiveEventRecurringPydantic, raw_response.body)
    
    
    def update_event_belonging_to_authenticated_user(
        self,
        live_event_id: typing.Union[int, float],
        title: typing.Optional[str] = None,
        auto_cc_enabled: typing.Optional[bool] = None,
        auto_cc_keywords: typing.Optional[str] = None,
        auto_cc_language: typing.Optional[str] = None,
        automatically_title_stream: typing.Optional[bool] = None,
        chat_enabled: typing.Optional[bool] = None,
        content_rating: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestContentRating] = None,
        dvr: typing.Optional[bool] = None,
        embed: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbed] = None,
        interaction_tools_settings: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings] = None,
        playlist_sort: typing.Optional[str] = None,
        schedule: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestSchedule] = None,
        scheduled_playback: typing.Optional[bool] = None,
        stream_description: typing.Optional[str] = None,
        stream_embed: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamEmbed] = None,
        stream_mode: typing.Optional[str] = None,
        stream_password: typing.Optional[str] = None,
        stream_privacy: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacy] = None,
        stream_title: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
        validate: bool = False,
    ) -> LiveEventRecurringPydantic:
        raw_response = self.raw.update_event_belonging_to_authenticated_user(
            live_event_id=live_event_id,
            title=title,
            auto_cc_enabled=auto_cc_enabled,
            auto_cc_keywords=auto_cc_keywords,
            auto_cc_language=auto_cc_language,
            automatically_title_stream=automatically_title_stream,
            chat_enabled=chat_enabled,
            content_rating=content_rating,
            dvr=dvr,
            embed=embed,
            interaction_tools_settings=interaction_tools_settings,
            playlist_sort=playlist_sort,
            schedule=schedule,
            scheduled_playback=scheduled_playback,
            stream_description=stream_description,
            stream_embed=stream_embed,
            stream_mode=stream_mode,
            stream_password=stream_password,
            stream_privacy=stream_privacy,
            stream_title=stream_title,
            time_zone=time_zone,
        )
        if validate:
            return LiveEventRecurringPydantic(**raw_response.body)
        return api_client.construct_model_instance(LiveEventRecurringPydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        live_event_id: typing.Union[int, float],
        title: typing.Optional[str] = None,
        auto_cc_enabled: typing.Optional[bool] = None,
        auto_cc_keywords: typing.Optional[str] = None,
        auto_cc_language: typing.Optional[str] = None,
        automatically_title_stream: typing.Optional[bool] = None,
        chat_enabled: typing.Optional[bool] = None,
        content_rating: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestContentRating] = None,
        dvr: typing.Optional[bool] = None,
        embed: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbed] = None,
        interaction_tools_settings: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings] = None,
        playlist_sort: typing.Optional[str] = None,
        schedule: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestSchedule] = None,
        scheduled_playback: typing.Optional[bool] = None,
        stream_description: typing.Optional[str] = None,
        stream_embed: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamEmbed] = None,
        stream_mode: typing.Optional[str] = None,
        stream_password: typing.Optional[str] = None,
        stream_privacy: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacy] = None,
        stream_title: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_event_belonging_to_authenticated_user_mapped_args(
            live_event_id=live_event_id,
            title=title,
            auto_cc_enabled=auto_cc_enabled,
            auto_cc_keywords=auto_cc_keywords,
            auto_cc_language=auto_cc_language,
            automatically_title_stream=automatically_title_stream,
            chat_enabled=chat_enabled,
            content_rating=content_rating,
            dvr=dvr,
            embed=embed,
            interaction_tools_settings=interaction_tools_settings,
            playlist_sort=playlist_sort,
            schedule=schedule,
            scheduled_playback=scheduled_playback,
            stream_description=stream_description,
            stream_embed=stream_embed,
            stream_mode=stream_mode,
            stream_password=stream_password,
            stream_privacy=stream_privacy,
            stream_title=stream_title,
            time_zone=time_zone,
        )
        return await self._aupdate_event_belonging_to_authenticated_user_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        live_event_id: typing.Union[int, float],
        title: typing.Optional[str] = None,
        auto_cc_enabled: typing.Optional[bool] = None,
        auto_cc_keywords: typing.Optional[str] = None,
        auto_cc_language: typing.Optional[str] = None,
        automatically_title_stream: typing.Optional[bool] = None,
        chat_enabled: typing.Optional[bool] = None,
        content_rating: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestContentRating] = None,
        dvr: typing.Optional[bool] = None,
        embed: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbed] = None,
        interaction_tools_settings: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings] = None,
        playlist_sort: typing.Optional[str] = None,
        schedule: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestSchedule] = None,
        scheduled_playback: typing.Optional[bool] = None,
        stream_description: typing.Optional[str] = None,
        stream_embed: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamEmbed] = None,
        stream_mode: typing.Optional[str] = None,
        stream_password: typing.Optional[str] = None,
        stream_privacy: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacy] = None,
        stream_title: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_event_belonging_to_authenticated_user_mapped_args(
            live_event_id=live_event_id,
            title=title,
            auto_cc_enabled=auto_cc_enabled,
            auto_cc_keywords=auto_cc_keywords,
            auto_cc_language=auto_cc_language,
            automatically_title_stream=automatically_title_stream,
            chat_enabled=chat_enabled,
            content_rating=content_rating,
            dvr=dvr,
            embed=embed,
            interaction_tools_settings=interaction_tools_settings,
            playlist_sort=playlist_sort,
            schedule=schedule,
            scheduled_playback=scheduled_playback,
            stream_description=stream_description,
            stream_embed=stream_embed,
            stream_mode=stream_mode,
            stream_password=stream_password,
            stream_privacy=stream_privacy,
            stream_title=stream_title,
            time_zone=time_zone,
        )
        return self._update_event_belonging_to_authenticated_user_oapg(
            body=args.body,
            path_params=args.path,
        )


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

from vimeo_python_sdk.model.videos_unlisted_videos_grant_access_to_users_response import VideosUnlistedVideosGrantAccessToUsersResponse as VideosUnlistedVideosGrantAccessToUsersResponseSchema

from vimeo_python_sdk.type.videos_unlisted_videos_grant_access_to_users_response import VideosUnlistedVideosGrantAccessToUsersResponse

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.videos_unlisted_videos_grant_access_to_users_response import VideosUnlistedVideosGrantAccessToUsersResponse as VideosUnlistedVideosGrantAccessToUsersResponsePydantic

from . import path

# Path params
ChannelIdSchema = schemas.NumberSchema
VideoIdSchema = schemas.NumberSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'channel_id': typing.Union[ChannelIdSchema, decimal.Decimal, int, float, ],
        'video_id': typing.Union[VideoIdSchema, decimal.Decimal, int, float, ],
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


request_path_channel_id = api_client.PathParameter(
    name="channel_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ChannelIdSchema,
    required=True,
)
request_path_video_id = api_client.PathParameter(
    name="video_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=VideoIdSchema,
    required=True,
)
_auth = [
    'oauth2',
    'oauth2',
]
SchemaFor200ResponseBodyApplicationVndVimeoUserjson = VideosUnlistedVideosGrantAccessToUsersResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: VideosUnlistedVideosGrantAccessToUsersResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: VideosUnlistedVideosGrantAccessToUsersResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.user+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoUserjson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/vnd.vimeo.user+json',
)


class BaseApi(api_client.Api):

    def _grant_access_to_users_mapped_args(
        self,
        channel_id: typing.Union[int, float],
        video_id: typing.Union[int, float],
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if channel_id is not None:
            _path_params["channel_id"] = channel_id
        if video_id is not None:
            _path_params["video_id"] = video_id
        args.path = _path_params
        return args

    async def _agrant_access_to_users_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Permit a list of users to access an unlisted video
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_channel_id,
            request_path_video_id,
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
        method = 'put'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/channels/{channel_id}/videos/{video_id}/privacy/users',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _grant_access_to_users_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Permit a list of users to access an unlisted video
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_channel_id,
            request_path_video_id,
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
        method = 'put'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/channels/{channel_id}/videos/{video_id}/privacy/users',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GrantAccessToUsersRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def agrant_access_to_users(
        self,
        channel_id: typing.Union[int, float],
        video_id: typing.Union[int, float],
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._grant_access_to_users_mapped_args(
            channel_id=channel_id,
            video_id=video_id,
        )
        return await self._agrant_access_to_users_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def grant_access_to_users(
        self,
        channel_id: typing.Union[int, float],
        video_id: typing.Union[int, float],
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._grant_access_to_users_mapped_args(
            channel_id=channel_id,
            video_id=video_id,
        )
        return self._grant_access_to_users_oapg(
            path_params=args.path,
        )

class GrantAccessToUsers(BaseApi):

    async def agrant_access_to_users(
        self,
        channel_id: typing.Union[int, float],
        video_id: typing.Union[int, float],
        validate: bool = False,
        **kwargs,
    ) -> VideosUnlistedVideosGrantAccessToUsersResponsePydantic:
        raw_response = await self.raw.agrant_access_to_users(
            channel_id=channel_id,
            video_id=video_id,
            **kwargs,
        )
        if validate:
            return RootModel[VideosUnlistedVideosGrantAccessToUsersResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(VideosUnlistedVideosGrantAccessToUsersResponsePydantic, raw_response.body)
    
    
    def grant_access_to_users(
        self,
        channel_id: typing.Union[int, float],
        video_id: typing.Union[int, float],
        validate: bool = False,
    ) -> VideosUnlistedVideosGrantAccessToUsersResponsePydantic:
        raw_response = self.raw.grant_access_to_users(
            channel_id=channel_id,
            video_id=video_id,
        )
        if validate:
            return RootModel[VideosUnlistedVideosGrantAccessToUsersResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(VideosUnlistedVideosGrantAccessToUsersResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        channel_id: typing.Union[int, float],
        video_id: typing.Union[int, float],
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._grant_access_to_users_mapped_args(
            channel_id=channel_id,
            video_id=video_id,
        )
        return await self._agrant_access_to_users_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        channel_id: typing.Union[int, float],
        video_id: typing.Union[int, float],
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._grant_access_to_users_mapped_args(
            channel_id=channel_id,
            video_id=video_id,
        )
        return self._grant_access_to_users_oapg(
            path_params=args.path,
        )


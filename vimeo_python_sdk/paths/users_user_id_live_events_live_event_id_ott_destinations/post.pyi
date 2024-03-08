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

from vimeo_python_sdk.model.error import Error as ErrorSchema
from vimeo_python_sdk.model.ott_destination import OttDestination as OttDestinationSchema

from vimeo_python_sdk.type.ott_destination import OttDestination
from vimeo_python_sdk.type.error import Error

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.error import Error as ErrorPydantic
from vimeo_python_sdk.pydantic.ott_destination import OttDestination as OttDestinationPydantic

# Path params
LiveEventIdSchema = schemas.NumberSchema
UserIdSchema = schemas.NumberSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'live_event_id': typing.Union[LiveEventIdSchema, decimal.Decimal, int, float, ],
        'user_id': typing.Union[UserIdSchema, decimal.Decimal, int, float, ],
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
request_path_user_id = api_client.PathParameter(
    name="user_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UserIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationVndVimeoLiveOttDestinationjson = OttDestinationSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: OttDestination


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: OttDestination


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.live.ott.destination+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoLiveOttDestinationjson),
    },
)
SchemaFor400ResponseBodyApplicationVndVimeoLiveOttDestinationjson = ErrorSchema


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
        'application/vnd.vimeo.live.ott.destination+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndVimeoLiveOttDestinationjson),
    },
)
SchemaFor401ResponseBodyApplicationVndVimeoLiveOttDestinationjson = ErrorSchema


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
        'application/vnd.vimeo.live.ott.destination+json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationVndVimeoLiveOttDestinationjson),
    },
)
SchemaFor403ResponseBodyApplicationVndVimeoLiveOttDestinationjson = ErrorSchema


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
        'application/vnd.vimeo.live.ott.destination+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationVndVimeoLiveOttDestinationjson),
    },
)
SchemaFor404ResponseBodyApplicationVndVimeoLiveOttDestinationjson = ErrorSchema


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
        'application/vnd.vimeo.live.ott.destination+json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationVndVimeoLiveOttDestinationjson),
    },
)
_all_accept_content_types = (
    'application/vnd.vimeo.live.ott.destination+json',
)


class BaseApi(api_client.Api):

    def _create_ott_destination_mapped_args(
        self,
        live_event_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if live_event_id is not None:
            _path_params["live_event_id"] = live_event_id
        if user_id is not None:
            _path_params["user_id"] = user_id
        args.path = _path_params
        return args

    async def _acreate_ott_destination_oapg(
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
        Create a live event OTT destination
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_live_event_id,
            request_path_user_id,
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
        method = 'post'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/users/{user_id}/live_events/{live_event_id}/ott_destinations',
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


    def _create_ott_destination_oapg(
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
        Create a live event OTT destination
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_live_event_id,
            request_path_user_id,
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
        method = 'post'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/users/{user_id}/live_events/{live_event_id}/ott_destinations',
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


class CreateOttDestinationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_ott_destination(
        self,
        live_event_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_ott_destination_mapped_args(
            live_event_id=live_event_id,
            user_id=user_id,
        )
        return await self._acreate_ott_destination_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def create_ott_destination(
        self,
        live_event_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_ott_destination_mapped_args(
            live_event_id=live_event_id,
            user_id=user_id,
        )
        return self._create_ott_destination_oapg(
            path_params=args.path,
        )

class CreateOttDestination(BaseApi):

    async def acreate_ott_destination(
        self,
        live_event_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        validate: bool = False,
        **kwargs,
    ) -> OttDestinationPydantic:
        raw_response = await self.raw.acreate_ott_destination(
            live_event_id=live_event_id,
            user_id=user_id,
            **kwargs,
        )
        if validate:
            return OttDestinationPydantic(**raw_response.body)
        return api_client.construct_model_instance(OttDestinationPydantic, raw_response.body)
    
    
    def create_ott_destination(
        self,
        live_event_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        validate: bool = False,
    ) -> OttDestinationPydantic:
        raw_response = self.raw.create_ott_destination(
            live_event_id=live_event_id,
            user_id=user_id,
        )
        if validate:
            return OttDestinationPydantic(**raw_response.body)
        return api_client.construct_model_instance(OttDestinationPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        live_event_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_ott_destination_mapped_args(
            live_event_id=live_event_id,
            user_id=user_id,
        )
        return await self._acreate_ott_destination_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        live_event_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_ott_destination_mapped_args(
            live_event_id=live_event_id,
            user_id=user_id,
        )
        return self._create_ott_destination_oapg(
            path_params=args.path,
        )


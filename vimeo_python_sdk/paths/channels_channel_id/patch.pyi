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

from vimeo_python_sdk.model.edit_channel_request import EditChannelRequest as EditChannelRequestSchema
from vimeo_python_sdk.model.channel import Channel as ChannelSchema
from vimeo_python_sdk.model.legacy_error import LegacyError as LegacyErrorSchema

from vimeo_python_sdk.type.channel import Channel
from vimeo_python_sdk.type.edit_channel_request import EditChannelRequest
from vimeo_python_sdk.type.legacy_error import LegacyError

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.channel import Channel as ChannelPydantic
from vimeo_python_sdk.pydantic.edit_channel_request import EditChannelRequest as EditChannelRequestPydantic
from vimeo_python_sdk.pydantic.legacy_error import LegacyError as LegacyErrorPydantic

# Path params
ChannelIdSchema = schemas.NumberSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'channel_id': typing.Union[ChannelIdSchema, decimal.Decimal, int, float, ],
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
# body param
SchemaForRequestBodyApplicationVndVimeoChanneljson = EditChannelRequestSchema


request_body_edit_channel_request = api_client.RequestBody(
    content={
        'application/vnd.vimeo.channel+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndVimeoChanneljson),
    },
)
SchemaFor200ResponseBodyApplicationVndVimeoChanneljson = ChannelSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Channel


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Channel


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.channel+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoChanneljson),
    },
)
SchemaFor400ResponseBodyApplicationVndVimeoChanneljson = LegacyErrorSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: LegacyError


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: LegacyError


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/vnd.vimeo.channel+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndVimeoChanneljson),
    },
)
_all_accept_content_types = (
    'application/vnd.vimeo.channel+json',
)


class BaseApi(api_client.Api):

    def _channel_2_mapped_args(
        self,
        channel_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        privacy: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if link is not None:
            _body["link"] = link
        if name is not None:
            _body["name"] = name
        if privacy is not None:
            _body["privacy"] = privacy
        args.body = _body
        if channel_id is not None:
            _path_params["channel_id"] = channel_id
        args.path = _path_params
        return args

    async def _achannel_2_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.channel+json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Edit a channel
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_channel_id,
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
            path_template='/channels/{channel_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_edit_channel_request.serialize(body, content_type)
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


    def _channel_2_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.channel+json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Edit a channel
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_channel_id,
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
            path_template='/channels/{channel_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_edit_channel_request.serialize(body, content_type)
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


class Channel2Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def achannel_2(
        self,
        channel_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        privacy: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._channel_2_mapped_args(
            channel_id=channel_id,
            description=description,
            link=link,
            name=name,
            privacy=privacy,
        )
        return await self._achannel_2_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def channel_2(
        self,
        channel_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        privacy: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._channel_2_mapped_args(
            channel_id=channel_id,
            description=description,
            link=link,
            name=name,
            privacy=privacy,
        )
        return self._channel_2_oapg(
            body=args.body,
            path_params=args.path,
        )

class Channel2(BaseApi):

    async def achannel_2(
        self,
        channel_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        privacy: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ChannelPydantic:
        raw_response = await self.raw.achannel_2(
            channel_id=channel_id,
            description=description,
            link=link,
            name=name,
            privacy=privacy,
            **kwargs,
        )
        if validate:
            return ChannelPydantic(**raw_response.body)
        return api_client.construct_model_instance(ChannelPydantic, raw_response.body)
    
    
    def channel_2(
        self,
        channel_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        privacy: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ChannelPydantic:
        raw_response = self.raw.channel_2(
            channel_id=channel_id,
            description=description,
            link=link,
            name=name,
            privacy=privacy,
        )
        if validate:
            return ChannelPydantic(**raw_response.body)
        return api_client.construct_model_instance(ChannelPydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        channel_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        privacy: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._channel_2_mapped_args(
            channel_id=channel_id,
            description=description,
            link=link,
            name=name,
            privacy=privacy,
        )
        return await self._achannel_2_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        channel_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        privacy: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._channel_2_mapped_args(
            channel_id=channel_id,
            description=description,
            link=link,
            name=name,
            privacy=privacy,
        )
        return self._channel_2_oapg(
            body=args.body,
            path_params=args.path,
        )


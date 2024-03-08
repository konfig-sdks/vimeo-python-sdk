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

from vimeo_python_sdk.model.auth import Auth as AuthSchema
from vimeo_python_sdk.model.client_auth_request import ClientAuthRequest as ClientAuthRequestSchema
from vimeo_python_sdk.model.error import Error as ErrorSchema

from vimeo_python_sdk.type.auth import Auth
from vimeo_python_sdk.type.error import Error
from vimeo_python_sdk.type.client_auth_request import ClientAuthRequest

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.error import Error as ErrorPydantic
from vimeo_python_sdk.pydantic.client_auth_request import ClientAuthRequest as ClientAuthRequestPydantic
from vimeo_python_sdk.pydantic.auth import Auth as AuthPydantic

# body param
SchemaForRequestBodyApplicationVndVimeoAuthjson = ClientAuthRequestSchema


request_body_client_auth_request = api_client.RequestBody(
    content={
        'application/vnd.vimeo.auth+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndVimeoAuthjson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationVndVimeoAuthjson = AuthSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Auth


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Auth


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.auth+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoAuthjson),
    },
)
SchemaFor401ResponseBodyApplicationVndVimeoAuthjson = ErrorSchema


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
        'application/vnd.vimeo.auth+json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationVndVimeoAuthjson),
    },
)
_all_accept_content_types = (
    'application/vnd.vimeo.auth+json',
)


class BaseApi(api_client.Api):

    def _auth_mapped_args(
        self,
        grant_type: str,
        scope: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if grant_type is not None:
            _body["grant_type"] = grant_type
        if scope is not None:
            _body["scope"] = scope
        args.body = _body
        return args

    async def _aauth_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.auth+json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Authorize a client with OAuth
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
            path_template='/oauth/authorize/client',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_client_auth_request.serialize(body, content_type)
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


    def _auth_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.auth+json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Authorize a client with OAuth
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
            path_template='/oauth/authorize/client',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_client_auth_request.serialize(body, content_type)
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


class AuthRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aauth(
        self,
        grant_type: str,
        scope: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._auth_mapped_args(
            grant_type=grant_type,
            scope=scope,
        )
        return await self._aauth_oapg(
            body=args.body,
            **kwargs,
        )
    
    def auth(
        self,
        grant_type: str,
        scope: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._auth_mapped_args(
            grant_type=grant_type,
            scope=scope,
        )
        return self._auth_oapg(
            body=args.body,
        )

class Auth(BaseApi):

    async def aauth(
        self,
        grant_type: str,
        scope: str,
        validate: bool = False,
        **kwargs,
    ) -> AuthPydantic:
        raw_response = await self.raw.aauth(
            grant_type=grant_type,
            scope=scope,
            **kwargs,
        )
        if validate:
            return AuthPydantic(**raw_response.body)
        return api_client.construct_model_instance(AuthPydantic, raw_response.body)
    
    
    def auth(
        self,
        grant_type: str,
        scope: str,
        validate: bool = False,
    ) -> AuthPydantic:
        raw_response = self.raw.auth(
            grant_type=grant_type,
            scope=scope,
        )
        if validate:
            return AuthPydantic(**raw_response.body)
        return api_client.construct_model_instance(AuthPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        grant_type: str,
        scope: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._auth_mapped_args(
            grant_type=grant_type,
            scope=scope,
        )
        return await self._aauth_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        grant_type: str,
        scope: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._auth_mapped_args(
            grant_type=grant_type,
            scope=scope,
        )
        return self._auth_oapg(
            body=args.body,
        )


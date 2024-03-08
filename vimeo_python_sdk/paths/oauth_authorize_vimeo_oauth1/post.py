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
from vimeo_python_sdk.model.authentication_extras_convert_o_auth1_to_o_auth2_request import AuthenticationExtrasConvertOAuth1ToOAuth2Request as AuthenticationExtrasConvertOAuth1ToOAuth2RequestSchema
from vimeo_python_sdk.model.auth_error import AuthError as AuthErrorSchema

from vimeo_python_sdk.type.authentication_extras_convert_o_auth1_to_o_auth2_request import AuthenticationExtrasConvertOAuth1ToOAuth2Request
from vimeo_python_sdk.type.auth_error import AuthError
from vimeo_python_sdk.type.auth import Auth

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.authentication_extras_convert_o_auth1_to_o_auth2_request import AuthenticationExtrasConvertOAuth1ToOAuth2Request as AuthenticationExtrasConvertOAuth1ToOAuth2RequestPydantic
from vimeo_python_sdk.pydantic.auth import Auth as AuthPydantic
from vimeo_python_sdk.pydantic.auth_error import AuthError as AuthErrorPydantic

from . import path

# body param
SchemaForRequestBodyApplicationVndVimeoAuthjson = AuthenticationExtrasConvertOAuth1ToOAuth2RequestSchema


request_body_authentication_extras_convert_o_auth1_to_o_auth2_request = api_client.RequestBody(
    content={
        'application/vnd.vimeo.auth+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndVimeoAuthjson),
    },
    required=True,
)
_auth = [
    'oauth2',
    'oauth2',
]
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
SchemaFor400ResponseBodyApplicationVndVimeoAuthjson = AuthErrorSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: AuthError


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: AuthError


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/vnd.vimeo.auth+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndVimeoAuthjson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
}
_all_accept_content_types = (
    'application/vnd.vimeo.auth+json',
)


class BaseApi(api_client.Api):

    def _o_auth1_to_o_auth2_mapped_args(
        self,
        grant_type: str,
        token: str,
        token_secret: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if grant_type is not None:
            _body["grant_type"] = grant_type
        if token is not None:
            _body["token"] = token
        if token_secret is not None:
            _body["token_secret"] = token_secret
        args.body = _body
        return args

    async def _ao_auth1_to_o_auth2_oapg(
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
        Convert an OAuth 1 access token to an OAuth 2 access token
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
            path_template='/oauth/authorize/vimeo_oauth1',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_authentication_extras_convert_o_auth1_to_o_auth2_request.serialize(body, content_type)
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


    def _o_auth1_to_o_auth2_oapg(
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
        Convert an OAuth 1 access token to an OAuth 2 access token
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
            path_template='/oauth/authorize/vimeo_oauth1',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_authentication_extras_convert_o_auth1_to_o_auth2_request.serialize(body, content_type)
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


class OAuth1ToOAuth2Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def ao_auth1_to_o_auth2(
        self,
        grant_type: str,
        token: str,
        token_secret: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._o_auth1_to_o_auth2_mapped_args(
            grant_type=grant_type,
            token=token,
            token_secret=token_secret,
        )
        return await self._ao_auth1_to_o_auth2_oapg(
            body=args.body,
            **kwargs,
        )
    
    def o_auth1_to_o_auth2(
        self,
        grant_type: str,
        token: str,
        token_secret: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._o_auth1_to_o_auth2_mapped_args(
            grant_type=grant_type,
            token=token,
            token_secret=token_secret,
        )
        return self._o_auth1_to_o_auth2_oapg(
            body=args.body,
        )

class OAuth1ToOAuth2(BaseApi):

    async def ao_auth1_to_o_auth2(
        self,
        grant_type: str,
        token: str,
        token_secret: str,
        validate: bool = False,
        **kwargs,
    ) -> AuthPydantic:
        raw_response = await self.raw.ao_auth1_to_o_auth2(
            grant_type=grant_type,
            token=token,
            token_secret=token_secret,
            **kwargs,
        )
        if validate:
            return AuthPydantic(**raw_response.body)
        return api_client.construct_model_instance(AuthPydantic, raw_response.body)
    
    
    def o_auth1_to_o_auth2(
        self,
        grant_type: str,
        token: str,
        token_secret: str,
        validate: bool = False,
    ) -> AuthPydantic:
        raw_response = self.raw.o_auth1_to_o_auth2(
            grant_type=grant_type,
            token=token,
            token_secret=token_secret,
        )
        if validate:
            return AuthPydantic(**raw_response.body)
        return api_client.construct_model_instance(AuthPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        grant_type: str,
        token: str,
        token_secret: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._o_auth1_to_o_auth2_mapped_args(
            grant_type=grant_type,
            token=token,
            token_secret=token_secret,
        )
        return await self._ao_auth1_to_o_auth2_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        grant_type: str,
        token: str,
        token_secret: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._o_auth1_to_o_auth2_mapped_args(
            grant_type=grant_type,
            token=token,
            token_secret=token_secret,
        )
        return self._o_auth1_to_o_auth2_oapg(
            body=args.body,
        )


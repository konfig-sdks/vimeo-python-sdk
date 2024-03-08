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

from vimeo_python_sdk.model.webinar import Webinar as WebinarSchema
from vimeo_python_sdk.model.error import Error as ErrorSchema

from vimeo_python_sdk.type.error import Error
from vimeo_python_sdk.type.webinar import Webinar

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.error import Error as ErrorPydantic
from vimeo_python_sdk.pydantic.webinar import Webinar as WebinarPydantic

from . import path

# Path params
WebinarIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'webinar_id': typing.Union[WebinarIdSchema, str, ],
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


request_path_webinar_id = api_client.PathParameter(
    name="webinar_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=WebinarIdSchema,
    required=True,
)
_auth = [
    'oauth2',
    'oauth2',
]
SchemaFor200ResponseBodyApplicationVndVimeoWebinarsjson = WebinarSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Webinar


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Webinar


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.webinars+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoWebinarsjson),
    },
)
SchemaFor404ResponseBodyApplicationVndVimeoWebinarsjson = ErrorSchema


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
        'application/vnd.vimeo.webinars+json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationVndVimeoWebinarsjson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/vnd.vimeo.webinars+json',
)


class BaseApi(api_client.Api):

    def _get_specific_webinar_mapped_args(
        self,
        webinar_id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if webinar_id is not None:
            _path_params["webinar_id"] = webinar_id
        args.path = _path_params
        return args

    async def _aget_specific_webinar_oapg(
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
        Get a specific webinar
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_webinar_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/me/webinars/{webinar_id}',
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


    def _get_specific_webinar_oapg(
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
        Get a specific webinar
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_webinar_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/me/webinars/{webinar_id}',
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


class GetSpecificWebinarRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @api_client.DeprecationWarningOnce(prefix="webinar\essentials")
    async def aget_specific_webinar(
        self,
        webinar_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_specific_webinar_mapped_args(
            webinar_id=webinar_id,
        )
        return await self._aget_specific_webinar_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="webinar\essentials")
    def get_specific_webinar(
        self,
        webinar_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_specific_webinar_mapped_args(
            webinar_id=webinar_id,
        )
        return self._get_specific_webinar_oapg(
            path_params=args.path,
        )

class GetSpecificWebinar(BaseApi):

    @api_client.DeprecationWarningOnce(prefix="webinar\essentials")
    async def aget_specific_webinar(
        self,
        webinar_id: str,
        validate: bool = False,
        **kwargs,
    ) -> WebinarPydantic:
        raw_response = await self.raw.aget_specific_webinar(
            webinar_id=webinar_id,
            **kwargs,
        )
        if validate:
            return WebinarPydantic(**raw_response.body)
        return api_client.construct_model_instance(WebinarPydantic, raw_response.body)
    
    
    @api_client.DeprecationWarningOnce(prefix="webinar\essentials")
    def get_specific_webinar(
        self,
        webinar_id: str,
        validate: bool = False,
    ) -> WebinarPydantic:
        raw_response = self.raw.get_specific_webinar(
            webinar_id=webinar_id,
        )
        if validate:
            return WebinarPydantic(**raw_response.body)
        return api_client.construct_model_instance(WebinarPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @api_client.DeprecationWarningOnce(prefix="webinar\essentials")
    async def aget(
        self,
        webinar_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_specific_webinar_mapped_args(
            webinar_id=webinar_id,
        )
        return await self._aget_specific_webinar_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="webinar\essentials")
    def get(
        self,
        webinar_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_specific_webinar_mapped_args(
            webinar_id=webinar_id,
        )
        return self._get_specific_webinar_oapg(
            path_params=args.path,
        )


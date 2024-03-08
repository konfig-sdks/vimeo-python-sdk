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

from vimeo_python_sdk.model.videos_showcases_add_to_multiple_showcases_request import VideosShowcasesAddToMultipleShowcasesRequest as VideosShowcasesAddToMultipleShowcasesRequestSchema
from vimeo_python_sdk.model.videos_showcases_add_to_multiple_showcases_request_remove import VideosShowcasesAddToMultipleShowcasesRequestRemove as VideosShowcasesAddToMultipleShowcasesRequestRemoveSchema
from vimeo_python_sdk.model.error import Error as ErrorSchema
from vimeo_python_sdk.model.videos_showcases_add_to_multiple_showcases_request_add import VideosShowcasesAddToMultipleShowcasesRequestAdd as VideosShowcasesAddToMultipleShowcasesRequestAddSchema
from vimeo_python_sdk.model.videos_showcases_add_to_multiple_showcases_response import VideosShowcasesAddToMultipleShowcasesResponse as VideosShowcasesAddToMultipleShowcasesResponseSchema

from vimeo_python_sdk.type.videos_showcases_add_to_multiple_showcases_request_remove import VideosShowcasesAddToMultipleShowcasesRequestRemove
from vimeo_python_sdk.type.videos_showcases_add_to_multiple_showcases_request_add import VideosShowcasesAddToMultipleShowcasesRequestAdd
from vimeo_python_sdk.type.error import Error
from vimeo_python_sdk.type.videos_showcases_add_to_multiple_showcases_request import VideosShowcasesAddToMultipleShowcasesRequest
from vimeo_python_sdk.type.videos_showcases_add_to_multiple_showcases_response import VideosShowcasesAddToMultipleShowcasesResponse

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.error import Error as ErrorPydantic
from vimeo_python_sdk.pydantic.videos_showcases_add_to_multiple_showcases_request_add import VideosShowcasesAddToMultipleShowcasesRequestAdd as VideosShowcasesAddToMultipleShowcasesRequestAddPydantic
from vimeo_python_sdk.pydantic.videos_showcases_add_to_multiple_showcases_response import VideosShowcasesAddToMultipleShowcasesResponse as VideosShowcasesAddToMultipleShowcasesResponsePydantic
from vimeo_python_sdk.pydantic.videos_showcases_add_to_multiple_showcases_request_remove import VideosShowcasesAddToMultipleShowcasesRequestRemove as VideosShowcasesAddToMultipleShowcasesRequestRemovePydantic
from vimeo_python_sdk.pydantic.videos_showcases_add_to_multiple_showcases_request import VideosShowcasesAddToMultipleShowcasesRequest as VideosShowcasesAddToMultipleShowcasesRequestPydantic

# Path params
VideoIdSchema = schemas.NumberSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
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


request_path_video_id = api_client.PathParameter(
    name="video_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=VideoIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationVndVimeoAlbumjson = VideosShowcasesAddToMultipleShowcasesRequestSchema


request_body_videos_showcases_add_to_multiple_showcases_request = api_client.RequestBody(
    content={
        'application/vnd.vimeo.album+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndVimeoAlbumjson),
    },
)
SchemaFor200ResponseBodyApplicationVndVimeoAlbumjson = VideosShowcasesAddToMultipleShowcasesResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: VideosShowcasesAddToMultipleShowcasesResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: VideosShowcasesAddToMultipleShowcasesResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.album+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoAlbumjson),
    },
)
SchemaFor404ResponseBodyApplicationVndVimeoAlbumjson = ErrorSchema


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
        'application/vnd.vimeo.album+json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationVndVimeoAlbumjson),
    },
)
_all_accept_content_types = (
    'application/vnd.vimeo.album+json',
)


class BaseApi(api_client.Api):

    def _add_to_multiple_showcases_mapped_args(
        self,
        video_id: typing.Union[int, float],
        add: typing.Optional[VideosShowcasesAddToMultipleShowcasesRequestAdd] = None,
        remove: typing.Optional[VideosShowcasesAddToMultipleShowcasesRequestRemove] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if add is not None:
            _body["add"] = add
        if remove is not None:
            _body["remove"] = remove
        args.body = _body
        if video_id is not None:
            _path_params["video_id"] = video_id
        args.path = _path_params
        return args

    async def _aadd_to_multiple_showcases_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.album+json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Add or remove a video from a list of showcases
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/videos/{video_id}/albums',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_videos_showcases_add_to_multiple_showcases_request.serialize(body, content_type)
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


    def _add_to_multiple_showcases_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.album+json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Add or remove a video from a list of showcases
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/videos/{video_id}/albums',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_videos_showcases_add_to_multiple_showcases_request.serialize(body, content_type)
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


class AddToMultipleShowcasesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_to_multiple_showcases(
        self,
        video_id: typing.Union[int, float],
        add: typing.Optional[VideosShowcasesAddToMultipleShowcasesRequestAdd] = None,
        remove: typing.Optional[VideosShowcasesAddToMultipleShowcasesRequestRemove] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_to_multiple_showcases_mapped_args(
            video_id=video_id,
            add=add,
            remove=remove,
        )
        return await self._aadd_to_multiple_showcases_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def add_to_multiple_showcases(
        self,
        video_id: typing.Union[int, float],
        add: typing.Optional[VideosShowcasesAddToMultipleShowcasesRequestAdd] = None,
        remove: typing.Optional[VideosShowcasesAddToMultipleShowcasesRequestRemove] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_to_multiple_showcases_mapped_args(
            video_id=video_id,
            add=add,
            remove=remove,
        )
        return self._add_to_multiple_showcases_oapg(
            body=args.body,
            path_params=args.path,
        )

class AddToMultipleShowcases(BaseApi):

    async def aadd_to_multiple_showcases(
        self,
        video_id: typing.Union[int, float],
        add: typing.Optional[VideosShowcasesAddToMultipleShowcasesRequestAdd] = None,
        remove: typing.Optional[VideosShowcasesAddToMultipleShowcasesRequestRemove] = None,
        validate: bool = False,
        **kwargs,
    ) -> VideosShowcasesAddToMultipleShowcasesResponsePydantic:
        raw_response = await self.raw.aadd_to_multiple_showcases(
            video_id=video_id,
            add=add,
            remove=remove,
            **kwargs,
        )
        if validate:
            return RootModel[VideosShowcasesAddToMultipleShowcasesResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(VideosShowcasesAddToMultipleShowcasesResponsePydantic, raw_response.body)
    
    
    def add_to_multiple_showcases(
        self,
        video_id: typing.Union[int, float],
        add: typing.Optional[VideosShowcasesAddToMultipleShowcasesRequestAdd] = None,
        remove: typing.Optional[VideosShowcasesAddToMultipleShowcasesRequestRemove] = None,
        validate: bool = False,
    ) -> VideosShowcasesAddToMultipleShowcasesResponsePydantic:
        raw_response = self.raw.add_to_multiple_showcases(
            video_id=video_id,
            add=add,
            remove=remove,
        )
        if validate:
            return RootModel[VideosShowcasesAddToMultipleShowcasesResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(VideosShowcasesAddToMultipleShowcasesResponsePydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        video_id: typing.Union[int, float],
        add: typing.Optional[VideosShowcasesAddToMultipleShowcasesRequestAdd] = None,
        remove: typing.Optional[VideosShowcasesAddToMultipleShowcasesRequestRemove] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_to_multiple_showcases_mapped_args(
            video_id=video_id,
            add=add,
            remove=remove,
        )
        return await self._aadd_to_multiple_showcases_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        video_id: typing.Union[int, float],
        add: typing.Optional[VideosShowcasesAddToMultipleShowcasesRequestAdd] = None,
        remove: typing.Optional[VideosShowcasesAddToMultipleShowcasesRequestRemove] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_to_multiple_showcases_mapped_args(
            video_id=video_id,
            add=add,
            remove=remove,
        )
        return self._add_to_multiple_showcases_oapg(
            body=args.body,
            path_params=args.path,
        )


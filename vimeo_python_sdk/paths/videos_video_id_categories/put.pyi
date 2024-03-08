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

from vimeo_python_sdk.model.categories_videos_set_video_categories_request_category import CategoriesVideosSetVideoCategoriesRequestCategory as CategoriesVideosSetVideoCategoriesRequestCategorySchema
from vimeo_python_sdk.model.category import Category as CategorySchema
from vimeo_python_sdk.model.categories_videos_set_video_categories_request import CategoriesVideosSetVideoCategoriesRequest as CategoriesVideosSetVideoCategoriesRequestSchema
from vimeo_python_sdk.model.legacy_error import LegacyError as LegacyErrorSchema

from vimeo_python_sdk.type.category import Category
from vimeo_python_sdk.type.categories_videos_set_video_categories_request import CategoriesVideosSetVideoCategoriesRequest
from vimeo_python_sdk.type.legacy_error import LegacyError
from vimeo_python_sdk.type.categories_videos_set_video_categories_request_category import CategoriesVideosSetVideoCategoriesRequestCategory

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.categories_videos_set_video_categories_request_category import CategoriesVideosSetVideoCategoriesRequestCategory as CategoriesVideosSetVideoCategoriesRequestCategoryPydantic
from vimeo_python_sdk.pydantic.category import Category as CategoryPydantic
from vimeo_python_sdk.pydantic.legacy_error import LegacyError as LegacyErrorPydantic
from vimeo_python_sdk.pydantic.categories_videos_set_video_categories_request import CategoriesVideosSetVideoCategoriesRequest as CategoriesVideosSetVideoCategoriesRequestPydantic

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
SchemaForRequestBodyApplicationVndVimeoCategoryjson = CategoriesVideosSetVideoCategoriesRequestSchema


request_body_categories_videos_set_video_categories_request = api_client.RequestBody(
    content={
        'application/vnd.vimeo.category+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndVimeoCategoryjson),
    },
    required=True,
)
SchemaFor201ResponseBodyApplicationVndVimeoCategoryjson = CategorySchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Category


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Category


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/vnd.vimeo.category+json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationVndVimeoCategoryjson),
    },
)
SchemaFor403ResponseBodyApplicationVndVimeoCategoryjson = LegacyErrorSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: LegacyError


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: LegacyError


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/vnd.vimeo.category+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationVndVimeoCategoryjson),
    },
)
SchemaFor404ResponseBodyApplicationVndVimeoCategoryjson = LegacyErrorSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: LegacyError


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: LegacyError


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/vnd.vimeo.category+json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationVndVimeoCategoryjson),
    },
)
_all_accept_content_types = (
    'application/vnd.vimeo.category+json',
)


class BaseApi(api_client.Api):

    def _set_video_categories_mapped_args(
        self,
        category: CategoriesVideosSetVideoCategoriesRequestCategory,
        video_id: typing.Union[int, float],
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if category is not None:
            _body["category"] = category
        args.body = _body
        if video_id is not None:
            _path_params["video_id"] = video_id
        args.path = _path_params
        return args

    async def _aset_video_categories_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.category+json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Suggest categories for a video
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
        method = 'put'.upper()
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
            path_template='/videos/{video_id}/categories',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_categories_videos_set_video_categories_request.serialize(body, content_type)
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


    def _set_video_categories_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.category+json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Suggest categories for a video
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
        method = 'put'.upper()
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
            path_template='/videos/{video_id}/categories',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_categories_videos_set_video_categories_request.serialize(body, content_type)
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


class SetVideoCategoriesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aset_video_categories(
        self,
        category: CategoriesVideosSetVideoCategoriesRequestCategory,
        video_id: typing.Union[int, float],
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._set_video_categories_mapped_args(
            category=category,
            video_id=video_id,
        )
        return await self._aset_video_categories_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def set_video_categories(
        self,
        category: CategoriesVideosSetVideoCategoriesRequestCategory,
        video_id: typing.Union[int, float],
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._set_video_categories_mapped_args(
            category=category,
            video_id=video_id,
        )
        return self._set_video_categories_oapg(
            body=args.body,
            path_params=args.path,
        )

class SetVideoCategories(BaseApi):

    async def aset_video_categories(
        self,
        category: CategoriesVideosSetVideoCategoriesRequestCategory,
        video_id: typing.Union[int, float],
        validate: bool = False,
        **kwargs,
    ) -> CategoryPydantic:
        raw_response = await self.raw.aset_video_categories(
            category=category,
            video_id=video_id,
            **kwargs,
        )
        if validate:
            return CategoryPydantic(**raw_response.body)
        return api_client.construct_model_instance(CategoryPydantic, raw_response.body)
    
    
    def set_video_categories(
        self,
        category: CategoriesVideosSetVideoCategoriesRequestCategory,
        video_id: typing.Union[int, float],
        validate: bool = False,
    ) -> CategoryPydantic:
        raw_response = self.raw.set_video_categories(
            category=category,
            video_id=video_id,
        )
        if validate:
            return CategoryPydantic(**raw_response.body)
        return api_client.construct_model_instance(CategoryPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        category: CategoriesVideosSetVideoCategoriesRequestCategory,
        video_id: typing.Union[int, float],
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._set_video_categories_mapped_args(
            category=category,
            video_id=video_id,
        )
        return await self._aset_video_categories_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        category: CategoriesVideosSetVideoCategoriesRequestCategory,
        video_id: typing.Union[int, float],
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._set_video_categories_mapped_args(
            category=category,
            video_id=video_id,
        )
        return self._set_video_categories_oapg(
            body=args.body,
            path_params=args.path,
        )


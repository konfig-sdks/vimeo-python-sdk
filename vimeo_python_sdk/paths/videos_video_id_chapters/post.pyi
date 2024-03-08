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

from vimeo_python_sdk.model.create_chapter_request_thumbnail_uris import CreateChapterRequestThumbnailUris as CreateChapterRequestThumbnailUrisSchema
from vimeo_python_sdk.model.chapter import Chapter as ChapterSchema
from vimeo_python_sdk.model.legacy_error import LegacyError as LegacyErrorSchema
from vimeo_python_sdk.model.create_chapter_request import CreateChapterRequest as CreateChapterRequestSchema

from vimeo_python_sdk.type.chapter import Chapter
from vimeo_python_sdk.type.create_chapter_request_thumbnail_uris import CreateChapterRequestThumbnailUris
from vimeo_python_sdk.type.create_chapter_request import CreateChapterRequest
from vimeo_python_sdk.type.legacy_error import LegacyError

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.chapter import Chapter as ChapterPydantic
from vimeo_python_sdk.pydantic.legacy_error import LegacyError as LegacyErrorPydantic
from vimeo_python_sdk.pydantic.create_chapter_request_thumbnail_uris import CreateChapterRequestThumbnailUris as CreateChapterRequestThumbnailUrisPydantic
from vimeo_python_sdk.pydantic.create_chapter_request import CreateChapterRequest as CreateChapterRequestPydantic

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
SchemaForRequestBodyApplicationVndVimeoVideoChapterjson = CreateChapterRequestSchema


request_body_create_chapter_request = api_client.RequestBody(
    content={
        'application/vnd.vimeo.video.chapter+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndVimeoVideoChapterjson),
    },
)
SchemaFor201ResponseBodyApplicationVndVimeoVideoChapterjson = ChapterSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Chapter


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Chapter


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/vnd.vimeo.video.chapter+json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationVndVimeoVideoChapterjson),
    },
)
SchemaFor403ResponseBodyApplicationVndVimeoVideoChapterjson = LegacyErrorSchema


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
        'application/vnd.vimeo.video.chapter+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationVndVimeoVideoChapterjson),
    },
)
_all_accept_content_types = (
    'application/vnd.vimeo.video.chapter+json',
)


class BaseApi(api_client.Api):

    def _chapter_mapped_args(
        self,
        video_id: typing.Union[int, float],
        title: typing.Optional[typing.Optional[str]] = None,
        active_thumbnail_uri: typing.Optional[str] = None,
        thumbnail_uris: typing.Optional[CreateChapterRequestThumbnailUris] = None,
        timecode: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if title is not None:
            _body["title"] = title
        if active_thumbnail_uri is not None:
            _body["active_thumbnail_uri"] = active_thumbnail_uri
        if thumbnail_uris is not None:
            _body["thumbnail_uris"] = thumbnail_uris
        if timecode is not None:
            _body["timecode"] = timecode
        args.body = _body
        if video_id is not None:
            _path_params["video_id"] = video_id
        args.path = _path_params
        return args

    async def _achapter_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.video.chapter+json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Add a chapter to a video
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/videos/{video_id}/chapters',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_chapter_request.serialize(body, content_type)
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


    def _chapter_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.video.chapter+json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Add a chapter to a video
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/videos/{video_id}/chapters',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_chapter_request.serialize(body, content_type)
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


class ChapterRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def achapter(
        self,
        video_id: typing.Union[int, float],
        title: typing.Optional[typing.Optional[str]] = None,
        active_thumbnail_uri: typing.Optional[str] = None,
        thumbnail_uris: typing.Optional[CreateChapterRequestThumbnailUris] = None,
        timecode: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._chapter_mapped_args(
            video_id=video_id,
            title=title,
            active_thumbnail_uri=active_thumbnail_uri,
            thumbnail_uris=thumbnail_uris,
            timecode=timecode,
        )
        return await self._achapter_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def chapter(
        self,
        video_id: typing.Union[int, float],
        title: typing.Optional[typing.Optional[str]] = None,
        active_thumbnail_uri: typing.Optional[str] = None,
        thumbnail_uris: typing.Optional[CreateChapterRequestThumbnailUris] = None,
        timecode: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._chapter_mapped_args(
            video_id=video_id,
            title=title,
            active_thumbnail_uri=active_thumbnail_uri,
            thumbnail_uris=thumbnail_uris,
            timecode=timecode,
        )
        return self._chapter_oapg(
            body=args.body,
            path_params=args.path,
        )

class Chapter(BaseApi):

    async def achapter(
        self,
        video_id: typing.Union[int, float],
        title: typing.Optional[typing.Optional[str]] = None,
        active_thumbnail_uri: typing.Optional[str] = None,
        thumbnail_uris: typing.Optional[CreateChapterRequestThumbnailUris] = None,
        timecode: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        validate: bool = False,
        **kwargs,
    ) -> ChapterPydantic:
        raw_response = await self.raw.achapter(
            video_id=video_id,
            title=title,
            active_thumbnail_uri=active_thumbnail_uri,
            thumbnail_uris=thumbnail_uris,
            timecode=timecode,
            **kwargs,
        )
        if validate:
            return ChapterPydantic(**raw_response.body)
        return api_client.construct_model_instance(ChapterPydantic, raw_response.body)
    
    
    def chapter(
        self,
        video_id: typing.Union[int, float],
        title: typing.Optional[typing.Optional[str]] = None,
        active_thumbnail_uri: typing.Optional[str] = None,
        thumbnail_uris: typing.Optional[CreateChapterRequestThumbnailUris] = None,
        timecode: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        validate: bool = False,
    ) -> ChapterPydantic:
        raw_response = self.raw.chapter(
            video_id=video_id,
            title=title,
            active_thumbnail_uri=active_thumbnail_uri,
            thumbnail_uris=thumbnail_uris,
            timecode=timecode,
        )
        if validate:
            return ChapterPydantic(**raw_response.body)
        return api_client.construct_model_instance(ChapterPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        video_id: typing.Union[int, float],
        title: typing.Optional[typing.Optional[str]] = None,
        active_thumbnail_uri: typing.Optional[str] = None,
        thumbnail_uris: typing.Optional[CreateChapterRequestThumbnailUris] = None,
        timecode: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._chapter_mapped_args(
            video_id=video_id,
            title=title,
            active_thumbnail_uri=active_thumbnail_uri,
            thumbnail_uris=thumbnail_uris,
            timecode=timecode,
        )
        return await self._achapter_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        video_id: typing.Union[int, float],
        title: typing.Optional[typing.Optional[str]] = None,
        active_thumbnail_uri: typing.Optional[str] = None,
        thumbnail_uris: typing.Optional[CreateChapterRequestThumbnailUris] = None,
        timecode: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._chapter_mapped_args(
            video_id=video_id,
            title=title,
            active_thumbnail_uri=active_thumbnail_uri,
            thumbnail_uris=thumbnail_uris,
            timecode=timecode,
        )
        return self._chapter_oapg(
            body=args.body,
            path_params=args.path,
        )


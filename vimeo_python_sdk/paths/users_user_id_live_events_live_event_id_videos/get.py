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
from vimeo_python_sdk.model.live_event_videos_list_all_videos_in_event_response import LiveEventVideosListAllVideosInEventResponse as LiveEventVideosListAllVideosInEventResponseSchema

from vimeo_python_sdk.type.error import Error
from vimeo_python_sdk.type.live_event_videos_list_all_videos_in_event_response import LiveEventVideosListAllVideosInEventResponse

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.error import Error as ErrorPydantic
from vimeo_python_sdk.pydantic.live_event_videos_list_all_videos_in_event_response import LiveEventVideosListAllVideosInEventResponse as LiveEventVideosListAllVideosInEventResponsePydantic

from . import path

# Query params
ContainingUriSchema = schemas.StrSchema


class DirectionSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "asc": "ASC",
            "desc": "DESC",
        }
    
    @schemas.classproperty
    def ASC(cls):
        return cls("asc")
    
    @schemas.classproperty
    def DESC(cls):
        return cls("desc")


class FilterSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "embeddable": "EMBEDDABLE",
        }
    
    @schemas.classproperty
    def EMBEDDABLE(cls):
        return cls("embeddable")
FilterEmbeddableSchema = schemas.BoolSchema
PageSchema = schemas.NumberSchema
PerPageSchema = schemas.NumberSchema
QuerySchema = schemas.StrSchema


class SortSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "added": "ADDED",
            "alphabetical": "ALPHABETICAL",
            "arranged": "ARRANGED",
            "comments": "COMMENTS",
            "date": "DATE",
            "duration": "DURATION",
            "likes": "LIKES",
            "plays": "PLAYS",
        }
    
    @schemas.classproperty
    def ADDED(cls):
        return cls("added")
    
    @schemas.classproperty
    def ALPHABETICAL(cls):
        return cls("alphabetical")
    
    @schemas.classproperty
    def ARRANGED(cls):
        return cls("arranged")
    
    @schemas.classproperty
    def COMMENTS(cls):
        return cls("comments")
    
    @schemas.classproperty
    def DATE(cls):
        return cls("date")
    
    @schemas.classproperty
    def DURATION(cls):
        return cls("duration")
    
    @schemas.classproperty
    def LIKES(cls):
        return cls("likes")
    
    @schemas.classproperty
    def PLAYS(cls):
        return cls("plays")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'containing_uri': typing.Union[ContainingUriSchema, str, ],
        'direction': typing.Union[DirectionSchema, str, ],
        'filter': typing.Union[FilterSchema, str, ],
        'filter_embeddable': typing.Union[FilterEmbeddableSchema, bool, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, float, ],
        'per_page': typing.Union[PerPageSchema, decimal.Decimal, int, float, ],
        'query': typing.Union[QuerySchema, str, ],
        'sort': typing.Union[SortSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_containing_uri = api_client.QueryParameter(
    name="containing_uri",
    style=api_client.ParameterStyle.FORM,
    schema=ContainingUriSchema,
    explode=True,
)
request_query_direction = api_client.QueryParameter(
    name="direction",
    style=api_client.ParameterStyle.FORM,
    schema=DirectionSchema,
    explode=True,
)
request_query_filter = api_client.QueryParameter(
    name="filter",
    style=api_client.ParameterStyle.FORM,
    schema=FilterSchema,
    explode=True,
)
request_query_filter_embeddable = api_client.QueryParameter(
    name="filter_embeddable",
    style=api_client.ParameterStyle.FORM,
    schema=FilterEmbeddableSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_per_page = api_client.QueryParameter(
    name="per_page",
    style=api_client.ParameterStyle.FORM,
    schema=PerPageSchema,
    explode=True,
)
request_query_query = api_client.QueryParameter(
    name="query",
    style=api_client.ParameterStyle.FORM,
    schema=QuerySchema,
    explode=True,
)
request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
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
_auth = [
    'oauth2',
    'oauth2',
]
SchemaFor200ResponseBodyApplicationVndVimeoVideojson = LiveEventVideosListAllVideosInEventResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: LiveEventVideosListAllVideosInEventResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: LiveEventVideosListAllVideosInEventResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.video+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoVideojson),
    },
)
SchemaFor400ResponseBodyApplicationVndVimeoVideojson = ErrorSchema


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
        'application/vnd.vimeo.video+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndVimeoVideojson),
    },
)
SchemaFor401ResponseBodyApplicationVndVimeoVideojson = ErrorSchema


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
        'application/vnd.vimeo.video+json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationVndVimeoVideojson),
    },
)
SchemaFor404ResponseBodyApplicationVndVimeoVideojson = ErrorSchema


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
        'application/vnd.vimeo.video+json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationVndVimeoVideojson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/vnd.vimeo.video+json',
)


class BaseApi(api_client.Api):

    def _list_all_videos_in_event_mapped_args(
        self,
        live_event_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        containing_uri: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_embeddable: typing.Optional[bool] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if containing_uri is not None:
            _query_params["containing_uri"] = containing_uri
        if direction is not None:
            _query_params["direction"] = direction
        if filter is not None:
            _query_params["filter"] = filter
        if filter_embeddable is not None:
            _query_params["filter_embeddable"] = filter_embeddable
        if page is not None:
            _query_params["page"] = page
        if per_page is not None:
            _query_params["per_page"] = per_page
        if query is not None:
            _query_params["query"] = query
        if sort is not None:
            _query_params["sort"] = sort
        if live_event_id is not None:
            _path_params["live_event_id"] = live_event_id
        if user_id is not None:
            _path_params["user_id"] = user_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _alist_all_videos_in_event_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        Get all the videos in a live event
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
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
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_containing_uri,
            request_query_direction,
            request_query_filter,
            request_query_filter_embeddable,
            request_query_page,
            request_query_per_page,
            request_query_query,
            request_query_sort,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
            path_template='/users/{user_id}/live_events/{live_event_id}/videos',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _list_all_videos_in_event_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        Get all the videos in a live event
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
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
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_containing_uri,
            request_query_direction,
            request_query_filter,
            request_query_filter_embeddable,
            request_query_page,
            request_query_per_page,
            request_query_query,
            request_query_sort,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
            path_template='/users/{user_id}/live_events/{live_event_id}/videos',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


class ListAllVideosInEventRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_all_videos_in_event(
        self,
        live_event_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        containing_uri: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_embeddable: typing.Optional[bool] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_all_videos_in_event_mapped_args(
            live_event_id=live_event_id,
            user_id=user_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
        )
        return await self._alist_all_videos_in_event_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def list_all_videos_in_event(
        self,
        live_event_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        containing_uri: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_embeddable: typing.Optional[bool] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_all_videos_in_event_mapped_args(
            live_event_id=live_event_id,
            user_id=user_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
        )
        return self._list_all_videos_in_event_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class ListAllVideosInEvent(BaseApi):

    async def alist_all_videos_in_event(
        self,
        live_event_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        containing_uri: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_embeddable: typing.Optional[bool] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> LiveEventVideosListAllVideosInEventResponsePydantic:
        raw_response = await self.raw.alist_all_videos_in_event(
            live_event_id=live_event_id,
            user_id=user_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            **kwargs,
        )
        if validate:
            return RootModel[LiveEventVideosListAllVideosInEventResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(LiveEventVideosListAllVideosInEventResponsePydantic, raw_response.body)
    
    
    def list_all_videos_in_event(
        self,
        live_event_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        containing_uri: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_embeddable: typing.Optional[bool] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        validate: bool = False,
    ) -> LiveEventVideosListAllVideosInEventResponsePydantic:
        raw_response = self.raw.list_all_videos_in_event(
            live_event_id=live_event_id,
            user_id=user_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
        )
        if validate:
            return RootModel[LiveEventVideosListAllVideosInEventResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(LiveEventVideosListAllVideosInEventResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        live_event_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        containing_uri: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_embeddable: typing.Optional[bool] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_all_videos_in_event_mapped_args(
            live_event_id=live_event_id,
            user_id=user_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
        )
        return await self._alist_all_videos_in_event_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        live_event_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        containing_uri: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_embeddable: typing.Optional[bool] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_all_videos_in_event_mapped_args(
            live_event_id=live_event_id,
            user_id=user_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
        )
        return self._list_all_videos_in_event_oapg(
            query_params=args.query,
            path_params=args.path,
        )


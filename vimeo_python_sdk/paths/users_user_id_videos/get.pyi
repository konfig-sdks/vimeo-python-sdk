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

from vimeo_python_sdk.model.get_videos_response import GetVideosResponse as GetVideosResponseSchema

from vimeo_python_sdk.type.get_videos_response import GetVideosResponse

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.get_videos_response import GetVideosResponse as GetVideosResponsePydantic

# Query params
ContainingUriSchema = schemas.StrSchema


class DirectionSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
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
    
    @schemas.classproperty
    def APP_ONLY(cls):
        return cls("app_only")
    
    @schemas.classproperty
    def EMBEDDABLE(cls):
        return cls("embeddable")
    
    @schemas.classproperty
    def FEATURED(cls):
        return cls("featured")
    
    @schemas.classproperty
    def LIVE(cls):
        return cls("live")
    
    @schemas.classproperty
    def NO_PLACEHOLDER(cls):
        return cls("no_placeholder")
    
    @schemas.classproperty
    def NOLIVE(cls):
        return cls("nolive")
    
    @schemas.classproperty
    def PLAYABLE(cls):
        return cls("playable")
    
    @schemas.classproperty
    def SCREEN_RECORDED(cls):
        return cls("screen_recorded")
FilterEmbeddableSchema = schemas.BoolSchema
FilterPlayableSchema = schemas.BoolSchema
FilterScreenRecordedSchema = schemas.BoolSchema
FilterTagSchema = schemas.StrSchema
FilterTagAllOfSchema = schemas.StrSchema
FilterTagExcludeSchema = schemas.StrSchema
IncludeTeamContentSchema = schemas.StrSchema
PageSchema = schemas.NumberSchema
PerPageSchema = schemas.NumberSchema
QuerySchema = schemas.StrSchema


class QueryFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'QueryFieldsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class SortSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def ALPHABETICAL(cls):
        return cls("alphabetical")
    
    @schemas.classproperty
    def DATE(cls):
        return cls("date")
    
    @schemas.classproperty
    def DEFAULT(cls):
        return cls("default")
    
    @schemas.classproperty
    def DURATION(cls):
        return cls("duration")
    
    @schemas.classproperty
    def LAST_USER_ACTION_EVENT_DATE(cls):
        return cls("last_user_action_event_date")
    
    @schemas.classproperty
    def LIKES(cls):
        return cls("likes")
    
    @schemas.classproperty
    def MODIFIED_TIME(cls):
        return cls("modified_time")
    
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
        'filter_playable': typing.Union[FilterPlayableSchema, bool, ],
        'filter_screen_recorded': typing.Union[FilterScreenRecordedSchema, bool, ],
        'filter_tag': typing.Union[FilterTagSchema, str, ],
        'filter_tag_all_of': typing.Union[FilterTagAllOfSchema, str, ],
        'filter_tag_exclude': typing.Union[FilterTagExcludeSchema, str, ],
        'include_team_content': typing.Union[IncludeTeamContentSchema, str, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, float, ],
        'per_page': typing.Union[PerPageSchema, decimal.Decimal, int, float, ],
        'query': typing.Union[QuerySchema, str, ],
        'query_fields': typing.Union[QueryFieldsSchema, list, tuple, ],
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
request_query_filter_playable = api_client.QueryParameter(
    name="filter_playable",
    style=api_client.ParameterStyle.FORM,
    schema=FilterPlayableSchema,
    explode=True,
)
request_query_filter_screen_recorded = api_client.QueryParameter(
    name="filter_screen_recorded",
    style=api_client.ParameterStyle.FORM,
    schema=FilterScreenRecordedSchema,
    explode=True,
)
request_query_filter_tag = api_client.QueryParameter(
    name="filter_tag",
    style=api_client.ParameterStyle.FORM,
    schema=FilterTagSchema,
    explode=True,
)
request_query_filter_tag_all_of = api_client.QueryParameter(
    name="filter_tag_all_of",
    style=api_client.ParameterStyle.FORM,
    schema=FilterTagAllOfSchema,
    explode=True,
)
request_query_filter_tag_exclude = api_client.QueryParameter(
    name="filter_tag_exclude",
    style=api_client.ParameterStyle.FORM,
    schema=FilterTagExcludeSchema,
    explode=True,
)
request_query_include_team_content = api_client.QueryParameter(
    name="include_team_content",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeTeamContentSchema,
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
request_query_query_fields = api_client.QueryParameter(
    name="query_fields",
    style=api_client.ParameterStyle.FORM,
    schema=QueryFieldsSchema,
    explode=True,
)
request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
# Path params
UserIdSchema = schemas.NumberSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
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


request_path_user_id = api_client.PathParameter(
    name="user_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UserIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationVndVimeoVideojson = GetVideosResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: GetVideosResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: GetVideosResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.video+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoVideojson),
    },
)


@dataclass
class ApiResponseFor304(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor304Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_304 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor304,
    response_cls_async=ApiResponseFor304Async,
)
_all_accept_content_types = (
    'application/vnd.vimeo.video+json',
)


class BaseApi(api_client.Api):

    def _videos_mapped_args(
        self,
        user_id: typing.Union[int, float],
        containing_uri: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_embeddable: typing.Optional[bool] = None,
        filter_playable: typing.Optional[bool] = None,
        filter_screen_recorded: typing.Optional[bool] = None,
        filter_tag: typing.Optional[str] = None,
        filter_tag_all_of: typing.Optional[str] = None,
        filter_tag_exclude: typing.Optional[str] = None,
        include_team_content: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        query_fields: typing.Optional[typing.List[str]] = None,
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
        if filter_playable is not None:
            _query_params["filter_playable"] = filter_playable
        if filter_screen_recorded is not None:
            _query_params["filter_screen_recorded"] = filter_screen_recorded
        if filter_tag is not None:
            _query_params["filter_tag"] = filter_tag
        if filter_tag_all_of is not None:
            _query_params["filter_tag_all_of"] = filter_tag_all_of
        if filter_tag_exclude is not None:
            _query_params["filter_tag_exclude"] = filter_tag_exclude
        if include_team_content is not None:
            _query_params["include_team_content"] = include_team_content
        if page is not None:
            _query_params["page"] = page
        if per_page is not None:
            _query_params["per_page"] = per_page
        if query is not None:
            _query_params["query"] = query
        if query_fields is not None:
            _query_params["query_fields"] = query_fields
        if sort is not None:
            _query_params["sort"] = sort
        if user_id is not None:
            _path_params["user_id"] = user_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _avideos_oapg(
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
        Get all the videos that the user has uploaded
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
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
            request_query_filter_playable,
            request_query_filter_screen_recorded,
            request_query_filter_tag,
            request_query_filter_tag_all_of,
            request_query_filter_tag_exclude,
            request_query_include_team_content,
            request_query_page,
            request_query_per_page,
            request_query_query,
            request_query_query_fields,
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
            path_template='/users/{user_id}/videos',
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


    def _videos_oapg(
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
        Get all the videos that the user has uploaded
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
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
            request_query_filter_playable,
            request_query_filter_screen_recorded,
            request_query_filter_tag,
            request_query_filter_tag_all_of,
            request_query_filter_tag_exclude,
            request_query_include_team_content,
            request_query_page,
            request_query_per_page,
            request_query_query,
            request_query_query_fields,
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
            path_template='/users/{user_id}/videos',
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


class VideosRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def avideos(
        self,
        user_id: typing.Union[int, float],
        containing_uri: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_embeddable: typing.Optional[bool] = None,
        filter_playable: typing.Optional[bool] = None,
        filter_screen_recorded: typing.Optional[bool] = None,
        filter_tag: typing.Optional[str] = None,
        filter_tag_all_of: typing.Optional[str] = None,
        filter_tag_exclude: typing.Optional[str] = None,
        include_team_content: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        query_fields: typing.Optional[typing.List[str]] = None,
        sort: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._videos_mapped_args(
            user_id=user_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            filter_playable=filter_playable,
            filter_screen_recorded=filter_screen_recorded,
            filter_tag=filter_tag,
            filter_tag_all_of=filter_tag_all_of,
            filter_tag_exclude=filter_tag_exclude,
            include_team_content=include_team_content,
            page=page,
            per_page=per_page,
            query=query,
            query_fields=query_fields,
            sort=sort,
        )
        return await self._avideos_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def videos(
        self,
        user_id: typing.Union[int, float],
        containing_uri: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_embeddable: typing.Optional[bool] = None,
        filter_playable: typing.Optional[bool] = None,
        filter_screen_recorded: typing.Optional[bool] = None,
        filter_tag: typing.Optional[str] = None,
        filter_tag_all_of: typing.Optional[str] = None,
        filter_tag_exclude: typing.Optional[str] = None,
        include_team_content: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        query_fields: typing.Optional[typing.List[str]] = None,
        sort: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._videos_mapped_args(
            user_id=user_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            filter_playable=filter_playable,
            filter_screen_recorded=filter_screen_recorded,
            filter_tag=filter_tag,
            filter_tag_all_of=filter_tag_all_of,
            filter_tag_exclude=filter_tag_exclude,
            include_team_content=include_team_content,
            page=page,
            per_page=per_page,
            query=query,
            query_fields=query_fields,
            sort=sort,
        )
        return self._videos_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class Videos(BaseApi):

    async def avideos(
        self,
        user_id: typing.Union[int, float],
        containing_uri: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_embeddable: typing.Optional[bool] = None,
        filter_playable: typing.Optional[bool] = None,
        filter_screen_recorded: typing.Optional[bool] = None,
        filter_tag: typing.Optional[str] = None,
        filter_tag_all_of: typing.Optional[str] = None,
        filter_tag_exclude: typing.Optional[str] = None,
        include_team_content: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        query_fields: typing.Optional[typing.List[str]] = None,
        sort: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> GetVideosResponsePydantic:
        raw_response = await self.raw.avideos(
            user_id=user_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            filter_playable=filter_playable,
            filter_screen_recorded=filter_screen_recorded,
            filter_tag=filter_tag,
            filter_tag_all_of=filter_tag_all_of,
            filter_tag_exclude=filter_tag_exclude,
            include_team_content=include_team_content,
            page=page,
            per_page=per_page,
            query=query,
            query_fields=query_fields,
            sort=sort,
            **kwargs,
        )
        if validate:
            return RootModel[GetVideosResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(GetVideosResponsePydantic, raw_response.body)
    
    
    def videos(
        self,
        user_id: typing.Union[int, float],
        containing_uri: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_embeddable: typing.Optional[bool] = None,
        filter_playable: typing.Optional[bool] = None,
        filter_screen_recorded: typing.Optional[bool] = None,
        filter_tag: typing.Optional[str] = None,
        filter_tag_all_of: typing.Optional[str] = None,
        filter_tag_exclude: typing.Optional[str] = None,
        include_team_content: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        query_fields: typing.Optional[typing.List[str]] = None,
        sort: typing.Optional[str] = None,
        validate: bool = False,
    ) -> GetVideosResponsePydantic:
        raw_response = self.raw.videos(
            user_id=user_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            filter_playable=filter_playable,
            filter_screen_recorded=filter_screen_recorded,
            filter_tag=filter_tag,
            filter_tag_all_of=filter_tag_all_of,
            filter_tag_exclude=filter_tag_exclude,
            include_team_content=include_team_content,
            page=page,
            per_page=per_page,
            query=query,
            query_fields=query_fields,
            sort=sort,
        )
        if validate:
            return RootModel[GetVideosResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(GetVideosResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        user_id: typing.Union[int, float],
        containing_uri: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_embeddable: typing.Optional[bool] = None,
        filter_playable: typing.Optional[bool] = None,
        filter_screen_recorded: typing.Optional[bool] = None,
        filter_tag: typing.Optional[str] = None,
        filter_tag_all_of: typing.Optional[str] = None,
        filter_tag_exclude: typing.Optional[str] = None,
        include_team_content: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        query_fields: typing.Optional[typing.List[str]] = None,
        sort: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._videos_mapped_args(
            user_id=user_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            filter_playable=filter_playable,
            filter_screen_recorded=filter_screen_recorded,
            filter_tag=filter_tag,
            filter_tag_all_of=filter_tag_all_of,
            filter_tag_exclude=filter_tag_exclude,
            include_team_content=include_team_content,
            page=page,
            per_page=per_page,
            query=query,
            query_fields=query_fields,
            sort=sort,
        )
        return await self._avideos_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        user_id: typing.Union[int, float],
        containing_uri: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_embeddable: typing.Optional[bool] = None,
        filter_playable: typing.Optional[bool] = None,
        filter_screen_recorded: typing.Optional[bool] = None,
        filter_tag: typing.Optional[str] = None,
        filter_tag_all_of: typing.Optional[str] = None,
        filter_tag_exclude: typing.Optional[str] = None,
        include_team_content: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        query_fields: typing.Optional[typing.List[str]] = None,
        sort: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._videos_mapped_args(
            user_id=user_id,
            containing_uri=containing_uri,
            direction=direction,
            filter=filter,
            filter_embeddable=filter_embeddable,
            filter_playable=filter_playable,
            filter_screen_recorded=filter_screen_recorded,
            filter_tag=filter_tag,
            filter_tag_all_of=filter_tag_all_of,
            filter_tag_exclude=filter_tag_exclude,
            include_team_content=include_team_content,
            page=page,
            per_page=per_page,
            query=query,
            query_fields=query_fields,
            sort=sort,
        )
        return self._videos_oapg(
            query_params=args.query,
            path_params=args.path,
        )


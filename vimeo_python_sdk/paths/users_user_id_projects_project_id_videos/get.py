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

from vimeo_python_sdk.model.folders_videos_get_all_folder_videos_response import FoldersVideosGetAllFolderVideosResponse as FoldersVideosGetAllFolderVideosResponseSchema
from vimeo_python_sdk.model.error import Error as ErrorSchema

from vimeo_python_sdk.type.error import Error
from vimeo_python_sdk.type.folders_videos_get_all_folder_videos_response import FoldersVideosGetAllFolderVideosResponse

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.error import Error as ErrorPydantic
from vimeo_python_sdk.pydantic.folders_videos_get_all_folder_videos_response import FoldersVideosGetAllFolderVideosResponse as FoldersVideosGetAllFolderVideosResponsePydantic

from . import path

# Query params


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
FilterTagSchema = schemas.StrSchema
FilterTagAllOfSchema = schemas.StrSchema
FilterTagExcludeSchema = schemas.StrSchema
IncludeSubfoldersSchema = schemas.BoolSchema
PageSchema = schemas.NumberSchema
PerPageSchema = schemas.NumberSchema
QuerySchema = schemas.StrSchema
QueryFieldsSchema = schemas.StrSchema


class SortSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "alphabetical": "ALPHABETICAL",
            "date": "DATE",
            "default": "DEFAULT",
            "duration": "DURATION",
            "last_user_action_event_date": "LAST_USER_ACTION_EVENT_DATE",
        }
    
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
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'direction': typing.Union[DirectionSchema, str, ],
        'filter_tag': typing.Union[FilterTagSchema, str, ],
        'filter_tag_all_of': typing.Union[FilterTagAllOfSchema, str, ],
        'filter_tag_exclude': typing.Union[FilterTagExcludeSchema, str, ],
        'include_subfolders': typing.Union[IncludeSubfoldersSchema, bool, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, float, ],
        'per_page': typing.Union[PerPageSchema, decimal.Decimal, int, float, ],
        'query': typing.Union[QuerySchema, str, ],
        'query_fields': typing.Union[QueryFieldsSchema, str, ],
        'sort': typing.Union[SortSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_direction = api_client.QueryParameter(
    name="direction",
    style=api_client.ParameterStyle.FORM,
    schema=DirectionSchema,
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
request_query_include_subfolders = api_client.QueryParameter(
    name="include_subfolders",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeSubfoldersSchema,
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
ProjectIdSchema = schemas.NumberSchema
UserIdSchema = schemas.NumberSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'project_id': typing.Union[ProjectIdSchema, decimal.Decimal, int, float, ],
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


request_path_project_id = api_client.PathParameter(
    name="project_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ProjectIdSchema,
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
SchemaFor200ResponseBodyApplicationJson = FoldersVideosGetAllFolderVideosResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: FoldersVideosGetAllFolderVideosResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: FoldersVideosGetAllFolderVideosResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ErrorSchema


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
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ErrorSchema


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
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '401': _response_for_401,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_all_folder_videos_mapped_args(
        self,
        project_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        direction: typing.Optional[str] = None,
        filter_tag: typing.Optional[str] = None,
        filter_tag_all_of: typing.Optional[str] = None,
        filter_tag_exclude: typing.Optional[str] = None,
        include_subfolders: typing.Optional[bool] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        query_fields: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if direction is not None:
            _query_params["direction"] = direction
        if filter_tag is not None:
            _query_params["filter_tag"] = filter_tag
        if filter_tag_all_of is not None:
            _query_params["filter_tag_all_of"] = filter_tag_all_of
        if filter_tag_exclude is not None:
            _query_params["filter_tag_exclude"] = filter_tag_exclude
        if include_subfolders is not None:
            _query_params["include_subfolders"] = include_subfolders
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
        if project_id is not None:
            _path_params["project_id"] = project_id
        if user_id is not None:
            _path_params["user_id"] = user_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_all_folder_videos_oapg(
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
        Get all the videos in a folder
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_project_id,
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
            request_query_direction,
            request_query_filter_tag,
            request_query_filter_tag_all_of,
            request_query_filter_tag_exclude,
            request_query_include_subfolders,
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
            path_template='/users/{user_id}/projects/{project_id}/videos',
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


    def _get_all_folder_videos_oapg(
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
        Get all the videos in a folder
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_project_id,
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
            request_query_direction,
            request_query_filter_tag,
            request_query_filter_tag_all_of,
            request_query_filter_tag_exclude,
            request_query_include_subfolders,
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
            path_template='/users/{user_id}/projects/{project_id}/videos',
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


class GetAllFolderVideosRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_all_folder_videos(
        self,
        project_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        direction: typing.Optional[str] = None,
        filter_tag: typing.Optional[str] = None,
        filter_tag_all_of: typing.Optional[str] = None,
        filter_tag_exclude: typing.Optional[str] = None,
        include_subfolders: typing.Optional[bool] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        query_fields: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_folder_videos_mapped_args(
            project_id=project_id,
            user_id=user_id,
            direction=direction,
            filter_tag=filter_tag,
            filter_tag_all_of=filter_tag_all_of,
            filter_tag_exclude=filter_tag_exclude,
            include_subfolders=include_subfolders,
            page=page,
            per_page=per_page,
            query=query,
            query_fields=query_fields,
            sort=sort,
        )
        return await self._aget_all_folder_videos_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_all_folder_videos(
        self,
        project_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        direction: typing.Optional[str] = None,
        filter_tag: typing.Optional[str] = None,
        filter_tag_all_of: typing.Optional[str] = None,
        filter_tag_exclude: typing.Optional[str] = None,
        include_subfolders: typing.Optional[bool] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        query_fields: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_folder_videos_mapped_args(
            project_id=project_id,
            user_id=user_id,
            direction=direction,
            filter_tag=filter_tag,
            filter_tag_all_of=filter_tag_all_of,
            filter_tag_exclude=filter_tag_exclude,
            include_subfolders=include_subfolders,
            page=page,
            per_page=per_page,
            query=query,
            query_fields=query_fields,
            sort=sort,
        )
        return self._get_all_folder_videos_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetAllFolderVideos(BaseApi):

    async def aget_all_folder_videos(
        self,
        project_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        direction: typing.Optional[str] = None,
        filter_tag: typing.Optional[str] = None,
        filter_tag_all_of: typing.Optional[str] = None,
        filter_tag_exclude: typing.Optional[str] = None,
        include_subfolders: typing.Optional[bool] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        query_fields: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> FoldersVideosGetAllFolderVideosResponsePydantic:
        raw_response = await self.raw.aget_all_folder_videos(
            project_id=project_id,
            user_id=user_id,
            direction=direction,
            filter_tag=filter_tag,
            filter_tag_all_of=filter_tag_all_of,
            filter_tag_exclude=filter_tag_exclude,
            include_subfolders=include_subfolders,
            page=page,
            per_page=per_page,
            query=query,
            query_fields=query_fields,
            sort=sort,
            **kwargs,
        )
        if validate:
            return RootModel[FoldersVideosGetAllFolderVideosResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(FoldersVideosGetAllFolderVideosResponsePydantic, raw_response.body)
    
    
    def get_all_folder_videos(
        self,
        project_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        direction: typing.Optional[str] = None,
        filter_tag: typing.Optional[str] = None,
        filter_tag_all_of: typing.Optional[str] = None,
        filter_tag_exclude: typing.Optional[str] = None,
        include_subfolders: typing.Optional[bool] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        query_fields: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        validate: bool = False,
    ) -> FoldersVideosGetAllFolderVideosResponsePydantic:
        raw_response = self.raw.get_all_folder_videos(
            project_id=project_id,
            user_id=user_id,
            direction=direction,
            filter_tag=filter_tag,
            filter_tag_all_of=filter_tag_all_of,
            filter_tag_exclude=filter_tag_exclude,
            include_subfolders=include_subfolders,
            page=page,
            per_page=per_page,
            query=query,
            query_fields=query_fields,
            sort=sort,
        )
        if validate:
            return RootModel[FoldersVideosGetAllFolderVideosResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(FoldersVideosGetAllFolderVideosResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        project_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        direction: typing.Optional[str] = None,
        filter_tag: typing.Optional[str] = None,
        filter_tag_all_of: typing.Optional[str] = None,
        filter_tag_exclude: typing.Optional[str] = None,
        include_subfolders: typing.Optional[bool] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        query_fields: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_folder_videos_mapped_args(
            project_id=project_id,
            user_id=user_id,
            direction=direction,
            filter_tag=filter_tag,
            filter_tag_all_of=filter_tag_all_of,
            filter_tag_exclude=filter_tag_exclude,
            include_subfolders=include_subfolders,
            page=page,
            per_page=per_page,
            query=query,
            query_fields=query_fields,
            sort=sort,
        )
        return await self._aget_all_folder_videos_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        project_id: typing.Union[int, float],
        user_id: typing.Union[int, float],
        direction: typing.Optional[str] = None,
        filter_tag: typing.Optional[str] = None,
        filter_tag_all_of: typing.Optional[str] = None,
        filter_tag_exclude: typing.Optional[str] = None,
        include_subfolders: typing.Optional[bool] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        query_fields: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_folder_videos_mapped_args(
            project_id=project_id,
            user_id=user_id,
            direction=direction,
            filter_tag=filter_tag,
            filter_tag_all_of=filter_tag_all_of,
            filter_tag_exclude=filter_tag_exclude,
            include_subfolders=include_subfolders,
            page=page,
            per_page=per_page,
            query=query,
            query_fields=query_fields,
            sort=sort,
        )
        return self._get_all_folder_videos_oapg(
            query_params=args.query,
            path_params=args.path,
        )


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

from vimeo_python_sdk.model.search_users_response import SearchUsersResponse as SearchUsersResponseSchema
from vimeo_python_sdk.model.legacy_error import LegacyError as LegacyErrorSchema

from vimeo_python_sdk.type.legacy_error import LegacyError
from vimeo_python_sdk.type.search_users_response import SearchUsersResponse

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.search_users_response import SearchUsersResponse as SearchUsersResponsePydantic
from vimeo_python_sdk.pydantic.legacy_error import LegacyError as LegacyErrorPydantic

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
PageSchema = schemas.NumberSchema
PerPageSchema = schemas.NumberSchema
QuerySchema = schemas.StrSchema


class SortSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "alphabetical": "ALPHABETICAL",
            "date": "DATE",
            "followers": "FOLLOWERS",
            "relevant": "RELEVANT",
            "videos": "VIDEOS",
        }
    
    @schemas.classproperty
    def ALPHABETICAL(cls):
        return cls("alphabetical")
    
    @schemas.classproperty
    def DATE(cls):
        return cls("date")
    
    @schemas.classproperty
    def FOLLOWERS(cls):
        return cls("followers")
    
    @schemas.classproperty
    def RELEVANT(cls):
        return cls("relevant")
    
    @schemas.classproperty
    def VIDEOS(cls):
        return cls("videos")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'direction': typing.Union[DirectionSchema, str, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, float, ],
        'per_page': typing.Union[PerPageSchema, decimal.Decimal, int, float, ],
        'query': typing.Union[QuerySchema, str, ],
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
_auth = [
    'oauth2',
    'oauth2',
]
SchemaFor200ResponseBodyApplicationVndVimeoUserjson = SearchUsersResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: SearchUsersResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SearchUsersResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.user+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoUserjson),
    },
)
SchemaFor500ResponseBodyApplicationVndVimeoUserjson = LegacyErrorSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: LegacyError


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: LegacyError


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/vnd.vimeo.user+json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationVndVimeoUserjson),
    },
)
SchemaFor503ResponseBodyApplicationVndVimeoUserjson = LegacyErrorSchema


@dataclass
class ApiResponseFor503(api_client.ApiResponse):
    body: LegacyError


@dataclass
class ApiResponseFor503Async(api_client.AsyncApiResponse):
    body: LegacyError


_response_for_503 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor503,
    response_cls_async=ApiResponseFor503Async,
    content={
        'application/vnd.vimeo.user+json': api_client.MediaType(
            schema=SchemaFor503ResponseBodyApplicationVndVimeoUserjson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '500': _response_for_500,
    '503': _response_for_503,
}
_all_accept_content_types = (
    'application/vnd.vimeo.user+json',
)


class BaseApi(api_client.Api):

    def _users_mapped_args(
        self,
        direction: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if direction is not None:
            _query_params["direction"] = direction
        if page is not None:
            _query_params["page"] = page
        if per_page is not None:
            _query_params["per_page"] = per_page
        if query is not None:
            _query_params["query"] = query
        if sort is not None:
            _query_params["sort"] = sort
        args.query = _query_params
        return args

    async def _ausers_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        Search for users
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_direction,
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
            path_template='/users',
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


    def _users_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Search for users
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_direction,
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
            path_template='/users',
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


class UsersRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def ausers(
        self,
        direction: typing.Optional[str] = None,
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
        args = self._users_mapped_args(
            direction=direction,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
        )
        return await self._ausers_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def users(
        self,
        direction: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._users_mapped_args(
            direction=direction,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
        )
        return self._users_oapg(
            query_params=args.query,
        )

class Users(BaseApi):

    async def ausers(
        self,
        direction: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> SearchUsersResponsePydantic:
        raw_response = await self.raw.ausers(
            direction=direction,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
            **kwargs,
        )
        if validate:
            return RootModel[SearchUsersResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(SearchUsersResponsePydantic, raw_response.body)
    
    
    def users(
        self,
        direction: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        validate: bool = False,
    ) -> SearchUsersResponsePydantic:
        raw_response = self.raw.users(
            direction=direction,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
        )
        if validate:
            return RootModel[SearchUsersResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(SearchUsersResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        direction: typing.Optional[str] = None,
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
        args = self._users_mapped_args(
            direction=direction,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
        )
        return await self._ausers_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        direction: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        query: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._users_mapped_args(
            direction=direction,
            page=page,
            per_page=per_page,
            query=query,
            sort=sort,
        )
        return self._users_oapg(
            query_params=args.query,
        )


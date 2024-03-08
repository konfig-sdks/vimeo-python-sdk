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

from vimeo_python_sdk.model.users_analytics_get_user_metrics_response import UsersAnalyticsGetUserMetricsResponse as UsersAnalyticsGetUserMetricsResponseSchema

from vimeo_python_sdk.type.users_analytics_get_user_metrics_response import UsersAnalyticsGetUserMetricsResponse

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.users_analytics_get_user_metrics_response import UsersAnalyticsGetUserMetricsResponse as UsersAnalyticsGetUserMetricsResponsePydantic

# Query params


class DimensionSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def COUNTRY(cls):
        return cls("country")
    
    @schemas.classproperty
    def EMBED_DOMAIN(cls):
        return cls("embed_domain")
    
    @schemas.classproperty
    def TOTAL(cls):
        return cls("total")
    
    @schemas.classproperty
    def VIDEO(cls):
        return cls("video")


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
FilterContentSchema = schemas.StrSchema


class FilterCountriesSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FilterCountriesSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class FilterDeviceTypesSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FilterDeviceTypesSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class FilterEmbedDomainsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FilterEmbedDomainsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class FilterStreamingTypesSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FilterStreamingTypesSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
ModelFromSchema = schemas.StrSchema
PageSchema = schemas.NumberSchema
PerPageSchema = schemas.NumberSchema


class SortSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def AVERAGE_PERCENT_WATCHED(cls):
        return cls("average_percent_watched")
    
    @schemas.classproperty
    def AVERAGE_TIME_WATCHED(cls):
        return cls("average_time_watched")
    
    @schemas.classproperty
    def COMMENTS(cls):
        return cls("comments")
    
    @schemas.classproperty
    def COUNTRY(cls):
        return cls("country")
    
    @schemas.classproperty
    def DEFAULT(cls):
        return cls("default")
    
    @schemas.classproperty
    def DOWNLOADS(cls):
        return cls("downloads")
    
    @schemas.classproperty
    def EMBED_DOMAIN(cls):
        return cls("embed_domain")
    
    @schemas.classproperty
    def FINISHES(cls):
        return cls("finishes")
    
    @schemas.classproperty
    def IMPRESSIONS(cls):
        return cls("impressions")
    
    @schemas.classproperty
    def LIKE(cls):
        return cls("like")
    
    @schemas.classproperty
    def TIME(cls):
        return cls("time")
    
    @schemas.classproperty
    def TOTAL_TIME_WATCHED(cls):
        return cls("total_time_watched")
    
    @schemas.classproperty
    def UNIQUE_IMPRESSIONS(cls):
        return cls("unique_impressions")
    
    @schemas.classproperty
    def UNIQUE_VIEWERS(cls):
        return cls("unique_viewers")
    
    @schemas.classproperty
    def VIDEO(cls):
        return cls("video")
    
    @schemas.classproperty
    def VIEWS(cls):
        return cls("views")


class TimeIntervalSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def DAY(cls):
        return cls("day")
    
    @schemas.classproperty
    def MONTH(cls):
        return cls("month")
    
    @schemas.classproperty
    def NONE(cls):
        return cls("none")
    
    @schemas.classproperty
    def WEEK(cls):
        return cls("week")
    
    @schemas.classproperty
    def YEAR(cls):
        return cls("year")
ToSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'dimension': typing.Union[DimensionSchema, str, ],
        'from': typing.Union[ModelFromSchema, str, ],
        'to': typing.Union[ToSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'direction': typing.Union[DirectionSchema, str, ],
        'filter_content': typing.Union[FilterContentSchema, str, ],
        'filter_countries': typing.Union[FilterCountriesSchema, list, tuple, ],
        'filter_device_types': typing.Union[FilterDeviceTypesSchema, list, tuple, ],
        'filter_embed_domains': typing.Union[FilterEmbedDomainsSchema, list, tuple, ],
        'filter_streaming_types': typing.Union[FilterStreamingTypesSchema, list, tuple, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, float, ],
        'per_page': typing.Union[PerPageSchema, decimal.Decimal, int, float, ],
        'sort': typing.Union[SortSchema, str, ],
        'time_interval': typing.Union[TimeIntervalSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_dimension = api_client.QueryParameter(
    name="dimension",
    style=api_client.ParameterStyle.FORM,
    schema=DimensionSchema,
    required=True,
    explode=True,
)
request_query_direction = api_client.QueryParameter(
    name="direction",
    style=api_client.ParameterStyle.FORM,
    schema=DirectionSchema,
    explode=True,
)
request_query_filter_content = api_client.QueryParameter(
    name="filter_content",
    style=api_client.ParameterStyle.FORM,
    schema=FilterContentSchema,
    explode=True,
)
request_query_filter_countries = api_client.QueryParameter(
    name="filter_countries",
    style=api_client.ParameterStyle.FORM,
    schema=FilterCountriesSchema,
    explode=True,
)
request_query_filter_device_types = api_client.QueryParameter(
    name="filter_device_types",
    style=api_client.ParameterStyle.FORM,
    schema=FilterDeviceTypesSchema,
    explode=True,
)
request_query_filter_embed_domains = api_client.QueryParameter(
    name="filter_embed_domains",
    style=api_client.ParameterStyle.FORM,
    schema=FilterEmbedDomainsSchema,
    explode=True,
)
request_query_filter_streaming_types = api_client.QueryParameter(
    name="filter_streaming_types",
    style=api_client.ParameterStyle.FORM,
    schema=FilterStreamingTypesSchema,
    explode=True,
)
request_query__from = api_client.QueryParameter(
    name="from",
    style=api_client.ParameterStyle.FORM,
    schema=ModelFromSchema,
    required=True,
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
request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
request_query_time_interval = api_client.QueryParameter(
    name="time_interval",
    style=api_client.ParameterStyle.FORM,
    schema=TimeIntervalSchema,
    explode=True,
)
request_query_to = api_client.QueryParameter(
    name="to",
    style=api_client.ParameterStyle.FORM,
    schema=ToSchema,
    required=True,
    explode=True,
)
SchemaFor200ResponseBodyApplicationVndVimeoAnalyticsjson = UsersAnalyticsGetUserMetricsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: UsersAnalyticsGetUserMetricsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UsersAnalyticsGetUserMetricsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.analytics+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoAnalyticsjson),
    },
)
_all_accept_content_types = (
    'application/vnd.vimeo.analytics+json',
)


class BaseApi(api_client.Api):

    def _get_user_metrics_mapped_args(
        self,
        dimension: str,
        _from: str,
        to: str,
        direction: typing.Optional[str] = None,
        filter_content: typing.Optional[str] = None,
        filter_countries: typing.Optional[typing.List[str]] = None,
        filter_device_types: typing.Optional[typing.List[str]] = None,
        filter_embed_domains: typing.Optional[typing.List[str]] = None,
        filter_streaming_types: typing.Optional[typing.List[str]] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        sort: typing.Optional[str] = None,
        time_interval: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if dimension is not None:
            _query_params["dimension"] = dimension
        if direction is not None:
            _query_params["direction"] = direction
        if filter_content is not None:
            _query_params["filter_content"] = filter_content
        if filter_countries is not None:
            _query_params["filter_countries"] = filter_countries
        if filter_device_types is not None:
            _query_params["filter_device_types"] = filter_device_types
        if filter_embed_domains is not None:
            _query_params["filter_embed_domains"] = filter_embed_domains
        if filter_streaming_types is not None:
            _query_params["filter_streaming_types"] = filter_streaming_types
        if _from is not None:
            _query_params["from"] = _from
        if page is not None:
            _query_params["page"] = page
        if per_page is not None:
            _query_params["per_page"] = per_page
        if sort is not None:
            _query_params["sort"] = sort
        if time_interval is not None:
            _query_params["time_interval"] = time_interval
        if to is not None:
            _query_params["to"] = to
        args.query = _query_params
        return args

    async def _aget_user_metrics_oapg(
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
        Get analytics for the user
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_dimension,
            request_query_direction,
            request_query_filter_content,
            request_query_filter_countries,
            request_query_filter_device_types,
            request_query_filter_embed_domains,
            request_query_filter_streaming_types,
            request_query__from,
            request_query_page,
            request_query_per_page,
            request_query_sort,
            request_query_time_interval,
            request_query_to,
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
            path_template='/me/analytics',
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


    def _get_user_metrics_oapg(
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
        Get analytics for the user
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_dimension,
            request_query_direction,
            request_query_filter_content,
            request_query_filter_countries,
            request_query_filter_device_types,
            request_query_filter_embed_domains,
            request_query_filter_streaming_types,
            request_query__from,
            request_query_page,
            request_query_per_page,
            request_query_sort,
            request_query_time_interval,
            request_query_to,
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
            path_template='/me/analytics',
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


class GetUserMetricsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_user_metrics(
        self,
        dimension: str,
        _from: str,
        to: str,
        direction: typing.Optional[str] = None,
        filter_content: typing.Optional[str] = None,
        filter_countries: typing.Optional[typing.List[str]] = None,
        filter_device_types: typing.Optional[typing.List[str]] = None,
        filter_embed_domains: typing.Optional[typing.List[str]] = None,
        filter_streaming_types: typing.Optional[typing.List[str]] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        sort: typing.Optional[str] = None,
        time_interval: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_metrics_mapped_args(
            dimension=dimension,
            _from=_from,
            to=to,
            direction=direction,
            filter_content=filter_content,
            filter_countries=filter_countries,
            filter_device_types=filter_device_types,
            filter_embed_domains=filter_embed_domains,
            filter_streaming_types=filter_streaming_types,
            page=page,
            per_page=per_page,
            sort=sort,
            time_interval=time_interval,
        )
        return await self._aget_user_metrics_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_user_metrics(
        self,
        dimension: str,
        _from: str,
        to: str,
        direction: typing.Optional[str] = None,
        filter_content: typing.Optional[str] = None,
        filter_countries: typing.Optional[typing.List[str]] = None,
        filter_device_types: typing.Optional[typing.List[str]] = None,
        filter_embed_domains: typing.Optional[typing.List[str]] = None,
        filter_streaming_types: typing.Optional[typing.List[str]] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        sort: typing.Optional[str] = None,
        time_interval: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_metrics_mapped_args(
            dimension=dimension,
            _from=_from,
            to=to,
            direction=direction,
            filter_content=filter_content,
            filter_countries=filter_countries,
            filter_device_types=filter_device_types,
            filter_embed_domains=filter_embed_domains,
            filter_streaming_types=filter_streaming_types,
            page=page,
            per_page=per_page,
            sort=sort,
            time_interval=time_interval,
        )
        return self._get_user_metrics_oapg(
            query_params=args.query,
        )

class GetUserMetrics(BaseApi):

    async def aget_user_metrics(
        self,
        dimension: str,
        _from: str,
        to: str,
        direction: typing.Optional[str] = None,
        filter_content: typing.Optional[str] = None,
        filter_countries: typing.Optional[typing.List[str]] = None,
        filter_device_types: typing.Optional[typing.List[str]] = None,
        filter_embed_domains: typing.Optional[typing.List[str]] = None,
        filter_streaming_types: typing.Optional[typing.List[str]] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        sort: typing.Optional[str] = None,
        time_interval: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> UsersAnalyticsGetUserMetricsResponsePydantic:
        raw_response = await self.raw.aget_user_metrics(
            dimension=dimension,
            _from=_from,
            to=to,
            direction=direction,
            filter_content=filter_content,
            filter_countries=filter_countries,
            filter_device_types=filter_device_types,
            filter_embed_domains=filter_embed_domains,
            filter_streaming_types=filter_streaming_types,
            page=page,
            per_page=per_page,
            sort=sort,
            time_interval=time_interval,
            **kwargs,
        )
        if validate:
            return RootModel[UsersAnalyticsGetUserMetricsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(UsersAnalyticsGetUserMetricsResponsePydantic, raw_response.body)
    
    
    def get_user_metrics(
        self,
        dimension: str,
        _from: str,
        to: str,
        direction: typing.Optional[str] = None,
        filter_content: typing.Optional[str] = None,
        filter_countries: typing.Optional[typing.List[str]] = None,
        filter_device_types: typing.Optional[typing.List[str]] = None,
        filter_embed_domains: typing.Optional[typing.List[str]] = None,
        filter_streaming_types: typing.Optional[typing.List[str]] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        sort: typing.Optional[str] = None,
        time_interval: typing.Optional[str] = None,
        validate: bool = False,
    ) -> UsersAnalyticsGetUserMetricsResponsePydantic:
        raw_response = self.raw.get_user_metrics(
            dimension=dimension,
            _from=_from,
            to=to,
            direction=direction,
            filter_content=filter_content,
            filter_countries=filter_countries,
            filter_device_types=filter_device_types,
            filter_embed_domains=filter_embed_domains,
            filter_streaming_types=filter_streaming_types,
            page=page,
            per_page=per_page,
            sort=sort,
            time_interval=time_interval,
        )
        if validate:
            return RootModel[UsersAnalyticsGetUserMetricsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(UsersAnalyticsGetUserMetricsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        dimension: str,
        _from: str,
        to: str,
        direction: typing.Optional[str] = None,
        filter_content: typing.Optional[str] = None,
        filter_countries: typing.Optional[typing.List[str]] = None,
        filter_device_types: typing.Optional[typing.List[str]] = None,
        filter_embed_domains: typing.Optional[typing.List[str]] = None,
        filter_streaming_types: typing.Optional[typing.List[str]] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        sort: typing.Optional[str] = None,
        time_interval: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_metrics_mapped_args(
            dimension=dimension,
            _from=_from,
            to=to,
            direction=direction,
            filter_content=filter_content,
            filter_countries=filter_countries,
            filter_device_types=filter_device_types,
            filter_embed_domains=filter_embed_domains,
            filter_streaming_types=filter_streaming_types,
            page=page,
            per_page=per_page,
            sort=sort,
            time_interval=time_interval,
        )
        return await self._aget_user_metrics_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        dimension: str,
        _from: str,
        to: str,
        direction: typing.Optional[str] = None,
        filter_content: typing.Optional[str] = None,
        filter_countries: typing.Optional[typing.List[str]] = None,
        filter_device_types: typing.Optional[typing.List[str]] = None,
        filter_embed_domains: typing.Optional[typing.List[str]] = None,
        filter_streaming_types: typing.Optional[typing.List[str]] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        sort: typing.Optional[str] = None,
        time_interval: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_metrics_mapped_args(
            dimension=dimension,
            _from=_from,
            to=to,
            direction=direction,
            filter_content=filter_content,
            filter_countries=filter_countries,
            filter_device_types=filter_device_types,
            filter_embed_domains=filter_embed_domains,
            filter_streaming_types=filter_streaming_types,
            page=page,
            per_page=per_page,
            sort=sort,
            time_interval=time_interval,
        )
        return self._get_user_metrics_oapg(
            query_params=args.query,
        )


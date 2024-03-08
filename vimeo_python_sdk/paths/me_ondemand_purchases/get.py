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

from vimeo_python_sdk.model.on_demand_purchases_and_rentals_get_all_user_purchases_and_rentals_response import OnDemandPurchasesAndRentalsGetAllUserPurchasesAndRentalsResponse as OnDemandPurchasesAndRentalsGetAllUserPurchasesAndRentalsResponseSchema
from vimeo_python_sdk.model.legacy_error import LegacyError as LegacyErrorSchema

from vimeo_python_sdk.type.on_demand_purchases_and_rentals_get_all_user_purchases_and_rentals_response import OnDemandPurchasesAndRentalsGetAllUserPurchasesAndRentalsResponse
from vimeo_python_sdk.type.legacy_error import LegacyError

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.legacy_error import LegacyError as LegacyErrorPydantic
from vimeo_python_sdk.pydantic.on_demand_purchases_and_rentals_get_all_user_purchases_and_rentals_response import OnDemandPurchasesAndRentalsGetAllUserPurchasesAndRentalsResponse as OnDemandPurchasesAndRentalsGetAllUserPurchasesAndRentalsResponsePydantic

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


class FilterSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "all": "ALL",
            "expiring_soon": "EXPIRING_SOON",
            "film": "FILM",
            "important": "IMPORTANT",
            "purchased": "PURCHASED",
            "rented": "RENTED",
            "series": "SERIES",
            "subscription": "SUBSCRIPTION",
            "unwatched": "UNWATCHED",
            "watched": "WATCHED",
        }
    
    @schemas.classproperty
    def ALL(cls):
        return cls("all")
    
    @schemas.classproperty
    def EXPIRING_SOON(cls):
        return cls("expiring_soon")
    
    @schemas.classproperty
    def FILM(cls):
        return cls("film")
    
    @schemas.classproperty
    def IMPORTANT(cls):
        return cls("important")
    
    @schemas.classproperty
    def PURCHASED(cls):
        return cls("purchased")
    
    @schemas.classproperty
    def RENTED(cls):
        return cls("rented")
    
    @schemas.classproperty
    def SERIES(cls):
        return cls("series")
    
    @schemas.classproperty
    def SUBSCRIPTION(cls):
        return cls("subscription")
    
    @schemas.classproperty
    def UNWATCHED(cls):
        return cls("unwatched")
    
    @schemas.classproperty
    def WATCHED(cls):
        return cls("watched")
PageSchema = schemas.NumberSchema
PerPageSchema = schemas.NumberSchema


class SortSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "added": "ADDED",
            "alphabetical": "ALPHABETICAL",
            "date": "DATE",
            "name": "NAME",
            "purchase_time": "PURCHASE_TIME",
            "rating": "RATING",
            "release_date": "RELEASE_DATE",
        }
    
    @schemas.classproperty
    def ADDED(cls):
        return cls("added")
    
    @schemas.classproperty
    def ALPHABETICAL(cls):
        return cls("alphabetical")
    
    @schemas.classproperty
    def DATE(cls):
        return cls("date")
    
    @schemas.classproperty
    def NAME(cls):
        return cls("name")
    
    @schemas.classproperty
    def PURCHASE_TIME(cls):
        return cls("purchase_time")
    
    @schemas.classproperty
    def RATING(cls):
        return cls("rating")
    
    @schemas.classproperty
    def RELEASE_DATE(cls):
        return cls("release_date")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'direction': typing.Union[DirectionSchema, str, ],
        'filter': typing.Union[FilterSchema, str, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, float, ],
        'per_page': typing.Union[PerPageSchema, decimal.Decimal, int, float, ],
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
request_query_filter = api_client.QueryParameter(
    name="filter",
    style=api_client.ParameterStyle.FORM,
    schema=FilterSchema,
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
_auth = [
    'oauth2',
    'oauth2',
]
SchemaFor200ResponseBodyApplicationVndVimeoOndemandPagejson = OnDemandPurchasesAndRentalsGetAllUserPurchasesAndRentalsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: OnDemandPurchasesAndRentalsGetAllUserPurchasesAndRentalsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: OnDemandPurchasesAndRentalsGetAllUserPurchasesAndRentalsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.ondemand.page+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoOndemandPagejson),
    },
)
SchemaFor403ResponseBodyApplicationVndVimeoOndemandPagejson = LegacyErrorSchema


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
        'application/vnd.vimeo.ondemand.page+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationVndVimeoOndemandPagejson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '403': _response_for_403,
}
_all_accept_content_types = (
    'application/vnd.vimeo.ondemand.page+json',
)


class BaseApi(api_client.Api):

    def _get_all_user_purchases_and_rentals_mapped_args(
        self,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        sort: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if direction is not None:
            _query_params["direction"] = direction
        if filter is not None:
            _query_params["filter"] = filter
        if page is not None:
            _query_params["page"] = page
        if per_page is not None:
            _query_params["per_page"] = per_page
        if sort is not None:
            _query_params["sort"] = sort
        args.query = _query_params
        return args

    async def _aget_all_user_purchases_and_rentals_oapg(
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
        Get all of the user&#x27;s On Demand purchases and rentals
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_direction,
            request_query_filter,
            request_query_page,
            request_query_per_page,
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
            path_template='/me/ondemand/purchases',
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


    def _get_all_user_purchases_and_rentals_oapg(
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
        Get all of the user&#x27;s On Demand purchases and rentals
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_direction,
            request_query_filter,
            request_query_page,
            request_query_per_page,
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
            path_template='/me/ondemand/purchases',
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


class GetAllUserPurchasesAndRentalsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_all_user_purchases_and_rentals(
        self,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        sort: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_user_purchases_and_rentals_mapped_args(
            direction=direction,
            filter=filter,
            page=page,
            per_page=per_page,
            sort=sort,
        )
        return await self._aget_all_user_purchases_and_rentals_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_all_user_purchases_and_rentals(
        self,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        sort: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_user_purchases_and_rentals_mapped_args(
            direction=direction,
            filter=filter,
            page=page,
            per_page=per_page,
            sort=sort,
        )
        return self._get_all_user_purchases_and_rentals_oapg(
            query_params=args.query,
        )

class GetAllUserPurchasesAndRentals(BaseApi):

    async def aget_all_user_purchases_and_rentals(
        self,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        sort: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> OnDemandPurchasesAndRentalsGetAllUserPurchasesAndRentalsResponsePydantic:
        raw_response = await self.raw.aget_all_user_purchases_and_rentals(
            direction=direction,
            filter=filter,
            page=page,
            per_page=per_page,
            sort=sort,
            **kwargs,
        )
        if validate:
            return RootModel[OnDemandPurchasesAndRentalsGetAllUserPurchasesAndRentalsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(OnDemandPurchasesAndRentalsGetAllUserPurchasesAndRentalsResponsePydantic, raw_response.body)
    
    
    def get_all_user_purchases_and_rentals(
        self,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        sort: typing.Optional[str] = None,
        validate: bool = False,
    ) -> OnDemandPurchasesAndRentalsGetAllUserPurchasesAndRentalsResponsePydantic:
        raw_response = self.raw.get_all_user_purchases_and_rentals(
            direction=direction,
            filter=filter,
            page=page,
            per_page=per_page,
            sort=sort,
        )
        if validate:
            return RootModel[OnDemandPurchasesAndRentalsGetAllUserPurchasesAndRentalsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(OnDemandPurchasesAndRentalsGetAllUserPurchasesAndRentalsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        sort: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_user_purchases_and_rentals_mapped_args(
            direction=direction,
            filter=filter,
            page=page,
            per_page=per_page,
            sort=sort,
        )
        return await self._aget_all_user_purchases_and_rentals_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        direction: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        sort: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_user_purchases_and_rentals_mapped_args(
            direction=direction,
            filter=filter,
            page=page,
            per_page=per_page,
            sort=sort,
        )
        return self._get_all_user_purchases_and_rentals_oapg(
            query_params=args.query,
        )


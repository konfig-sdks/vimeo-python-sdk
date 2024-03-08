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

from vimeo_python_sdk.model.payments_essentials_list_payment_methods_request import PaymentsEssentialsListPaymentMethodsRequest as PaymentsEssentialsListPaymentMethodsRequestSchema
from vimeo_python_sdk.model.error import Error as ErrorSchema
from vimeo_python_sdk.model.payments_essentials_list_payment_methods_response import PaymentsEssentialsListPaymentMethodsResponse as PaymentsEssentialsListPaymentMethodsResponseSchema

from vimeo_python_sdk.type.error import Error
from vimeo_python_sdk.type.payments_essentials_list_payment_methods_response import PaymentsEssentialsListPaymentMethodsResponse
from vimeo_python_sdk.type.payments_essentials_list_payment_methods_request import PaymentsEssentialsListPaymentMethodsRequest

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.error import Error as ErrorPydantic
from vimeo_python_sdk.pydantic.payments_essentials_list_payment_methods_request import PaymentsEssentialsListPaymentMethodsRequest as PaymentsEssentialsListPaymentMethodsRequestPydantic
from vimeo_python_sdk.pydantic.payments_essentials_list_payment_methods_response import PaymentsEssentialsListPaymentMethodsResponse as PaymentsEssentialsListPaymentMethodsResponsePydantic

# Query params
CardmemberNameSchema = schemas.StrSchema
PageSchema = schemas.NumberSchema
PerPageSchema = schemas.NumberSchema
ShowDisabledSchema = schemas.BoolSchema
UserIdSchema = schemas.NumberSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'user_id': typing.Union[UserIdSchema, decimal.Decimal, int, float, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'cardmember_name': typing.Union[CardmemberNameSchema, str, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, float, ],
        'per_page': typing.Union[PerPageSchema, decimal.Decimal, int, float, ],
        'show_disabled': typing.Union[ShowDisabledSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_cardmember_name = api_client.QueryParameter(
    name="cardmember_name",
    style=api_client.ParameterStyle.FORM,
    schema=CardmemberNameSchema,
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
request_query_show_disabled = api_client.QueryParameter(
    name="show_disabled",
    style=api_client.ParameterStyle.FORM,
    schema=ShowDisabledSchema,
    explode=True,
)
request_query_user_id = api_client.QueryParameter(
    name="user_id",
    style=api_client.ParameterStyle.FORM,
    schema=UserIdSchema,
    required=True,
    explode=True,
)
# body param
SchemaForRequestBodyApplicationJson = PaymentsEssentialsListPaymentMethodsRequestSchema


request_body_payments_essentials_list_payment_methods_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = PaymentsEssentialsListPaymentMethodsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PaymentsEssentialsListPaymentMethodsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PaymentsEssentialsListPaymentMethodsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ErrorSchema


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
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_payment_methods_mapped_args(
        self,
        user_id: typing.Union[int, float],
        type: typing.Optional[str] = None,
        cardmember_name: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        show_disabled: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if type is not None:
            _body["type"] = type
        args.body = _body
        if cardmember_name is not None:
            _query_params["cardmember_name"] = cardmember_name
        if page is not None:
            _query_params["page"] = page
        if per_page is not None:
            _query_params["per_page"] = per_page
        if show_disabled is not None:
            _query_params["show_disabled"] = show_disabled
        if user_id is not None:
            _query_params["user_id"] = user_id
        args.query = _query_params
        return args

    async def _alist_payment_methods_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get a list of all payments service payment methods
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_cardmember_name,
            request_query_page,
            request_query_per_page,
            request_query_show_disabled,
            request_query_user_id,
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
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/me/payment_methods',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_payments_essentials_list_payment_methods_request.serialize(body, content_type)
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


    def _list_payment_methods_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get a list of all payments service payment methods
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_cardmember_name,
            request_query_page,
            request_query_per_page,
            request_query_show_disabled,
            request_query_user_id,
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
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/me/payment_methods',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_payments_essentials_list_payment_methods_request.serialize(body, content_type)
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


class ListPaymentMethodsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_payment_methods(
        self,
        user_id: typing.Union[int, float],
        type: typing.Optional[str] = None,
        cardmember_name: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        show_disabled: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_payment_methods_mapped_args(
            user_id=user_id,
            type=type,
            cardmember_name=cardmember_name,
            page=page,
            per_page=per_page,
            show_disabled=show_disabled,
        )
        return await self._alist_payment_methods_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def list_payment_methods(
        self,
        user_id: typing.Union[int, float],
        type: typing.Optional[str] = None,
        cardmember_name: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        show_disabled: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_payment_methods_mapped_args(
            user_id=user_id,
            type=type,
            cardmember_name=cardmember_name,
            page=page,
            per_page=per_page,
            show_disabled=show_disabled,
        )
        return self._list_payment_methods_oapg(
            body=args.body,
            query_params=args.query,
        )

class ListPaymentMethods(BaseApi):

    async def alist_payment_methods(
        self,
        user_id: typing.Union[int, float],
        type: typing.Optional[str] = None,
        cardmember_name: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        show_disabled: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> PaymentsEssentialsListPaymentMethodsResponsePydantic:
        raw_response = await self.raw.alist_payment_methods(
            user_id=user_id,
            type=type,
            cardmember_name=cardmember_name,
            page=page,
            per_page=per_page,
            show_disabled=show_disabled,
            **kwargs,
        )
        if validate:
            return RootModel[PaymentsEssentialsListPaymentMethodsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(PaymentsEssentialsListPaymentMethodsResponsePydantic, raw_response.body)
    
    
    def list_payment_methods(
        self,
        user_id: typing.Union[int, float],
        type: typing.Optional[str] = None,
        cardmember_name: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        show_disabled: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> PaymentsEssentialsListPaymentMethodsResponsePydantic:
        raw_response = self.raw.list_payment_methods(
            user_id=user_id,
            type=type,
            cardmember_name=cardmember_name,
            page=page,
            per_page=per_page,
            show_disabled=show_disabled,
        )
        if validate:
            return RootModel[PaymentsEssentialsListPaymentMethodsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(PaymentsEssentialsListPaymentMethodsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        user_id: typing.Union[int, float],
        type: typing.Optional[str] = None,
        cardmember_name: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        show_disabled: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_payment_methods_mapped_args(
            user_id=user_id,
            type=type,
            cardmember_name=cardmember_name,
            page=page,
            per_page=per_page,
            show_disabled=show_disabled,
        )
        return await self._alist_payment_methods_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        user_id: typing.Union[int, float],
        type: typing.Optional[str] = None,
        cardmember_name: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        show_disabled: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_payment_methods_mapped_args(
            user_id=user_id,
            type=type,
            cardmember_name=cardmember_name,
            page=page,
            per_page=per_page,
            show_disabled=show_disabled,
        )
        return self._list_payment_methods_oapg(
            body=args.body,
            query_params=args.query,
        )


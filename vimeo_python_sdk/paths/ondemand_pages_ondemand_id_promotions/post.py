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

from vimeo_python_sdk.model.on_demand_promotion import OnDemandPromotion as OnDemandPromotionSchema
from vimeo_python_sdk.model.legacy_error import LegacyError as LegacyErrorSchema
from vimeo_python_sdk.model.on_demand_promotions_add_promotion_to_page_request import OnDemandPromotionsAddPromotionToPageRequest as OnDemandPromotionsAddPromotionToPageRequestSchema

from vimeo_python_sdk.type.on_demand_promotion import OnDemandPromotion
from vimeo_python_sdk.type.on_demand_promotions_add_promotion_to_page_request import OnDemandPromotionsAddPromotionToPageRequest
from vimeo_python_sdk.type.legacy_error import LegacyError

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.on_demand_promotion import OnDemandPromotion as OnDemandPromotionPydantic
from vimeo_python_sdk.pydantic.legacy_error import LegacyError as LegacyErrorPydantic
from vimeo_python_sdk.pydantic.on_demand_promotions_add_promotion_to_page_request import OnDemandPromotionsAddPromotionToPageRequest as OnDemandPromotionsAddPromotionToPageRequestPydantic

from . import path

# Path params
OndemandIdSchema = schemas.NumberSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'ondemand_id': typing.Union[OndemandIdSchema, decimal.Decimal, int, float, ],
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


request_path_ondemand_id = api_client.PathParameter(
    name="ondemand_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=OndemandIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationVndVimeoOndemandPromotionjson = OnDemandPromotionsAddPromotionToPageRequestSchema


request_body_on_demand_promotions_add_promotion_to_page_request = api_client.RequestBody(
    content={
        'application/vnd.vimeo.ondemand.promotion+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndVimeoOndemandPromotionjson),
    },
    required=True,
)
_auth = [
    'oauth2',
    'oauth2',
]
SchemaFor200ResponseBodyApplicationVndVimeoOndemandPromotionjson = OnDemandPromotionSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: OnDemandPromotion


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: OnDemandPromotion


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.ondemand.promotion+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoOndemandPromotionjson),
    },
)
SchemaFor400ResponseBodyApplicationVndVimeoOndemandPromotionjson = LegacyErrorSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: LegacyError


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: LegacyError


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/vnd.vimeo.ondemand.promotion+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndVimeoOndemandPromotionjson),
    },
)
SchemaFor403ResponseBodyApplicationVndVimeoOndemandPromotionjson = LegacyErrorSchema


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
        'application/vnd.vimeo.ondemand.promotion+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationVndVimeoOndemandPromotionjson),
    },
)
SchemaFor404ResponseBodyApplicationVndVimeoOndemandPromotionjson = LegacyErrorSchema


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
        'application/vnd.vimeo.ondemand.promotion+json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationVndVimeoOndemandPromotionjson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '403': _response_for_403,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/vnd.vimeo.ondemand.promotion+json',
)


class BaseApi(api_client.Api):

    def _add_promotion_to_page_mapped_args(
        self,
        download: bool,
        stream_period: str,
        total: typing.Union[int, float],
        type: str,
        ondemand_id: typing.Union[int, float],
        access_type: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        discount_type: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        percent_off: typing.Optional[typing.Union[int, float]] = None,
        product_type: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if access_type is not None:
            _body["access_type"] = access_type
        if code is not None:
            _body["code"] = code
        if discount_type is not None:
            _body["discount_type"] = discount_type
        if download is not None:
            _body["download"] = download
        if end_time is not None:
            _body["end_time"] = end_time
        if label is not None:
            _body["label"] = label
        if percent_off is not None:
            _body["percent_off"] = percent_off
        if product_type is not None:
            _body["product_type"] = product_type
        if start_time is not None:
            _body["start_time"] = start_time
        if stream_period is not None:
            _body["stream_period"] = stream_period
        if total is not None:
            _body["total"] = total
        if type is not None:
            _body["type"] = type
        args.body = _body
        if ondemand_id is not None:
            _path_params["ondemand_id"] = ondemand_id
        args.path = _path_params
        return args

    async def _aadd_promotion_to_page_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.ondemand.promotion+json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Add a promotion to an On Demand page
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_ondemand_id,
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
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/ondemand/pages/{ondemand_id}/promotions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_on_demand_promotions_add_promotion_to_page_request.serialize(body, content_type)
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


    def _add_promotion_to_page_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.ondemand.promotion+json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Add a promotion to an On Demand page
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_ondemand_id,
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
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/ondemand/pages/{ondemand_id}/promotions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_on_demand_promotions_add_promotion_to_page_request.serialize(body, content_type)
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


class AddPromotionToPageRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_promotion_to_page(
        self,
        download: bool,
        stream_period: str,
        total: typing.Union[int, float],
        type: str,
        ondemand_id: typing.Union[int, float],
        access_type: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        discount_type: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        percent_off: typing.Optional[typing.Union[int, float]] = None,
        product_type: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_promotion_to_page_mapped_args(
            download=download,
            stream_period=stream_period,
            total=total,
            type=type,
            ondemand_id=ondemand_id,
            access_type=access_type,
            code=code,
            discount_type=discount_type,
            end_time=end_time,
            label=label,
            percent_off=percent_off,
            product_type=product_type,
            start_time=start_time,
        )
        return await self._aadd_promotion_to_page_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def add_promotion_to_page(
        self,
        download: bool,
        stream_period: str,
        total: typing.Union[int, float],
        type: str,
        ondemand_id: typing.Union[int, float],
        access_type: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        discount_type: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        percent_off: typing.Optional[typing.Union[int, float]] = None,
        product_type: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_promotion_to_page_mapped_args(
            download=download,
            stream_period=stream_period,
            total=total,
            type=type,
            ondemand_id=ondemand_id,
            access_type=access_type,
            code=code,
            discount_type=discount_type,
            end_time=end_time,
            label=label,
            percent_off=percent_off,
            product_type=product_type,
            start_time=start_time,
        )
        return self._add_promotion_to_page_oapg(
            body=args.body,
            path_params=args.path,
        )

class AddPromotionToPage(BaseApi):

    async def aadd_promotion_to_page(
        self,
        download: bool,
        stream_period: str,
        total: typing.Union[int, float],
        type: str,
        ondemand_id: typing.Union[int, float],
        access_type: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        discount_type: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        percent_off: typing.Optional[typing.Union[int, float]] = None,
        product_type: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> OnDemandPromotionPydantic:
        raw_response = await self.raw.aadd_promotion_to_page(
            download=download,
            stream_period=stream_period,
            total=total,
            type=type,
            ondemand_id=ondemand_id,
            access_type=access_type,
            code=code,
            discount_type=discount_type,
            end_time=end_time,
            label=label,
            percent_off=percent_off,
            product_type=product_type,
            start_time=start_time,
            **kwargs,
        )
        if validate:
            return OnDemandPromotionPydantic(**raw_response.body)
        return api_client.construct_model_instance(OnDemandPromotionPydantic, raw_response.body)
    
    
    def add_promotion_to_page(
        self,
        download: bool,
        stream_period: str,
        total: typing.Union[int, float],
        type: str,
        ondemand_id: typing.Union[int, float],
        access_type: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        discount_type: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        percent_off: typing.Optional[typing.Union[int, float]] = None,
        product_type: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
        validate: bool = False,
    ) -> OnDemandPromotionPydantic:
        raw_response = self.raw.add_promotion_to_page(
            download=download,
            stream_period=stream_period,
            total=total,
            type=type,
            ondemand_id=ondemand_id,
            access_type=access_type,
            code=code,
            discount_type=discount_type,
            end_time=end_time,
            label=label,
            percent_off=percent_off,
            product_type=product_type,
            start_time=start_time,
        )
        if validate:
            return OnDemandPromotionPydantic(**raw_response.body)
        return api_client.construct_model_instance(OnDemandPromotionPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        download: bool,
        stream_period: str,
        total: typing.Union[int, float],
        type: str,
        ondemand_id: typing.Union[int, float],
        access_type: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        discount_type: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        percent_off: typing.Optional[typing.Union[int, float]] = None,
        product_type: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_promotion_to_page_mapped_args(
            download=download,
            stream_period=stream_period,
            total=total,
            type=type,
            ondemand_id=ondemand_id,
            access_type=access_type,
            code=code,
            discount_type=discount_type,
            end_time=end_time,
            label=label,
            percent_off=percent_off,
            product_type=product_type,
            start_time=start_time,
        )
        return await self._aadd_promotion_to_page_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        download: bool,
        stream_period: str,
        total: typing.Union[int, float],
        type: str,
        ondemand_id: typing.Union[int, float],
        access_type: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        discount_type: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        percent_off: typing.Optional[typing.Union[int, float]] = None,
        product_type: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_promotion_to_page_mapped_args(
            download=download,
            stream_period=stream_period,
            total=total,
            type=type,
            ondemand_id=ondemand_id,
            access_type=access_type,
            code=code,
            discount_type=discount_type,
            end_time=end_time,
            label=label,
            percent_off=percent_off,
            product_type=product_type,
            start_time=start_time,
        )
        return self._add_promotion_to_page_oapg(
            body=args.body,
            path_params=args.path,
        )


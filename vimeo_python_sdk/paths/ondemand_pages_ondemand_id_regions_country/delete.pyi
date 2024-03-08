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

from vimeo_python_sdk.model.legacy_error import LegacyError as LegacyErrorSchema

from vimeo_python_sdk.type.legacy_error import LegacyError

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.legacy_error import LegacyError as LegacyErrorPydantic

# Path params
CountrySchema = schemas.StrSchema
OndemandIdSchema = schemas.NumberSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'country': typing.Union[CountrySchema, str, ],
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


request_path_country = api_client.PathParameter(
    name="country",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CountrySchema,
    required=True,
)
request_path_ondemand_id = api_client.PathParameter(
    name="ondemand_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=OndemandIdSchema,
    required=True,
)


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor204Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_204 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor204,
    response_cls_async=ApiResponseFor204Async,
)
SchemaFor403ResponseBodyApplicationVndVimeoOndemandRegionjson = LegacyErrorSchema


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
        'application/vnd.vimeo.ondemand.region+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationVndVimeoOndemandRegionjson),
    },
)
SchemaFor404ResponseBodyApplicationVndVimeoOndemandRegionjson = LegacyErrorSchema


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
        'application/vnd.vimeo.ondemand.region+json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationVndVimeoOndemandRegionjson),
    },
)
_all_accept_content_types = (
    'application/vnd.vimeo.ondemand.region+json',
)


class BaseApi(api_client.Api):

    def _remove_specific_region_mapped_args(
        self,
        country: str,
        ondemand_id: typing.Union[int, float],
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if country is not None:
            _path_params["country"] = country
        if ondemand_id is not None:
            _path_params["ondemand_id"] = ondemand_id
        args.path = _path_params
        return args

    async def _aremove_specific_region_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Remove a specific region from an On Demand page
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_country,
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
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/ondemand/pages/{ondemand_id}/regions/{country}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _remove_specific_region_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Remove a specific region from an On Demand page
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_country,
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
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/ondemand/pages/{ondemand_id}/regions/{country}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class RemoveSpecificRegionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aremove_specific_region(
        self,
        country: str,
        ondemand_id: typing.Union[int, float],
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._remove_specific_region_mapped_args(
            country=country,
            ondemand_id=ondemand_id,
        )
        return await self._aremove_specific_region_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def remove_specific_region(
        self,
        country: str,
        ondemand_id: typing.Union[int, float],
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._remove_specific_region_mapped_args(
            country=country,
            ondemand_id=ondemand_id,
        )
        return self._remove_specific_region_oapg(
            path_params=args.path,
        )

class RemoveSpecificRegion(BaseApi):

    async def aremove_specific_region(
        self,
        country: str,
        ondemand_id: typing.Union[int, float],
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aremove_specific_region(
            country=country,
            ondemand_id=ondemand_id,
            **kwargs,
        )
    
    
    def remove_specific_region(
        self,
        country: str,
        ondemand_id: typing.Union[int, float],
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.remove_specific_region(
            country=country,
            ondemand_id=ondemand_id,
        )


class ApiFordelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def adelete(
        self,
        country: str,
        ondemand_id: typing.Union[int, float],
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._remove_specific_region_mapped_args(
            country=country,
            ondemand_id=ondemand_id,
        )
        return await self._aremove_specific_region_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def delete(
        self,
        country: str,
        ondemand_id: typing.Union[int, float],
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._remove_specific_region_mapped_args(
            country=country,
            ondemand_id=ondemand_id,
        )
        return self._remove_specific_region_oapg(
            path_params=args.path,
        )


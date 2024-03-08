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

from vimeo_python_sdk.model.edit_vod_request_publish import EditVodRequestPublish as EditVodRequestPublishSchema
from vimeo_python_sdk.model.on_demand_page import OnDemandPage as OnDemandPageSchema
from vimeo_python_sdk.model.edit_vod_request import EditVodRequest as EditVodRequestSchema
from vimeo_python_sdk.model.legacy_error import LegacyError as LegacyErrorSchema
from vimeo_python_sdk.model.edit_vod_request_preorder import EditVodRequestPreorder as EditVodRequestPreorderSchema

from vimeo_python_sdk.type.on_demand_page import OnDemandPage
from vimeo_python_sdk.type.edit_vod_request_publish import EditVodRequestPublish
from vimeo_python_sdk.type.legacy_error import LegacyError
from vimeo_python_sdk.type.edit_vod_request_preorder import EditVodRequestPreorder
from vimeo_python_sdk.type.edit_vod_request import EditVodRequest

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.edit_vod_request import EditVodRequest as EditVodRequestPydantic
from vimeo_python_sdk.pydantic.edit_vod_request_preorder import EditVodRequestPreorder as EditVodRequestPreorderPydantic
from vimeo_python_sdk.pydantic.edit_vod_request_publish import EditVodRequestPublish as EditVodRequestPublishPydantic
from vimeo_python_sdk.pydantic.on_demand_page import OnDemandPage as OnDemandPagePydantic
from vimeo_python_sdk.pydantic.legacy_error import LegacyError as LegacyErrorPydantic

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
SchemaForRequestBodyApplicationVndVimeoOndemandPagejson = EditVodRequestSchema


request_body_edit_vod_request = api_client.RequestBody(
    content={
        'application/vnd.vimeo.ondemand.page+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndVimeoOndemandPagejson),
    },
)
SchemaFor200ResponseBodyApplicationVndVimeoOndemandPagejson = OnDemandPageSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: OnDemandPage


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: OnDemandPage


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
SchemaFor404ResponseBodyApplicationVndVimeoOndemandPagejson = LegacyErrorSchema


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
        'application/vnd.vimeo.ondemand.page+json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationVndVimeoOndemandPagejson),
    },
)
_all_accept_content_types = (
    'application/vnd.vimeo.ondemand.page+json',
)


class BaseApi(api_client.Api):

    def _vod_0_mapped_args(
        self,
        ondemand_id: typing.Union[int, float],
        link: typing.Optional[str] = None,
        preorder: typing.Optional[EditVodRequestPreorder] = None,
        publish: typing.Optional[EditVodRequestPublish] = None,
        publish_when_ready: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if link is not None:
            _body["link"] = link
        if preorder is not None:
            _body["preorder"] = preorder
        if publish is not None:
            _body["publish"] = publish
        if publish_when_ready is not None:
            _body["publish_when_ready"] = publish_when_ready
        args.body = _body
        if ondemand_id is not None:
            _path_params["ondemand_id"] = ondemand_id
        args.path = _path_params
        return args

    async def _avod_0_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.ondemand.page+json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Edit an On Demand page
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/ondemand/pages/{ondemand_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_edit_vod_request.serialize(body, content_type)
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


    def _vod_0_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.ondemand.page+json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Edit an On Demand page
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/ondemand/pages/{ondemand_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_edit_vod_request.serialize(body, content_type)
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


class Vod0Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def avod_0(
        self,
        ondemand_id: typing.Union[int, float],
        link: typing.Optional[str] = None,
        preorder: typing.Optional[EditVodRequestPreorder] = None,
        publish: typing.Optional[EditVodRequestPublish] = None,
        publish_when_ready: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._vod_0_mapped_args(
            ondemand_id=ondemand_id,
            link=link,
            preorder=preorder,
            publish=publish,
            publish_when_ready=publish_when_ready,
        )
        return await self._avod_0_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def vod_0(
        self,
        ondemand_id: typing.Union[int, float],
        link: typing.Optional[str] = None,
        preorder: typing.Optional[EditVodRequestPreorder] = None,
        publish: typing.Optional[EditVodRequestPublish] = None,
        publish_when_ready: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._vod_0_mapped_args(
            ondemand_id=ondemand_id,
            link=link,
            preorder=preorder,
            publish=publish,
            publish_when_ready=publish_when_ready,
        )
        return self._vod_0_oapg(
            body=args.body,
            path_params=args.path,
        )

class Vod0(BaseApi):

    async def avod_0(
        self,
        ondemand_id: typing.Union[int, float],
        link: typing.Optional[str] = None,
        preorder: typing.Optional[EditVodRequestPreorder] = None,
        publish: typing.Optional[EditVodRequestPublish] = None,
        publish_when_ready: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> OnDemandPagePydantic:
        raw_response = await self.raw.avod_0(
            ondemand_id=ondemand_id,
            link=link,
            preorder=preorder,
            publish=publish,
            publish_when_ready=publish_when_ready,
            **kwargs,
        )
        if validate:
            return OnDemandPagePydantic(**raw_response.body)
        return api_client.construct_model_instance(OnDemandPagePydantic, raw_response.body)
    
    
    def vod_0(
        self,
        ondemand_id: typing.Union[int, float],
        link: typing.Optional[str] = None,
        preorder: typing.Optional[EditVodRequestPreorder] = None,
        publish: typing.Optional[EditVodRequestPublish] = None,
        publish_when_ready: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> OnDemandPagePydantic:
        raw_response = self.raw.vod_0(
            ondemand_id=ondemand_id,
            link=link,
            preorder=preorder,
            publish=publish,
            publish_when_ready=publish_when_ready,
        )
        if validate:
            return OnDemandPagePydantic(**raw_response.body)
        return api_client.construct_model_instance(OnDemandPagePydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        ondemand_id: typing.Union[int, float],
        link: typing.Optional[str] = None,
        preorder: typing.Optional[EditVodRequestPreorder] = None,
        publish: typing.Optional[EditVodRequestPublish] = None,
        publish_when_ready: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._vod_0_mapped_args(
            ondemand_id=ondemand_id,
            link=link,
            preorder=preorder,
            publish=publish,
            publish_when_ready=publish_when_ready,
        )
        return await self._avod_0_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        ondemand_id: typing.Union[int, float],
        link: typing.Optional[str] = None,
        preorder: typing.Optional[EditVodRequestPreorder] = None,
        publish: typing.Optional[EditVodRequestPublish] = None,
        publish_when_ready: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._vod_0_mapped_args(
            ondemand_id=ondemand_id,
            link=link,
            preorder=preorder,
            publish=publish,
            publish_when_ready=publish_when_ready,
        )
        return self._vod_0_oapg(
            body=args.body,
            path_params=args.path,
        )


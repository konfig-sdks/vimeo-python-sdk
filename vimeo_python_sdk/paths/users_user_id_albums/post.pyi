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

from vimeo_python_sdk.model.create_showcase_request import CreateShowcaseRequest as CreateShowcaseRequestSchema
from vimeo_python_sdk.model.album import Album as AlbumSchema
from vimeo_python_sdk.model.legacy_error import LegacyError as LegacyErrorSchema

from vimeo_python_sdk.type.create_showcase_request import CreateShowcaseRequest
from vimeo_python_sdk.type.album import Album
from vimeo_python_sdk.type.legacy_error import LegacyError

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.create_showcase_request import CreateShowcaseRequest as CreateShowcaseRequestPydantic
from vimeo_python_sdk.pydantic.legacy_error import LegacyError as LegacyErrorPydantic
from vimeo_python_sdk.pydantic.album import Album as AlbumPydantic

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
# body param
SchemaForRequestBodyApplicationVndVimeoAlbumjson = CreateShowcaseRequestSchema


request_body_create_showcase_request = api_client.RequestBody(
    content={
        'application/vnd.vimeo.album+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndVimeoAlbumjson),
    },
    required=True,
)
SchemaFor201ResponseBodyApplicationVndVimeoAlbumjson = AlbumSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Album


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Album


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/vnd.vimeo.album+json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationVndVimeoAlbumjson),
    },
)
SchemaFor400ResponseBodyApplicationVndVimeoAlbumjson = LegacyErrorSchema


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
        'application/vnd.vimeo.album+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndVimeoAlbumjson),
    },
)
SchemaFor403ResponseBodyApplicationVndVimeoAlbumjson = LegacyErrorSchema


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
        'application/vnd.vimeo.album+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationVndVimeoAlbumjson),
    },
)
_all_accept_content_types = (
    'application/vnd.vimeo.album+json',
)


class BaseApi(api_client.Api):

    def _showcase_mapped_args(
        self,
        name: str,
        user_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        brand_color: typing.Optional[str] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        hide_nav: typing.Optional[bool] = None,
        hide_upcoming: typing.Optional[bool] = None,
        layout: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[str] = None,
        review_mode: typing.Optional[bool] = None,
        sort: typing.Optional[str] = None,
        theme: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if brand_color is not None:
            _body["brand_color"] = brand_color
        if hide_from_vimeo is not None:
            _body["hide_from_vimeo"] = hide_from_vimeo
        if hide_nav is not None:
            _body["hide_nav"] = hide_nav
        if hide_upcoming is not None:
            _body["hide_upcoming"] = hide_upcoming
        if layout is not None:
            _body["layout"] = layout
        if name is not None:
            _body["name"] = name
        if password is not None:
            _body["password"] = password
        if privacy is not None:
            _body["privacy"] = privacy
        if review_mode is not None:
            _body["review_mode"] = review_mode
        if sort is not None:
            _body["sort"] = sort
        if theme is not None:
            _body["theme"] = theme
        args.body = _body
        if user_id is not None:
            _path_params["user_id"] = user_id
        args.path = _path_params
        return args

    async def _ashowcase_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.album+json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a showcase
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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
            path_template='/users/{user_id}/albums',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_showcase_request.serialize(body, content_type)
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


    def _showcase_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.album+json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a showcase
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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
            path_template='/users/{user_id}/albums',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_showcase_request.serialize(body, content_type)
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


class ShowcaseRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def ashowcase(
        self,
        name: str,
        user_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        brand_color: typing.Optional[str] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        hide_nav: typing.Optional[bool] = None,
        hide_upcoming: typing.Optional[bool] = None,
        layout: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[str] = None,
        review_mode: typing.Optional[bool] = None,
        sort: typing.Optional[str] = None,
        theme: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._showcase_mapped_args(
            name=name,
            user_id=user_id,
            description=description,
            brand_color=brand_color,
            hide_from_vimeo=hide_from_vimeo,
            hide_nav=hide_nav,
            hide_upcoming=hide_upcoming,
            layout=layout,
            password=password,
            privacy=privacy,
            review_mode=review_mode,
            sort=sort,
            theme=theme,
        )
        return await self._ashowcase_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def showcase(
        self,
        name: str,
        user_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        brand_color: typing.Optional[str] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        hide_nav: typing.Optional[bool] = None,
        hide_upcoming: typing.Optional[bool] = None,
        layout: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[str] = None,
        review_mode: typing.Optional[bool] = None,
        sort: typing.Optional[str] = None,
        theme: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._showcase_mapped_args(
            name=name,
            user_id=user_id,
            description=description,
            brand_color=brand_color,
            hide_from_vimeo=hide_from_vimeo,
            hide_nav=hide_nav,
            hide_upcoming=hide_upcoming,
            layout=layout,
            password=password,
            privacy=privacy,
            review_mode=review_mode,
            sort=sort,
            theme=theme,
        )
        return self._showcase_oapg(
            body=args.body,
            path_params=args.path,
        )

class Showcase(BaseApi):

    async def ashowcase(
        self,
        name: str,
        user_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        brand_color: typing.Optional[str] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        hide_nav: typing.Optional[bool] = None,
        hide_upcoming: typing.Optional[bool] = None,
        layout: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[str] = None,
        review_mode: typing.Optional[bool] = None,
        sort: typing.Optional[str] = None,
        theme: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> AlbumPydantic:
        raw_response = await self.raw.ashowcase(
            name=name,
            user_id=user_id,
            description=description,
            brand_color=brand_color,
            hide_from_vimeo=hide_from_vimeo,
            hide_nav=hide_nav,
            hide_upcoming=hide_upcoming,
            layout=layout,
            password=password,
            privacy=privacy,
            review_mode=review_mode,
            sort=sort,
            theme=theme,
            **kwargs,
        )
        if validate:
            return AlbumPydantic(**raw_response.body)
        return api_client.construct_model_instance(AlbumPydantic, raw_response.body)
    
    
    def showcase(
        self,
        name: str,
        user_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        brand_color: typing.Optional[str] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        hide_nav: typing.Optional[bool] = None,
        hide_upcoming: typing.Optional[bool] = None,
        layout: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[str] = None,
        review_mode: typing.Optional[bool] = None,
        sort: typing.Optional[str] = None,
        theme: typing.Optional[str] = None,
        validate: bool = False,
    ) -> AlbumPydantic:
        raw_response = self.raw.showcase(
            name=name,
            user_id=user_id,
            description=description,
            brand_color=brand_color,
            hide_from_vimeo=hide_from_vimeo,
            hide_nav=hide_nav,
            hide_upcoming=hide_upcoming,
            layout=layout,
            password=password,
            privacy=privacy,
            review_mode=review_mode,
            sort=sort,
            theme=theme,
        )
        if validate:
            return AlbumPydantic(**raw_response.body)
        return api_client.construct_model_instance(AlbumPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        user_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        brand_color: typing.Optional[str] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        hide_nav: typing.Optional[bool] = None,
        hide_upcoming: typing.Optional[bool] = None,
        layout: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[str] = None,
        review_mode: typing.Optional[bool] = None,
        sort: typing.Optional[str] = None,
        theme: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._showcase_mapped_args(
            name=name,
            user_id=user_id,
            description=description,
            brand_color=brand_color,
            hide_from_vimeo=hide_from_vimeo,
            hide_nav=hide_nav,
            hide_upcoming=hide_upcoming,
            layout=layout,
            password=password,
            privacy=privacy,
            review_mode=review_mode,
            sort=sort,
            theme=theme,
        )
        return await self._ashowcase_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        user_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        brand_color: typing.Optional[str] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        hide_nav: typing.Optional[bool] = None,
        hide_upcoming: typing.Optional[bool] = None,
        layout: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[str] = None,
        review_mode: typing.Optional[bool] = None,
        sort: typing.Optional[str] = None,
        theme: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._showcase_mapped_args(
            name=name,
            user_id=user_id,
            description=description,
            brand_color=brand_color,
            hide_from_vimeo=hide_from_vimeo,
            hide_nav=hide_nav,
            hide_upcoming=hide_upcoming,
            layout=layout,
            password=password,
            privacy=privacy,
            review_mode=review_mode,
            sort=sort,
            theme=theme,
        )
        return self._showcase_oapg(
            body=args.body,
            path_params=args.path,
        )


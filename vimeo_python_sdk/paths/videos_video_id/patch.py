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

from vimeo_python_sdk.model.edit_video_request_embed_domains import EditVideoRequestEmbedDomains as EditVideoRequestEmbedDomainsSchema
from vimeo_python_sdk.model.edit_video_request_spatial import EditVideoRequestSpatial as EditVideoRequestSpatialSchema
from vimeo_python_sdk.model.edit_video_request_embed_domains_add import EditVideoRequestEmbedDomainsAdd as EditVideoRequestEmbedDomainsAddSchema
from vimeo_python_sdk.model.edit_video_request_embed_domains_delete import EditVideoRequestEmbedDomainsDelete as EditVideoRequestEmbedDomainsDeleteSchema
from vimeo_python_sdk.model.edit_video_request import EditVideoRequest as EditVideoRequestSchema
from vimeo_python_sdk.model.video import Video as VideoSchema
from vimeo_python_sdk.model.edit_video_request_review_page import EditVideoRequestReviewPage as EditVideoRequestReviewPageSchema
from vimeo_python_sdk.model.edit_video_request_privacy import EditVideoRequestPrivacy as EditVideoRequestPrivacySchema
from vimeo_python_sdk.model.legacy_error import LegacyError as LegacyErrorSchema
from vimeo_python_sdk.model.edit_video_request_content_rating import EditVideoRequestContentRating as EditVideoRequestContentRatingSchema
from vimeo_python_sdk.model.edit_video_request_embed import EditVideoRequestEmbed as EditVideoRequestEmbedSchema

from vimeo_python_sdk.type.edit_video_request_review_page import EditVideoRequestReviewPage
from vimeo_python_sdk.type.video import Video
from vimeo_python_sdk.type.edit_video_request_embed_domains_delete import EditVideoRequestEmbedDomainsDelete
from vimeo_python_sdk.type.edit_video_request_spatial import EditVideoRequestSpatial
from vimeo_python_sdk.type.edit_video_request_privacy import EditVideoRequestPrivacy
from vimeo_python_sdk.type.edit_video_request_embed_domains import EditVideoRequestEmbedDomains
from vimeo_python_sdk.type.edit_video_request_embed import EditVideoRequestEmbed
from vimeo_python_sdk.type.edit_video_request_embed_domains_add import EditVideoRequestEmbedDomainsAdd
from vimeo_python_sdk.type.legacy_error import LegacyError
from vimeo_python_sdk.type.edit_video_request_content_rating import EditVideoRequestContentRating
from vimeo_python_sdk.type.edit_video_request import EditVideoRequest

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.edit_video_request_review_page import EditVideoRequestReviewPage as EditVideoRequestReviewPagePydantic
from vimeo_python_sdk.pydantic.edit_video_request_embed_domains import EditVideoRequestEmbedDomains as EditVideoRequestEmbedDomainsPydantic
from vimeo_python_sdk.pydantic.edit_video_request_embed_domains_delete import EditVideoRequestEmbedDomainsDelete as EditVideoRequestEmbedDomainsDeletePydantic
from vimeo_python_sdk.pydantic.edit_video_request import EditVideoRequest as EditVideoRequestPydantic
from vimeo_python_sdk.pydantic.edit_video_request_embed import EditVideoRequestEmbed as EditVideoRequestEmbedPydantic
from vimeo_python_sdk.pydantic.edit_video_request_content_rating import EditVideoRequestContentRating as EditVideoRequestContentRatingPydantic
from vimeo_python_sdk.pydantic.edit_video_request_embed_domains_add import EditVideoRequestEmbedDomainsAdd as EditVideoRequestEmbedDomainsAddPydantic
from vimeo_python_sdk.pydantic.edit_video_request_privacy import EditVideoRequestPrivacy as EditVideoRequestPrivacyPydantic
from vimeo_python_sdk.pydantic.video import Video as VideoPydantic
from vimeo_python_sdk.pydantic.legacy_error import LegacyError as LegacyErrorPydantic
from vimeo_python_sdk.pydantic.edit_video_request_spatial import EditVideoRequestSpatial as EditVideoRequestSpatialPydantic

from . import path

# Path params
VideoIdSchema = schemas.NumberSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'video_id': typing.Union[VideoIdSchema, decimal.Decimal, int, float, ],
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


request_path_video_id = api_client.PathParameter(
    name="video_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=VideoIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationVndVimeoVideojson = EditVideoRequestSchema


request_body_edit_video_request = api_client.RequestBody(
    content={
        'application/vnd.vimeo.video+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndVimeoVideojson),
    },
    required=True,
)
_auth = [
    'oauth2',
    'oauth2',
]
SchemaFor200ResponseBodyApplicationVndVimeoVideojson = VideoSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Video


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Video


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.video+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoVideojson),
    },
)
SchemaFor400ResponseBodyApplicationVndVimeoVideojson = LegacyErrorSchema


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
        'application/vnd.vimeo.video+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndVimeoVideojson),
    },
)
SchemaFor403ResponseBodyApplicationVndVimeoVideojson = LegacyErrorSchema


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
        'application/vnd.vimeo.video+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationVndVimeoVideojson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '403': _response_for_403,
}
_all_accept_content_types = (
    'application/vnd.vimeo.video+json',
)


class BaseApi(api_client.Api):

    def _video_1_mapped_args(
        self,
        video_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        content_rating: typing.Optional[EditVideoRequestContentRating] = None,
        custom_url: typing.Optional[str] = None,
        embed: typing.Optional[EditVideoRequestEmbed] = None,
        embed_domains: typing.Optional[EditVideoRequestEmbedDomains] = None,
        embed_domains_add: typing.Optional[EditVideoRequestEmbedDomainsAdd] = None,
        embed_domains_delete: typing.Optional[EditVideoRequestEmbedDomainsDelete] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        license: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[EditVideoRequestPrivacy] = None,
        review_page: typing.Optional[EditVideoRequestReviewPage] = None,
        spatial: typing.Optional[EditVideoRequestSpatial] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if content_rating is not None:
            _body["content_rating"] = content_rating
        if custom_url is not None:
            _body["custom_url"] = custom_url
        if embed is not None:
            _body["embed"] = embed
        if embed_domains is not None:
            _body["embed_domains"] = embed_domains
        if embed_domains_add is not None:
            _body["embed_domains_add"] = embed_domains_add
        if embed_domains_delete is not None:
            _body["embed_domains_delete"] = embed_domains_delete
        if hide_from_vimeo is not None:
            _body["hide_from_vimeo"] = hide_from_vimeo
        if license is not None:
            _body["license"] = license
        if locale is not None:
            _body["locale"] = locale
        if name is not None:
            _body["name"] = name
        if password is not None:
            _body["password"] = password
        if privacy is not None:
            _body["privacy"] = privacy
        if review_page is not None:
            _body["review_page"] = review_page
        if spatial is not None:
            _body["spatial"] = spatial
        args.body = _body
        if video_id is not None:
            _path_params["video_id"] = video_id
        args.path = _path_params
        return args

    async def _avideo_1_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.video+json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Edit a video
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_video_id,
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
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/videos/{video_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_edit_video_request.serialize(body, content_type)
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


    def _video_1_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.video+json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Edit a video
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_video_id,
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
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/videos/{video_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_edit_video_request.serialize(body, content_type)
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


class Video1Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def avideo_1(
        self,
        video_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        content_rating: typing.Optional[EditVideoRequestContentRating] = None,
        custom_url: typing.Optional[str] = None,
        embed: typing.Optional[EditVideoRequestEmbed] = None,
        embed_domains: typing.Optional[EditVideoRequestEmbedDomains] = None,
        embed_domains_add: typing.Optional[EditVideoRequestEmbedDomainsAdd] = None,
        embed_domains_delete: typing.Optional[EditVideoRequestEmbedDomainsDelete] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        license: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[EditVideoRequestPrivacy] = None,
        review_page: typing.Optional[EditVideoRequestReviewPage] = None,
        spatial: typing.Optional[EditVideoRequestSpatial] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._video_1_mapped_args(
            video_id=video_id,
            description=description,
            content_rating=content_rating,
            custom_url=custom_url,
            embed=embed,
            embed_domains=embed_domains,
            embed_domains_add=embed_domains_add,
            embed_domains_delete=embed_domains_delete,
            hide_from_vimeo=hide_from_vimeo,
            license=license,
            locale=locale,
            name=name,
            password=password,
            privacy=privacy,
            review_page=review_page,
            spatial=spatial,
        )
        return await self._avideo_1_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def video_1(
        self,
        video_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        content_rating: typing.Optional[EditVideoRequestContentRating] = None,
        custom_url: typing.Optional[str] = None,
        embed: typing.Optional[EditVideoRequestEmbed] = None,
        embed_domains: typing.Optional[EditVideoRequestEmbedDomains] = None,
        embed_domains_add: typing.Optional[EditVideoRequestEmbedDomainsAdd] = None,
        embed_domains_delete: typing.Optional[EditVideoRequestEmbedDomainsDelete] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        license: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[EditVideoRequestPrivacy] = None,
        review_page: typing.Optional[EditVideoRequestReviewPage] = None,
        spatial: typing.Optional[EditVideoRequestSpatial] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._video_1_mapped_args(
            video_id=video_id,
            description=description,
            content_rating=content_rating,
            custom_url=custom_url,
            embed=embed,
            embed_domains=embed_domains,
            embed_domains_add=embed_domains_add,
            embed_domains_delete=embed_domains_delete,
            hide_from_vimeo=hide_from_vimeo,
            license=license,
            locale=locale,
            name=name,
            password=password,
            privacy=privacy,
            review_page=review_page,
            spatial=spatial,
        )
        return self._video_1_oapg(
            body=args.body,
            path_params=args.path,
        )

class Video1(BaseApi):

    async def avideo_1(
        self,
        video_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        content_rating: typing.Optional[EditVideoRequestContentRating] = None,
        custom_url: typing.Optional[str] = None,
        embed: typing.Optional[EditVideoRequestEmbed] = None,
        embed_domains: typing.Optional[EditVideoRequestEmbedDomains] = None,
        embed_domains_add: typing.Optional[EditVideoRequestEmbedDomainsAdd] = None,
        embed_domains_delete: typing.Optional[EditVideoRequestEmbedDomainsDelete] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        license: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[EditVideoRequestPrivacy] = None,
        review_page: typing.Optional[EditVideoRequestReviewPage] = None,
        spatial: typing.Optional[EditVideoRequestSpatial] = None,
        validate: bool = False,
        **kwargs,
    ) -> VideoPydantic:
        raw_response = await self.raw.avideo_1(
            video_id=video_id,
            description=description,
            content_rating=content_rating,
            custom_url=custom_url,
            embed=embed,
            embed_domains=embed_domains,
            embed_domains_add=embed_domains_add,
            embed_domains_delete=embed_domains_delete,
            hide_from_vimeo=hide_from_vimeo,
            license=license,
            locale=locale,
            name=name,
            password=password,
            privacy=privacy,
            review_page=review_page,
            spatial=spatial,
            **kwargs,
        )
        if validate:
            return VideoPydantic(**raw_response.body)
        return api_client.construct_model_instance(VideoPydantic, raw_response.body)
    
    
    def video_1(
        self,
        video_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        content_rating: typing.Optional[EditVideoRequestContentRating] = None,
        custom_url: typing.Optional[str] = None,
        embed: typing.Optional[EditVideoRequestEmbed] = None,
        embed_domains: typing.Optional[EditVideoRequestEmbedDomains] = None,
        embed_domains_add: typing.Optional[EditVideoRequestEmbedDomainsAdd] = None,
        embed_domains_delete: typing.Optional[EditVideoRequestEmbedDomainsDelete] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        license: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[EditVideoRequestPrivacy] = None,
        review_page: typing.Optional[EditVideoRequestReviewPage] = None,
        spatial: typing.Optional[EditVideoRequestSpatial] = None,
        validate: bool = False,
    ) -> VideoPydantic:
        raw_response = self.raw.video_1(
            video_id=video_id,
            description=description,
            content_rating=content_rating,
            custom_url=custom_url,
            embed=embed,
            embed_domains=embed_domains,
            embed_domains_add=embed_domains_add,
            embed_domains_delete=embed_domains_delete,
            hide_from_vimeo=hide_from_vimeo,
            license=license,
            locale=locale,
            name=name,
            password=password,
            privacy=privacy,
            review_page=review_page,
            spatial=spatial,
        )
        if validate:
            return VideoPydantic(**raw_response.body)
        return api_client.construct_model_instance(VideoPydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        video_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        content_rating: typing.Optional[EditVideoRequestContentRating] = None,
        custom_url: typing.Optional[str] = None,
        embed: typing.Optional[EditVideoRequestEmbed] = None,
        embed_domains: typing.Optional[EditVideoRequestEmbedDomains] = None,
        embed_domains_add: typing.Optional[EditVideoRequestEmbedDomainsAdd] = None,
        embed_domains_delete: typing.Optional[EditVideoRequestEmbedDomainsDelete] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        license: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[EditVideoRequestPrivacy] = None,
        review_page: typing.Optional[EditVideoRequestReviewPage] = None,
        spatial: typing.Optional[EditVideoRequestSpatial] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._video_1_mapped_args(
            video_id=video_id,
            description=description,
            content_rating=content_rating,
            custom_url=custom_url,
            embed=embed,
            embed_domains=embed_domains,
            embed_domains_add=embed_domains_add,
            embed_domains_delete=embed_domains_delete,
            hide_from_vimeo=hide_from_vimeo,
            license=license,
            locale=locale,
            name=name,
            password=password,
            privacy=privacy,
            review_page=review_page,
            spatial=spatial,
        )
        return await self._avideo_1_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        video_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        content_rating: typing.Optional[EditVideoRequestContentRating] = None,
        custom_url: typing.Optional[str] = None,
        embed: typing.Optional[EditVideoRequestEmbed] = None,
        embed_domains: typing.Optional[EditVideoRequestEmbedDomains] = None,
        embed_domains_add: typing.Optional[EditVideoRequestEmbedDomainsAdd] = None,
        embed_domains_delete: typing.Optional[EditVideoRequestEmbedDomainsDelete] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        license: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[EditVideoRequestPrivacy] = None,
        review_page: typing.Optional[EditVideoRequestReviewPage] = None,
        spatial: typing.Optional[EditVideoRequestSpatial] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._video_1_mapped_args(
            video_id=video_id,
            description=description,
            content_rating=content_rating,
            custom_url=custom_url,
            embed=embed,
            embed_domains=embed_domains,
            embed_domains_add=embed_domains_add,
            embed_domains_delete=embed_domains_delete,
            hide_from_vimeo=hide_from_vimeo,
            license=license,
            locale=locale,
            name=name,
            password=password,
            privacy=privacy,
            review_page=review_page,
            spatial=spatial,
        )
        return self._video_1_oapg(
            body=args.body,
            path_params=args.path,
        )


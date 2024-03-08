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

from vimeo_python_sdk.model.upload_video_request import UploadVideoRequest as UploadVideoRequestSchema
from vimeo_python_sdk.model.upload_video_request_content_rating import UploadVideoRequestContentRating as UploadVideoRequestContentRatingSchema
from vimeo_python_sdk.model.upload_video_request_review_page import UploadVideoRequestReviewPage as UploadVideoRequestReviewPageSchema
from vimeo_python_sdk.model.upload_video_request_upload import UploadVideoRequestUpload as UploadVideoRequestUploadSchema
from vimeo_python_sdk.model.upload_video_request_embed_domains import UploadVideoRequestEmbedDomains as UploadVideoRequestEmbedDomainsSchema
from vimeo_python_sdk.model.error import Error as ErrorSchema
from vimeo_python_sdk.model.upload_video_request_privacy import UploadVideoRequestPrivacy as UploadVideoRequestPrivacySchema
from vimeo_python_sdk.model.upload_video_request_spatial import UploadVideoRequestSpatial as UploadVideoRequestSpatialSchema
from vimeo_python_sdk.model.video import Video as VideoSchema
from vimeo_python_sdk.model.upload_video_request_embed import UploadVideoRequestEmbed as UploadVideoRequestEmbedSchema

from vimeo_python_sdk.type.video import Video
from vimeo_python_sdk.type.upload_video_request_embed import UploadVideoRequestEmbed
from vimeo_python_sdk.type.upload_video_request_spatial import UploadVideoRequestSpatial
from vimeo_python_sdk.type.upload_video_request import UploadVideoRequest
from vimeo_python_sdk.type.upload_video_request_upload import UploadVideoRequestUpload
from vimeo_python_sdk.type.error import Error
from vimeo_python_sdk.type.upload_video_request_privacy import UploadVideoRequestPrivacy
from vimeo_python_sdk.type.upload_video_request_review_page import UploadVideoRequestReviewPage
from vimeo_python_sdk.type.upload_video_request_content_rating import UploadVideoRequestContentRating
from vimeo_python_sdk.type.upload_video_request_embed_domains import UploadVideoRequestEmbedDomains

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.upload_video_request_upload import UploadVideoRequestUpload as UploadVideoRequestUploadPydantic
from vimeo_python_sdk.pydantic.error import Error as ErrorPydantic
from vimeo_python_sdk.pydantic.upload_video_request_review_page import UploadVideoRequestReviewPage as UploadVideoRequestReviewPagePydantic
from vimeo_python_sdk.pydantic.upload_video_request import UploadVideoRequest as UploadVideoRequestPydantic
from vimeo_python_sdk.pydantic.upload_video_request_content_rating import UploadVideoRequestContentRating as UploadVideoRequestContentRatingPydantic
from vimeo_python_sdk.pydantic.video import Video as VideoPydantic
from vimeo_python_sdk.pydantic.upload_video_request_embed_domains import UploadVideoRequestEmbedDomains as UploadVideoRequestEmbedDomainsPydantic
from vimeo_python_sdk.pydantic.upload_video_request_embed import UploadVideoRequestEmbed as UploadVideoRequestEmbedPydantic
from vimeo_python_sdk.pydantic.upload_video_request_spatial import UploadVideoRequestSpatial as UploadVideoRequestSpatialPydantic
from vimeo_python_sdk.pydantic.upload_video_request_privacy import UploadVideoRequestPrivacy as UploadVideoRequestPrivacyPydantic

from . import path

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
SchemaForRequestBodyApplicationVndVimeoVideojson = UploadVideoRequestSchema


request_body_upload_video_request = api_client.RequestBody(
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
SchemaFor201ResponseBodyApplicationVndVimeoVideojson = VideoSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Video


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Video


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/vnd.vimeo.video+json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationVndVimeoVideojson),
    },
)
SchemaFor400ResponseBodyApplicationVndVimeoVideojson = ErrorSchema


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
        'application/vnd.vimeo.video+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndVimeoVideojson),
    },
)
SchemaFor401ResponseBodyApplicationVndVimeoVideojson = ErrorSchema


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
        'application/vnd.vimeo.video+json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationVndVimeoVideojson),
    },
)
SchemaFor403ResponseBodyApplicationVndVimeoVideojson = ErrorSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: Error


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/vnd.vimeo.video+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationVndVimeoVideojson),
    },
)
SchemaFor500ResponseBodyApplicationVndVimeoVideojson = ErrorSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: Error


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/vnd.vimeo.video+json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationVndVimeoVideojson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/vnd.vimeo.video+json',
)


class BaseApi(api_client.Api):

    def _video_mapped_args(
        self,
        upload: UploadVideoRequestUpload,
        user_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        content_rating: typing.Optional[UploadVideoRequestContentRating] = None,
        embed: typing.Optional[UploadVideoRequestEmbed] = None,
        embed_domains: typing.Optional[UploadVideoRequestEmbedDomains] = None,
        folder_uri: typing.Optional[str] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        license: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[UploadVideoRequestPrivacy] = None,
        review_page: typing.Optional[UploadVideoRequestReviewPage] = None,
        spatial: typing.Optional[UploadVideoRequestSpatial] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if content_rating is not None:
            _body["content_rating"] = content_rating
        if embed is not None:
            _body["embed"] = embed
        if embed_domains is not None:
            _body["embed_domains"] = embed_domains
        if folder_uri is not None:
            _body["folder_uri"] = folder_uri
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
        if upload is not None:
            _body["upload"] = upload
        args.body = _body
        if user_id is not None:
            _path_params["user_id"] = user_id
        args.path = _path_params
        return args

    async def _avideo_oapg(
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
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Upload a video
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
            path_template='/users/{user_id}/videos',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_upload_video_request.serialize(body, content_type)
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


    def _video_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.video+json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Upload a video
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
            path_template='/users/{user_id}/videos',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_upload_video_request.serialize(body, content_type)
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


class VideoRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def avideo(
        self,
        upload: UploadVideoRequestUpload,
        user_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        content_rating: typing.Optional[UploadVideoRequestContentRating] = None,
        embed: typing.Optional[UploadVideoRequestEmbed] = None,
        embed_domains: typing.Optional[UploadVideoRequestEmbedDomains] = None,
        folder_uri: typing.Optional[str] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        license: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[UploadVideoRequestPrivacy] = None,
        review_page: typing.Optional[UploadVideoRequestReviewPage] = None,
        spatial: typing.Optional[UploadVideoRequestSpatial] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._video_mapped_args(
            upload=upload,
            user_id=user_id,
            description=description,
            content_rating=content_rating,
            embed=embed,
            embed_domains=embed_domains,
            folder_uri=folder_uri,
            hide_from_vimeo=hide_from_vimeo,
            license=license,
            locale=locale,
            name=name,
            password=password,
            privacy=privacy,
            review_page=review_page,
            spatial=spatial,
        )
        return await self._avideo_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def video(
        self,
        upload: UploadVideoRequestUpload,
        user_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        content_rating: typing.Optional[UploadVideoRequestContentRating] = None,
        embed: typing.Optional[UploadVideoRequestEmbed] = None,
        embed_domains: typing.Optional[UploadVideoRequestEmbedDomains] = None,
        folder_uri: typing.Optional[str] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        license: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[UploadVideoRequestPrivacy] = None,
        review_page: typing.Optional[UploadVideoRequestReviewPage] = None,
        spatial: typing.Optional[UploadVideoRequestSpatial] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._video_mapped_args(
            upload=upload,
            user_id=user_id,
            description=description,
            content_rating=content_rating,
            embed=embed,
            embed_domains=embed_domains,
            folder_uri=folder_uri,
            hide_from_vimeo=hide_from_vimeo,
            license=license,
            locale=locale,
            name=name,
            password=password,
            privacy=privacy,
            review_page=review_page,
            spatial=spatial,
        )
        return self._video_oapg(
            body=args.body,
            path_params=args.path,
        )

class Video(BaseApi):

    async def avideo(
        self,
        upload: UploadVideoRequestUpload,
        user_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        content_rating: typing.Optional[UploadVideoRequestContentRating] = None,
        embed: typing.Optional[UploadVideoRequestEmbed] = None,
        embed_domains: typing.Optional[UploadVideoRequestEmbedDomains] = None,
        folder_uri: typing.Optional[str] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        license: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[UploadVideoRequestPrivacy] = None,
        review_page: typing.Optional[UploadVideoRequestReviewPage] = None,
        spatial: typing.Optional[UploadVideoRequestSpatial] = None,
        validate: bool = False,
        **kwargs,
    ) -> VideoPydantic:
        raw_response = await self.raw.avideo(
            upload=upload,
            user_id=user_id,
            description=description,
            content_rating=content_rating,
            embed=embed,
            embed_domains=embed_domains,
            folder_uri=folder_uri,
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
    
    
    def video(
        self,
        upload: UploadVideoRequestUpload,
        user_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        content_rating: typing.Optional[UploadVideoRequestContentRating] = None,
        embed: typing.Optional[UploadVideoRequestEmbed] = None,
        embed_domains: typing.Optional[UploadVideoRequestEmbedDomains] = None,
        folder_uri: typing.Optional[str] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        license: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[UploadVideoRequestPrivacy] = None,
        review_page: typing.Optional[UploadVideoRequestReviewPage] = None,
        spatial: typing.Optional[UploadVideoRequestSpatial] = None,
        validate: bool = False,
    ) -> VideoPydantic:
        raw_response = self.raw.video(
            upload=upload,
            user_id=user_id,
            description=description,
            content_rating=content_rating,
            embed=embed,
            embed_domains=embed_domains,
            folder_uri=folder_uri,
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


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        upload: UploadVideoRequestUpload,
        user_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        content_rating: typing.Optional[UploadVideoRequestContentRating] = None,
        embed: typing.Optional[UploadVideoRequestEmbed] = None,
        embed_domains: typing.Optional[UploadVideoRequestEmbedDomains] = None,
        folder_uri: typing.Optional[str] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        license: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[UploadVideoRequestPrivacy] = None,
        review_page: typing.Optional[UploadVideoRequestReviewPage] = None,
        spatial: typing.Optional[UploadVideoRequestSpatial] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._video_mapped_args(
            upload=upload,
            user_id=user_id,
            description=description,
            content_rating=content_rating,
            embed=embed,
            embed_domains=embed_domains,
            folder_uri=folder_uri,
            hide_from_vimeo=hide_from_vimeo,
            license=license,
            locale=locale,
            name=name,
            password=password,
            privacy=privacy,
            review_page=review_page,
            spatial=spatial,
        )
        return await self._avideo_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        upload: UploadVideoRequestUpload,
        user_id: typing.Union[int, float],
        description: typing.Optional[str] = None,
        content_rating: typing.Optional[UploadVideoRequestContentRating] = None,
        embed: typing.Optional[UploadVideoRequestEmbed] = None,
        embed_domains: typing.Optional[UploadVideoRequestEmbedDomains] = None,
        folder_uri: typing.Optional[str] = None,
        hide_from_vimeo: typing.Optional[bool] = None,
        license: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[UploadVideoRequestPrivacy] = None,
        review_page: typing.Optional[UploadVideoRequestReviewPage] = None,
        spatial: typing.Optional[UploadVideoRequestSpatial] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._video_mapped_args(
            upload=upload,
            user_id=user_id,
            description=description,
            content_rating=content_rating,
            embed=embed,
            embed_domains=embed_domains,
            folder_uri=folder_uri,
            hide_from_vimeo=hide_from_vimeo,
            license=license,
            locale=locale,
            name=name,
            password=password,
            privacy=privacy,
            review_page=review_page,
            spatial=spatial,
        )
        return self._video_oapg(
            body=args.body,
            path_params=args.path,
        )


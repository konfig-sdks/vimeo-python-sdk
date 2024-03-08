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

from vimeo_python_sdk.model.users_feeds_get_user_feed_videos_response import UsersFeedsGetUserFeedVideosResponse as UsersFeedsGetUserFeedVideosResponseSchema

from vimeo_python_sdk.type.users_feeds_get_user_feed_videos_response import UsersFeedsGetUserFeedVideosResponse

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.users_feeds_get_user_feed_videos_response import UsersFeedsGetUserFeedVideosResponse as UsersFeedsGetUserFeedVideosResponsePydantic

from . import path

# Query params
OffsetSchema = schemas.StrSchema
PageSchema = schemas.NumberSchema
PerPageSchema = schemas.NumberSchema


class TypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "appears": "APPEARS",
            "category_featured": "CATEGORY_FEATURED",
            "channel": "CHANNEL",
            "facebook_feed": "FACEBOOK_FEED",
            "following": "FOLLOWING",
            "group": "GROUP",
            "likes": "LIKES",
            "ondemand_publish": "ONDEMAND_PUBLISH",
            "share": "SHARE",
            "tagged_with": "TAGGED_WITH",
            "twitter_timeline": "TWITTER_TIMELINE",
            "uploads": "UPLOADS",
        }
    
    @schemas.classproperty
    def APPEARS(cls):
        return cls("appears")
    
    @schemas.classproperty
    def CATEGORY_FEATURED(cls):
        return cls("category_featured")
    
    @schemas.classproperty
    def CHANNEL(cls):
        return cls("channel")
    
    @schemas.classproperty
    def FACEBOOK_FEED(cls):
        return cls("facebook_feed")
    
    @schemas.classproperty
    def FOLLOWING(cls):
        return cls("following")
    
    @schemas.classproperty
    def GROUP(cls):
        return cls("group")
    
    @schemas.classproperty
    def LIKES(cls):
        return cls("likes")
    
    @schemas.classproperty
    def ONDEMAND_PUBLISH(cls):
        return cls("ondemand_publish")
    
    @schemas.classproperty
    def SHARE(cls):
        return cls("share")
    
    @schemas.classproperty
    def TAGGED_WITH(cls):
        return cls("tagged_with")
    
    @schemas.classproperty
    def TWITTER_TIMELINE(cls):
        return cls("twitter_timeline")
    
    @schemas.classproperty
    def UPLOADS(cls):
        return cls("uploads")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'offset': typing.Union[OffsetSchema, str, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, float, ],
        'per_page': typing.Union[PerPageSchema, decimal.Decimal, int, float, ],
        'type': typing.Union[TypeSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_offset = api_client.QueryParameter(
    name="offset",
    style=api_client.ParameterStyle.FORM,
    schema=OffsetSchema,
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
request_query_type = api_client.QueryParameter(
    name="type",
    style=api_client.ParameterStyle.FORM,
    schema=TypeSchema,
    explode=True,
)
_auth = [
    'oauth2',
    'oauth2',
]
SchemaFor200ResponseBodyApplicationVndVimeoActivityjson = UsersFeedsGetUserFeedVideosResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: UsersFeedsGetUserFeedVideosResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UsersFeedsGetUserFeedVideosResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.activity+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoActivityjson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/vnd.vimeo.activity+json',
)


class BaseApi(api_client.Api):

    def _get_user_feed_videos_mapped_args(
        self,
        offset: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        type: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if offset is not None:
            _query_params["offset"] = offset
        if page is not None:
            _query_params["page"] = page
        if per_page is not None:
            _query_params["per_page"] = per_page
        if type is not None:
            _query_params["type"] = type
        args.query = _query_params
        return args

    async def _aget_user_feed_videos_oapg(
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
        Get all the videos in the user&#x27;s feed
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_offset,
            request_query_page,
            request_query_per_page,
            request_query_type,
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
            path_template='/me/feed',
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


    def _get_user_feed_videos_oapg(
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
        Get all the videos in the user&#x27;s feed
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_offset,
            request_query_page,
            request_query_per_page,
            request_query_type,
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
            path_template='/me/feed',
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


class GetUserFeedVideosRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_user_feed_videos(
        self,
        offset: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_feed_videos_mapped_args(
            offset=offset,
            page=page,
            per_page=per_page,
            type=type,
        )
        return await self._aget_user_feed_videos_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_user_feed_videos(
        self,
        offset: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_feed_videos_mapped_args(
            offset=offset,
            page=page,
            per_page=per_page,
            type=type,
        )
        return self._get_user_feed_videos_oapg(
            query_params=args.query,
        )

class GetUserFeedVideos(BaseApi):

    async def aget_user_feed_videos(
        self,
        offset: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        type: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> UsersFeedsGetUserFeedVideosResponsePydantic:
        raw_response = await self.raw.aget_user_feed_videos(
            offset=offset,
            page=page,
            per_page=per_page,
            type=type,
            **kwargs,
        )
        if validate:
            return RootModel[UsersFeedsGetUserFeedVideosResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(UsersFeedsGetUserFeedVideosResponsePydantic, raw_response.body)
    
    
    def get_user_feed_videos(
        self,
        offset: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        type: typing.Optional[str] = None,
        validate: bool = False,
    ) -> UsersFeedsGetUserFeedVideosResponsePydantic:
        raw_response = self.raw.get_user_feed_videos(
            offset=offset,
            page=page,
            per_page=per_page,
            type=type,
        )
        if validate:
            return RootModel[UsersFeedsGetUserFeedVideosResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(UsersFeedsGetUserFeedVideosResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        offset: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_feed_videos_mapped_args(
            offset=offset,
            page=page,
            per_page=per_page,
            type=type,
        )
        return await self._aget_user_feed_videos_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        offset: typing.Optional[str] = None,
        page: typing.Optional[typing.Union[int, float]] = None,
        per_page: typing.Optional[typing.Union[int, float]] = None,
        type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_feed_videos_mapped_args(
            offset=offset,
            page=page,
            per_page=per_page,
            type=type,
        )
        return self._get_user_feed_videos_oapg(
            query_params=args.query,
        )


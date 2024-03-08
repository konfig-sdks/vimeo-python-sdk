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

from vimeo_python_sdk.model.users_essentials_edit_vimeo_account_request_videos import UsersEssentialsEditVimeoAccountRequestVideos as UsersEssentialsEditVimeoAccountRequestVideosSchema
from vimeo_python_sdk.model.error import Error as ErrorSchema
from vimeo_python_sdk.model.users_essentials_edit_vimeo_account_request import UsersEssentialsEditVimeoAccountRequest as UsersEssentialsEditVimeoAccountRequestSchema
from vimeo_python_sdk.model.users_essentials_edit_vimeo_account_request_content_filter import UsersEssentialsEditVimeoAccountRequestContentFilter as UsersEssentialsEditVimeoAccountRequestContentFilterSchema
from vimeo_python_sdk.model.user import User as UserSchema

from vimeo_python_sdk.type.users_essentials_edit_vimeo_account_request import UsersEssentialsEditVimeoAccountRequest
from vimeo_python_sdk.type.users_essentials_edit_vimeo_account_request_content_filter import UsersEssentialsEditVimeoAccountRequestContentFilter
from vimeo_python_sdk.type.error import Error
from vimeo_python_sdk.type.user import User
from vimeo_python_sdk.type.users_essentials_edit_vimeo_account_request_videos import UsersEssentialsEditVimeoAccountRequestVideos

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.users_essentials_edit_vimeo_account_request import UsersEssentialsEditVimeoAccountRequest as UsersEssentialsEditVimeoAccountRequestPydantic
from vimeo_python_sdk.pydantic.user import User as UserPydantic
from vimeo_python_sdk.pydantic.error import Error as ErrorPydantic
from vimeo_python_sdk.pydantic.users_essentials_edit_vimeo_account_request_content_filter import UsersEssentialsEditVimeoAccountRequestContentFilter as UsersEssentialsEditVimeoAccountRequestContentFilterPydantic
from vimeo_python_sdk.pydantic.users_essentials_edit_vimeo_account_request_videos import UsersEssentialsEditVimeoAccountRequestVideos as UsersEssentialsEditVimeoAccountRequestVideosPydantic

# body param
SchemaForRequestBodyApplicationVndVimeoUserjson = UsersEssentialsEditVimeoAccountRequestSchema


request_body_users_essentials_edit_vimeo_account_request = api_client.RequestBody(
    content={
        'application/vnd.vimeo.user+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndVimeoUserjson),
    },
)
SchemaFor200ResponseBodyApplicationVndVimeoUserjson = UserSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: User


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: User


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.user+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoUserjson),
    },
)
SchemaFor400ResponseBodyApplicationVndVimeoUserjson = ErrorSchema


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
        'application/vnd.vimeo.user+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndVimeoUserjson),
    },
)
_all_accept_content_types = (
    'application/vnd.vimeo.user+json',
)


class BaseApi(api_client.Api):

    def _edit_vimeo_account_mapped_args(
        self,
        bio: typing.Optional[str] = None,
        content_filter: typing.Optional[UsersEssentialsEditVimeoAccountRequestContentFilter] = None,
        gender: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        videos: typing.Optional[UsersEssentialsEditVimeoAccountRequestVideos] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if bio is not None:
            _body["bio"] = bio
        if content_filter is not None:
            _body["content_filter"] = content_filter
        if gender is not None:
            _body["gender"] = gender
        if link is not None:
            _body["link"] = link
        if location is not None:
            _body["location"] = location
        if name is not None:
            _body["name"] = name
        if password is not None:
            _body["password"] = password
        if videos is not None:
            _body["videos"] = videos
        args.body = _body
        return args

    async def _aedit_vimeo_account_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.user+json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Edit the user
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/me',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_users_essentials_edit_vimeo_account_request.serialize(body, content_type)
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


    def _edit_vimeo_account_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.user+json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Edit the user
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/me',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_users_essentials_edit_vimeo_account_request.serialize(body, content_type)
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


class EditVimeoAccountRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aedit_vimeo_account(
        self,
        bio: typing.Optional[str] = None,
        content_filter: typing.Optional[UsersEssentialsEditVimeoAccountRequestContentFilter] = None,
        gender: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        videos: typing.Optional[UsersEssentialsEditVimeoAccountRequestVideos] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._edit_vimeo_account_mapped_args(
            bio=bio,
            content_filter=content_filter,
            gender=gender,
            link=link,
            location=location,
            name=name,
            password=password,
            videos=videos,
        )
        return await self._aedit_vimeo_account_oapg(
            body=args.body,
            **kwargs,
        )
    
    def edit_vimeo_account(
        self,
        bio: typing.Optional[str] = None,
        content_filter: typing.Optional[UsersEssentialsEditVimeoAccountRequestContentFilter] = None,
        gender: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        videos: typing.Optional[UsersEssentialsEditVimeoAccountRequestVideos] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._edit_vimeo_account_mapped_args(
            bio=bio,
            content_filter=content_filter,
            gender=gender,
            link=link,
            location=location,
            name=name,
            password=password,
            videos=videos,
        )
        return self._edit_vimeo_account_oapg(
            body=args.body,
        )

class EditVimeoAccount(BaseApi):

    async def aedit_vimeo_account(
        self,
        bio: typing.Optional[str] = None,
        content_filter: typing.Optional[UsersEssentialsEditVimeoAccountRequestContentFilter] = None,
        gender: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        videos: typing.Optional[UsersEssentialsEditVimeoAccountRequestVideos] = None,
        validate: bool = False,
        **kwargs,
    ) -> UserPydantic:
        raw_response = await self.raw.aedit_vimeo_account(
            bio=bio,
            content_filter=content_filter,
            gender=gender,
            link=link,
            location=location,
            name=name,
            password=password,
            videos=videos,
            **kwargs,
        )
        if validate:
            return UserPydantic(**raw_response.body)
        return api_client.construct_model_instance(UserPydantic, raw_response.body)
    
    
    def edit_vimeo_account(
        self,
        bio: typing.Optional[str] = None,
        content_filter: typing.Optional[UsersEssentialsEditVimeoAccountRequestContentFilter] = None,
        gender: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        videos: typing.Optional[UsersEssentialsEditVimeoAccountRequestVideos] = None,
        validate: bool = False,
    ) -> UserPydantic:
        raw_response = self.raw.edit_vimeo_account(
            bio=bio,
            content_filter=content_filter,
            gender=gender,
            link=link,
            location=location,
            name=name,
            password=password,
            videos=videos,
        )
        if validate:
            return UserPydantic(**raw_response.body)
        return api_client.construct_model_instance(UserPydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        bio: typing.Optional[str] = None,
        content_filter: typing.Optional[UsersEssentialsEditVimeoAccountRequestContentFilter] = None,
        gender: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        videos: typing.Optional[UsersEssentialsEditVimeoAccountRequestVideos] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._edit_vimeo_account_mapped_args(
            bio=bio,
            content_filter=content_filter,
            gender=gender,
            link=link,
            location=location,
            name=name,
            password=password,
            videos=videos,
        )
        return await self._aedit_vimeo_account_oapg(
            body=args.body,
            **kwargs,
        )
    
    def patch(
        self,
        bio: typing.Optional[str] = None,
        content_filter: typing.Optional[UsersEssentialsEditVimeoAccountRequestContentFilter] = None,
        gender: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        videos: typing.Optional[UsersEssentialsEditVimeoAccountRequestVideos] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._edit_vimeo_account_mapped_args(
            bio=bio,
            content_filter=content_filter,
            gender=gender,
            link=link,
            location=location,
            name=name,
            password=password,
            videos=videos,
        )
        return self._edit_vimeo_account_oapg(
            body=args.body,
        )


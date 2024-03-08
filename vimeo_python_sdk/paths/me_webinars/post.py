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

from vimeo_python_sdk.model.webinar_essentials_create_webinar_request_schedule import WebinarEssentialsCreateWebinarRequestSchedule as WebinarEssentialsCreateWebinarRequestScheduleSchema
from vimeo_python_sdk.model.webinar_essentials_create_webinar_request import WebinarEssentialsCreateWebinarRequest as WebinarEssentialsCreateWebinarRequestSchema
from vimeo_python_sdk.model.webinar import Webinar as WebinarSchema
from vimeo_python_sdk.model.error import Error as ErrorSchema
from vimeo_python_sdk.model.webinar_essentials_create_webinar_request_privacy import WebinarEssentialsCreateWebinarRequestPrivacy as WebinarEssentialsCreateWebinarRequestPrivacySchema
from vimeo_python_sdk.model.webinar_essentials_create_webinar_request_email_settings import WebinarEssentialsCreateWebinarRequestEmailSettings as WebinarEssentialsCreateWebinarRequestEmailSettingsSchema

from vimeo_python_sdk.type.webinar_essentials_create_webinar_request import WebinarEssentialsCreateWebinarRequest
from vimeo_python_sdk.type.webinar_essentials_create_webinar_request_schedule import WebinarEssentialsCreateWebinarRequestSchedule
from vimeo_python_sdk.type.error import Error
from vimeo_python_sdk.type.webinar import Webinar
from vimeo_python_sdk.type.webinar_essentials_create_webinar_request_privacy import WebinarEssentialsCreateWebinarRequestPrivacy
from vimeo_python_sdk.type.webinar_essentials_create_webinar_request_email_settings import WebinarEssentialsCreateWebinarRequestEmailSettings

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.error import Error as ErrorPydantic
from vimeo_python_sdk.pydantic.webinar_essentials_create_webinar_request_privacy import WebinarEssentialsCreateWebinarRequestPrivacy as WebinarEssentialsCreateWebinarRequestPrivacyPydantic
from vimeo_python_sdk.pydantic.webinar_essentials_create_webinar_request_email_settings import WebinarEssentialsCreateWebinarRequestEmailSettings as WebinarEssentialsCreateWebinarRequestEmailSettingsPydantic
from vimeo_python_sdk.pydantic.webinar import Webinar as WebinarPydantic
from vimeo_python_sdk.pydantic.webinar_essentials_create_webinar_request_schedule import WebinarEssentialsCreateWebinarRequestSchedule as WebinarEssentialsCreateWebinarRequestSchedulePydantic
from vimeo_python_sdk.pydantic.webinar_essentials_create_webinar_request import WebinarEssentialsCreateWebinarRequest as WebinarEssentialsCreateWebinarRequestPydantic

from . import path

# body param
SchemaForRequestBodyApplicationVndVimeoWebinarsjson = WebinarEssentialsCreateWebinarRequestSchema


request_body_webinar_essentials_create_webinar_request = api_client.RequestBody(
    content={
        'application/vnd.vimeo.webinars+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndVimeoWebinarsjson),
    },
    required=True,
)
_auth = [
    'oauth2',
    'oauth2',
]
SchemaFor200ResponseBodyApplicationVndVimeoWebinarsjson = WebinarSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Webinar


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Webinar


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.webinars+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoWebinarsjson),
    },
)
SchemaFor400ResponseBodyApplicationVndVimeoWebinarsjson = ErrorSchema


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
        'application/vnd.vimeo.webinars+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndVimeoWebinarsjson),
    },
)
SchemaFor403ResponseBodyApplicationVndVimeoWebinarsjson = ErrorSchema


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
        'application/vnd.vimeo.webinars+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationVndVimeoWebinarsjson),
    },
)
SchemaFor429ResponseBodyApplicationVndVimeoWebinarsjson = ErrorSchema


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: Error


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
    content={
        'application/vnd.vimeo.webinars+json': api_client.MediaType(
            schema=SchemaFor429ResponseBodyApplicationVndVimeoWebinarsjson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '403': _response_for_403,
    '429': _response_for_429,
}
_all_accept_content_types = (
    'application/vnd.vimeo.webinars+json',
)


class BaseApi(api_client.Api):

    def _create_webinar_mapped_args(
        self,
        title: str,
        description: typing.Optional[str] = None,
        email_settings: typing.Optional[WebinarEssentialsCreateWebinarRequestEmailSettings] = None,
        folder_uri: typing.Optional[typing.Union[int, float]] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[WebinarEssentialsCreateWebinarRequestPrivacy] = None,
        schedule: typing.Optional[WebinarEssentialsCreateWebinarRequestSchedule] = None,
        time_zone: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if title is not None:
            _body["title"] = title
        if description is not None:
            _body["description"] = description
        if email_settings is not None:
            _body["email_settings"] = email_settings
        if folder_uri is not None:
            _body["folder_uri"] = folder_uri
        if password is not None:
            _body["password"] = password
        if privacy is not None:
            _body["privacy"] = privacy
        if schedule is not None:
            _body["schedule"] = schedule
        if time_zone is not None:
            _body["time_zone"] = time_zone
        args.body = _body
        return args

    async def _acreate_webinar_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.webinars+json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a webinar
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
            path_template='/me/webinars',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_webinar_essentials_create_webinar_request.serialize(body, content_type)
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


    def _create_webinar_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.webinars+json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a webinar
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
            path_template='/me/webinars',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_webinar_essentials_create_webinar_request.serialize(body, content_type)
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


class CreateWebinarRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_webinar(
        self,
        title: str,
        description: typing.Optional[str] = None,
        email_settings: typing.Optional[WebinarEssentialsCreateWebinarRequestEmailSettings] = None,
        folder_uri: typing.Optional[typing.Union[int, float]] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[WebinarEssentialsCreateWebinarRequestPrivacy] = None,
        schedule: typing.Optional[WebinarEssentialsCreateWebinarRequestSchedule] = None,
        time_zone: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_webinar_mapped_args(
            title=title,
            description=description,
            email_settings=email_settings,
            folder_uri=folder_uri,
            password=password,
            privacy=privacy,
            schedule=schedule,
            time_zone=time_zone,
        )
        return await self._acreate_webinar_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_webinar(
        self,
        title: str,
        description: typing.Optional[str] = None,
        email_settings: typing.Optional[WebinarEssentialsCreateWebinarRequestEmailSettings] = None,
        folder_uri: typing.Optional[typing.Union[int, float]] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[WebinarEssentialsCreateWebinarRequestPrivacy] = None,
        schedule: typing.Optional[WebinarEssentialsCreateWebinarRequestSchedule] = None,
        time_zone: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_webinar_mapped_args(
            title=title,
            description=description,
            email_settings=email_settings,
            folder_uri=folder_uri,
            password=password,
            privacy=privacy,
            schedule=schedule,
            time_zone=time_zone,
        )
        return self._create_webinar_oapg(
            body=args.body,
        )

class CreateWebinar(BaseApi):

    async def acreate_webinar(
        self,
        title: str,
        description: typing.Optional[str] = None,
        email_settings: typing.Optional[WebinarEssentialsCreateWebinarRequestEmailSettings] = None,
        folder_uri: typing.Optional[typing.Union[int, float]] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[WebinarEssentialsCreateWebinarRequestPrivacy] = None,
        schedule: typing.Optional[WebinarEssentialsCreateWebinarRequestSchedule] = None,
        time_zone: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> WebinarPydantic:
        raw_response = await self.raw.acreate_webinar(
            title=title,
            description=description,
            email_settings=email_settings,
            folder_uri=folder_uri,
            password=password,
            privacy=privacy,
            schedule=schedule,
            time_zone=time_zone,
            **kwargs,
        )
        if validate:
            return WebinarPydantic(**raw_response.body)
        return api_client.construct_model_instance(WebinarPydantic, raw_response.body)
    
    
    def create_webinar(
        self,
        title: str,
        description: typing.Optional[str] = None,
        email_settings: typing.Optional[WebinarEssentialsCreateWebinarRequestEmailSettings] = None,
        folder_uri: typing.Optional[typing.Union[int, float]] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[WebinarEssentialsCreateWebinarRequestPrivacy] = None,
        schedule: typing.Optional[WebinarEssentialsCreateWebinarRequestSchedule] = None,
        time_zone: typing.Optional[str] = None,
        validate: bool = False,
    ) -> WebinarPydantic:
        raw_response = self.raw.create_webinar(
            title=title,
            description=description,
            email_settings=email_settings,
            folder_uri=folder_uri,
            password=password,
            privacy=privacy,
            schedule=schedule,
            time_zone=time_zone,
        )
        if validate:
            return WebinarPydantic(**raw_response.body)
        return api_client.construct_model_instance(WebinarPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        title: str,
        description: typing.Optional[str] = None,
        email_settings: typing.Optional[WebinarEssentialsCreateWebinarRequestEmailSettings] = None,
        folder_uri: typing.Optional[typing.Union[int, float]] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[WebinarEssentialsCreateWebinarRequestPrivacy] = None,
        schedule: typing.Optional[WebinarEssentialsCreateWebinarRequestSchedule] = None,
        time_zone: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_webinar_mapped_args(
            title=title,
            description=description,
            email_settings=email_settings,
            folder_uri=folder_uri,
            password=password,
            privacy=privacy,
            schedule=schedule,
            time_zone=time_zone,
        )
        return await self._acreate_webinar_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        title: str,
        description: typing.Optional[str] = None,
        email_settings: typing.Optional[WebinarEssentialsCreateWebinarRequestEmailSettings] = None,
        folder_uri: typing.Optional[typing.Union[int, float]] = None,
        password: typing.Optional[str] = None,
        privacy: typing.Optional[WebinarEssentialsCreateWebinarRequestPrivacy] = None,
        schedule: typing.Optional[WebinarEssentialsCreateWebinarRequestSchedule] = None,
        time_zone: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_webinar_mapped_args(
            title=title,
            description=description,
            email_settings=email_settings,
            folder_uri=folder_uri,
            password=password,
            privacy=privacy,
            schedule=schedule,
            time_zone=time_zone,
        )
        return self._create_webinar_oapg(
            body=args.body,
        )


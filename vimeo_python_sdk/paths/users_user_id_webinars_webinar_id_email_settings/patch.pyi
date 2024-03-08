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

from vimeo_python_sdk.model.error import Error as ErrorSchema
from vimeo_python_sdk.model.webinar_emails_customize_preferences_request1_email_preferences import WebinarEmailsCustomizePreferencesRequest1EmailPreferences as WebinarEmailsCustomizePreferencesRequest1EmailPreferencesSchema
from vimeo_python_sdk.model.webinar_emails_customize_preferences_request1 import WebinarEmailsCustomizePreferencesRequest1 as WebinarEmailsCustomizePreferencesRequest1Schema
from vimeo_python_sdk.model.webinar_email_settings import WebinarEmailSettings as WebinarEmailSettingsSchema

from vimeo_python_sdk.type.webinar_emails_customize_preferences_request1 import WebinarEmailsCustomizePreferencesRequest1
from vimeo_python_sdk.type.error import Error
from vimeo_python_sdk.type.webinar_email_settings import WebinarEmailSettings
from vimeo_python_sdk.type.webinar_emails_customize_preferences_request1_email_preferences import WebinarEmailsCustomizePreferencesRequest1EmailPreferences

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.error import Error as ErrorPydantic
from vimeo_python_sdk.pydantic.webinar_emails_customize_preferences_request1_email_preferences import WebinarEmailsCustomizePreferencesRequest1EmailPreferences as WebinarEmailsCustomizePreferencesRequest1EmailPreferencesPydantic
from vimeo_python_sdk.pydantic.webinar_emails_customize_preferences_request1 import WebinarEmailsCustomizePreferencesRequest1 as WebinarEmailsCustomizePreferencesRequest1Pydantic
from vimeo_python_sdk.pydantic.webinar_email_settings import WebinarEmailSettings as WebinarEmailSettingsPydantic

# Path params
UserIdSchema = schemas.NumberSchema
WebinarIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'user_id': typing.Union[UserIdSchema, decimal.Decimal, int, float, ],
        'webinar_id': typing.Union[WebinarIdSchema, str, ],
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
request_path_webinar_id = api_client.PathParameter(
    name="webinar_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=WebinarIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationVndVimeoWebinarEmailSettingsjson = WebinarEmailsCustomizePreferencesRequest1Schema


request_body_webinar_emails_customize_preferences_request1 = api_client.RequestBody(
    content={
        'application/vnd.vimeo.webinar.email.settings+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndVimeoWebinarEmailSettingsjson),
    },
)
SchemaFor200ResponseBodyApplicationVndVimeoWebinarEmailSettingsjson = WebinarEmailSettingsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: WebinarEmailSettings


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: WebinarEmailSettings


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.vimeo.webinar.email.settings+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndVimeoWebinarEmailSettingsjson),
    },
)
SchemaFor400ResponseBodyApplicationVndVimeoWebinarEmailSettingsjson = ErrorSchema


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
        'application/vnd.vimeo.webinar.email.settings+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndVimeoWebinarEmailSettingsjson),
    },
)
SchemaFor404ResponseBodyApplicationVndVimeoWebinarEmailSettingsjson = ErrorSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: Error


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/vnd.vimeo.webinar.email.settings+json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationVndVimeoWebinarEmailSettingsjson),
    },
)
_all_accept_content_types = (
    'application/vnd.vimeo.webinar.email.settings+json',
)


class BaseApi(api_client.Api):

    def _customize_preferences_0_mapped_args(
        self,
        user_id: typing.Union[int, float],
        webinar_id: str,
        accent_color: typing.Optional[str] = None,
        custom_link: typing.Optional[str] = None,
        email_event_reminder_24_hrs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_post_event_thank_you: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_preferences: typing.Optional[WebinarEmailsCustomizePreferencesRequest1EmailPreferences] = None,
        email_registration_confirmation: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        _from: typing.Optional[str] = None,
        logo_uri: typing.Optional[str] = None,
        reply_email: typing.Optional[str] = None,
        sender_address: typing.Optional[str] = None,
        sender_policy_url: typing.Optional[str] = None,
        use_custom_link: typing.Optional[bool] = None,
        use_reply_email: typing.Optional[bool] = None,
        use_sender_address: typing.Optional[bool] = None,
        use_sender_policy_url: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if accent_color is not None:
            _body["accent_color"] = accent_color
        if custom_link is not None:
            _body["custom_link"] = custom_link
        if email_event_reminder_24_hrs is not None:
            _body["email_event_reminder_24_hrs"] = email_event_reminder_24_hrs
        if email_post_event_thank_you is not None:
            _body["email_post_event_thank_you"] = email_post_event_thank_you
        if email_preferences is not None:
            _body["email_preferences"] = email_preferences
        if email_registration_confirmation is not None:
            _body["email_registration_confirmation"] = email_registration_confirmation
        if _from is not None:
            _body["from"] = _from
        if logo_uri is not None:
            _body["logo_uri"] = logo_uri
        if reply_email is not None:
            _body["reply_email"] = reply_email
        if sender_address is not None:
            _body["sender_address"] = sender_address
        if sender_policy_url is not None:
            _body["sender_policy_url"] = sender_policy_url
        if use_custom_link is not None:
            _body["use_custom_link"] = use_custom_link
        if use_reply_email is not None:
            _body["use_reply_email"] = use_reply_email
        if use_sender_address is not None:
            _body["use_sender_address"] = use_sender_address
        if use_sender_policy_url is not None:
            _body["use_sender_policy_url"] = use_sender_policy_url
        args.body = _body
        if user_id is not None:
            _path_params["user_id"] = user_id
        if webinar_id is not None:
            _path_params["webinar_id"] = webinar_id
        args.path = _path_params
        return args

    async def _acustomize_preferences_0_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.webinar.email.settings+json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Customize the email preferences of a webinar
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_id,
            request_path_webinar_id,
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
            path_template='/users/{user_id}/webinars/{webinar_id}/email_settings',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_webinar_emails_customize_preferences_request1.serialize(body, content_type)
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


    def _customize_preferences_0_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.vimeo.webinar.email.settings+json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Customize the email preferences of a webinar
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_id,
            request_path_webinar_id,
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
            path_template='/users/{user_id}/webinars/{webinar_id}/email_settings',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_webinar_emails_customize_preferences_request1.serialize(body, content_type)
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


class CustomizePreferences0Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @api_client.DeprecationWarningOnce(prefix="webinar\emails")
    async def acustomize_preferences_0(
        self,
        user_id: typing.Union[int, float],
        webinar_id: str,
        accent_color: typing.Optional[str] = None,
        custom_link: typing.Optional[str] = None,
        email_event_reminder_24_hrs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_post_event_thank_you: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_preferences: typing.Optional[WebinarEmailsCustomizePreferencesRequest1EmailPreferences] = None,
        email_registration_confirmation: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        _from: typing.Optional[str] = None,
        logo_uri: typing.Optional[str] = None,
        reply_email: typing.Optional[str] = None,
        sender_address: typing.Optional[str] = None,
        sender_policy_url: typing.Optional[str] = None,
        use_custom_link: typing.Optional[bool] = None,
        use_reply_email: typing.Optional[bool] = None,
        use_sender_address: typing.Optional[bool] = None,
        use_sender_policy_url: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._customize_preferences_0_mapped_args(
            user_id=user_id,
            webinar_id=webinar_id,
            accent_color=accent_color,
            custom_link=custom_link,
            email_event_reminder_24_hrs=email_event_reminder_24_hrs,
            email_post_event_thank_you=email_post_event_thank_you,
            email_preferences=email_preferences,
            email_registration_confirmation=email_registration_confirmation,
            _from=_from,
            logo_uri=logo_uri,
            reply_email=reply_email,
            sender_address=sender_address,
            sender_policy_url=sender_policy_url,
            use_custom_link=use_custom_link,
            use_reply_email=use_reply_email,
            use_sender_address=use_sender_address,
            use_sender_policy_url=use_sender_policy_url,
        )
        return await self._acustomize_preferences_0_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="webinar\emails")
    def customize_preferences_0(
        self,
        user_id: typing.Union[int, float],
        webinar_id: str,
        accent_color: typing.Optional[str] = None,
        custom_link: typing.Optional[str] = None,
        email_event_reminder_24_hrs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_post_event_thank_you: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_preferences: typing.Optional[WebinarEmailsCustomizePreferencesRequest1EmailPreferences] = None,
        email_registration_confirmation: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        _from: typing.Optional[str] = None,
        logo_uri: typing.Optional[str] = None,
        reply_email: typing.Optional[str] = None,
        sender_address: typing.Optional[str] = None,
        sender_policy_url: typing.Optional[str] = None,
        use_custom_link: typing.Optional[bool] = None,
        use_reply_email: typing.Optional[bool] = None,
        use_sender_address: typing.Optional[bool] = None,
        use_sender_policy_url: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._customize_preferences_0_mapped_args(
            user_id=user_id,
            webinar_id=webinar_id,
            accent_color=accent_color,
            custom_link=custom_link,
            email_event_reminder_24_hrs=email_event_reminder_24_hrs,
            email_post_event_thank_you=email_post_event_thank_you,
            email_preferences=email_preferences,
            email_registration_confirmation=email_registration_confirmation,
            _from=_from,
            logo_uri=logo_uri,
            reply_email=reply_email,
            sender_address=sender_address,
            sender_policy_url=sender_policy_url,
            use_custom_link=use_custom_link,
            use_reply_email=use_reply_email,
            use_sender_address=use_sender_address,
            use_sender_policy_url=use_sender_policy_url,
        )
        return self._customize_preferences_0_oapg(
            body=args.body,
            path_params=args.path,
        )

class CustomizePreferences0(BaseApi):

    @api_client.DeprecationWarningOnce(prefix="webinar\emails")
    async def acustomize_preferences_0(
        self,
        user_id: typing.Union[int, float],
        webinar_id: str,
        accent_color: typing.Optional[str] = None,
        custom_link: typing.Optional[str] = None,
        email_event_reminder_24_hrs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_post_event_thank_you: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_preferences: typing.Optional[WebinarEmailsCustomizePreferencesRequest1EmailPreferences] = None,
        email_registration_confirmation: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        _from: typing.Optional[str] = None,
        logo_uri: typing.Optional[str] = None,
        reply_email: typing.Optional[str] = None,
        sender_address: typing.Optional[str] = None,
        sender_policy_url: typing.Optional[str] = None,
        use_custom_link: typing.Optional[bool] = None,
        use_reply_email: typing.Optional[bool] = None,
        use_sender_address: typing.Optional[bool] = None,
        use_sender_policy_url: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> WebinarEmailSettingsPydantic:
        raw_response = await self.raw.acustomize_preferences_0(
            user_id=user_id,
            webinar_id=webinar_id,
            accent_color=accent_color,
            custom_link=custom_link,
            email_event_reminder_24_hrs=email_event_reminder_24_hrs,
            email_post_event_thank_you=email_post_event_thank_you,
            email_preferences=email_preferences,
            email_registration_confirmation=email_registration_confirmation,
            _from=_from,
            logo_uri=logo_uri,
            reply_email=reply_email,
            sender_address=sender_address,
            sender_policy_url=sender_policy_url,
            use_custom_link=use_custom_link,
            use_reply_email=use_reply_email,
            use_sender_address=use_sender_address,
            use_sender_policy_url=use_sender_policy_url,
            **kwargs,
        )
        if validate:
            return WebinarEmailSettingsPydantic(**raw_response.body)
        return api_client.construct_model_instance(WebinarEmailSettingsPydantic, raw_response.body)
    
    
    @api_client.DeprecationWarningOnce(prefix="webinar\emails")
    def customize_preferences_0(
        self,
        user_id: typing.Union[int, float],
        webinar_id: str,
        accent_color: typing.Optional[str] = None,
        custom_link: typing.Optional[str] = None,
        email_event_reminder_24_hrs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_post_event_thank_you: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_preferences: typing.Optional[WebinarEmailsCustomizePreferencesRequest1EmailPreferences] = None,
        email_registration_confirmation: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        _from: typing.Optional[str] = None,
        logo_uri: typing.Optional[str] = None,
        reply_email: typing.Optional[str] = None,
        sender_address: typing.Optional[str] = None,
        sender_policy_url: typing.Optional[str] = None,
        use_custom_link: typing.Optional[bool] = None,
        use_reply_email: typing.Optional[bool] = None,
        use_sender_address: typing.Optional[bool] = None,
        use_sender_policy_url: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> WebinarEmailSettingsPydantic:
        raw_response = self.raw.customize_preferences_0(
            user_id=user_id,
            webinar_id=webinar_id,
            accent_color=accent_color,
            custom_link=custom_link,
            email_event_reminder_24_hrs=email_event_reminder_24_hrs,
            email_post_event_thank_you=email_post_event_thank_you,
            email_preferences=email_preferences,
            email_registration_confirmation=email_registration_confirmation,
            _from=_from,
            logo_uri=logo_uri,
            reply_email=reply_email,
            sender_address=sender_address,
            sender_policy_url=sender_policy_url,
            use_custom_link=use_custom_link,
            use_reply_email=use_reply_email,
            use_sender_address=use_sender_address,
            use_sender_policy_url=use_sender_policy_url,
        )
        if validate:
            return WebinarEmailSettingsPydantic(**raw_response.body)
        return api_client.construct_model_instance(WebinarEmailSettingsPydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @api_client.DeprecationWarningOnce(prefix="webinar\emails")
    async def apatch(
        self,
        user_id: typing.Union[int, float],
        webinar_id: str,
        accent_color: typing.Optional[str] = None,
        custom_link: typing.Optional[str] = None,
        email_event_reminder_24_hrs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_post_event_thank_you: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_preferences: typing.Optional[WebinarEmailsCustomizePreferencesRequest1EmailPreferences] = None,
        email_registration_confirmation: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        _from: typing.Optional[str] = None,
        logo_uri: typing.Optional[str] = None,
        reply_email: typing.Optional[str] = None,
        sender_address: typing.Optional[str] = None,
        sender_policy_url: typing.Optional[str] = None,
        use_custom_link: typing.Optional[bool] = None,
        use_reply_email: typing.Optional[bool] = None,
        use_sender_address: typing.Optional[bool] = None,
        use_sender_policy_url: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._customize_preferences_0_mapped_args(
            user_id=user_id,
            webinar_id=webinar_id,
            accent_color=accent_color,
            custom_link=custom_link,
            email_event_reminder_24_hrs=email_event_reminder_24_hrs,
            email_post_event_thank_you=email_post_event_thank_you,
            email_preferences=email_preferences,
            email_registration_confirmation=email_registration_confirmation,
            _from=_from,
            logo_uri=logo_uri,
            reply_email=reply_email,
            sender_address=sender_address,
            sender_policy_url=sender_policy_url,
            use_custom_link=use_custom_link,
            use_reply_email=use_reply_email,
            use_sender_address=use_sender_address,
            use_sender_policy_url=use_sender_policy_url,
        )
        return await self._acustomize_preferences_0_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="webinar\emails")
    def patch(
        self,
        user_id: typing.Union[int, float],
        webinar_id: str,
        accent_color: typing.Optional[str] = None,
        custom_link: typing.Optional[str] = None,
        email_event_reminder_24_hrs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_post_event_thank_you: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_preferences: typing.Optional[WebinarEmailsCustomizePreferencesRequest1EmailPreferences] = None,
        email_registration_confirmation: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        _from: typing.Optional[str] = None,
        logo_uri: typing.Optional[str] = None,
        reply_email: typing.Optional[str] = None,
        sender_address: typing.Optional[str] = None,
        sender_policy_url: typing.Optional[str] = None,
        use_custom_link: typing.Optional[bool] = None,
        use_reply_email: typing.Optional[bool] = None,
        use_sender_address: typing.Optional[bool] = None,
        use_sender_policy_url: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._customize_preferences_0_mapped_args(
            user_id=user_id,
            webinar_id=webinar_id,
            accent_color=accent_color,
            custom_link=custom_link,
            email_event_reminder_24_hrs=email_event_reminder_24_hrs,
            email_post_event_thank_you=email_post_event_thank_you,
            email_preferences=email_preferences,
            email_registration_confirmation=email_registration_confirmation,
            _from=_from,
            logo_uri=logo_uri,
            reply_email=reply_email,
            sender_address=sender_address,
            sender_policy_url=sender_policy_url,
            use_custom_link=use_custom_link,
            use_reply_email=use_reply_email,
            use_sender_address=use_sender_address,
            use_sender_policy_url=use_sender_policy_url,
        )
        return self._customize_preferences_0_oapg(
            body=args.body,
            path_params=args.path,
        )


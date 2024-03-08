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

from vimeo_python_sdk.model.create_vod_request_rent import CreateVodRequestRent as CreateVodRequestRentSchema
from vimeo_python_sdk.model.on_demand_page import OnDemandPage as OnDemandPageSchema
from vimeo_python_sdk.model.create_vod_request_episodes import CreateVodRequestEpisodes as CreateVodRequestEpisodesSchema
from vimeo_python_sdk.model.create_vod_request import CreateVodRequest as CreateVodRequestSchema
from vimeo_python_sdk.model.create_vod_request_buy import CreateVodRequestBuy as CreateVodRequestBuySchema
from vimeo_python_sdk.model.create_vod_request_subscription import CreateVodRequestSubscription as CreateVodRequestSubscriptionSchema

from vimeo_python_sdk.type.create_vod_request_buy import CreateVodRequestBuy
from vimeo_python_sdk.type.create_vod_request_episodes import CreateVodRequestEpisodes
from vimeo_python_sdk.type.create_vod_request_subscription import CreateVodRequestSubscription
from vimeo_python_sdk.type.create_vod_request_rent import CreateVodRequestRent
from vimeo_python_sdk.type.on_demand_page import OnDemandPage
from vimeo_python_sdk.type.create_vod_request import CreateVodRequest

from ...api_client import Dictionary
from vimeo_python_sdk.pydantic.create_vod_request_subscription import CreateVodRequestSubscription as CreateVodRequestSubscriptionPydantic
from vimeo_python_sdk.pydantic.on_demand_page import OnDemandPage as OnDemandPagePydantic
from vimeo_python_sdk.pydantic.create_vod_request_episodes import CreateVodRequestEpisodes as CreateVodRequestEpisodesPydantic
from vimeo_python_sdk.pydantic.create_vod_request_rent import CreateVodRequestRent as CreateVodRequestRentPydantic
from vimeo_python_sdk.pydantic.create_vod_request import CreateVodRequest as CreateVodRequestPydantic
from vimeo_python_sdk.pydantic.create_vod_request_buy import CreateVodRequestBuy as CreateVodRequestBuyPydantic

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
SchemaForRequestBodyApplicationJson = CreateVodRequestSchema


request_body_create_vod_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'oauth2',
    'oauth2',
]
SchemaFor201ResponseBodyApplicationJson = OnDemandPageSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: OnDemandPage


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: OnDemandPage


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _vod_1_mapped_args(
        self,
        description: str,
        content_rating: str,
        name: str,
        type: str,
        user_id: typing.Union[int, float],
        accepted_currencies: typing.Optional[str] = None,
        buy: typing.Optional[CreateVodRequestBuy] = None,
        domain_link: typing.Optional[str] = None,
        episodes: typing.Optional[CreateVodRequestEpisodes] = None,
        link: typing.Optional[str] = None,
        rent: typing.Optional[CreateVodRequestRent] = None,
        subscription: typing.Optional[CreateVodRequestSubscription] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if accepted_currencies is not None:
            _body["accepted_currencies"] = accepted_currencies
        if buy is not None:
            _body["buy"] = buy
        if content_rating is not None:
            _body["content_rating"] = content_rating
        if domain_link is not None:
            _body["domain_link"] = domain_link
        if episodes is not None:
            _body["episodes"] = episodes
        if link is not None:
            _body["link"] = link
        if name is not None:
            _body["name"] = name
        if rent is not None:
            _body["rent"] = rent
        if subscription is not None:
            _body["subscription"] = subscription
        if type is not None:
            _body["type"] = type
        args.body = _body
        if user_id is not None:
            _path_params["user_id"] = user_id
        args.path = _path_params
        return args

    async def _avod_1_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create an On Demand page
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
            path_template='/users/{user_id}/ondemand/pages',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_vod_request.serialize(body, content_type)
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


    def _vod_1_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create an On Demand page
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
            path_template='/users/{user_id}/ondemand/pages',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_vod_request.serialize(body, content_type)
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


class Vod1Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def avod_1(
        self,
        description: str,
        content_rating: str,
        name: str,
        type: str,
        user_id: typing.Union[int, float],
        accepted_currencies: typing.Optional[str] = None,
        buy: typing.Optional[CreateVodRequestBuy] = None,
        domain_link: typing.Optional[str] = None,
        episodes: typing.Optional[CreateVodRequestEpisodes] = None,
        link: typing.Optional[str] = None,
        rent: typing.Optional[CreateVodRequestRent] = None,
        subscription: typing.Optional[CreateVodRequestSubscription] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._vod_1_mapped_args(
            description=description,
            content_rating=content_rating,
            name=name,
            type=type,
            user_id=user_id,
            accepted_currencies=accepted_currencies,
            buy=buy,
            domain_link=domain_link,
            episodes=episodes,
            link=link,
            rent=rent,
            subscription=subscription,
        )
        return await self._avod_1_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def vod_1(
        self,
        description: str,
        content_rating: str,
        name: str,
        type: str,
        user_id: typing.Union[int, float],
        accepted_currencies: typing.Optional[str] = None,
        buy: typing.Optional[CreateVodRequestBuy] = None,
        domain_link: typing.Optional[str] = None,
        episodes: typing.Optional[CreateVodRequestEpisodes] = None,
        link: typing.Optional[str] = None,
        rent: typing.Optional[CreateVodRequestRent] = None,
        subscription: typing.Optional[CreateVodRequestSubscription] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._vod_1_mapped_args(
            description=description,
            content_rating=content_rating,
            name=name,
            type=type,
            user_id=user_id,
            accepted_currencies=accepted_currencies,
            buy=buy,
            domain_link=domain_link,
            episodes=episodes,
            link=link,
            rent=rent,
            subscription=subscription,
        )
        return self._vod_1_oapg(
            body=args.body,
            path_params=args.path,
        )

class Vod1(BaseApi):

    async def avod_1(
        self,
        description: str,
        content_rating: str,
        name: str,
        type: str,
        user_id: typing.Union[int, float],
        accepted_currencies: typing.Optional[str] = None,
        buy: typing.Optional[CreateVodRequestBuy] = None,
        domain_link: typing.Optional[str] = None,
        episodes: typing.Optional[CreateVodRequestEpisodes] = None,
        link: typing.Optional[str] = None,
        rent: typing.Optional[CreateVodRequestRent] = None,
        subscription: typing.Optional[CreateVodRequestSubscription] = None,
        validate: bool = False,
        **kwargs,
    ) -> OnDemandPagePydantic:
        raw_response = await self.raw.avod_1(
            description=description,
            content_rating=content_rating,
            name=name,
            type=type,
            user_id=user_id,
            accepted_currencies=accepted_currencies,
            buy=buy,
            domain_link=domain_link,
            episodes=episodes,
            link=link,
            rent=rent,
            subscription=subscription,
            **kwargs,
        )
        if validate:
            return OnDemandPagePydantic(**raw_response.body)
        return api_client.construct_model_instance(OnDemandPagePydantic, raw_response.body)
    
    
    def vod_1(
        self,
        description: str,
        content_rating: str,
        name: str,
        type: str,
        user_id: typing.Union[int, float],
        accepted_currencies: typing.Optional[str] = None,
        buy: typing.Optional[CreateVodRequestBuy] = None,
        domain_link: typing.Optional[str] = None,
        episodes: typing.Optional[CreateVodRequestEpisodes] = None,
        link: typing.Optional[str] = None,
        rent: typing.Optional[CreateVodRequestRent] = None,
        subscription: typing.Optional[CreateVodRequestSubscription] = None,
        validate: bool = False,
    ) -> OnDemandPagePydantic:
        raw_response = self.raw.vod_1(
            description=description,
            content_rating=content_rating,
            name=name,
            type=type,
            user_id=user_id,
            accepted_currencies=accepted_currencies,
            buy=buy,
            domain_link=domain_link,
            episodes=episodes,
            link=link,
            rent=rent,
            subscription=subscription,
        )
        if validate:
            return OnDemandPagePydantic(**raw_response.body)
        return api_client.construct_model_instance(OnDemandPagePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        description: str,
        content_rating: str,
        name: str,
        type: str,
        user_id: typing.Union[int, float],
        accepted_currencies: typing.Optional[str] = None,
        buy: typing.Optional[CreateVodRequestBuy] = None,
        domain_link: typing.Optional[str] = None,
        episodes: typing.Optional[CreateVodRequestEpisodes] = None,
        link: typing.Optional[str] = None,
        rent: typing.Optional[CreateVodRequestRent] = None,
        subscription: typing.Optional[CreateVodRequestSubscription] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._vod_1_mapped_args(
            description=description,
            content_rating=content_rating,
            name=name,
            type=type,
            user_id=user_id,
            accepted_currencies=accepted_currencies,
            buy=buy,
            domain_link=domain_link,
            episodes=episodes,
            link=link,
            rent=rent,
            subscription=subscription,
        )
        return await self._avod_1_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        description: str,
        content_rating: str,
        name: str,
        type: str,
        user_id: typing.Union[int, float],
        accepted_currencies: typing.Optional[str] = None,
        buy: typing.Optional[CreateVodRequestBuy] = None,
        domain_link: typing.Optional[str] = None,
        episodes: typing.Optional[CreateVodRequestEpisodes] = None,
        link: typing.Optional[str] = None,
        rent: typing.Optional[CreateVodRequestRent] = None,
        subscription: typing.Optional[CreateVodRequestSubscription] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._vod_1_mapped_args(
            description=description,
            content_rating=content_rating,
            name=name,
            type=type,
            user_id=user_id,
            accepted_currencies=accepted_currencies,
            buy=buy,
            domain_link=domain_link,
            episodes=episodes,
            link=link,
            rent=rent,
            subscription=subscription,
        )
        return self._vod_1_oapg(
            body=args.body,
            path_params=args.path,
        )


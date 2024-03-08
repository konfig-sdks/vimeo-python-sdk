# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

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


class LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2InteractionToolsSettings(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The settings for the interaction tools.
    """


    class MetaOapg:
        
        class properties:
            is_anonymous_questions_disabled = schemas.BoolSchema
            is_qna_moderated = schemas.BoolSchema
            __annotations__ = {
                "is_anonymous_questions_disabled": is_anonymous_questions_disabled,
                "is_qna_moderated": is_qna_moderated,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_anonymous_questions_disabled"]) -> MetaOapg.properties.is_anonymous_questions_disabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_qna_moderated"]) -> MetaOapg.properties.is_qna_moderated: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_anonymous_questions_disabled", "is_qna_moderated", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_anonymous_questions_disabled"]) -> typing.Union[MetaOapg.properties.is_anonymous_questions_disabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_qna_moderated"]) -> typing.Union[MetaOapg.properties.is_qna_moderated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_anonymous_questions_disabled", "is_qna_moderated", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        is_anonymous_questions_disabled: typing.Union[MetaOapg.properties.is_anonymous_questions_disabled, bool, schemas.Unset] = schemas.unset,
        is_qna_moderated: typing.Union[MetaOapg.properties.is_qna_moderated, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2InteractionToolsSettings':
        return super().__new__(
            cls,
            *args,
            is_anonymous_questions_disabled=is_anonymous_questions_disabled,
            is_qna_moderated=is_qna_moderated,
            _configuration=_configuration,
            **kwargs,
        )

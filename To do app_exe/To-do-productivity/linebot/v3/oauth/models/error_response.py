# coding: utf-8

"""
    Channel Access Token API

    This document describes Channel Access Token API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic.v1 import BaseModel, Field, StrictStr

class ErrorResponse(BaseModel):
    """
    Error response of the Channel access token
    """
    error: Optional[StrictStr] = Field(None, description="Error summary")
    error_description: Optional[StrictStr] = Field(None, description="Details of the error. Not returned in certain situations.")

    __properties = ["error", "error_description"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ErrorResponse:
        """Create an instance of ErrorResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ErrorResponse:
        """Create an instance of ErrorResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ErrorResponse.parse_obj(obj)

        _obj = ErrorResponse.parse_obj({
            "error": obj.get("error"),
            "error_description": obj.get("error_description")
        })
        return _obj

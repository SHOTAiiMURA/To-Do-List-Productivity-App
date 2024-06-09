# coding: utf-8

"""
    Webhook Type Definition

    Webhook event definition of the LINE Messaging API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic.v1 import Field, StrictInt, StrictStr
from linebot.v3.webhooks.models.content_provider import ContentProvider
from linebot.v3.webhooks.models.message_content import MessageContent

class VideoMessageContent(MessageContent):
    """
    VideoMessageContent
    """
    duration: Optional[StrictInt] = Field(None, description="Length of video file (milliseconds)")
    content_provider: ContentProvider = Field(..., alias="contentProvider")
    quote_token: StrictStr = Field(..., alias="quoteToken", description="Quote token to quote this message. ")
    type: str = "video"

    __properties = ["type", "id", "duration", "contentProvider", "quoteToken"]

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
    def from_json(cls, json_str: str) -> VideoMessageContent:
        """Create an instance of VideoMessageContent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of content_provider
        if self.content_provider:
            _dict['contentProvider'] = self.content_provider.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VideoMessageContent:
        """Create an instance of VideoMessageContent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VideoMessageContent.parse_obj(obj)

        _obj = VideoMessageContent.parse_obj({
            "type": obj.get("type"),
            "id": obj.get("id"),
            "duration": obj.get("duration"),
            "content_provider": ContentProvider.from_dict(obj.get("contentProvider")) if obj.get("contentProvider") is not None else None,
            "quote_token": obj.get("quoteToken")
        })
        return _obj


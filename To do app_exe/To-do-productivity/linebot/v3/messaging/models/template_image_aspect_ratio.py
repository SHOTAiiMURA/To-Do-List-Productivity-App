# coding: utf-8

"""
    LINE Messaging API

    This document describes LINE Messaging API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class TemplateImageAspectRatio(str, Enum):
    """
    Aspect ratio of the image. This is only for the `imageAspectRatio` in ButtonsTemplate. Specify one of the following values:  `rectangle`: 1.51:1 `square`: 1:1 
    """

    """
    allowed enum values
    """
    RECTANGLE = 'rectangle'
    SQUARE = 'square'

    @classmethod
    def from_json(cls, json_str: str) -> TemplateImageAspectRatio:
        """Create an instance of TemplateImageAspectRatio from a JSON string"""
        return TemplateImageAspectRatio(json.loads(json_str))



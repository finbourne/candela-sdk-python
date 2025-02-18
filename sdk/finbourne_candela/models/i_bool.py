# coding: utf-8

"""
    FINBOURNE Candela Platform Web API

    FINBOURNE Technology  # noqa: E501

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic.v1 import StrictStr, Field, BaseModel 

class IBool(BaseModel):
    """
    Class representing a boolean-valued field in an intent.        # noqa: E501
    """
    is_nullable: Optional[Any] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["is_nullable"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> IBool:
        """Create an instance of IBool from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if is_nullable (nullable) is None
        # and __fields_set__ contains the field
        if self.is_nullable is None and "is_nullable" in self.__fields_set__:
            _dict['is_nullable'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IBool:
        """Create an instance of IBool from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IBool.parse_obj(obj)

        _obj = IBool.parse_obj({
            "is_nullable": obj.get("is_nullable")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

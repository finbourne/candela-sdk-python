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
from pydantic.v1 import StrictStr, Field, BaseModel, StrictStr 

class BaseTool(BaseModel):
    """
    Base class for tools  # noqa: E501
    """
    tool_type:  Optional[StrictStr] = Field(None,alias="tool_type") 
    instruction:  Optional[StrictStr] = Field(None,alias="instruction") 
    additional_properties: Dict[str, Any] = {}
    __properties = ["tool_type", "instruction"]

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
    def from_json(cls, json_str: str) -> BaseTool:
        """Create an instance of BaseTool from a JSON string"""
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

        # set to None if tool_type (nullable) is None
        # and __fields_set__ contains the field
        if self.tool_type is None and "tool_type" in self.__fields_set__:
            _dict['tool_type'] = None

        # set to None if instruction (nullable) is None
        # and __fields_set__ contains the field
        if self.instruction is None and "instruction" in self.__fields_set__:
            _dict['instruction'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BaseTool:
        """Create an instance of BaseTool from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BaseTool.parse_obj(obj)

        _obj = BaseTool.parse_obj({
            "tool_type": obj.get("tool_type"),
            "instruction": obj.get("instruction")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr 
from finbourne_candela.models.circuit_dto import CircuitDTO
from finbourne_candela.models.directive import Directive
from finbourne_candela.models.object_id import ObjectId
from finbourne_candela.models.tool_module import ToolModule

class DevSessionStartRequest(BaseModel):
    """
    DevSessionStartRequest
    """
    model_id: ObjectId = Field(...)
    circuit: CircuitDTO = Field(...)
    directive: Directive = Field(...)
    scope:  Optional[StrictStr] = Field(None,alias="scope") 
    parent_session: Optional[ObjectId] = None
    tool_module_override: Optional[ToolModule] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["model_id", "circuit", "directive", "scope", "parent_session", "tool_module_override"]

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
    def from_json(cls, json_str: str) -> DevSessionStartRequest:
        """Create an instance of DevSessionStartRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of model_id
        if self.model_id:
            _dict['model_id'] = self.model_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of circuit
        if self.circuit:
            _dict['circuit'] = self.circuit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of directive
        if self.directive:
            _dict['directive'] = self.directive.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parent_session
        if self.parent_session:
            _dict['parent_session'] = self.parent_session.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tool_module_override
        if self.tool_module_override:
            _dict['tool_module_override'] = self.tool_module_override.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if scope (nullable) is None
        # and __fields_set__ contains the field
        if self.scope is None and "scope" in self.__fields_set__:
            _dict['scope'] = None

        # set to None if parent_session (nullable) is None
        # and __fields_set__ contains the field
        if self.parent_session is None and "parent_session" in self.__fields_set__:
            _dict['parent_session'] = None

        # set to None if tool_module_override (nullable) is None
        # and __fields_set__ contains the field
        if self.tool_module_override is None and "tool_module_override" in self.__fields_set__:
            _dict['tool_module_override'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DevSessionStartRequest:
        """Create an instance of DevSessionStartRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DevSessionStartRequest.parse_obj(obj)

        _obj = DevSessionStartRequest.parse_obj({
            "model_id": ObjectId.from_dict(obj.get("model_id")) if obj.get("model_id") is not None else None,
            "circuit": CircuitDTO.from_dict(obj.get("circuit")) if obj.get("circuit") is not None else None,
            "directive": Directive.from_dict(obj.get("directive")) if obj.get("directive") is not None else None,
            "scope": obj.get("scope"),
            "parent_session": ObjectId.from_dict(obj.get("parent_session")) if obj.get("parent_session") is not None else None,
            "tool_module_override": ToolModule.from_dict(obj.get("tool_module_override")) if obj.get("tool_module_override") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

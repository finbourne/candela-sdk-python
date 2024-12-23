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
from pydantic.v1 import BaseModel, Field, StrictStr
from finbourne_candela.models.object_id import ObjectId

class SessionStartRequest(BaseModel):
    """
    SessionStartRequest
    """
    app: ObjectId = Field(...)
    model_cfg: ObjectId = Field(...)
    scope: Optional[StrictStr] = None
    parent_session: Optional[ObjectId] = None
    circuit_override: Optional[ObjectId] = None
    directive_override: Optional[ObjectId] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["app", "model_cfg", "scope", "parent_session", "circuit_override", "directive_override"]

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
    def from_json(cls, json_str: str) -> SessionStartRequest:
        """Create an instance of SessionStartRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of app
        if self.app:
            _dict['app'] = self.app.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model_cfg
        if self.model_cfg:
            _dict['model_cfg'] = self.model_cfg.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parent_session
        if self.parent_session:
            _dict['parent_session'] = self.parent_session.to_dict()
        # override the default output from pydantic by calling `to_dict()` of circuit_override
        if self.circuit_override:
            _dict['circuit_override'] = self.circuit_override.to_dict()
        # override the default output from pydantic by calling `to_dict()` of directive_override
        if self.directive_override:
            _dict['directive_override'] = self.directive_override.to_dict()
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

        # set to None if circuit_override (nullable) is None
        # and __fields_set__ contains the field
        if self.circuit_override is None and "circuit_override" in self.__fields_set__:
            _dict['circuit_override'] = None

        # set to None if directive_override (nullable) is None
        # and __fields_set__ contains the field
        if self.directive_override is None and "directive_override" in self.__fields_set__:
            _dict['directive_override'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SessionStartRequest:
        """Create an instance of SessionStartRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SessionStartRequest.parse_obj(obj)

        _obj = SessionStartRequest.parse_obj({
            "app": ObjectId.from_dict(obj.get("app")) if obj.get("app") is not None else None,
            "model_cfg": ObjectId.from_dict(obj.get("model_cfg")) if obj.get("model_cfg") is not None else None,
            "scope": obj.get("scope"),
            "parent_session": ObjectId.from_dict(obj.get("parent_session")) if obj.get("parent_session") is not None else None,
            "circuit_override": ObjectId.from_dict(obj.get("circuit_override")) if obj.get("circuit_override") is not None else None,
            "directive_override": ObjectId.from_dict(obj.get("directive_override")) if obj.get("directive_override") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
